from apps.users.models import User


def get_user_by_chat_id(request):
    """
    request ichidan chat_id ni oladi (body yoki querydan)
    va shunga mos userni qaytaradi.
    Agar user topilmasa yoki tasdiqlanmagan bo‘lsa -> None qaytaradi.
    """
    chat_id = (
        request.data.get("chat_id") or
        request.query_params.get("chat_id")
    )

    if not chat_id:
        return None

    user = User.objects.filter(chat_id=chat_id).first()
    if not user:
        return None

    return user
