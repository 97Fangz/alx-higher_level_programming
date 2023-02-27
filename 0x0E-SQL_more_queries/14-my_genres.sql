-- import the database dump from hbtn_0d_tvshows to mysql server
-- script that uses the hbtn_0d_tvshows database to lists all genres
-- of the show Dexter

SELEcT tv_genres.name AS genre, COUNT(tv_genres.id) AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
