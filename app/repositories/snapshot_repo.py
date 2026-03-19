from app.db.mongo import db

class SnapshotRepository:

    @staticmethod
    async def get_latest_version(patient_id: str):
        doc = await db.snapshots.find_one(
            {"patient_id": patient_id},
            sort=[("version", -1)]
        )
        return doc.get("version", 0) if doc else 0

    @staticmethod
    async def create(snapshot: dict):
        result = await db.snapshots.insert_one(snapshot)
        return str(result.inserted_id)
    
    @staticmethod
    async def get_latest_snapshot(patient_id: str):
        return await db.snapshots.find_one(
            {"patient_id": patient_id},
            sort=[("version", -1)]
        )