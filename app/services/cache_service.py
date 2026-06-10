from typing import Any, Optional
from datetime import datetime, timedelta
import asyncio


class CacheService:
    """Simple in-memory cache service"""
    def __init__(self):
        self._cache = {}
        self._ttl = {}
    
    async def get(self, key: str) -> Optional[Any]:
        """Get value from cache"""
        if key not in self._cache:
            return None
        
        # Check if TTL expired
        if key in self._ttl and self._ttl[key] < datetime.now():
            del self._cache[key]
            del self._ttl[key]
            return None
        
        return self._cache.get(key)
    
    async def set(self, key: str, value: Any, ttl: int = 3600) -> bool:
        """Set value in cache with TTL (default 1 hour)"""
        self._cache[key] = value
        self._ttl[key] = datetime.now() + timedelta(seconds=ttl)
        return True
    
    async def delete(self, key: str) -> bool:
        """Delete key from cache"""
        if key in self._cache:
            del self._cache[key]
        if key in self._ttl:
            del self._ttl[key]
        return True
    
    async def clear(self) -> bool:
        """Clear all cache"""
        self._cache.clear()
        self._ttl.clear()
        return True


# Global cache service instance
cache_service = CacheService()
