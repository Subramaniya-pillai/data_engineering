

-- Create the Employee Attendance Table
CREATE TABLE EmployeeAttendance (
    AttendanceID INT PRIMARY KEY,
    EmployeeName VARCHAR(50),
    Department VARCHAR(30),
    Date DATE,
    Status VARCHAR(20),
    HoursWorked DECIMAL(4,1)
);

-- Insert Initial Data
INSERT INTO EmployeeAttendance VALUES
(1, 'John Doe', 'IT', '2025-05-01', 'Present', 8),
(2, 'Priya Singh', 'HR', '2025-05-01', 'Absent', 0),
(3, 'Ali Khan', 'IT', '2025-05-01', 'Present', 7),
(4, 'Riya Patel', 'Sales', '2025-05-01', 'Late', 6),
(5, 'David Brown', 'Marketing', '2025-05-01', 'Present', 8),
(6, 'Neha Sharma', 'Finance', '2025-05-01', 'Present', 8);

-- Update: Change Riya Patel's status to Present
UPDATE EmployeeAttendance
SET Status = 'Present'
WHERE EmployeeName = 'Riya Patel' AND Date = '2025-05-01';

-- Delete: Remove Priya Singh's record
DELETE FROM EmployeeAttendance
WHERE EmployeeName = 'Priya Singh';

-- Read: All records sorted by EmployeeName
SELECT * FROM EmployeeAttendance
ORDER BY EmployeeName;

-- Sort by HoursWorked descending
SELECT * FROM EmployeeAttendance
ORDER BY HoursWorked DESC;

-- Filter by IT department
SELECT * FROM EmployeeAttendance
WHERE Department = 'IT';

-- Present employees from IT department
SELECT * FROM EmployeeAttendance
WHERE Status = 'Present' AND Department = 'IT';

-- Absent or Late employees
SELECT * FROM EmployeeAttendance
WHERE Status IN ('Absent', 'Late');

-- Total hours worked by department
SELECT Department, SUM(HoursWorked) AS TotalHours
FROM EmployeeAttendance
GROUP BY Department;

-- Average hours worked overall
SELECT AVG(HoursWorked) AS AverageHours
FROM EmployeeAttendance;

-- Count by attendance status
SELECT Status, COUNT(*) AS EmployeeCount
FROM EmployeeAttendance
GROUP BY Status;

-- Employee names starting with 'R'
SELECT * FROM EmployeeAttendance
WHERE EmployeeName LIKE 'R%';

-- Worked more than 6 hours and Present
SELECT * FROM EmployeeAttendance
WHERE HoursWorked > 6 AND Status = 'Present';

-- Hours between 6 and 8
SELECT * FROM EmployeeAttendance
WHERE HoursWorked BETWEEN 6 AND 8;

-- Top 2 employees with most hours
SELECT * FROM EmployeeAttendance
ORDER BY HoursWorked DESC
LIMIT 2;

-- Employees with hours less than average
SELECT * FROM EmployeeAttendance
WHERE HoursWorked < (
    SELECT AVG(HoursWorked) FROM EmployeeAttendance
);

-- Average hours by status
SELECT Status, AVG(HoursWorked) AS AvgHours
FROM EmployeeAttendance
GROUP BY Status;

-- Duplicate entries on the same date
SELECT EmployeeName, Date, COUNT(*) AS Records
FROM EmployeeAttendance
GROUP BY EmployeeName, Date
HAVING COUNT(*) > 1;

-- Department with most Present employees
SELECT Department, COUNT(*) AS PresentCount
FROM EmployeeAttendance
WHERE Status = 'Present'
GROUP BY Department
ORDER BY PresentCount DESC
LIMIT 1;

-- Employee with most hours per department
SELECT e.Department, e.EmployeeName, e.HoursWorked
FROM EmployeeAttendance e
INNER JOIN (
    SELECT Department, MAX(HoursWorked) AS MaxHours
    FROM EmployeeAttendance
    GROUP BY Department
) m ON e.Department = m.Department AND e.HoursWorked = m.MaxHours;
