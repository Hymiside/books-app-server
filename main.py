from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import books, readers, issuances

app = FastAPI(title="Library API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:4173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(books.router, prefix="/api")
app.include_router(readers.router, prefix="/api")
app.include_router(issuances.router, prefix="/api")


@app.get("/api/health")
async def health():
    return {"status": "ok"}
