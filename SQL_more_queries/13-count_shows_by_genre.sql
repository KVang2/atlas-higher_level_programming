-- Script that lists all genres and displays number of shows linked to each
SELECT tv_show_genres.genre_id AS genre, COUNT(tv_shows.id)
AS number_of_shows FROM tv_show_genres
JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
GROUP BY genre
ORDER BY number_of_shows DESC;