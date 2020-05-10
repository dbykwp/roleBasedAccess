from role_base_access.models import UserRoles, Role, User, RoleResourceAction


def get_role(role_name):
    role = Role.objects.get(name=role_name)
    return role


def get_user(user_id):
    return User.objects.get(id=user_id)


def get_role_for_given_action_and_resource(resource_id, action):
    query = {
        'role_resource_id': resource_id,
        'action': action
    }
    role_ids = RoleResourceAction.objects.filter(
        **query).values_list('resource_role_id', flat=True)
    return role_ids
