import requests
from drf_spectacular.utils import extend_schema

from config.settings.base import TELEGRAM_GROUP_ID, BOT_TOKEN
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ContactSerializer


def send_telegram_message(data: dict):
    TELEGRAM_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    text = (
        f"📩 *Yangi kontakt!* \n\n"
        f"👤 *Ismi:* {data['name']}\n"
        f"📞 *Telefon:* {data['phone']}\n"
        f"📧 *Email:* {data['email']}\n"
        f"📌 *Subject:* {data['message_subject']}\n"
        f"💬 *Xabar:* {data['message']}\n"
    )

    if data.get("company"):
        text += f"🏢 *Biznes nomi:* {data['company']}\n"

    if data.get("address"):
        text += f"🏠 *Manzil:* {data['address']}\n"

    payload = {
        "chat_id": TELEGRAM_GROUP_ID,
        "text": text,
        "parse_mode": "Markdown"
    }

    try:
        response = requests.post(TELEGRAM_URL, data=payload)
        response.raise_for_status()
    except Exception as e:
        print("❌ Telegramga yuborishda xatolik:", e)


class ContactAPIView(APIView):
    @extend_schema(request=ContactSerializer)
    def post(self, request, *args, **kwargs):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            send_telegram_message(serializer.validated_data)

            return Response(
                {"message": "Xabaringiz yuborildi!"},
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
