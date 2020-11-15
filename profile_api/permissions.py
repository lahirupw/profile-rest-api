from rest_framework import permissions

class update_own_profile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user whether user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id  == request.user.id


class Update_Own_Status(permissions.BasePermission):
    """Allow users to update their own status"""

    def has_object_permission(self,request,view,obj):
        """Check whether the user is updating their own status"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_profile.id  == request.user.id
