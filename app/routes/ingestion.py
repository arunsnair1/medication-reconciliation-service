from fastapi import APIRouter
from app.models.snapshot import SnapshotCreate
from app.services.ingestion_service import IngestionService

router = APIRouter()

@router.post("/patients/{patient_id}/medications")
async def ingest_medications(patient_id: str, payload: SnapshotCreate):
    return await IngestionService.ingest(patient_id, payload.dict())