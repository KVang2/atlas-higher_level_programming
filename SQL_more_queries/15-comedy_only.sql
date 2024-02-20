-- Lists all Comdey shows in database
-- Table contains one recodrd where name = Comedy
SELECT tv_shows.title FROM tv_shows
JOIN tv_genres_shows ON tv_shows.id = tv_genres_shows.show_id
JOIN tv_genres ON tv_genres.id = tv_genres.genre_id
WHERE tv_shows.name = "Comedy" ORDER BY tv_genres.name ASC;