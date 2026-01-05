# Write your MySQL query statement below
SELECT
  t.request_at AS Day,
  ROUND(
    SUM(CASE WHEN t.status != 'completed' THEN 1 ELSE 0 END) * 1.0
    / COUNT(*),
    2
  ) AS "Cancellation Rate"
FROM Trips t
JOIN Users u1 ON u1.users_id = t.client_id AND u1.banned = 'No'
JOIN Users u2 ON u2.users_id = t.driver_id AND u2.banned = 'No'
WHERE t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY t.request_at
ORDER BY t.request_at;
