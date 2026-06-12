from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models.ticket import Ticket
from models.employee import Employee
from schemas.ticket import TicketCreate, TicketUpdate

router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"]
)


@router.post("")
def create_ticket(
    ticket: TicketCreate,
    db: Session = Depends(get_db)
):

    db_ticket = Ticket(
        title=ticket.title,
        description=ticket.description,
        priority=ticket.priority,
        status="Open"
    )

    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)

    return db_ticket


@router.get("")
def get_tickets(
    db: Session = Depends(get_db)
):
    return db.query(Ticket).all()


@router.get("/{ticket_id}")
def get_ticket(
    ticket_id: int,
    db: Session = Depends(get_db)
):

    ticket = db.query(Ticket).filter(
        Ticket.id == ticket_id
    ).first()

    if not ticket:
        raise HTTPException(
            404,
            "Ticket not found"
        )

    return ticket


@router.put("/{ticket_id}")
def update_ticket(
    ticket_id: int,
    ticket: TicketUpdate,
    db: Session = Depends(get_db)
):

    db_ticket = db.query(Ticket).filter(
        Ticket.id == ticket_id
    ).first()

    if not db_ticket:
        raise HTTPException(
            404,
            "Ticket not found"
        )

    db_ticket.status = ticket.status

    db.commit()

    return {"message": "Ticket updated"}


@router.delete("/{ticket_id}")
def delete_ticket(
    ticket_id: int,
    db: Session = Depends(get_db)
):

    ticket = db.query(Ticket).filter(
        Ticket.id == ticket_id
    ).first()

    if not ticket:
        raise HTTPException(
            404,
            "Ticket not found"
        )

    db.delete(ticket)
    db.commit()

    return {"message": "Ticket deleted"}


@router.post("/{ticket_id}/assign/{employee_id}")
def assign_ticket(
    ticket_id: int,
    employee_id: int,
    db: Session = Depends(get_db)
):

    ticket = db.query(Ticket).filter(
        Ticket.id == ticket_id
    ).first()

    employee = db.query(Employee).filter(
        Employee.id == employee_id
    ).first()

    if not ticket:
        raise HTTPException(404, "Ticket not found")

    if not employee:
        raise HTTPException(404, "Employee not found")

    ticket.assigned_to = employee_id

    db.commit()

    return {"message": "Ticket assigned"}


@router.get("/employee/{employee_id}")
def employee_tickets(
    employee_id: int,
    db: Session = Depends(get_db)
):

    return db.query(Ticket).filter(
        Ticket.assigned_to == employee_id
    ).all()
