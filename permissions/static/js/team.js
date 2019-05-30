const courseSelectField = $("#courses");
const courseFormGroup = $(".form-group").eq(3);

courseSelectField.change(function(e) {
  const { value } = e.target;
  const data = { course_id: value };
  console.log(value);

  $.ajax({
    data,
    url: "/permissions/units/get/",
    success: function(result) {
      addModuleOptions(result);
    }
  });
});

function addModuleOptions({ units }) {
  let html = `
    <div class="form-group" id="unit-group">
        <label for="units">Units</label>
        <select name="units" id="units" class="form-control" multiple>
            <option disabled selected>No unit selected</option>`;

  units.forEach(({ key, name }) => {
    html += `<option value=${key}>${name}</option>`;
  });

  html += `        
        </select>
    </div>
    `;

  if ($("#unit-group").length != 0) {
    // elem. already exists
    $("#unit-group").remove();
  }

  courseFormGroup.after(html);
}
