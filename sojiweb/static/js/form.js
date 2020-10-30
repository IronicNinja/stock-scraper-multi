/* Modal JS */
var modal = document.getElementById("myModal");
$(".modal").toggle(localStorage.Form==="true");

// When the user clicks on the button, open the modal
function openForm() {
  localStorage.Form = $(".modal").toggle().is(":visible");
}

// When the user clicks on the x, close the modal
function closeForm() {
  localStorage.Form = $(".modal").toggle().is(":visible");
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    localStorage.Form = $(".modal").toggle().is(":visible");
  }
}