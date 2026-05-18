"""
recommend.py — POST /recommend Route
======================================
Tool-04 | Risk Appetite Framework | AI Developer 1 (route) + AI Developer 3 (middleware)

Returns 3 actionable recommendations for a given risk input.
"""

from flask import Blueprint, g, jsonify
from datetime import datetime, timezone

recommend_bp = Blueprint("recommend", __name__)


@recommend_bp.route("/recommend", methods=["GET", "POST"])
def recommend():
    """
    POST /recommend

    Returns 3 actionable recommendations as a JSON array.

    Request body:
        { "description": "string", "category": "string" }

    Response:
        {
            "recommendations": [
                {
                    "action_type": "string",
                    "description": "string",
                    "priority": "HIGH|MEDIUM|LOW"
                }
            ],
            "generated_at": "2026-04-18T10:00:00Z",
            "meta": { ... }
        }
    """
    body = getattr(g, "sanitised_body", {})
    description = body.get("description", "")

    # TODO (AI Developer 1): replace stub with actual Groq call
    # from services.groq_client import GroqClient
    # recommendations = GroqClient().recommend(description)

    # Stub response for testing
    recommendations = [
        {
            "action_type": "Mitigate",
            "description": f"Implement controls to reduce exposure for: {description}",
            "priority": "HIGH"
        },
        {
            "action_type": "Monitor",
            "description": "Set up quarterly review cycle and KRI tracking.",
            "priority": "MEDIUM"
        },
        {
            "action_type": "Report",
            "description": "Escalate findings to risk committee in next board report.",
            "priority": "LOW"
        }
    ]

    return jsonify({
        "recommendations": recommendations,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "meta": {
            "model_used": "llama-3.3-70b-versatile",
            "cached": False,
            "is_fallback": False,
        }
    }), 200