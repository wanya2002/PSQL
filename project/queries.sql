SELECT employees.name, COUNT(*) AS kol_vac FROM employees
INNER JOIN vacancies USING(emp_id)
GROUP BY employees.name

SELECT vacancies.vac_id, vacancies.name, employees.name, salary_from, vacancy_url FROM employees
INNER JOIN vacancies USING(emp_id)

SELECT round((AVG(salary_from)),2) FROM vacancies

SELECT * FROM vacancies
WHERE salary_from > (SELECT round((AVG(salary_from)),2) FROM vacancies)

SELECT * FROM vacancies
WHERE vacancies.name LIKE '%python%'