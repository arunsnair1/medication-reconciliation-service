import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime
import random

client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client.med_reconciliation

medications = ["aspirin", "metformin", "atorvastatin", "ibuprofen"]

async def seed():
    for patient in range(1, 11):  
        patient_id = str(patient)
        med = random.choice(medications)
        await db.snapshots.insert_one({
            "patient_id": patient_id,
            "version": 1,
            "source": "clinic_emr",
            "medications": [{
                "name": med,
                "dose": 100,
                "unit": "mg",
                "status": "active"
            }],
            "created_at": datetime.utcnow()
        })
        await db.snapshots.insert_one({
            "patient_id": patient_id,
            "version": 2,
            "source": "hospital",
            "medications": [{
                "name": med,
                "dose": random.choice([100, 150]),  
                "unit": "mg",
                "status": "active"
            }],
            "created_at": datetime.utcnow()
        })

    print("seed data inserted")

asyncio.run(seed())