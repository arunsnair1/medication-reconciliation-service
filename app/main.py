from fastapi import FastAPI
from app.db.mongo import db
from app.routes.ingestion import router as ingestion_router
from app.routes.reports import router as report_router
from app.routes.conflicts import router as conflict_router




app = FastAPI()

app.include_router(ingestion_router)
app.include_router(report_router)
app.include_router(conflict_router)

@app.get("/")
async def root():
    collections = await db.list_collection_names()
    return {
        "message": "API is working",
        "collections": collections
    }