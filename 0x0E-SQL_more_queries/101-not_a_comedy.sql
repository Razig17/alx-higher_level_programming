-- SQL script to list all shows without the genre Comedy in the hbtn_0d_tvshows database
-- Select all shows from the tv_shows table
-- Exclude shows with the genre Comedy using a subquery
-- Results are sorted in ascending order by the show title

SELECT tv_shows.title FROM tv_shows
WHERE tv_shows.id NOT IN (
SELECT tv_show_genres.show_id FROM tv_show_genres
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
)
ORDER BY tv_shows.title;
