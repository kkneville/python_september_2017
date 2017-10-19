-- INSERT INTO users(first_name, last_name)
-- VALUES('Alyssa', 'McKee');
-- INSERT INTO users(first_name, last_name)
-- VALUES('Chris', 'Baker');
-- 
-- INSERT INTO users(first_name, last_name)
-- VALUES('Diana', 'Smith');
-- 
-- INSERT INTO users(first_name, last_name)
-- VALUES('Jessica', 'Jones');

-- INSERT INTO friendships (user_id, friend_id)
-- VALUES(1,5);
-- INSERT INTO friendships (user_id, friend_id)
-- VALUES(3,4);
-- INSERT INTO friendships (user_id, friend_id)
-- VALUES(1,4);
-- INSERT INTO friendships (user_id, friend_id)
-- VALUES(3,4);
-- INSERT INTO friendships (user_id, friend_id)
-- VALUES(4,5);


SELECT users.first_name, users.last_name, user2.first_name AS friend_first_name, user2.last_name AS friend_last_name FROM users
LEFT JOIN friendships ON friendships.user_id = users.id
LEFT JOIN users AS user2 ON friendships.friend_id = user2.id
ORDER BY friend_last_name;

