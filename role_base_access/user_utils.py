from role_base_access.models import UserRoles, Role, User


def get_role(role_name):
    role = Role.objects.get(name=role_name)
    return role


def get_user(user_id):
    return User.objects.get(id=user_id)
