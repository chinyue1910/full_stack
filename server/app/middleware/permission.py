from functools import wraps

from fastapi import HTTPException


class PermissionMiddleware:
    @classmethod
    def admin(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not kwargs['current_user'].superuser:
                raise HTTPException(
                    status_code=401, detail="Permisssion denied")
            result = func(*args, **kwargs)
            return result
        return wrapper

    @classmethod
    def member(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not kwargs['current_user'].superuser and kwargs['current_user'].id != kwargs['user_id']:
                raise HTTPException(
                    status_code=401, detail="Permisssion denied")
            result = func(*args, **kwargs)
            return result
        return wrapper
