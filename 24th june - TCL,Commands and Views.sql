-- Transaction Control Language (TCL), Triggers, and Views Example Script

-- TCL
-- Transaction Control Language (TCL) is used to manage transactions in SQL, ensuring data integrity by controlling the beginning and ending of transactions.

use school;

CREATE TABLE Students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    gender VARCHAR(10)
);

CREATE TABLE Courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(50),
    enrollment_count INT DEFAULT 0
);

CREATE TABLE Enrollments (
    enrollment_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    CONSTRAINT fk_student FOREIGN KEY (student_id) REFERENCES Students(id),
    CONSTRAINT fk_course FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

-- TCL Example: Managing transactions with BEGIN, COMMIT, and ROLLBACK
BEGIN;

-- Inserting data into Students table
INSERT INTO Students (id, name, age, gender) VALUES
(1, 'Arpita', 18, 'Female'),
(2, 'Sunita', 19, 'Female'),
(3, 'Shivam', 20, 'Male');

-- Inserting data into Courses table
INSERT INTO Courses (course_id, course_name) VALUES
(101, 'Mathematics'),
(102, 'Science');

-- Commit the transaction to make changes permanent
COMMIT;

-- Rollback example (commented out for now)
-- ROLLBACK;

-- Triggers
-- Triggers are special types of stored procedures that automatically execute when a specific event occurs in the database.

-- Example: Update enrollment count in Courses table after insertion into Enrollments
DELIMITER //
CREATE TRIGGER UpdateEnrollmentCount
AFTER INSERT ON Enrollments
FOR EACH ROW
BEGIN
    DECLARE course_enrollment_count INT;
    SELECT COUNT(*) INTO course_enrollment_count FROM Enrollments WHERE course_id = NEW.course_id;
    UPDATE Courses SET enrollment_count = course_enrollment_count WHERE course_id = NEW.course_id;
END //
DELIMITER ;

-- Example insert into Enrollments triggering the update
INSERT INTO Enrollments (enrollment_id, student_id, course_id, enrollment_date) VALUES
(1, 1, 101, '2024-01-15');

-- Check if trigger updated enrollment_count in Courses table
SELECT * FROM Courses;

-- Views
-- Views are virtual tables created by a query. They can simplify complex queries and provide a layer of security by restricting access to certain columns.

-- Example: Create a view to display student information with course details
CREATE VIEW StudentCourseView AS
SELECT S.name AS student_name, S.age, S.gender, C.course_name
FROM Students S
JOIN Enrollments E ON S.id = E.student_id
JOIN Courses C ON E.course_id = C.course_id;

-- Query the view
SELECT * FROM StudentCourseView;
