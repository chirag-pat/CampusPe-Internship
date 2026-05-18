"""
auth_middleware.py — Simple JWT Auth Simulation for Day 13 Testing
===================================================================
Tool-04 | Risk Appetite Framework | AI Developer 3

Simulates 401 (no token) and 403 (wrong role) directly in Flask
so Day 13 security tests can be completed without Spring Boot running.

IMPORTANT: This is for TESTING ONLY.
In production, auth is handled by Spring Boot + AiServiceClient.java.
Remove the @require_auth decorator from routes after testing is done.
"""

import jwt
import logging
from functools import wraps
from flask import request, jsonify, g

logger = logging.getLogger("tool04.auth_middleware")

# Same secret your Spring Boot team uses in application.yml
# Ask Java Developer 1 for the actual value — use any string for local testing
JWT_SECRET = "test-secret-key-for-local-testing-only"
JWT_ALGORITHM = "HS256"


def require_auth(required_role=None):
    """
    Decorator that checks for a valid JWT and optionally enforces a role.

    Usage:
        @require_auth()                    # just needs a valid token — 401 if missing
        @require_auth(required_role="ADMIN")  # needs ADMIN role — 403 if wrong role
    """
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            # ── Step 1: Check Authorization header exists ──────────────
            auth_header = request.headers.get("Authorization", "")
            if not auth_header or not auth_header.startswith("Bearer "):
                logger.warning("401 — No token | path=%s", request.path)
                return jsonify({
                    "error": "Unauthorized",
                    "message": "Missing or invalid Authorization header. Include: Bearer <token>",
                    "status": 401
                }), 401

            token = auth_header.split(" ")[1]

            # ── Step 2: Decode and validate the JWT ────────────────────
            try:
                payload = jwt.decode(
                    token,
                    JWT_SECRET,
                    algorithms=[JWT_ALGORITHM]
                )
            except jwt.ExpiredSignatureError:
                return jsonify({
                    "error": "Unauthorized",
                    "message": "Token has expired. Please login again.",
                    "status": 401
                }), 401
            except jwt.InvalidTokenError:
                return jsonify({
                    "error": "Unauthorized",
                    "message": "Invalid token.",
                    "status": 401
                }), 401

            # ── Step 3: Check role if required ─────────────────────────
            user_role = payload.get("role", "")
            g.current_user = payload  # make user info available in route

            if required_role and user_role != required_role:
                logger.warning(
                    "403 — Wrong role | user_role=%s | required=%s | path=%s",
                    user_role, required_role, request.path
                )
                return jsonify({
                    "error": "Forbidden",
                    "message": f"Access denied. Required role: {required_role}. Your role: {user_role}",
                    "status": 403
                }), 403

            return f(*args, **kwargs)
        return decorated
    return decorator


def generate_test_token(role="VIEWER"):
    """
    Helper to generate test JWT tokens for Postman testing.
    Run this once to get tokens, paste them into Postman.

    Usage:
        python -c "from auth_middleware import generate_test_token; print(generate_test_token('ADMIN'))"
        python -c "from auth_middleware import generate_test_token; print(generate_test_token('VIEWER'))"
    """
    import datetime
    payload = {
        "sub": f"test-{role.lower()}@tool04.com",
        "role": role,
        "iat": datetime.datetime.utcnow(),
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token