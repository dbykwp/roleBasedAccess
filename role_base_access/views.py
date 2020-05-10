from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from role_base_access.serializers import RoleSerializer, UserSerializer, UserRolesSerializer, ResourceSerializer, RoleResourceActionSerializer
from rest_framework import status
from role_base_access.models import Role, User, UserRoles, Resource, RoleResourceAction
from role_base_access import user_utils as utils


import traceback


class RolesView(APIView):

    def post(self, request, format=None):
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        snippets = Role.objects.all()
        serializer = RoleSerializer(snippets, many=True)
        return Response(serializer.data)


class UserView(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        snippets = User.objects.all()
        serializer = UserSerializer(snippets, many=True)
        return Response(serializer.data)


class UserRolesView(APIView):

    def post(self, request, format=None):
        data = request.data

        if 'role' not in data:
            return Response('Role not present in request', status=status.HTTP_400_BAD_REQUEST)
        if 'user_id' not in data:
            return Response('User Id not present in request', status=status.HTTP_400_BAD_REQUEST)
        data = {
            'user_role': utils.get_role(data['role']),
            'role_user': utils.get_user(data['user_id'])
        }
        serializer = UserRolesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        user_roles = UserRoles.objects.all()
        serializer = UserRolesSerializer(user_roles, many=True)
        return Response(serializer.data)

    def delete(self, request, format=None):
        data = request.data
        try:
            if 'role' not in data:
                return Response('Role not present in request', status=status.HTTP_400_BAD_REQUEST)
            if 'user_id' not in data:
                return Response('User Id not present in request', status=status.HTTP_400_BAD_REQUEST)
            role = utils.get_role(data['role'])
            user = utils.get_user(data['user_id'])
            user_roles = UserRoles.objects.get(
                user_role=role, role_user=user)
            user_roles.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            print(traceback.format_exc())
            return Response(status=status.HTTP_404_NOT_FOUND)


class ResourceView(APIView):
    def post(self, request, format=None):
        serializer = ResourceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        resources = Resource.objects.all()
        serializer = ResourceSerializer(resources, many=True)
        return Response(serializer.data)


class RoleResourceActionView(APIView):
    def post(self, request, format=None):
        serializer = RoleResourceActionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        resources = RoleResourceAction.objects.all()
        serializer = RoleResourceActionSerializer(resources, many=True)
        return Response(serializer.data)
