from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.database import get_db
from app.models import Reader
from app.schemas import ReaderCreate, ReaderOut, ReaderUpdate

router = APIRouter(prefix="/readers", tags=["readers"])


@router.get("/", response_model=list[ReaderOut])
async def list_readers(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Reader).order_by(Reader.last_name))
    return result.scalars().all()


@router.post("/", response_model=ReaderOut, status_code=201)
async def create_reader(data: ReaderCreate, db: AsyncSession = Depends(get_db)):
    reader = Reader(**data.model_dump())
    db.add(reader)
    await db.commit()
    await db.refresh(reader)
    return reader


@router.put("/{reader_id}", response_model=ReaderOut)
async def update_reader(reader_id: int, data: ReaderUpdate, db: AsyncSession = Depends(get_db)):
    reader = await db.get(Reader, reader_id)
    if not reader:
        raise HTTPException(404, "Reader not found")
    for k, v in data.model_dump().items():
        setattr(reader, k, v)
    await db.commit()
    await db.refresh(reader)
    return reader


@router.delete("/{reader_id}", status_code=204)
async def delete_reader(reader_id: int, db: AsyncSession = Depends(get_db)):
    reader = await db.get(Reader, reader_id)
    if not reader:
        raise HTTPException(404, "Reader not found")
    await db.delete(reader)
    await db.commit()
