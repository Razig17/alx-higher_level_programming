-- SQL script to list all shows in hbtn_0d_tvshows without a genre linked
-- Select the title of the TV show and the genre ID from the TV show genres table
-- Use a LEFT JOIN to include all shows from tv_shows regardless of whether they have a linked genre
-- Filter the results to only include shows without a genre linked (genre_id is NULL)
-- Order the results in ascending order by tv_shows.title and tv_show_genres.genre_id
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
