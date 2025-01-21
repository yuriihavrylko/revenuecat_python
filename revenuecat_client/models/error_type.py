from enum import Enum


class ErrorType(str, Enum):
    AUTHENTICATION_ERROR = "authentication_error"
    AUTHORIZATION_ERROR = "authorization_error"
    IDEMPOTENCY_ERROR = "idempotency_error"
    INVALID_REQUEST = "invalid_request"
    PARAMETER_ERROR = "parameter_error"
    RATE_LIMIT_ERROR = "rate_limit_error"
    RESOURCE_ALREADY_EXISTS = "resource_already_exists"
    RESOURCE_LOCKED_ERROR = "resource_locked_error"
    RESOURCE_MISSING = "resource_missing"
    SERVER_ERROR = "server_error"
    STORE_ERROR = "store_error"
    UNPROCESSABLE_ENTITY_ERROR = "unprocessable_entity_error"

    def __str__(self) -> str:
        return str(self.value)
