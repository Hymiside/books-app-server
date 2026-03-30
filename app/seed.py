"""Run once: uv run python -m app.seed"""
import asyncio
import datetime
from app.database import AsyncSessionLocal, engine, Base
from app.models import Book, Reader, Issuance


BOOKS = [
    dict(isbn="978-5-389-06178-4", title="Поединок", author="Куприн А.И.", genre="Роман", year=2015, publisher="Азбука", total_copies=5, available_copies=3, shelf_location="А-1-01"),
    dict(isbn="978-5-389-07234-1", title="Гранатовый браслет", author="Куприн А.И.", genre="Повесть", year=2018, publisher="Азбука", total_copies=4, available_copies=2, shelf_location="А-1-02"),
    dict(isbn="978-5-389-08901-1", title="Олеся", author="Куприн А.И.", genre="Повесть", year=2019, publisher="Азбука", total_copies=3, available_copies=3, shelf_location="А-1-03"),
    dict(isbn="978-5-17-077348-8", title="Война и мир", author="Толстой Л.Н.", genre="Роман-эпопея", year=2020, publisher="АСТ", total_copies=6, available_copies=4, shelf_location="Т-2-01"),
    dict(isbn="978-5-699-12345-6", title="Преступление и наказание", author="Достоевский Ф.М.", genre="Роман", year=2017, publisher="Эксмо", total_copies=5, available_copies=1, shelf_location="Д-3-01"),
    dict(isbn="978-5-699-54321-0", title="Мастер и Маргарита", author="Булгаков М.А.", genre="Роман", year=2021, publisher="Эксмо", total_copies=7, available_copies=5, shelf_location="Б-4-01"),
    dict(isbn="978-5-389-03402-3", title="Евгений Онегин", author="Пушкин А.С.", genre="Поэма", year=2016, publisher="Азбука", total_copies=4, available_copies=4, shelf_location="П-5-01"),
    dict(isbn="978-5-04-089765-2", title="Мёртвые души", author="Гоголь Н.В.", genre="Поэма", year=2019, publisher="Эксмо", total_copies=3, available_copies=2, shelf_location="Г-6-01"),
    dict(isbn="978-5-17-112233-4", title="Три сестры", author="Чехов А.П.", genre="Пьеса", year=2022, publisher="АСТ", total_copies=2, available_copies=2, shelf_location="Ч-7-01"),
    dict(isbn="978-5-389-05678-0", title="Анна Каренина", author="Толстой Л.Н.", genre="Роман", year=2020, publisher="Азбука", total_copies=4, available_copies=0, shelf_location="Т-2-02"),
    dict(isbn="978-5-699-87654-3", title="Идиот", author="Достоевский Ф.М.", genre="Роман", year=2018, publisher="Эксмо", total_copies=3, available_copies=3, shelf_location="Д-3-02"),
    dict(isbn="978-5-17-099887-6", title="Вишнёвый сад", author="Чехов А.П.", genre="Пьеса", year=2021, publisher="АСТ", total_copies=2, available_copies=1, shelf_location="Ч-7-02"),
]

