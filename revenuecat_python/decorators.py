from functools import wraps

from .responses import RevenueCatError


def require_secret():
    def decorator(f):
        @wraps(f)
        def decorated(self, *args, **kwargs):
            if not self.secret_key:
                raise RevenueCatError(message="Secret key required")
            return f(self, *args, **kwargs)

        return decorated

    return decorator
