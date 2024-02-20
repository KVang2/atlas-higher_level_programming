-- Importing database dump from tvshow in MySQL server
SELECT hbtn_0d_tvshows, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_show.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_show.title ASC; 