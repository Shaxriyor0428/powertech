import os
from rest_framework import serializers


# 🧠 Yordamchi funksiya: eski faylni o‘chirish
def delete_file(file_field):
    """Agar fayl mavjud bo‘lsa — faylni o‘chiradi"""
    if file_field and os.path.isfile(file_field.path):
        os.remove(file_field.path)



def validate_video_size(value):
    max_size = 5 * 1024 * 1024  # 5 MB
    if value.size > max_size:
        raise serializers.ValidationError(
            f"Video must be ≤ 5 MB (current: {value.size / (1024*1024):.2f} MB)"
        )
    return value
