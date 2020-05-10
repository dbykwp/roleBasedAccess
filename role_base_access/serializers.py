from rest_framework import serializers
from role_base_access.models import Role, User, UserRoles, Resource, RoleResourceAction


class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserRolesSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserRoles
        fields = '__all__'


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'


class RoleResourceActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleResourceAction
        fields = '__all__'
