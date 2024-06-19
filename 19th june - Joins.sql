use school;

CREATE TABLE If not exists Students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    gender VARCHAR(10)
);

CREATE TABLE Courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(50)
);

CREATE TABLE Enrollments (
    enrollment_id INT PRIMARY KEY,
   id INT,
    course_id INT,
    FOREIGN KEY (id) REFERENCES Students(id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);


INSERT INTO Students (id, name, age, gender) VALUES
(1, 'Arpita', 18, 'Female'),
(2, 'Sunita', 19, 'Female'),
(3, 'Shivam', 20, 'Male');

INSERT INTO Courses (course_id, course_name) VALUES
(101, 'Mathematics'),
(102, 'Science'),
(103, 'English');

INSERT INTO Enrollments (enrollment_id, id, course_id) VALUES
(1, 1, 101),
(2, 1, 102),
(3, 2, 103),
(4, 3, 101);


-- INNER JOIN: Students and their enrolled courses
SELECT Students.name, Courses.course_name
FROM Students
INNER JOIN Enrollments ON Students.student_id = Enrollments.student_id
INNER JOIN Courses ON Enrollments.course_id = Courses.course_id;

-- LEFT JOIN: All students and their enrolled courses (including those with no enrollments)
SELECT Students.name, Courses.course_name
FROM Students
LEFT JOIN Enrollments ON Students.id = Enrollments.id
LEFT JOIN Courses ON Enrollments.course_id = Courses.course_id;

-- RIGHT JOIN: All courses and the students enrolled in them (including courses with no students)
SELECT Students.name, Courses.course_name
FROM Students
RIGHT JOIN Enrollments ON Students.id = Enrollments.id
RIGHT JOIN Courses ON Enrollments.course_id = Courses.course_id;

--
