-- Importing database dump from tvshow in MySQL server
SELECT hbtn_0d_tvshows
FROM hbtn_0d_tvshows
LEFT JOIN tv_show_genres
ON tv_show.id = tv_show_genres.show_id
WHERE tv_show_genres.show_id IS NULL
ORDER BY tv_show.title ASC; 