from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(String)
    status = Column(String, default="Open")
    assigned_to = Column(Integer, ForeignKey("employees.id"), nullable=True)
