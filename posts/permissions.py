from rest_framework import permissions


class IsOwnerAndUpdateFields(permissions.BasePermission):
     def has_object_permission(self, request, view, obj):
        # Check if the request method is a safe method (GET, HEAD, OPTIONS)
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True  # Allow read-only access

        # Check if the user making the request is the owner of the object
        if obj.creator == request.user:
            # You can further customize this logic to check which fields can be updated
            # For example, allow updates only to specific fields:
            # if 'field_to_update' in request.data:
            #     return True

            # For simplicity, we'll allow updates to all fields
            return True

        return False
