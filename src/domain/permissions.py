
# Se implementa únicamente a partir de tests.

# Cursor no debería escribir acá sin un test previo.

from dataclasses import dataclass


_PREMIUM_ACTIONS = {"ADVANCED_EXPORT"}


@dataclass
class User:
    id: int
    license_active: bool
    premium: bool = False


class PermissionService:
    def can_execute(self, user: User, action: str) -> bool:
        if not user.license_active:
            return False
        if action in _PREMIUM_ACTIONS:
            return user.premium
        return True
