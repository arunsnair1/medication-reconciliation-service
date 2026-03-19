from fastapi import APIRouter
from app.db.mongo import db

router = APIRouter()

@router.get("/reports/unresolved-conflicts")
async def get_unresolved_conflicts():
    pipeline = [
        {"$match": {"status": "unresolved"}},
        {"$group": {
            "_id": "$patient_id",
            "count": {"$sum": 1}
        }}
    ]

    results = []
    async for doc in db.conflicts.aggregate(pipeline):
        results.append(doc)

    return results