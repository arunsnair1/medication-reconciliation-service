# Medication Reconciliation & Conflict Reporting Service

##  Overview

Backend service to ingest medication lists from multiple sources, detect conflicts, maintain versioned history, and support resolution + reporting.

---

##  Setup 

```bash
git clone <repo-url>
cd med-reconciliation-service
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open: http://127.0.0.1:8000/docs

---

##  Architecture

```
Routes → Services → Repositories → MongoDB
```

* Routes: API endpoints
* Services: business logic (versioning, conflict detection)
* Repositories: DB access
* MongoDB: snapshots + conflicts

---

##  Data Model

### Snapshots

* versioned medication history per patient
* append-only (no overwrite)

### Conflicts

* stored separately for querying/reporting
* fields: patient_id, drug, type, status, timestamps

---

##  API

* `POST /patients/{id}/medications` → ingest + detect conflicts
* `GET /reports/unresolved-conflicts` → aggregation report
* `PATCH /conflicts/{id}/resolve` → mark resolved

---

##  Seed Data

```bash
python scripts/seed.py
```

Creates 10+ patients with varied conflicts.

---

##  Tests

```bash
pytest
```

Covers ingestion flow (core domain logic).

---

##  Assumptions & Trade-offs

* No single “truth source” → latest snapshot used for comparison
* Conflict detection limited to:

  * dose mismatch
  * status mismatch
* Used MongoDB (schema flexibility, faster iteration)
* Denormalized snapshots for simplicity vs strict normalization

---

## Limitations / Next Steps

* No drug interaction rules (only basic conflicts)
* No authentication / multi-user handling
* No severity prioritization
* Would add:

  * rule engine (drug classes, blacklists)
  * better normalization layer
  * UI/dashboard



## AI Usage

Used AI for:

* initial boilerplate setup (FastAPI structure)
* debugging environment/setup issues

Manually implemented/refined:

* data model design
* versioning strategy
* conflict detection logic
* separation of snapshot vs conflict storage


---

## Author

Arun S Nair
