# Generated by Django 3.0.6 on 2020-05-10 10:04

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='role_base_access.BaseModel')),
                ('name', models.CharField(max_length=50, unique=True, validators=[django.core.validators.MinLengthValidator(1)])),
                ('description', models.CharField(default='', max_length=300)),
            ],
            options={
                'db_table': 'resources',
            },
            bases=('role_base_access.basemodel',),
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='role_base_access.BaseModel')),
                ('name', models.CharField(max_length=50, unique=True, validators=[django.core.validators.MinLengthValidator(1)])),
                ('description', models.CharField(default='', max_length=300)),
            ],
            options={
                'db_table': 'roles',
            },
            bases=('role_base_access.basemodel',),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='role_base_access.BaseModel')),
                ('first_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(1)])),
                ('last_name', models.CharField(default='', max_length=30)),
            ],
            options={
                'db_table': 'users',
            },
            bases=('role_base_access.basemodel',),
        ),
        migrations.CreateModel(
            name='UserRoles',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='role_base_access.BaseModel')),
                ('role_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='role_user_id', to='role_base_access.User')),
                ('user_role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_role_id', to='role_base_access.Role')),
            ],
            options={
                'db_table': 'user_roles',
                'unique_together': {('role_user', 'user_role')},
            },
            bases=('role_base_access.basemodel',),
        ),
        migrations.CreateModel(
            name='RoleResourceAction',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='role_base_access.BaseModel')),
                ('action', models.CharField(choices=[('R', 'Read'), ('W', 'Write'), ('D', 'Delete')], max_length=10)),
                ('resource_role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resouce_role_id', to='role_base_access.Role')),
                ('role_resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='role_resource_id', to='role_base_access.Resource')),
            ],
            options={
                'db_table': 'role_resource_actions',
                'unique_together': {('role_resource', 'resource_role', 'action')},
            },
            bases=('role_base_access.basemodel',),
        ),
    ]
