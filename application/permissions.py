from rest_framework import permissions as p


class GetCreateOrAuthorize(p.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated or request.method in ("GET", "POST")
