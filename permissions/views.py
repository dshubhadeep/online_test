from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from yaksh.models import Course

from .models import Team, Role

# Create your views here.


@login_required
def home(request):

    # Get users
    users = User.objects.all()
    teams = Team.objects.all()

    context = {
        "users": users,
        "teams": teams
    }

    return render(request, "home.html", context)


@require_POST
@login_required
def create_team(request):

    team_name = request.POST.get("team_name")
    members_list = request.POST.getlist("members")

    if len(team_name) > 0:
        team = Team.objects.create(
            name=team_name,
            created_by=request.user
        )

        for member in members_list:
            team.members.add(User.objects.get(username=member))

        # Add creator to members
        team.members.add(request.user)

        team.save()

    return redirect("permissions:home")


@login_required()
def team_detail(request, id):
    print(id)

    users = User.objects.all()
    # roles = Role.objects.filter(team=Team.objects.ge)

    context = {
        "users": users
    }

    try:
        team = Team.objects.get(id=id)
        roles = Role.objects.filter(team=team)
        context["team"] = team
        context["roles"] = roles
    except Team.DoesNotExist:
        print("Team doesn't exist")
        pass

    return render(request, "team_page.html", context)


@require_POST
@login_required
def create_role(request):

    team_id = request.POST.get("team_id")
    role_name = request.POST.get("role_name")
    members = request.POST.getlist("members")

    try:
        team = Team.objects.get(id=team_id)

        role = Role(
            name=role_name,
            created_by=request.user,
            team=team
        )

        role.save()
    except Team.DoesNotExist:
        print("Team doesn't exist")
        pass

    return redirect('permissions:team_detail', team_id)
