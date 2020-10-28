/* Animation JS */
$(document).ready(function() {
  var $window = $(window);

  $window.on('scroll resize', function() {
      check_if_in_view('.slide-up', 'do-slide-up');
      check_if_in_view('.grow-animation', 'do-grow-animation');
      check_if_in_view('.slide-left', 'do-slide-left');
      check_if_in_view('.slide-right', 'do-slide-right');
  });

  $window.trigger('scroll');

  function check_if_in_view(elementToCheck, animationToAdd) {
      
      $(elementToCheck).each(function(i, el) {
          var el = $(el);
          if (checkVisible(el)) {
            el.addClass(animationToAdd); 
          } 
        });
      
  }   
  function checkVisible(elm) {
    var rect = elm[0].getBoundingClientRect();
    var viewHeight = Math.max(document.documentElement.clientHeight, window.innerHeight);
    return !(rect.bottom < 0 || rect.top - viewHeight >= 0);
  }
});

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

/* Slideshow */
var slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}

