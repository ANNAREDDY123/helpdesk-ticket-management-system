from fastapi import FastAPI

from database import engine, Base

from models.user import User
from models.employee import Employee
from models.ticket import Ticket

from routers.auth import router as auth_router
from routers.employee import router as employee_router
from routers.ticket import router as ticket_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Helpdesk Ticket Management System"
)

app.include_router(auth_router)
app.include_router(employee_router)
app.include_router(ticket_router)


@app.get("/")
def home():
    return {
        "message":
        "Helpdesk Ticket Management System"}
