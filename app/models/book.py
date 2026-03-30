from sqlalchemy import String, Integer, Text, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base
import datetime


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    isbn: Mapped[str] = mapped_column(String(20), unique=True, index=True)
    title: Mapped[str] = mapped_column(String(300))
    author: Mapped[str] = mapped_column(String(200))
    genre: Mapped[str] = mapped_column(String(100))
    year: Mapped[int] = mapped_column(Integer)
    publisher: Mapped[str] = mapped_column(String(200))
    total_copies: Mapped[int] = mapped_column(Integer, default=1)
    available_copies: Mapped[int] = mapped_column(Integer, default=1)
    shelf_location: Mapped[str] = mapped_column(String(50))
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime.date] = mapped_column(Date, default=datetime.date.today)

    issuances: Mapped[list["Issuance"]] = relationship(back_populates="book")
