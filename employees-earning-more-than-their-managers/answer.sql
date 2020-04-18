# Write your MySQL query statement below
-- 1
select 
    e.Name as Employee 
from Employee e 
    join Employee m 
        on (
            e.ManagerId = m.id
            ) 
where e.Salary > m.Salary;

-- 2
SELECT
    a.Name AS 'Employee'
FROM
    Employee AS a,
    Employee AS b
WHERE
    a.ManagerId = b.Id
        AND a.Salary > b.Salary

