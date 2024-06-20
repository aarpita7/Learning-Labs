
-- Complex JOIN 
-- List all students along with their courses and the corresponding teacher
SELECT 
    Students.name AS student_name, 
    Courses.course_name, 
    Teachers.teacher_name
FROM 
    Students
JOIN 
    Enrollments ON Students.id = Enrollments.id
JOIN 
    Courses ON Enrollments.course_id = Courses.course_id
JOIN 
    CourseTeachers ON Courses.course_id = CourseTeachers.course_id
JOIN 
    Teachers ON CourseTeachers.teacher_id = Teachers.teacher_id;

-- Subquery 
-- List students who are enrolled in more than one course
SELECT 
    name
FROM 
    Students
WHERE 
    id IN (
        SELECT 
            id
        FROM 
            Enrollments
        GROUP BY 
            id
        HAVING 
            COUNT(course_id) > 1
    );

-- Date-Time Functions example
-- List all enrollments with the duration since the enrollment date
SELECT 
    id,
    course_id,
    enrollment_date,
    DATEDIFF(CURRENT_DATE, enrollment_date) AS days_since_enrollment
FROM 
    Enrollments;

-- Find the average age of students enrolled in each course
SELECT 
    Courses.course_name,
    AVG(Students.age) AS average_age
FROM 
    Enrollments
JOIN 
    Students ON Enrollments.id = Students.id
JOIN 
    Courses ON Enrollments.course_id = Courses.course_id
GROUP BY 
    Courses.course_name;

-- Use a subquery to find the most recent enrollment date for each student
SELECT 
    id,
    (SELECT MAX(enrollment_date) FROM Enrollments E WHERE E.id = S.id) AS most_recent_enrollment
FROM 
    Students S;

-- Use date-time functions to format and display enrollment dates
SELECT 
    id,
    course_id,
    DATE_FORMAT(enrollment_date, '%W, %M %d, %Y') AS formatted_enrollment_date
FROM 
    Enrollments;

-- Additional Date-Time Functions Examples
-- Extract the year, month, and day from the enrollment date
SELECT 
    id,
    course_id,
    enrollment_date,
    YEAR(enrollment_date) AS enrollment_year,
    MONTH(enrollment_date) AS enrollment_month,
    DAY(enrollment_date) AS enrollment_day
FROM 
    Enrollments;

-- Add and subtract intervals to/from the enrollment date
SELECT 
    id,
    course_id,
    enrollment_date,
    DATE_ADD(enrollment_date, INTERVAL 7 DAY) AS one_week_later,
    DATE_SUB(enrollment_date, INTERVAL 7 DAY) AS one_week_earlier
FROM 
    Enrollments;

-- Calculate the difference in months between the current date and the enrollment date
SELECT 
    id,
    course_id,
    enrollment_date,
    TIMESTAMPDIFF(MONTH, enrollment_date, CURRENT_DATE) AS months_since_enrollment
FROM 
    Enrollments;

-- Find enrollments made in the last 30 days
SELECT 
    id,
    course_id,
    enrollment_date
FROM 
    Enrollments
WHERE 
    enrollment_date >= DATE_SUB(CURRENT_DATE, INTERVAL 30 DAY);

-- Format the enrollment date as 'YYYY-MM-DD'
SELECT 
    id,
    course_id,
    DATE_FORMAT(enrollment_date, '%Y-%m-%d') AS formatted_enrollment_date
FROM 
    Enrollments;

-- Combine date and time functions to create a timestamp
SELECT 
    id,
    course_id,
    CONCAT(enrollment_date, ' ', TIME(NOW())) AS enrollment_timestamp
FROM 
    Enrollments;
