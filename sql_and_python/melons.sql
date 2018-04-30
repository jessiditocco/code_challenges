CREATE TABLE melons (
	id SERIAL PRIMARY KEY, 
	type VARCHAR(30) NOT NULL,
	name VARCHAR(30) NOT NULL,
	price NUMERIC(8, 2) NOT NULL
);

INSERT INTO melons (type, name, price) VALUES('Musk','Honeydew',1);
INSERT INTO melons (type, name, price) VALUES('Hybrid','Crenshaw',2);
INSERT INTO melons (type, name, price) VALUES('Hybrid','Crane',2.5);
INSERT INTO melons (type, name, price) VALUES('Musk','Casaba',2.5);
INSERT INTO melons (type, name, price) VALUES('Musk','Cantaloupe',0.99);
INSERT INTO melons (type, name, price) VALUES('Hybrid','Galia',3.75);
INSERT INTO melons (type, name, price) VALUES('Winter','Winter Melon',0.99);
INSERT INTO melons (type, name, price) VALUES('Musk','Canary',1.50);
INSERT INTO melons (type, name, price) VALUES('Musk','Hami',2.75);
INSERT INTO melons (type, name, price) VALUES('Watermelon','Densuke',250);
INSERT INTO melons (type, name, price) VALUES('Watermelon','Ali Baba',2.50);
INSERT INTO melons (type, name, price) VALUES('Watermelon','Ancient',3.00);

SELECT setval('melons_id_seq', 12, True);
