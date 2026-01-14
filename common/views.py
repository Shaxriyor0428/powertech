from rest_framework import  viewsets
from apps.users.models import User


class BaseTelegramViewSet(viewsets.ModelViewSet):

    def initial(self, request, *args, **kwargs):
        """
        Har bir request boshida avtomatik ishlaydi.
        """
        chat_id = (
            request.data.get("chat_id") or
            request.query_params.get("chat_id")
        )

        if not chat_id:
            self.permission_denied(
                request,
                message="chat_id yuborilmadi."
            )

        user = User.objects.filter(chat_id=chat_id).first()

        if not user:
            self.permission_denied(
                request,
                message="Foydalanuvchi topilmadi yoki ro‘yxatdan o‘tmagan."
            )


        request.user = user
        super().initial(request, *args, **kwargs)

    def get_queryset(self):
        """
        Foydalanuvchining faqat o‘z obyektlarini ko‘rsatadi.
        """
        return self.queryset.filter(user=self.request.user).order_by("-created_at")

    def perform_create(self, serializer):
        """
        Yangi obyekt yaratilganda userni avtomatik bog‘laydi.
        """
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
