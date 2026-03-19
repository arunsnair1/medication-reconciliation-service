# Medication Reconciliation Service

A backend service for ingesting patient medication data from multiple sources, detecting conflicts, and managing their resolution.

---

## 🚀 Live Demo

API Documentation (Swagger UI):
👉 https://medication-reconciliation-service-1.onrender.com/docs

---

## ⚙️ Setup Instructions (Run Locally)

```bash
# Clone the repository
git clone <your-repo-link>
cd medication-reconciliation-service

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Set environment variable
set MONGO_URL=your_mongodb_atlas_url

# Run the server
uvicorn app.main:app --reload
```

---

## Architecture Overview

The service follows a layered architecture:

* **Routes** → API endpoints (FastAPI)
* **Services** → Business logic (ingestion, conflict detection)
* **Repositories** → Database interaction (MongoDB)
* **Models/Schemas** → Data validation (Pydantic)

### Flow:

1. Client sends medication data
2. Service compares with latest snapshot
3. Conflicts are detected
4. New snapshot stored with versioning
5. Conflicts stored separately for tracking

---

## Assumptions & Trade-offs

* Conflict detection is based on simple field comparison (e.g., dose mismatch)
* Versioning is linear (no branching/merging of histories)
* No authentication added to keep scope focused
* MongoDB chosen for flexibility with nested medication data

---

## Known Limitations & Future Improvements

* No user authentication / authorization
* Conflict resolution is manual only
* No pagination for reports
* No advanced conflict rules (e.g., drug interactions)

### Next Steps:

* Add auth (JWT)
* Improve conflict detection rules
* Add audit logs
* Deploy with Docker for portability

---

## Seed Data

You can populate sample data using:

```bash
python scripts/seed.py
```

---

## Tests

Run tests with:

```bash
pytest
```

Covers core ingestion and conflict detection logic.

---

## AI Usage

AI tools were used to:

* Speed up boilerplate setup (FastAPI structure, initial scaffolding)
* Assist in refining architecture and edge-case handling

### Manual Work:

* Designed overall architecture and data flow
* Implemented conflict detection and versioning logic
* Structured repositories and services cleanly


---

## Tech Stack

* FastAPI
* MongoDB (Atlas)
* Motor (async MongoDB driver)
* Pydantic
* Pytest

---

## Deployment

* Hosted on Render
* Uses MongoDB Atlas for cloud database
* Environment-based configuration for production readiness

---

## Key Features

* Medication ingestion with versioning
* Conflict detection across sources
* Conflict storage and resolution
* Reporting of unresolved conflicts
* Fully async backend

---

## Author

Arun S Nair
