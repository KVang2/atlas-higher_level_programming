-- A database to lists all genres of the show
SELECT tv_genres.name FROM tv_shows
JOIN tv_show ON tv_shows_genres.show_id = tv_shows.id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_shows.title = "Dexter" ORDER BY tv_genres.name;
