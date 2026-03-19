from app.db.mongo import db
from datetime import datetime

class ConflictRepository:

    @staticmethod
    async def create_many(conflicts: list, patient_id: str):
        docs = []

        for c in conflicts:
            doc = {
                "patient_id": patient_id,
                "type": c["type"],
                "drug": c["drug"],
                "details": c,
                "status": "unresolved",
                "created_at": datetime.utcnow()
            }
            docs.append(doc)

        if docs:
            await db.conflicts.insert_many(docs)