from sqlalchemy import String, Date, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base
import datetime


class Issuance(Base):
    __tablename__ = "issuances"

    id: Mapped[int] = mapped_column(primary_key=True)
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"))
    reader_id: Mapped[int] = mapped_column(ForeignKey("readers.id"))
    issued_at: Mapped[datetime.date] = mapped_column(Date, default=datetime.date.today)
    due_date: Mapped[datetime.date] = mapped_column(Date)
    returned_at: Mapped[datetime.date | None] = mapped_column(Date, nullable=True)
    status: Mapped[str] = mapped_column(String(20), default="active")  # active | returned | overdue
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)

    book: Mapped["Book"] = relationship(back_populates="issuances")
    reader: Mapped["Reader"] = relationship(back_populates="issuances")
