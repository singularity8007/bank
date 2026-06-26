# Bank Backend

This is the FastAPI backend for the educational bank simulation project.

## How to run

1. Create a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate     # Linux/Mac
   
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Copy `.env.example` to `.env` and fill in your database credentials.

4. Run the server:
   ```bash
   uvicorn app.main:app --reload
   ```

Visit http://127.0.0.1:8000/docs for the interactive API documentation.
