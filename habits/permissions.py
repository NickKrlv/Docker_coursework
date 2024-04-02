from rest_framework.permissions import BasePermission, IsAuthenticated


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsStaff(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff
