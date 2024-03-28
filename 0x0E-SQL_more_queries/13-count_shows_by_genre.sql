-- SQL script to list all genres from hbtn_0d_tvshows and display the number of shows linked to each

-- Select the genre name from tv_genres and count the number of linked shows for each genre
-- Join tv_genres and tv_show_genres tables to get the relationship between genres and shows
-- Group the results by genre name and count the number of shows linked to each genre
-- Order the results in descending order by the number of shows linked

SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
WHERE number_of_shows > 0
ORDER BY number_of_shows DESC;
