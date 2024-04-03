#!/usr/bin/node
$(document).ready(function() {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function(data) {
    const movies = data.results;
    $.each(movies, function(index, movie) {
      $('<li>').text(movie.title).appendTo('ul#list_movies');
    });
  });
});
