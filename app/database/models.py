from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text, Float, DateTime

from app.database.database import Base



class RequestRecord(Base):

    __tablename__ = "requests"

    id: Mapped[int] = mapped_column(
        primary_key=True, 
        autoincrement=True
    )

    title: Mapped[str] = mapped_column(
        String(255), 
        nullable=False
    )

    description: Mapped[str] = mapped_column(
        Text, 
        nullable=False
    )

    category: Mapped[str | None] = mapped_column(
        String(100), 
        nullable=True
    )

    priority: Mapped[str | None] = mapped_column(
        String(50), 
        nullable=True
    )

    escalation_probability: Mapped[float | None] = mapped_column(
        Float, 
        nullable=True
    )

    workflow_state: Mapped[str | None] = mapped_column(
        String(50), 
        nullable=True
    )

    assigned_team: Mapped[str | None] = mapped_column(
        String(100), 
        nullable=True
    )

    workflow_action: Mapped[str | None] = mapped_column(
        String(100), 
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime, 
        default=datetime.utcnow, 
        nullable=False
    )