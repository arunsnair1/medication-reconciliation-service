from fastapi import APIRouter
from app.db.mongo import db
from datetime import datetime
from bson import ObjectId

router = APIRouter()

@router.patch("/conflicts/{conflict_id}/resolve")
async def resolve_conflict(conflict_id: str):

    result = await db.conflicts.update_one(
        {"_id": ObjectId(conflict_id)},
        {
            "$set": {
                "status": "resolved",
                "resolved_at": datetime.utcnow(),
                "resolution_reason": "manual review"
            }
        }
    )

    return {"message": "Conflict resolved"}