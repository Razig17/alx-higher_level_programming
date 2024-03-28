-- SQL script to list all genres of the show Dexter from the hbtn_0d_tvshows database

-- Select the genre name from the tv_genres table
-- Join tv_genres, tv_show_genres, and tv_shows tables to establish the relationship between genres and shows
-- Filter the results to include only genres related to the show Dexter
-- Order the results in ascending order by the genre name

SELECT tv_genres.name FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
