<<<<<<< HEAD
$(document).ready(function () {
  $(".sidenav").sidenav({ edge: "right" });
  $('.tooltipped').tooltip();
  $('select').formSelect();
  $('#carousel-auto').carousel();
  setInterval(function () {
    $('#carousel-auto').carousel(
      'next');
  }, 3000);
});
=======
$(document).ready(function(){
    $(".sidenav").sidenav({edge: "right"});
    $('.tooltipped').tooltip();
    $('select').formSelect();
    $('#carousel-auto').carousel();
     setInterval(function(){
        $('#carousel-auto').carousel('next');
    }, 2000);
  });
>>>>>>> 2950223347f1fd0f1bdf9244092b251c761f228f

