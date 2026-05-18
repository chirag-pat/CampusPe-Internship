"""
describe.py — POST /describe Route
====================================
Tool-04 | Risk Appetite Framework | AI Developer 1 (route) + AI Developer 3 (middleware)

Generates a professional AI description for a given risk input.
Sanitisation and rate limiting are applied automatically by middleware
registered in app.py — this route only handles business logic.
"""

from flask import Blueprint, g, jsonify
from datetime import datetime, timezone
from auth_middleware import require_auth # For testing only — remove after Day 13 security tests are done

describe_bp = Blueprint("describe", __name__)


@describe_bp.route("/describe", methods=["GET", "POST"])
@require_auth()
def describe():
    """
    POST /describe

    Accepts a JSON body with a risk description and returns an AI-generated
    professional description.

    Request body:
        { "description": "string" }

    Response:
        {
            "result": "AI generated description...",
            "generated_at": "2026-04-18T10:00:00Z",
            "meta": {
                "model_used": "llama-3.3-70b-versatile",
                "cached": false,
                "is_fallback": false
            }
        }
    """
    # g.sanitised_body is set by sanitisation.py middleware
    body = getattr(g, "sanitised_body", {})
    description = body.get("description", "")

    # TODO (AI Developer 1): replace stub with actual Groq call
    # from services.groq_client import GroqClient
    # result = GroqClient().describe(description)

    # Stub response for testing
    result = f"Professional risk description for: {description}" if description else "No description provided."

    return jsonify({
        "result": result,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "meta": {
            "model_used": "llama-3.3-70b-versatile",
            "cached": False,
            "is_fallback": False,
        }
    }), 200