# Se implementa únicamente a partir de tests.

# Cursor no debería escribir acá sin un test previo.

PREMIUM_ACTIONS = frozenset({"ADVANCED_EXPORT"})


class User:
    def __init__(self, id: int, license_active: bool, premium: bool = True):
        self.id = id
        self.license_active = license_active
        self.premium = premium


class PermissionService:
    def can_execute(self, user: User, action: str) -> bool:
        if not user.license_active:
            return False
        if action in PREMIUM_ACTIONS:
            return user.premium
        return True
