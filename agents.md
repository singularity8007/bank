# Bank Project - Project Structure (agents.md)

This document describes the simple architecture and folder structure for our educational bank simulation project.

**Important Goal**: This is a learning project for a 13-year-old. We prioritize **clarity, simplicity, and good habits** over advanced architecture patterns. We want clean, well-documented code that is easy to understand and modify.

We are building a basic REST API backend that mimics real bank behavior (no real money). The system uses double-entry accounting, current vs available balances, and proper transaction handling with rollbacks.

---

## 1. Repository Approach: One Monorepo

We keep **everything in a single Git repository** with clear folder separation.

This makes it easy to manage while still allowing future separation if needed.

### Recommended Folder Structure

```
bank-project/
├── backend/                     # ← Current main focus (FastAPI + business logic)
│   ├── app/
│   │   ├── main.py              # FastAPI application entry point
│   │   ├── database.py          # Database connection and session handling
│   │   ├── models/              # SQLAlchemy database models
│   │   ├── schemas/             # Pydantic request/response models
│   │   ├── crud/                # Database operations (Create, Read, Update, Delete)
│   │   ├── routers/             # FastAPI API endpoints (routes)
│   │   ├── utils/               # Helper functions (password hashing, validators)
│   │   └── dependencies.py      # Common dependencies (DB session, current user)
│   ├── requirements.txt
│   ├── .env                     # Backend-specific configuration (DB URL, secrets)
│   └── README.md
│
├── web-ui/                      # Placeholder for future Web UI (React, Vue, or plain HTML/JS)
│   ├── README.md
│   └── .env                     # (only if needed later)
│
├── mobile/                      # Placeholder for future Mobile app (Flutter, React Native, etc.)
│   ├── README.md
│   └── .env
│
├── desktop/                     # Placeholder for future Desktop app
│   ├── README.md
│   └── .env
│
├── docs/
│   └── agents.md                # This file
│
├── README.md                    # Main project README
└── .gitignore
```

**Why this structure?**
- Backend is fully isolated.
- Each presentation layer (web, mobile, desktop) has its own folder and can have its own configuration.
- Keeps the project simple while remaining flexible.
- Easy to understand for a beginner.

---

## 2. Technology Stack (Latest Stable Versions - June 2026)

| Component              | Library / Tool          | Recommended Version      | Notes |
|------------------------|-------------------------|--------------------------|-------|
| Language               | Python                  | 3.14+                    | Use latest stable |
| Web Framework          | FastAPI                 | **0.137.1**              | Modern, fast, excellent docs |
| Database ORM           | SQLAlchemy              | **2.0.51**               | Stable & mature. Avoid 2.1 beta for now |
| Data Validation        | Pydantic                | **2.13.4**               | Excellent with FastAPI |
| Environment Variables  | python-dotenv           | **1.2.2**                | For loading `.env` files |
| Password Hashing       | argon2-cffi             | **25.1.0**               | Modern & secure recommendation (Argon2id) |
| Database               | PostgreSQL              | 18                       | As specified |

**Notes on choices**:
- We use **argon2-cffi** for password hashing because it is currently the recommended secure algorithm (Argon2id).
- We avoid raw SQL — everything goes through SQLAlchemy.
- No Alembic migrations for now (keep it simple). We can use `create_all()` during early development.
- No Docker, no heavy CI/CD, no Pandas.

---

## 3. Architecture Layers (Simple & Clear)

We follow a **standard layered architecture** that is easy to learn:

### Layer 1: Models (`backend/app/models/`)
- Define database tables using SQLAlchemy.
- Based on the provided SQL files (`Customers`, `Account`, `Transaction`, `Session`).
- Add relationships between tables here.

### Layer 2: Schemas (`backend/app/schemas/`)
- Define the shape of data for API requests and responses using Pydantic.
- Used for validation (e.g., amount must be > 0, required fields, etc.).

### Layer 3: CRUD (`backend/app/crud/`)
- All functions that interact with the database.
- Contains the core business logic (deposits, withdrawals, transfers, double-entry logic, balance updates).
- Handles database transactions and rollbacks.

### Layer 4: Routers (`backend/app/routers/`)
- FastAPI route definitions (the actual API endpoints).
- Thin layer: receives request → calls CRUD functions → returns response.
- Handles authentication via sessions.

### Supporting Files
- `database.py` — Creates the database engine and session.
- `dependencies.py` — Provides database session and current logged-in user to routes.
- `utils/` — Password hashing, input validation helpers.

---

## 4. Configuration Management

Each major folder can have its own `.env` file:

- `backend/.env` → Database connection string, secret keys, etc.
- `web-ui/.env`, `mobile/.env`, `desktop/.env` → Created only when those parts are developed.

This keeps configuration isolated and simple.

Example `backend/.env`:
```env
DATABASE_URL=postgresql://user:password@localhost:5432/bankdb
SECRET_KEY=your-super-secret-key-here
```

---

## 5. Key Learning Concepts

As we build, we will focus on these important ideas:

- **Database Transactions** — Using `with db.begin():` so everything succeeds or everything rolls back.
- **Double-Entry Ledger** — Every money movement creates two records (debit + credit).
- **Current vs Available Balance** — Understanding pending transactions.
- **Session-based Authentication** — Login creates a server-side session (HTTP-only cookie).
- **Input Validation** — Never trust user input.
- **Clean Code & Documentation** — Good variable names, docstrings, and comments.

---

## 6. Development Guidelines

1. Start simple. Get one feature working end-to-end before adding more.
2. Write clear comments explaining *why* something is done.
3. Use type hints everywhere.
4. Test manually first, then consider adding simple tests later.
5. Commit your work to Git regularly.
6. Ask questions when stuck — this is how you learn.

---

## 7. Recommended Development Order

1. Set up the project structure and virtual environment.
2. Create database models from the provided SQL files.
3. Implement customer signup + login (with password hashing).
4. Add account creation (Checking & Savings).
5. Build deposit and withdrawal functionality.
6. Implement internal transfers (Checking ↔ Savings).
7. Add external transfers with pending state + double-entry.
8. Add session management and protected routes.
9. (Later) Build a simple frontend in the `web-ui/` folder.

---

This structure gives us a solid foundation while staying beginner-friendly.

We can always improve it later as understanding grows.

---

**End of agents.md**

*Last updated: June 2026*