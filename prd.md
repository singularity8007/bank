# Bank Simulation Project - Product Requirements Document (PRD)

**Project Name:** Educational Bank Simulation  
**Purpose:** Learning project to teach software engineering fundamentals to a 13-year-old.  
**Status:** Active Development (Backend focus)  
**Last Updated:** June 2026

---

## 1. Project Goals

This is **not** a production bank. It is a simplified simulation built for educational purposes.

**Primary Objectives:**
- Learn Python, databases, web APIs, and basic software development discipline.
- Understand core banking concepts (accounts, balances, transactions, double-entry).
- Practice clean code, documentation, testing mindset, and iterative development.
- Build something functional that can later have web, mobile, or desktop frontends.

**Key Constraints (Important):**
- Keep everything **simple and beginner-friendly**.
- One monorepo with clear folder separation.
- Focus on the **backend** first.
- No over-engineering for scalability, security, or "future-proofing".
- No Docker, no heavy CI/CD, no Alembic migrations for now.

---

## 2. Technology Stack

| Area                    | Technology              | Version          | Notes |
|-------------------------|-------------------------|------------------|-------|
| Language                | Python                  | 3.14+            | - |
| Web Framework           | FastAPI                 | 0.137.1          | REST API over HTTP/2 |
| ORM                     | SQLAlchemy              | 2.0.51           | No raw SQL |
| Validation              | Pydantic                | 2.13.4           | - |
| Environment Config      | python-dotenv           | 1.2.2            | Per-folder `.env` files |
| Password Hashing        | argon2-cffi             | 25.1.0           | Argon2id |
| Database                | PostgreSQL              | 18               | - |
| Migrations              | None (for now)          | -                | Use `create_all()` during development |

**Important Rules:**
- No naked/raw SQL.
- No Pandas.
- All frontend clients (future) will consume the REST API. No frontend logic lives in the backend.

---

## 3. Repository Structure

We use **one monorepo** with clear separation:

```
bank-project/
├── backend/          # Current focus - FastAPI application
│   ├── app/
│   │   ├── main.py
│   │   ├── database.py
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── crud/
│   │   ├── routers/
│   │   └── utils/
│   ├── requirements.txt
│   ├── .env
│   └── README.md
├── web-ui/           # Future web frontend (placeholder for now)
├── mobile/           # Future mobile app (placeholder)
├── desktop/          # Future desktop app (placeholder)
├── docs/
│   └── agents.md     # Architecture & structure guide
└── README.md
```

Each presentation layer folder (`web-ui/`, `mobile/`, `desktop/`) can have its own `.env` file when development starts there.

See `agents.md` for detailed responsibilities of each layer.

---

## 4. Core Features (User Stories)

### 4.1 Customer Account
- User can sign up with: FirstName, LastName, Email (username), Phone, SSN (fake ok), DateOfBirth, Address, Password.
- Email is used as the username.
- Passwords are securely hashed.
- Basic validation on signup.

### 4.2 Login / Logout
- Login with Email + Password.
- Server-side sessions stored in database (HTTP-only cookie).
- Logout invalidates the session.

### 4.3 Accounts
- Every customer can have **Checking** and/or **Savings** accounts.
- Two balance columns: `Current_balance` and `Available_balance`.
- External payments/transfers can only come from **Checking** accounts.

### 4.4 Deposits
- Deposit into Checking or Savings.
- Immediately updates **both** Current and Available balances.
- No pending state for deposits.

### 4.5 Withdrawals
- Withdraw from Checking or Savings.
- Must not exceed Available balance.
- Updates both balances immediately.
- Full rollback on failure.

### 4.6 Transfers
- **Internal Transfer**: Between Checking ↔ Savings of the same customer. Updates both balances immediately. Uses double-entry.
- **External Transfer**: From Checking only. 
  - Debit leg applied first → Available balance reduced, Current unchanged → status = `PENDING`.
  - Later settlement updates both balances and sets status = `SETTLED`.
- All money movements must follow **double-entry** principles (debit + credit).

### 4.7 Transaction History
- Every transaction is recorded with status: `PENDING`, `SETTLED`, or `ROLLED_BACK`.
- Full audit log of important events (login, deposit, transfer, etc.).

### 4.8 Close Account
- Can only close an account if balance is zero.
- Account record is kept but marked as closed/inactive.

---

## 5. Key Business Rules

- **Double-Entry Ledger**: Money is never created or destroyed. Every transaction has two sides.
- **Current vs Available Balance**:
  - `Current_balance` = actual settled amount.
  - `Available_balance` = amount that can be spent right now (Current minus pending outgoing transactions).
- **Transaction States**:
  - `PENDING` — External transfer debit applied, credit not yet settled.
  - `SETTLED` — Both legs complete.
  - `ROLLED_BACK` — Transaction failed and reversed.
- **Rollback**: Any failure during a transaction must fully rollback changes.
- **Only Checking** can be source of external transfers/payments.

---

## 6. Architecture & Code Guidelines

- Follow the simple layered structure defined in `agents.md`:
  - `models/` → Database tables
  - `schemas/` → Pydantic validation
  - `crud/` → Business logic + database operations
  - `routers/` → API endpoints (thin)
- Use database transactions for atomic operations.
- All code must be well documented with docstrings and comments.
- Keep functions small and focused.
- Start simple. Add complexity only when needed for learning.

**Non-Goals (Do NOT implement these now):**
- Advanced security (2FA, rate limiting, encryption at rest, etc.)
- Background job processing / scheduled tasks
- Real money or integration with payment gateways
- Complex reporting or admin dashboards
- Docker / Kubernetes / CI-CD pipelines
- Alembic database migrations
- Heavy design patterns or "agentic" architectures

---

## 7. Development Approach

1. Build the backend first using the structure in `agents.md`.
2. Get core flows working end-to-end (signup → login → account → deposit/withdraw/transfer).
3. Keep the code clean and well-commented.
4. Once backend is stable, we can decide on a simple frontend (start with plain HTML/JS if desired).
5. Iterate and improve based on what we learn.

---

## 8. Success Criteria

- A working backend where a user can:
  - Create an account and log in
  - Open Checking and Savings accounts
  - Deposit, withdraw, and transfer money (internal + external with pending state)
  - See proper balance updates and transaction history
- All money movements follow double-entry rules with proper rollbacks.
- Code is understandable by a beginner developer.
- Project follows the folder structure and technology choices defined above.

---

This PRD is intentionally kept focused and simple to avoid scope creep and rabbit holes during development.

For architecture details and folder responsibilities, always refer to the latest `agents.md`.