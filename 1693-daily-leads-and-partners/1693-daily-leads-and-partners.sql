# Write your MySQL query statement below
Select
    date_id,
    make_name,
    Count(distinct lead_id) AS unique_leads,
    Count(distinct partner_id) AS unique_partners
From
    DailySales
Group By 1,2;