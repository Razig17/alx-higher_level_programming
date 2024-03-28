-- SQL script to list all Comedy shows in the database hbtn_0d_tvshows
-- Select the show titles from the tv_shows table
-- Join tv_shows, tv_show_genres, and tv_genres tables to establish the relationship between shows and genres
-- Filter the results to include only shows with the genre name 'Comedy' by matching the name in the tv_genres table
-- Order the results in ascending order by the show title

SELECT tv_shows.title FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title;
