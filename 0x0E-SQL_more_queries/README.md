### 0x0E. SQL - More queries

* 0-priviledges - script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server
* 1-create_user - script that creates the MySQL server user user_0d_1
* 2-create_read_user - script that creates the database hbtn_0d_2 and the user user_0d_2, user_0d_2 should have only SELECT privilege in the database hbtn_0d_2, user_0d_2 password should be set to user_0d_2_pwd
* 3-force_name - script that creates the table force_name
* 4-never_empty - script that creates the table id_not_null
* 5-unique_id - script that creates the table unique_id
* 6-states - script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa)
* 7-cities - script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa)
* 8-cities_of_california_subqury - script that lists all the cities of California that can be found in the database hbtn_0d_usa
* 9-cities_by_state_join - script that lists all cities contained in the database hbtn_0d_usa
* 10-genre_id_by_show - script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked, each record should display: tv_shows.title - tv_show_genres.genre_id, sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
* 11-genre_id_all_shows - script that lists all shows contained in the database hbtn_0d_tvshows, each record should display: tv_shows.title - tv_show_genres.genre_id, sorted in ascending order by tv_shows.title and tv_show_genres.genre_id, if a show doesn’t have a genre, display NULL
* 12-no_genre - script that lists all shows contained in hbtn_0d_tvshows without a genre linked, each record should display: tv_shows.title - tv_show_genres.genre_id, sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
* 13-count_shows_by_genre - script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each, each record should display: `<TV Show genre>` - `<Number of shows linked to this genre>`, first column must be called genre, second column must be called number_of_shows, do not display a genre that doesn’t have any shows linked, sorted in descending order by the number of shows linked
* 14-my_generes - script that uses the `hbtn_0d_tvshows` database to lists all genres of the show `Dexter`, `tv_shows` table contains only one record where title = Dexter (but the id can be different), each record should display: `tv_genres.name`, sorted in ascending order by the genre name
* 15-comedy_only - script that lists all `Comedy` shows in the database `hbtn_0d_tvshows`, `tv_genres` table contains only one record where `name` = `Comedy` (but the `id` can be different), each record should display: `tv_shows.title`, sorted in ascending order by the show title
* 16-shows_by_genere - script that lists all shows, and all genres linked to that show, from the database `hbtn_0d_tvshows`, if a show doesn’t have a genre, display `NULL` in the genre column, each record should display: `tv_shows.title - tv_genres.name`, sorted in ascending order by the show title and genre name
* 100-not_my_genres - script that uses the `hbtn_0d_tvshows` database to list all genres not linked to the show `Dexter`, the `tv_shows` table contains only one record where `title = Dexter` (but the id can be different), each record should display: `tv_genres.name`, sorted in ascending order by the genre name
* 101-not_a_comedy - script that lists all shows without the genre `Comedy` in the database `hbtn_0d_tvshows`, the `tv_genres` table contains only one record where `name = Comedy` (but the id can be different), each record should display: `tv_shows.title`, sorted in ascending order by the show title
* 102-rating_shows - script that lists all shows from `hbtn_0d_tvshows_rate` by their rating, each record should display: `tv_shows.title - rating sum`, sorted in descending order by the rating
* 103-rating_genres - script that lists all genres in the database `hbtn_0d_tvshows_rate` by their rating, each record should display: `tv_genres.name - rating sum`, sorted in descending order by their rating

