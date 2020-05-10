from django.db import models
from django.core.validators import MinLengthValidator
from enum import Enum
# Create your models here.


class BaseModel(models.Model):
    # base fields common to all models
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class User(BaseModel):
    first_name = models.CharField(
        max_length=30, validators=[MinLengthValidator(1)])
    last_name = models.CharField(max_length=30, default='')

    class Meta:
        db_table = 'users'


class Resource(BaseModel):
    name = models.CharField(max_length=50, validators=[
                            MinLengthValidator(1)], unique=True)
    description = models.CharField(max_length=300, default='')

    class Meta:
        db_table = 'resources'


class Role(BaseModel):
    name = models.CharField(max_length=50, validators=[
                            MinLengthValidator(1)], unique=True)
    description = models.CharField(max_length=300, default='')

    class Meta:
        db_table = 'roles'


class ActionChoice(Enum):   # A subclass of Enum
    R = 'Read'
    W = 'Write'
    D = 'Delete'


class RoleResourceAction(BaseModel):
    role_resource = models.ForeignKey(
        Resource, on_delete=models.CASCADE, null=False, related_name='role_resource_id')
    resource_role = models.ForeignKey(
        Role, on_delete=models.CASCADE, null=False, related_name='resouce_role_id')
    action = models.CharField(
        max_length=10,
        choices=[(tag.name, tag.value)
                 for tag in ActionChoice]  # Choices is a list of Tuple
    )

    class Meta:
        db_table = 'role_resource_actions'
        unique_together = ['role_resource', 'resource_role', 'action']


class UserRoles(BaseModel):

    # user to role many to many (one user can have multiple role and vice versa)
    role_user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, related_name='role_user_id')
    user_role = models.ForeignKey(
        Role, on_delete=models.CASCADE, null=False, related_name='user_role_id')

    class Meta:
        db_table = 'user_roles'
        unique_together = ['role_user', 'user_role']
