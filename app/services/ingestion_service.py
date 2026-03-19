from datetime import datetime
from app.repositories.snapshot_repo import SnapshotRepository
from app.services.conflict_service import detect_conflicts
from app.repositories.conflict_repo import ConflictRepository

class IngestionService:

    @staticmethod
    async def ingest(patient_id: str, data: dict):

        latest_snapshot = await SnapshotRepository.get_latest_snapshot(patient_id)

        latest_version = latest_snapshot["version"] if latest_snapshot else 0
        new_version = latest_version + 1

        conflicts = []

        if latest_snapshot:
            conflicts = detect_conflicts(
                latest_snapshot["medications"],
                data["medications"]
            )

        snapshot = {
            "patient_id": patient_id,
            "source": data["source"],
            "version": new_version,
            "medications": data["medications"],
            "conflicts": conflicts,
            "created_at": datetime.utcnow()
        }

        snapshot_id = await SnapshotRepository.create(snapshot)
        
        if conflicts:
            await ConflictRepository.create_many(conflicts, patient_id)

        return {
            "message": "Snapshot stored",
            "version": new_version,
            "conflicts": conflicts
        }