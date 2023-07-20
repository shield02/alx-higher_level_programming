-- list all cities contained in the database hbtn_0d_usa
-- list all rows of a particular column in a database order by cities id column
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON states.id = cities.state_id ORDER BY cities.id;

