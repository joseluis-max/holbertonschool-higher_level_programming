/* script that fetches and lists the title for all movies */
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data, textState) {
  for (movie in data.results){
      $('UL#list_movies').append(`<li>${data.results[movie].title}</li>`);
  }
});
