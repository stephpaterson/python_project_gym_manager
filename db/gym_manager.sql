DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS gym_classes;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    phone_number VARCHAR(255),
    email VARCHAR(255)
);

CREATE TABLE gym_classes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    instructor VARCHAR(255),
    location VARCHAR(255),
    date VARCHAR(255),
    time VARCHAR(255)
);
