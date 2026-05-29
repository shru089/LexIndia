import time
from fastapi import Request, HTTPException, status, Depends
import auth_utils
import models

# Store user query histories in memory
# Format: { "user_ID": [timestamp1, timestamp2, ...] }
request_history: dict[str, list[float]] = {}

def check_rate_limit(
    request: Request,
    current_user: models.User = Depends(auth_utils.get_current_user)
) -> models.User:
    now = time.time()
    key = f"user_{current_user.id}"
    
    # Configure rate limits based on user tier
    # free: 10 requests per minute
    # citizen_pro / advocate: 100 requests per minute
    limit = 10
    if current_user.tier in ["citizen_pro", "advocate"]:
        limit = 100
        
    window_seconds = 60
    
    if key not in request_history:
        request_history[key] = []
        
    # Clean up timestamps older than the sliding window
    request_history[key] = [t for t in request_history[key] if now - t < window_seconds]
    
    # Check if request count exceeds the limit
    if len(request_history[key]) >= limit:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail=f"Rate limit exceeded. Tier '{current_user.tier}' allows {limit} requests per {window_seconds}s."
        )
        
    # Append the current request timestamp
    request_history[key].append(now)
    
    # Pass the authenticated user back to the endpoint
    return current_user
