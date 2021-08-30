$(document).ready(function () {
  $(".sidenav").sidenav({ edge: "right" });
  $('.tooltipped').tooltip();
  $('select').formSelect();
  $('#carousel-auto').carousel();
  setInterval(function () {
    $('#carousel-auto').carousel(
      'next');
  }, 3000);
  $('.modal').modal();
});

