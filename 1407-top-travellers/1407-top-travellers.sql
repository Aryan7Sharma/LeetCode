# Write your MySQL query statement below
SELECT name,
    IFNULL(SUM(distance), 0) AS travelled_distance
FROM 
    Users u
    Left JOIN Rides r
    ON user_id = u.id
GROUP BY 
    u.id
ORDER BY 
    travelled_distance DESC,name;