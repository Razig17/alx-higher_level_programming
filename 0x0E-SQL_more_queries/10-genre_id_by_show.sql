-- SQL script to list all shows contained in hbtn_0d_tvshows that have at least one genre linked
-- Select the title of the TV show and the genre ID from the TV show genres table
-- Join the tv_shows and tv_show_genres tables using INNER JOIN to retrieve linked genres
-- Order the results in ascending order by tv_shows.title and tv_show_genres.genre_id

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
