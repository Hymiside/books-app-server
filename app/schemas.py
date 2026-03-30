from pydantic import BaseModel
from datetime import date
from typing import Optional


# Book
class BookBase(BaseModel):
    isbn: str
    title: str
    author: str
    genre: str
    year: int
    publisher: str
    total_copies: int
    available_copies: int
    shelf_location: str
    description: Optional[str] = None


class BookCreate(BookBase):
    pass


class BookUpdate(BookBase):
    pass


class BookOut(BookBase):
    id: int
    created_at: date

    model_config = {"from_attributes": True}


# Reader
class ReaderBase(BaseModel):
    card_number: str
    last_name: str
    first_name: str
    patronymic: str = ""
    birth_date: date
    address: str = ""
    phone: str
    email: str = ""
    registration_date: date
    is_active: bool = True


class ReaderCreate(ReaderBase):
    pass


class ReaderUpdate(ReaderBase):
    pass


class ReaderOut(ReaderBase):
    id: int

    model_config = {"from_attributes": True}


# Issuance
class IssuanceCreate(BaseModel):
    book_id: int
    reader_id: int
    due_date: date
    notes: Optional[str] = None


class IssuanceReturn(BaseModel):
    returned_at: date


class IssuanceOut(BaseModel):
    id: int
    book_id: int
    reader_id: int
    issued_at: date
    due_date: date
    returned_at: Optional[date]
    status: str
    notes: Optional[str]
    book: BookOut
    reader: ReaderOut

    model_config = {"from_attributes": True}
