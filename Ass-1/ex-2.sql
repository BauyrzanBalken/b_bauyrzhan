CREATE TABLE employee_salary (
    employee_id INT,
    department_id INT,
    salary NUMERIC(10, 2)
);
INSERT INTO employee_salary (employee_id, department_id, salary) VALUES
(1, 101, 5000),
(2, 101, 5500),
(3, 102, 6000),
(4, 102, 6200),
(5, 103, 4800),
(6, 103, 5000),
(7, 104, 7000),
(8, 104, 7200),
(9, 105, 8000),
(10, 105, 8500);
SELECT department_id, AVG(salary) AS average_salary
FROM employee_salary
GROUP BY department_id
ORDER BY average_salary DESC;