SELECT name FROM people WHERE id = (SELECT id FROM movies WHERE (SELECT name FROM movies WHERE name = "Toy Story"));
