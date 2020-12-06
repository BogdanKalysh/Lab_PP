CREATE TABLE student(
    student_id SERIAL NOT NULL,
    name VARCHAR NOT NULL,
    marks VARCHAR[], 
    PRIMARY KEY(student_id)
);

CREATE TABLE teacher(
    teacher_id SERIAL NOT NULL,
    name VARCHAR NOT NULL,
    email VARCHAR NOT NULL,
    password VARCHAR NOT NULL,
    PRIMARY KEY(teacher_id)
);