-- 1
select name from states; 

-- 2
select * from states where id > 2;

-- 3
select count(cities.id) from cities;

-- 4
select * from cities where states_id=2;

-- alternate 4
select cities.* from cities 
join states on states.id=cities.states_id
where states.name = "Nevada";

-- 5
select * from states order by name;

-- 6
select * from states join cities on states.id = cities.states_id;

-- 7
select businesses.* , states.name from businesses 
join cities on cities.id = businesses.cities_id 
join states on cities.states_id = states.id 
where states.name = "California";

-- 8
select Count(businesses.id), cities.name from businesses
join cities on cities.id = businesses.cities_id
group by cities.id
order by Count(*);































-- -- insert into states (name)
-- ---- Values("California");

-- -- insert into states (name)
-- ---- Values("Nevada");

-- -- insert into states (name)
-- ---- Values("Utah");

-- -- insert into states (name)
-- ---- Values("Washington");

-- -- insert into states (name)
-- ---- Values("New York");

-- insert into cities (name, states_id)
-- Values("Los Angeles",1);

-- insert into cities (name, states_id)
-- Values("Las Vegas",2);

-- insert into cities (name, states_id)
-- Values("Park City",3);

-- insert into cities (name, states_id)
-- Values("San Francisco",1);

-- insert into cities (name, states_id)
-- Values("Reno",2);

-- insert into cities (name, states_id)
-- Values("New York City",5);

-- insert into cities (name, states_id)
-- Values("Seattle",4);

-- insert into businesses (name, cities_id)
-- values("Bubba Gump", 4); 

-- insert into businesses (name, cities_id)
-- values("Ceasars Buffet", 2); 

-- insert into businesses (name, cities_id)
-- values("Sonic", 3); 

-- insert into businesses (name, cities_id)
-- values("Starbucks", 7); 

-- insert into businesses (name, cities_id)
-- values("Trump Hotel", 6); 

-- insert into businesses (name, cities_id)
-- values("In in Out Burger", 1); 

-- insert into businesses (name, cities_id)
-- values("Microsoft", 7); 

-- insert into businesses (name, cities_id)
-- values("Starks Steakhouse", 5); 

-- insert into businesses (name, cities_id)
-- values("Liberty Tours", 6); 

-- insert into businesses (name, cities_id)
-- values("Giradelli", 4); 



















