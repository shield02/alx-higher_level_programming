--  lists all shows contained in hbtn_0d_tvshows without a genre linked
-- lists all rows of a database that don't have one column order by tv shows title and tv shw genre genre_d columns ascending
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

