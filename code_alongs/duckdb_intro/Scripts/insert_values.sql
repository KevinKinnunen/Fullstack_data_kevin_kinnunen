CREATE TABLE jokes (
	id INTEGER PRIMARY KEY,
	joke_text VARCHAR,
	rating INTEGER);

desc;

INSERT
	INTO
	main.jokes(id,
	joke_text,
	rating)
VALUES
(1,
'Why dont scientists trust atoms? Because they make up everything!',
8),
(2,
'Beaver, use DBeaver',
3),
(3,
'Idk',
-1);

SELECT * FROM jokes;

SELECT * FROM jokes WHERE rating > 2;

desc jokes;

INSERT INTO jokes (id, joke_text, rating) VALUES
(4, 'Why don’t skeletons fight each other? They don’t have the guts.', 6),
(5, 'Why don’t some couples go to the gym? Because some relationships don’t work out.', 8),
(6, 'I would avoid the sushi if I was you. It’s a little fishy.', 7),
(7, 'Want to hear a joke about construction? I’m still working on it.', 6),
(8, 'Why don’t programmers like nature? It has too many bugs.', 9),
(9, 'How does a penguin build its house? Igloos it together.', 1),
(10, 'A gothenburg person stands in queue for star wars. When someone cuts the line he says ge daj.', 2);