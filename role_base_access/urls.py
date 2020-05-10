from django.urls import path

from role_base_access.views import RolesView, UserView, UserRolesView, ResourceView, RoleResourceActionView

app_name = 'role_base_access'
urlpatterns = [
    path('role',  RolesView.as_view()),
    path('user',  UserView.as_view()),
    path('user_role',  UserRolesView.as_view()),
    path('resource',  ResourceView.as_view()),
    path('role_resource_action',  RoleResourceActionView.as_view()),
]
