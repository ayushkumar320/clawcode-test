"""Session management for a future web frontend."""

SESSION_TTL_SECONDS = 3600


def new_session(player_id: str) -> dict:
    return {"player_id": player_id, "ttl": SESSION_TTL_SECONDS}