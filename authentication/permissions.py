from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated

class AnonPermissionOnly(permissions.BasePermission):
    message = 'You are already authenticated'

    def has_permission(self, request, view):
        return not request.user.is_authenticated