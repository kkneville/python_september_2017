select *
from users;

insert into friendships (user_id, friend_id, created_at, updated_at)
values (2, 1, now(), now()),
(3, 1, now(), now()),
(4, 1, now(), now());


select users.first_name, users.last_name, user2.first_name as friend_first_name, user2.last_name as friend_last_name
from users
left join friendships on users.id = friendships.user_id
left join users as user2 on  user2.id = friendships.friend_id;
