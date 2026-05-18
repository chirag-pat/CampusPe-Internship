"""
categorise.py — POST /categorise Route
Tool-04 | Risk Appetite Framework | AI Developer 2
Classifies a risk into a predefined category with a confidence score.
"""

from flask import Blueprint, g, jsonify
from datetime import datetime, timezone

categorise_bp = Blueprint("categorise", __name__)

VALID_CATEGORIES = [
    "Operational", "Financial", "Strategic", "Compliance",
    "Reputational", "Technology", "Credit", "Market", "Liquidity"
]


@categorise_bp.route("/categorise", methods=["POST"])
def categorise():
    """
    POST /categorise

    Classifies input into a risk category.

    Request body:
        { "description": "string" }

    Response:
        {
            "category": "Operational",
            "confidence": 0.87,
            "reasoning": "string",
            "generated_at": "...",
            "meta": { ... }
        }
    """
    body = getattr(g, "sanitised_body", {})
    description = body.get("description", "")

    # TODO (AI Developer 2): replace stub with actual Groq call
    # from services.groq_client import GroqClient
    # result = GroqClient().categorise(description)

    return jsonify({
        "category": "Operational",
        "confidence": 0.85,
        "reasoning": f"Based on the description, this risk relates to operational processes: {description}",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "meta": {
            "model_used": "llama-3.3-70b-versatile",
            "cached": False,
            "is_fallback": False,
        }
    }), 200