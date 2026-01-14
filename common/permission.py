from rest_framework.permissions import BasePermission


class IsAdminAuthenticated(BasePermission):
    """
    Faqat autentifikatsiyadan o'tgan admin foydalanuvchilar uchun ruxsat.
    """

    def has_permission(self, request, view):
        # foydalanuvchi login bo'lganmi?
        if not request.user or not request.user.is_authenticated:
            return False

        # foydalanuvchi adminmi?
        return request.user.role == "admin"


class IsUserVerification(BasePermission):

    def has_permission(self, request, view):
        # foydalanuvchi login bo'lganmi?
        if not request.user or not request.user.is_authenticated:
            return False

        # foydalanuvchi adminmi?
        return bool(request.user.is_verified)
