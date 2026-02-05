# Acá arranca TODO.
# Los tests definen el diseño.

# Cursor puede generar tests, pero no implementación sin RED.

from domain.permissions import User, can_execute


def test_usuario_con_licencia_activa_puede_ejecutar_accion():
    user = User(license_active=True)

    assert can_execute(user, "cualquier_accion") is True


def test_accion_premium_requiere_licencia_premium():
    user = User(license_active=True)

    assert can_execute(user, "accion_premium") is False