READERS = [
    dict(card_number="ЧБ-0001", last_name="Иванова", first_name="Мария", patronymic="Петровна", birth_date=datetime.date(1985,3,15), address="г. Пермь, ул. Ленина, д. 10, кв. 5", phone="+7 (342) 201-11-11", email="ivanova@mail.ru", registration_date=datetime.date(2020,9,1)),
    dict(card_number="ЧБ-0002", last_name="Петров", first_name="Алексей", patronymic="Николаевич", birth_date=datetime.date(1990,7,22), address="г. Пермь, ул. Пушкина, д. 3, кв. 12", phone="+7 (342) 202-22-22", email="petrov@gmail.com", registration_date=datetime.date(2021,1,15)),
    dict(card_number="ЧБ-0003", last_name="Сидорова", first_name="Елена", patronymic="Владимировна", birth_date=datetime.date(2000,11,30), address="г. Пермь, ул. Советская, д. 45, кв. 8", phone="+7 (342) 203-33-33", email="sidorova@yandex.ru", registration_date=datetime.date(2022,3,10)),
    dict(card_number="ЧБ-0004", last_name="Козлов", first_name="Дмитрий", patronymic="Сергеевич", birth_date=datetime.date(1978,5,18), address="г. Пермь, ул. Мира, д. 7, кв. 22", phone="+7 (342) 204-44-44", email="kozlov@mail.ru", registration_date=datetime.date(2019,6,20)),
    dict(card_number="ЧБ-0005", last_name="Новикова", first_name="Ольга", patronymic="Андреевна", birth_date=datetime.date(1995,9,5), address="г. Пермь, ул. Комсомольская, д. 15, кв. 3", phone="+7 (342) 205-55-55", email="novikova@inbox.ru", registration_date=datetime.date(2022,9,1)),
    dict(card_number="ЧБ-0006", last_name="Морозов", first_name="Игорь", patronymic="Александрович", birth_date=datetime.date(1988,12,1), address="г. Пермь, ул. Екатерининская, д. 88, кв. 14", phone="+7 (342) 206-66-66", email="morozov@gmail.com", registration_date=datetime.date(2021,5,12)),
    dict(card_number="ЧБ-0007", last_name="Волкова", first_name="Татьяна", patronymic="Ивановна", birth_date=datetime.date(2003,2,14), address="г. Пермь, ул. Луначарского, д. 33, кв. 7", phone="+7 (342) 207-77-77", email="volkova@mail.ru", registration_date=datetime.date(2023,1,8)),
    dict(card_number="ЧБ-0008", last_name="Соколов", first_name="Павел", patronymic="Геннадьевич", birth_date=datetime.date(1972,8,27), address="г. Пермь, ул. Газеты Звезда, д. 51, кв. 19", phone="+7 (342) 208-88-88", email="sokolov@yandex.ru", registration_date=datetime.date(2018,11,30), is_active=False),
    dict(card_number="ЧБ-0009", last_name="Лебедева", first_name="Наталья", patronymic="Михайловна", birth_date=datetime.date(1993,4,9), address="г. Пермь, ул. Революции, д. 22, кв. 11", phone="+7 (342) 209-99-99", email="lebedeva@inbox.ru", registration_date=datetime.date(2023,4,1)),
    dict(card_number="ЧБ-0010", last_name="Никитин", first_name="Сергей", patronymic="Владимирович", birth_date=datetime.date(1981,6,16), address="г. Пермь, пр. Парковый, д. 2, кв. 34", phone="+7 (342) 210-10-10", email="nikitin@mail.ru", registration_date=datetime.date(2020,2,14)),
]


async def main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with AsyncSessionLocal() as db:
        # skip if already seeded
        from sqlalchemy import select, func
        count = await db.scalar(select(func.count()).select_from(Book))
        if count:
            print("Already seeded")
            return

        books = [Book(**b) for b in BOOKS]
        db.add_all(books)
        await db.flush()

        readers = [Reader(**r) for r in READERS]
        db.add_all(readers)
        await db.flush()

        b = {book.isbn: book for book in books}
        r = readers

        issuances = [
            Issuance(book_id=b["978-5-389-06178-4"].id, reader_id=r[0].id, issued_at=datetime.date(2026,3,1), due_date=datetime.date(2026,3,22), status="active"),
            Issuance(book_id=b["978-5-389-07234-1"].id, reader_id=r[1].id, issued_at=datetime.date(2026,2,15), due_date=datetime.date(2026,3,8), status="overdue"),
            Issuance(book_id=b["978-5-699-12345-6"].id, reader_id=r[2].id, issued_at=datetime.date(2026,3,10), due_date=datetime.date(2026,3,31), status="active"),
            Issuance(book_id=b["978-5-389-05678-0"].id, reader_id=r[3].id, issued_at=datetime.date(2026,3,5), due_date=datetime.date(2026,3,26), status="active"),
            Issuance(book_id=b["978-5-389-05678-0"].id, reader_id=r[4].id, issued_at=datetime.date(2026,3,12), due_date=datetime.date(2026,4,2), status="active"),
            Issuance(book_id=b["978-5-17-077348-8"].id, reader_id=r[5].id, issued_at=datetime.date(2026,3,15), due_date=datetime.date(2026,4,5), status="active"),
            Issuance(book_id=b["978-5-699-54321-0"].id, reader_id=r[6].id, issued_at=datetime.date(2026,2,10), due_date=datetime.date(2026,3,3), returned_at=datetime.date(2026,3,2), status="returned"),
            Issuance(book_id=b["978-5-389-08901-1"].id, reader_id=r[7].id, issued_at=datetime.date(2026,1,20), due_date=datetime.date(2026,2,10), returned_at=datetime.date(2026,2,9), status="returned"),
            Issuance(book_id=b["978-5-04-089765-2"].id, reader_id=r[8].id, issued_at=datetime.date(2026,3,20), due_date=datetime.date(2026,4,10), status="active"),
            Issuance(book_id=b["978-5-17-099887-6"].id, reader_id=r[9].id, issued_at=datetime.date(2026,1,5), due_date=datetime.date(2026,1,26), returned_at=datetime.date(2026,1,25), status="returned"),
        ]
        db.add_all(issuances)
        await db.commit()
        print("Seeded successfully")


asyncio.run(main())
