from pydantic import BaseModel
from typing import List
from app.models.medication import Medication

class SnapshotCreate(BaseModel):
    source: str
    medications: List[Medication]