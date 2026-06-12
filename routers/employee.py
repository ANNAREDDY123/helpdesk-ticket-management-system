from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models.employee import Employee
from schemas.employee import EmployeeCreate

router = APIRouter(
    prefix="/employees",
    tags=["Employees"])


@router.post("")
def create_employee(
    employee: EmployeeCreate,
    db: Session = Depends(get_db)
):

    existing = db.query(Employee).filter(
        Employee.email == employee.email
    ).first()

    if existing:
        raise HTTPException(
            400,
            "Email already exists"
        )

    db_employee = Employee(
        name=employee.name,
        email=employee.email,
        department=employee.department
    )

    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)

    return db_employee


@router.get("")
def get_employees(
    db: Session = Depends(get_db)
):
    return db.query(Employee).all()


@router.put("/{employee_id}")
def update_employee(
    employee_id: int,
    employee: EmployeeCreate,
    db: Session = Depends(get_db)
):

    db_employee = db.query(Employee).filter(
        Employee.id == employee_id
    ).first()

    if not db_employee:
        raise HTTPException(
            404,
            "Employee not found"
        )

    db_employee.name = employee.name
    db_employee.email = employee.email
    db_employee.department = employee.department

    db.commit()

    return {"message": "Employee updated"}


@router.delete("/{employee_id}")
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):

    employee = db.query(Employee).filter(
        Employee.id == employee_id
    ).first()

    if not employee:
        raise HTTPException(
            404,
            "Employee not found"
        )

    db.delete(employee)
    db.commit()

    return {"message": "Employee deleted"}
