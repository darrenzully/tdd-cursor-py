
# Se implementa únicamente a partir de tests.

# Cursor no debería escribir acá sin un test previo.


from dataclasses import dataclass


PREMIUM_ACTION = "accion_premium"


@dataclass
class User:
    license_active: bool
    premium_license_active: bool = False


def can_execute(user: User, action: str) -> bool:
    if action == PREMIUM_ACTION:
        return user.premium_license_active

    return user.license_active
