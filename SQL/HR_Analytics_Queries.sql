-- HR Analytics SQL Queries


-- 1. Display all employee records
SELECT * FROM employees;

-- 2. Total number of employees
SELECT COUNT(*) AS Total_Employees
FROM employees;

-- 3. Total employees who left the company
SELECT COUNT(*) AS Attrition_Count
FROM employees
WHERE Attrition = 'Yes';

-- 4. Attrition rate (%)
SELECT ROUND(
    (COUNT(CASE WHEN Attrition = 'Yes' THEN 1 END) * 100.0) / COUNT(*),
    2
) AS Attrition_Rate
FROM employees;

-- 5. Average employee age
SELECT ROUND(AVG(Age), 2) AS Average_Age
FROM employees;

-- 6. Average monthly income
SELECT ROUND(AVG(MonthlyIncome), 2) AS Average_Monthly_Income
FROM employees;

-- 7. Average years at company
SELECT ROUND(AVG(YearsAtCompany), 2) AS Average_Years_At_Company
FROM employees;

-- 8. Employees by department
SELECT Department,
       COUNT(*) AS Employee_Count
FROM employees
GROUP BY Department
ORDER BY Employee_Count DESC;

-- 9. Attrition by department
SELECT Department,
       COUNT(*) AS Attrition_Count
FROM employees
WHERE Attrition = 'Yes'
GROUP BY Department
ORDER BY Attrition_Count DESC;

-- 10. Employees by job role
SELECT JobRole,
       COUNT(*) AS Employee_Count
FROM employees
GROUP BY JobRole
ORDER BY Employee_Count DESC;

-- 11. Attrition by job role
SELECT JobRole,
       COUNT(*) AS Attrition_Count
FROM employees
WHERE Attrition = 'Yes'
GROUP BY JobRole
ORDER BY Attrition_Count DESC;

-- 12. Employees by gender
SELECT Gender,
       COUNT(*) AS Employee_Count
FROM employees
GROUP BY Gender;

-- 13. Employees by education field
SELECT EducationField,
       COUNT(*) AS Employee_Count
FROM employees
GROUP BY EducationField;

-- 14. Employees by overtime
SELECT OverTime,
       COUNT(*) AS Employee_Count
FROM employees
GROUP BY OverTime;

-- 15. Employees by business travel
SELECT BusinessTravel,
       COUNT(*) AS Employee_Count
FROM employees
GROUP BY BusinessTravel;

-- 16. Highest monthly income
SELECT MAX(MonthlyIncome) AS Highest_Monthly_Income
FROM employees;

-- 17. Lowest monthly income
SELECT MIN(MonthlyIncome) AS Lowest_Monthly_Income
FROM employees;

-- 18. Average salary by department
SELECT Department,
       ROUND(AVG(MonthlyIncome), 2) AS Average_Salary
FROM employees
GROUP BY Department
ORDER BY Average_Salary DESC;

-- 19. Employees by job satisfaction
SELECT JobSatisfaction,
       COUNT(*) AS Employee_Count
FROM employees
GROUP BY JobSatisfaction
ORDER BY JobSatisfaction;

-- 20. Employees by marital status
SELECT MaritalStatus,
       COUNT(*) AS Employee_Count
FROM employees
GROUP BY MaritalStatus
ORDER BY Employee_Count DESC;

-- 21. Top 10 highest-paid employees
SELECT Age,
       Department,
       JobRole,
       MonthlyIncome
FROM employees
ORDER BY MonthlyIncome DESC
LIMIT 10;