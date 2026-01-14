from rest_framework import serializers


class ContactSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    company = serializers.CharField(max_length=255, required=False, allow_blank=True)
    address = serializers.CharField(max_length=500, required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_blank=True, max_length=500)
    phone = serializers.CharField(max_length=50)
    message_subject = serializers.CharField(max_length=255, required=False, allow_blank=True)
    message = serializers.CharField(required=False, allow_blank=True)
