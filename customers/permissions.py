from rest_framework.permissions import BasePermission


class IsObjectOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        # return False
        return obj.user == request.user




