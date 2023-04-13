/** processForm: get data from form and make AJAX call to our API. */

async function processForm(evt) {
  evt.preventDefault();
  const name = $("#name").val();
  const email = $("#email").val();
  const birth_year = $("#birth_year").val();
  const color = $("#color").val();
  const data = {
    birth_year: birth_year,
    name: name,
    color: color,
    email: email,
  };
  const response = await axios.post("/api/get-lucky-num", data);
  $("input").val("");
  $("b").html("");
  handleResponse(response);
}

/** handleResponse: deal with response from our lucky-num API. */

function handleResponse(resp) {
  const errors = resp.data.errors;
  if (errors) {
    for (error in errors) {
      $(`#${error}-err`).html(errors[error]);
    }
  } else {
    $("#lucky-results")
      .html(`Your lucky number is ${resp.data.num.num}, ${resp.data.num.fact}<br>
    Your birth year is ${resp.data.year.year}, ${resp.data.year.fact}`);
  }
}

$("#lucky-form").on("submit", processForm);
