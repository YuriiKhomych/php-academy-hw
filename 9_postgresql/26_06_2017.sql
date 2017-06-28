CREATE DATABASE HW_26_06;

CREATE TABLE countries (id serial,
                        name varchar(50),
                        territory varchar(50),
                        population integer,
                        currency varchar(10));

INSERT INTO countries (name,
                       territory,
                       population,
                       currency) VALUES ('Ukraine',
                                         'Europe',
                                         47000000,
                                         'hryvna');
INSERT INTO countries (name,
                       territory,
                       population,
                       currency) VALUES ('Poland',
                                         'Europe',
                                         3000000,
                                         'zlotiy');
INSERT INTO countries (name,
                       territory,
                       population,
                       currency) VALUES ('Czech',
                                         'Europe',
                                         3000000,
                                         'crona');
INSERT INTO countries (name,
                       territory,
                       population,
                       currency) VALUES ('Spain',
                                         'Europe',
                                         4000000,
                                         'euro');
INSERT INTO countries (name,
                       territory,
                       population,
                       currency) VALUES ('Germany',
                                         'Europe',
                                         2000000,
                                         'euro');
INSERT INTO countries (name,
                       territory,
                       population,
                       currency) VALUES ('USA',
                                         'North America',
                                         50000000,
                                         'dollar');
INSERT INTO countries (name,
                       territory,
                       population,
                       currency) VALUES ('Brazil',
                                         'South America',
                                         60000000,
                                         'real');

ALTER TABLE countries ADD capital varchar(30);

UPDATE countries SET capital='Kyiv' WHERE name='Ukraine';
UPDATE countries SET capital='Warszawa' WHERE name='Poland';
UPDATE countries SET capital='Prague' WHERE name='Czech';
UPDATE countries SET capital='Madrid' WHERE name='Spain';
UPDATE countries SET capital='Washington' WHERE name='USA';
UPDATE countries SET capital='Brasília' WHERE name='Brazil';
UPDATE countries SET capital='Berlin' WHERE name='Germany';

CREATE TABLE continents (id serial PRIMARY KEY,
                         name varchar(50),
                         climate varchar(30));

INSERT INTO continents (name, climate) VALUES ('Eurasia', 'Humid continental');
INSERT INTO continents (name, climate) VALUES ('Asia', 'Humid tropical');
INSERT INTO continents (name, climate) VALUES ('North America', 'Semiarid');
INSERT INTO continents (name, climate) VALUES ('South America', 'Tropic');
INSERT INTO continents (name, climate) VALUES ('Africa', 'Arid');
INSERT INTO continents (name, climate) VALUES ('Australia', 'Arid');
INSERT INTO continents (name, climate) VALUES ('Antarctica', 'Ice');


ALTER TABLE countries ADD continent_id integer REFERENCES continents;

UPDATE countries SET continent_id=1 WHERE name='Ukraine';
UPDATE countries SET continent_id=1 WHERE name='Poland';
UPDATE countries SET continent_id=1 WHERE name='Czech';
UPDATE countries SET continent_id=1 WHERE name='Spain';
UPDATE countries SET continent_id=4 WHERE name='Brazil';
UPDATE countries SET continent_id=1 WHERE name='Germany';
UPDATE countries SET continent_id=3 WHERE name='USA';

SELECT capital FROM countries WHERE continent_id=1;
SELECT capital FROM countries WHERE continent_id=2;
SELECT capital FROM countries WHERE continent_id=3;
SELECT capital FROM countries WHERE continent_id=4;
SELECT capital FROM countries WHERE continent_id=5;
SELECT capital FROM countries WHERE continent_id=6;

SELECT count(*) FROM countries WHERE continent_id=1;
SELECT count(*) FROM countries WHERE continent_id=2;
SELECT count(*) FROM countries WHERE continent_id=3;
SELECT count(*) FROM countries WHERE continent_id=4;
SELECT count(*) FROM countries WHERE continent_id=5;
SELECT count(*) FROM countries WHERE continent_id=6;

SELECT SUM(population) FROM countries WHERE continent_id=1;
SELECT SUM(population) FROM countries WHERE continent_id=2;
SELECT SUM(population) FROM countries WHERE continent_id=3;
SELECT SUM(population) FROM countries WHERE continent_id=4;
SELECT SUM(population) FROM countries WHERE continent_id=5;
SELECT SUM(population) FROM countries WHERE continent_id=6;

SELECT currency FROM countries WHERE continent_id=1;
SELECT currency FROM countries WHERE continent_id=2;
SELECT currency FROM countries WHERE continent_id=3;
SELECT currency FROM countries WHERE continent_id=4;
SELECT currency FROM countries WHERE continent_id=5;
SELECT currency FROM countries WHERE continent_id=6;

