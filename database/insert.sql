-- Insert dummy data into advisor table
INSERT INTO advisor (advisorID, lastName, firstName, initials, jobTitle, department)
VALUES
    ('ADV001', 'Smith', 'John', 'J.', 'Senior Advisor', 'Computer Science'),
    ('ADV002', 'Johnson', 'Emily', 'E.', 'Academic Counselor', 'Engineering'),
    ('ADV003', 'Williams', 'Michael', 'M.', 'Student Advisor', 'Mathematics'),
    ('ADV004', 'Jones', 'Sarah', 'S.', 'Career Advisor', 'Business'),
    ('ADV005', 'Brown', 'David', 'D.', 'Financial Aid Advisor', 'Psychology');

-- Insert dummy data into student table
INSERT INTO student (studentID, lastName, firstName, initials, dateOfBirth, gender, email, address, city, state, zipCode, phone, major, advisorID)
VALUES
    ('STU001', 'Johnson', 'Alice', 'A.', '1998-03-15', 'F', 'alice.johnson@example.com', '123 Main St', 'Anytown', 'NY', '12345', '555-123-4567', 'Computer Science', 'ADV001'),
    ('STU002', 'Williams', 'James', 'J.', '1999-05-20', 'M', 'james.williams@example.com', '456 Elm St', 'Sometown', 'CA', '54321', '555-987-6543', 'Engineering', 'ADV002'),
    ('STU003', 'Miller', 'Emma', 'E.', '1997-12-10', 'F', 'emma.miller@example.com', '789 Oak Ave', 'Othercity', 'TX', '67890', '555-234-5678', 'Mathematics', 'ADV003'),
    ('STU004', 'Davis', 'Matthew', 'M.', '2000-02-25', 'M', 'matthew.davis@example.com', '101 Pine Rd', 'Anycity', 'FL', '13579', '555-876-5432', 'Business', 'ADV004'),
    ('STU005', 'Wilson', 'Olivia', 'O.', '1996-08-05', 'F', 'olivia.wilson@example.com', '321 Cedar Ln', 'Someplace', 'WA', '97531', '555-345-6789', 'Psychology', 'ADV005');

-- Insert dummy data into course table
INSERT INTO course (coursePrefix, courseName, creditHours, department, description)
VALUES
    ('CS101', 'Introduction to Computer Science', 3, 'Computer Science', 'Introduction to basic concepts of computer science.'),
    ('ENG201', 'Advanced Engineering Mathematics', 4, 'Engineering', 'Advanced topics in mathematics for engineering majors.'),
    ('MATH301', 'Linear Algebra', 3, 'Mathematics', 'Study of linear equations and their applications.'),
    ('BUS401', 'Business Strategy', 3, 'Business', 'Strategic planning and decision-making in business.'),
    ('PSYCH501', 'Introduction to Psychology', 3, 'Psychology', 'Basic principles and theories of psychology.');

-- Insert dummy data into enrollment table
INSERT INTO enrollment (studentID, coursePrefix, semester, year, grade)
VALUES
    ('STU001', 'CS101', 'Spring', 2023, 3.5),
    ('STU001', 'ENG201', 'Fall', 2022, 4.0),
    ('STU002', 'MATH301', 'Spring', 2023, 3.7),
    ('STU002', 'BUS401', 'Fall', 2022, 3.2),
    ('STU003', 'PSYCH501', 'Spring', 2023, 3.9),
    ('STU003', 'CS101', 'Fall', 2022, 3.8),
    ('STU004', 'MATH301', 'Spring', 2023, 3.5),
    ('STU004', 'ENG201', 'Fall', 2022, 3.9),
    ('STU005', 'BUS401', 'Spring', 2023, 4.0),
    ('STU005', 'PSYCH501', 'Fall', 2022, 3.6);

-- Insert dummy data into instructor table
INSERT INTO instructor (instructorID, lastName, firstName, initials, department)
VALUES
    ('INS001', 'Anderson', 'Robert', 'R.', 'Computer Science'),
    ('INS002', 'Thomas', 'Jennifer', 'J.', 'Engineering'),
    ('INS003', 'Martinez', 'Daniel', 'D.', 'Mathematics'),
    ('INS004', 'Garcia', 'Jessica', 'J.', 'Business'),
    ('INS005', 'Lee', 'Michelle', 'M.', 'Psychology');

-- Insert dummy data into teaches table
INSERT INTO teaches (instructorID, coursePrefix, semester, year)
VALUES
    ('INS001', 'CS101', 'Spring', 2023),
    ('INS002', 'ENG201', 'Fall', 2022),
    ('INS003', 'MATH301', 'Spring', 2023),
    ('INS004', 'BUS401', 'Fall', 2022),
    ('INS005', 'PSYCH501', 'Spring', 2023);

-- Insert dummy data into department table
INSERT INTO department (departmentCode, departmentName, officeLocation, chairpersonID)
VALUES
    ('CS', 'Computer Science', 'Science Building, Room 101', 'INS001'),
    ('ENG', 'Engineering', 'Engineering Building, Room 201', 'INS002'),
    ('MATH', 'Mathematics', 'Mathematics Building, Room 301', 'INS003'),
    ('BUS', 'Business', 'Business Building, Room 401', 'INS004'),
    ('PSYCH', 'Psychology', 'Psychology Building, Room 501', 'INS005');

-- Insert dummy data into transcript table
INSERT INTO transcript (studentID, totalCredits, cumulativeGPA, graduationStatus)
VALUES
    ('STU001', 90, 3.6, true),
    ('STU002', 85, 3.8, true),
    ('STU003', 92, 3.9, true),
    ('STU004', 87, 3.5, true),
    ('STU005', 88, 4.0, true);

-- Insert dummy data into prerequisite table
INSERT INTO prerequisite (coursePrefix, prerequisitePrefix)
VALUES
    ('CS101', 'None'),
    ('ENG201', 'None'),
    ('MATH301', 'None'),
    ('BUS401', 'None'),
    ('PSYCH501', 'None');

-- Insert dummy data into campus table
INSERT INTO campus (campusCode, campusName, address, city, state, zipCode, phoneNumber)
VALUES
    ('CAMP001', 'Main Campus', '123 University Ave', 'Anytown', 'NY', '12345', '555-111-2222'),
    ('CAMP002', 'Downtown Campus', '456 Downtown Blvd', 'Cityville', 'CA', '54321', '555-333-4444'),
    ('CAMP003', 'North Campus', '789 North Rd', 'Northcity', 'TX', '67890', '555-555-6666');

-- Insert dummy data into student_campus table
INSERT INTO student_campus (studentID, campusCode)
VALUES
    ('STU001', 'CAMP001'),
    ('STU002', 'CAMP002'),
    ('STU003', 'CAMP001'),
    ('STU004', 'CAMP003'),
    ('STU005', 'CAMP002');

-- Insert dummy data into course_department table
INSERT INTO course_department (coursePrefix, departmentCode)
VALUES
    ('CS101', 'CS'),
    ('ENG201', 'ENG'),
    ('MATH301', 'MATH'),
    ('BUS401', 'BUS'),
    ('PSYCH501', 'PSYCH');
