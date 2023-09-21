17.1:
SELECT COUNT(DISTINCT JOB_ID)
FROM wrpracti_bookinfo. employees;

17.2:
SELECT AVG(SALARY), COUNT(*)
FROM wrpracti_bookinfo. employees
WHERE DEPARTMENT_ID = 90;

17.3:
SELECT JOB_ID, COUNT(*)
FROM wrpracti_bookinfo. employees
group by JOB_ID;

17.4:
SELECT FIRST_NAME, LAST_NAME, DEPARTMENT_ID
FROM wrpracti_bookinfo. employees;

17.5:
SELECT employees.FIRST_NAME, employees.LAST_NAME, jobs.JOB_TITLE, employees.DEPARTMENT_ID
FROM employees
JOIN jobs
ON employees.JOB_ID = jobs.JOB_ID
JOIN departments
ON employees.DEPARTMENT_ID = departments.DEPARTMENT_ID JOIN locations
ON departments.LOCATION_ID = locations.LOCATION_ID
WHERE locations.CITY = "London";
