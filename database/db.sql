CREATE TABLE advisor (
    advisorID VARCHAR(6) PRIMARY KEY,
    lastName VARCHAR(50) NOT NULL,
    firstName VARCHAR(50) NOT NULL,
    initials VARCHAR(3),
    jobTitle VARCHAR(128),
    department VARCHAR(50)
);

CREATE TABLE student (
    studentID VARCHAR(9) PRIMARY KEY,
    lastName VARCHAR(50) NOT NULL,
    firstName VARCHAR(50) NOT NULL,
    initials VARCHAR(3),
    dateOfBirth DATE,
    gender CHAR(1),
    email VARCHAR(100),
    address VARCHAR(255),
    city VARCHAR(100),
    state VARCHAR(50),
    zipCode VARCHAR(20),
    phone VARCHAR(20),
    major VARCHAR(128),
    advisorID VARCHAR(6),
    FOREIGN KEY (advisorID) REFERENCES advisor(advisorID) ON DELETE SET NULL
);

CREATE TABLE course (
    coursePrefix VARCHAR(9) PRIMARY KEY,
    courseName VARCHAR(100) NOT NULL,
    creditHours INT,
    department VARCHAR(50),
    description TEXT
);

CREATE TABLE enrollment (
    enrollmentID SERIAL PRIMARY KEY,
    studentID VARCHAR(9),
    coursePrefix VARCHAR(9),
    semester VARCHAR(6),
    year INT,
    grade DECIMAL(5, 2),
    UNIQUE (coursePrefix, semester, year), -- Ensure uniqueness
    FOREIGN KEY (studentID) REFERENCES student(studentID),
    FOREIGN KEY (coursePrefix) REFERENCES course(coursePrefix)
);

CREATE TABLE instructor (
    instructorID VARCHAR(6) PRIMARY KEY,
    lastName VARCHAR(50) NOT NULL,
    firstName VARCHAR(50) NOT NULL,
    initials VARCHAR(3),
    department VARCHAR(50)
);

CREATE TABLE teaches (
    instructorID VARCHAR(6),
    coursePrefix VARCHAR(9),
    semester VARCHAR(6),
    year INT,
    PRIMARY KEY (instructorID, coursePrefix, semester, year),
    FOREIGN KEY (instructorID) REFERENCES instructor(instructorID),
    FOREIGN KEY (coursePrefix, semester, year) REFERENCES enrollment(coursePrefix, semester, year)
);

CREATE TABLE department (
    departmentCode VARCHAR(10) PRIMARY KEY,
    departmentName VARCHAR(100) NOT NULL,
    officeLocation VARCHAR(255),
    chairpersonID VARCHAR(6),
    FOREIGN KEY (chairpersonID) REFERENCES instructor(instructorID) ON DELETE SET NULL
);

CREATE TABLE transcript (
    studentID VARCHAR(9) PRIMARY KEY,
    totalCredits INT,
    cumulativeGPA DECIMAL(4, 2),
    graduationStatus BOOLEAN,
    FOREIGN KEY (studentID) REFERENCES student(studentID)
);

CREATE TABLE prerequisite (
    coursePrefix VARCHAR(9),
    prerequisitePrefix VARCHAR(9),
    PRIMARY KEY (coursePrefix, prerequisitePrefix),
    FOREIGN KEY (coursePrefix) REFERENCES course(coursePrefix),
    FOREIGN KEY (prerequisitePrefix) REFERENCES course(coursePrefix)
);

CREATE TABLE campus (
    campusCode VARCHAR(10) PRIMARY KEY,
    campusName VARCHAR(100) NOT NULL,
    address VARCHAR(255),
    city VARCHAR(100),
    state VARCHAR(50),
    zipCode VARCHAR(20),
    phoneNumber VARCHAR(20)
);

CREATE TABLE student_campus (
    studentID VARCHAR(9),
    campusCode VARCHAR(10),
    PRIMARY KEY (studentID, campusCode),
    FOREIGN KEY (studentID) REFERENCES student(studentID),
    FOREIGN KEY (campusCode) REFERENCES campus(campusCode)
);

CREATE TABLE course_department (
    coursePrefix VARCHAR(9),
    departmentCode VARCHAR(10),
    PRIMARY KEY (coursePrefix, departmentCode),
    FOREIGN KEY (coursePrefix) REFERENCES course(coursePrefix),
    FOREIGN KEY (departmentCode) REFERENCES department(departmentCode)
);
