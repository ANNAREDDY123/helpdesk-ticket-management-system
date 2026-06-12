# helpdesk-ticket-management-system
Helpdesk Ticket Management System built with FastAPI, SQLAlchemy, JWT Authentication, Employee Management, Ticket Assignment, and SQLite Database.
# Helpdesk Ticket Management System

## Features

- JWT Authentication
- Employee Management
- Ticket Management
- Ticket Assignment
- SQLite Database
- Swagger Documentation

## APIs

### Authentication

- POST /auth/register
- POST /auth/login

### Employees

- POST /employees
- GET /employees
- PUT /employees/{id}
- DELETE /employees/{id}

### Tickets

- POST /tickets
- GET /tickets
- GET /tickets/{id}
- PUT /tickets/{id}
- DELETE /tickets/{id}

### Assignment

- POST /tickets/{ticket_id}/assign/{employee_id}
- GET /tickets/employee/{employee_id}

## Run

py -m pip install -r requirements.txt
py -m uvicorn main:app --reload


Swagger:

http://127.0.0.1:8000/docs
