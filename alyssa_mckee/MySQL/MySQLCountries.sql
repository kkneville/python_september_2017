-- 1
SELECT countries.name  AS country, languages.language, languages.percentage FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE languages.language = 'Slovene'
ORDER BY languages.percentage DESC;

-- 2
SELECT countries.name, COUNT(cities.id) AS number_of_cities FROM cities
JOIN countries ON countries.id=cities.country_id
GROUP BY countries.id
ORDER BY COUNT(cities.id) DESC;

-- 3
SELECT cities.name, cities.population FROM cities
JOIN countries ON countries.id=cities.country_id
WHERE cities.population > 500000
ORDER BY cities.population DESC;

-- 4
SELECT language FROM languages
WHERE percentage>89
ORDER BY percentage DESC;

-- 5
SELECT name FROM countries
WHERE surface_area < 501 AND population > 100000;

-- 6
SELECT name FROM countries
WHERE government_form = 'Constitutional Monarchy' AND capital > 200 AND life_expectancy > 75;

-- 7
SELECT countries.name AS countries, cities.name AS cities, cities.district, cities.population AS 'city_population' FROM cities
JOIN countries ON countries.id=cities.country_id
WHERE countries.name = 'Argentina' AND cities.district = 'Buenos Aires' AND cities.population> 500000;

-- 8
SELECT  region, COUNT(id) AS 'number of countries' FROM countries
GROUP BY region
ORDER BY 'number_of_countries';