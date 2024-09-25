-- Drop the table if it already exists
DROP TABLE IF EXISTS employee_data;

-- Create the employee_data table
CREATE TABLE employee_data (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    job_title VARCHAR(100),
    supervisor VARCHAR(100)
);

-- Insert sample data into employee_data
INSERT INTO employee_data (name, job_title, supervisor) VALUES
('Alice', 'Engineer', 'Bob'),
('Carol', 'Engineer', 'Bob'),
('Eve', 'Designer', 'Carol'),
('Bob', 'Manager', 'Dave'),
('Dave', 'Director', NULL),
('Faythe', 'Engineer', 'Bob'),
('Grace', 'Designer', 'Eve');

WITH RECURSIVE job_hierarchy AS (
    SELECT id, name, job_title, supervisor
    FROM employee_data
    WHERE supervisor IS NULL
    UNION ALL
    SELECT e.id, e.name, e.job_title, e.supervisor
    FROM employee_data e
    JOIN job_hierarchy jh ON e.supervisor = jh.name
)
, job_counts AS (
    SELECT job_title, COUNT(*) AS employee_count
    FROM job_hierarchy
    GROUP BY job_title
)
SELECT job_title, SUM(employee_count) AS total_employees
FROM job_counts
GROUP BY job_title;

