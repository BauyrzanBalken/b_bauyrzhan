Ex-4
CREATE TABLE employees (
    employee_id INT,
    department_id INT,
    salary NUMERIC(10, 2)
);
CREATE TABLE departments (
    department_id INT,
    department_name VARCHAR(50)
);
INSERT INTO employees (employee_id, department_id, salary) VALUES
(1, 101, 5000.00),
(2, 101, 5500.00),
(3, 102, 6000.00),
(4, 102, 6200.00),
(5, 103, 4800.00),
(6, 103, 5000.00),
(7, 104, 7000.00),
(8, 104, 7200.00),
(9, 105, 8000.00),
(10, 105, 8500.00);
INSERT INTO departments (department_id, department_name) VALUES
(101, 'Sales'),
(102, 'Marketing'),
(103, 'Finance'),
(104, 'Human Resources'),
(105, 'IT');
SELECT d.department_name, AVG(e.salary) AS average_salary
FROM employees e
INNER JOIN departments d ON e.department_id = d.department_id
GROUP BY d.department_name
ORDER BY average_salary DESC;