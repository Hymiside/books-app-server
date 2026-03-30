from sqlalchemy import String, Date, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base
import datetime


class Reader(Base):
    __tablename__ = "readers"

    id: Mapped[int] = mapped_column(primary_key=True)
    card_number: Mapped[str] = mapped_column(String(20), unique=True, index=True)
    last_name: Mapped[str] = mapped_column(String(100))
    first_name: Mapped[str] = mapped_column(String(100))
    patronymic: Mapped[str] = mapped_column(String(100), default="")
    birth_date: Mapped[datetime.date] = mapped_column(Date)
    address: Mapped[str] = mapped_column(String(300), default="")
    phone: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(150), default="")
    registration_date: Mapped[datetime.date] = mapped_column(Date, default=datetime.date.today)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    issuances: Mapped[list["Issuance"]] = relationship(back_populates="reader")
