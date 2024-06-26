# Write your MySQL query statement below
(SELECT name as results
FROM users u
JOIN movierating mr
ON u.user_id = mr.user_id
GROUP BY 1
ORDER BY count(rating) desc, 1 asc
Limit 1)

UNION ALL

(SELECT title as results
FROM movies m
JOIN movierating mr
ON m.movie_id = mr.movie_id
WHERE month(created_at) = 2 and year(created_at) = 2020
GROUP BY 1
ORDER BY avg(rating) desc, 1 asc
Limit 1)