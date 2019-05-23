from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

# # Course, Quiz same as yaksh


class GroupMixin(models.Model):

    class Meta:
        abstract = True

    name = models.CharField(max_length=50)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="%(class)s_creator")


class Team(GroupMixin):
    members = models.ManyToManyField(User, related_name="team_members")

    def __str__(self):
        return self.name


class Role(GroupMixin):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    members = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class Permission(models.Model):
    type_choices = [
        ("read", "Read"),
        ("write", "Write"),
    ]

    perm_type = models.CharField(max_length=20, choices=type_choices)
    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, related_name="custom_permission", null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    team = models.ManyToManyField(Role)
