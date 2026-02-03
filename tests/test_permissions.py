from src.domain.permissions import PermissionService, User


def test_user_with_active_license_can_execute_action():
    user = User(id=1, license_active=True)
    service = PermissionService()

    assert service.can_execute(user, "EXPORT_DATA") is True


def test_premium_action_requires_premium_license():
    user = User(id=2, license_active=True, premium=False)
    service = PermissionService()

    assert service.can_execute(user, "ADVANCED_EXPORT") is False

