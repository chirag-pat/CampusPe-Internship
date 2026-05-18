"""
query.py — POST /query Route
Tool-04 | Risk Appetite Framework | AI Developer 2
RAG pipeline — embed question, retrieve ChromaDB chunks, return answer + sources.
"""

from flask import Blueprint, g, jsonify
from datetime import datetime, timezone

query_bp = Blueprint("query", __name__)


@query_bp.route("/query", methods=["POST"])
def query():
    """
    POST /query

    Embeds a question, retrieves top-3 ChromaDB chunks as context,
    calls Groq, and returns the answer with source references.

    Request body:
        { "question": "string" }

    Response:
        {
            "answer": "string",
            "sources": ["chunk1...", "chunk2...", "chunk3..."],
            "generated_at": "...",
            "meta": { ... }
        }
    """
    body = getattr(g, "sanitised_body", {})
    question = body.get("question", "")

    # TODO (AI Developer 2): replace stub with actual ChromaDB + Groq RAG call
    # from services.chroma_client import ChromaClient
    # from services.groq_client import GroqClient
    # chunks = ChromaClient().query(question, n_results=3)
    # answer = GroqClient().answer_with_context(question, chunks)

    return jsonify({
        "answer": f"Stub RAG answer for: {question}",
        "sources": [
            "Source chunk 1 — replace with ChromaDB result",
            "Source chunk 2 — replace with ChromaDB result",
            "Source chunk 3 — replace with ChromaDB result",
        ],
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "meta": {
            "model_used": "llama-3.3-70b-versatile",
            "cached": False,
            "is_fallback": False,
            "chunks_retrieved": 3,
        }
    }), 200