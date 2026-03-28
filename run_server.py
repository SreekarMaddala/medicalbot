"""Run the FastAPI medical recommendation server (from repo root)."""

import uvicorn

if __name__ == "__main__":
    uvicorn.run("backend.app.main:app", host="127.0.0.1", port=8000, reload=True)
