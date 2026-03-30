from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
import datetime
from app.database import get_db
from app.models import Issuance, Book
from app.schemas import IssuanceCreate, IssuanceOut, IssuanceReturn

router = APIRouter(prefix="/issuances", tags=["issuances"])

_load = selectinload(Issuance.book), selectinload(Issuance.reader)


@router.get("/", response_model=list[IssuanceOut])
async def list_issuances(db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(Issuance).options(*_load).order_by(Issuance.issued_at.desc())
    )
    issuances = result.scalars().all()
    today = datetime.date.today()
    for iss in issuances:
        if iss.status == "active" and iss.due_date < today:
            iss.status = "overdue"
    return issuances


@router.post("/", response_model=IssuanceOut, status_code=201)
async def create_issuance(data: IssuanceCreate, db: AsyncSession = Depends(get_db)):
    book = await db.get(Book, data.book_id)
    if not book:
        raise HTTPException(404, "Book not found")
    if book.available_copies < 1:
        raise HTTPException(400, "No available copies")
    book.available_copies -= 1
    iss = Issuance(**data.model_dump(), issued_at=datetime.date.today(), status="active")
    db.add(iss)
    await db.commit()
    await db.refresh(iss)
    result = await db.execute(select(Issuance).options(*_load).where(Issuance.id == iss.id))
    return result.scalar_one()


@router.patch("/{issuance_id}/return", response_model=IssuanceOut)
async def return_book(issuance_id: int, data: IssuanceReturn, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Issuance).options(*_load).where(Issuance.id == issuance_id))
    iss = result.scalar_one_or_none()
    if not iss:
        raise HTTPException(404, "Issuance not found")
    if iss.status == "returned":
        raise HTTPException(400, "Already returned")
    iss.status = "returned"
    iss.returned_at = data.returned_at
    book = await db.get(Book, iss.book_id)
    if book:
        book.available_copies += 1
    await db.commit()
    await db.refresh(iss)
    result = await db.execute(select(Issuance).options(*_load).where(Issuance.id == iss.id))
    return result.scalar_one()
