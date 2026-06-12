CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255),
    role VARCHAR(50));

CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    department VARCHAR(100)
);

CREATE TABLE tickets (
    id INTEGER PRIMARY KEY,
    title VARCHAR(255),
    description TEXT,
    priority VARCHAR(20),
    status VARCHAR(50),
    assigned_to INTEGER
);
