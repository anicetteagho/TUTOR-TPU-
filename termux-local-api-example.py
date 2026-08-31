#!/usr/bin/env python3
"""
SYCAM-PUB — API locale Termux (exemple minimal)
Usage:
  pip install fastapi uvicorn
  uvicorn termux-local-api-example:app --host 127.0.0.1 --port 8765

Uniquement loopback. Pas de clé cloud. L'UI SYCAM s'y rattache à la demande.
"""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

try:
    from fastapi import FastAPI
    from pydantic import BaseModel
except ImportError:
    raise SystemExit("pip install fastapi uvicorn")

app = FastAPI(title="SYCAM Termux Local API", version="217")

FEED: List[Dict[str, Any]] = []
PENDING: Dict[str, Dict[str, Any]] = {}


class NotificationPayload(BaseModel):
    source: str
    title: str = ""
    content: str = ""
    timestamp: Optional[int] = None


@app.get("/api/healthz")
def healthz():
    return {
        "status": "ok",
        "service": "sycam-termux-local",
        "host": "127.0.0.1",
        "attached": True,
    }


@app.get("/api/version")
def version():
    return {"version": "217", "sycam_pub": True, "termux_local": True}


@app.post("/api/jarvis")
def jarvis(body: Dict[str, Any]):
    text = str(body.get("text") or "")
    task = str(body.get("task") or "summarize")
    return {
        "ok": True,
        "provider": "termux-local",
        "task": task,
        "result": text.replace("\n", " ").strip()[:280] or "(vide)",
    }


@app.post("/ingest/notification")
def ingest(payload: NotificationPayload):
    card_id = f"n_{int(datetime.now(tz=timezone.utc).timestamp())}"
    item = {
        "id": card_id,
        "source": payload.source,
        "title": payload.title,
        "content": payload.content,
        "timestamp": payload.timestamp or int(datetime.now(tz=timezone.utc).timestamp() * 1000),
        "requires_approval": True,
        "summary": f"{payload.title}: {payload.content}"[:160],
    }
    FEED.insert(0, item)
    PENDING[card_id] = item
    return {
        "action": "ask_user",
        "summary": item["summary"],
        "card_id": card_id,
        "requires_approval": True,
    }


@app.get("/feed")
def feed():
    return {"items": FEED[:50]}


@app.post("/approve/{card_id}")
def approve(card_id: str):
    action = PENDING.pop(card_id, None)
    if not action:
        return {"executed": False, "error": "unknown_card"}
    # L'UI native ouvrirait l'app via Intent — ici on renvoie le package source
    return {
        "executed": True,
        "intent_package": action.get("source"),
        "intent_uri": None,
        "card_id": card_id,
    }
