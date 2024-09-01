from rest_framework import permissions

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Operaciones de lectura (SAFE_METHODS)
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated

        # Operaciones de creación, actualización y eliminación
        return obj.user == request.user or request.user.is_staff
