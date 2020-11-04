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