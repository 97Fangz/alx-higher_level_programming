-- import the database dump from hbtn_0d_tvshows to mysql server
-- and lists all genres from the database and displays the number of
-- shows linked to each:

SELECT tv_genres.name AS genre, COUNT(tv_genres.id) AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id=tv_show_genres.genres_id
GROUP BY genre
ORDER BY number_of_shows DESC;
