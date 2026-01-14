from django.contrib import admin
from django.contrib.auth.hashers import make_password
from apps.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "full_name",
        "is_superuser",
        "is_staff",
        "is_active",
        "created_at",
    )

    list_filter = (
        "is_superuser",
        "is_active",
        "is_staff",
        "created_at",
    )

    search_fields = (
        "full_name",
        "username",
    )

    ordering = ("-created_at",)
    list_per_page = 25

    fieldsets = (
        ("Asosiy ma'lumotlar", {
            "fields": (
                "full_name",
                "username",
                "password",
            )
        }),
        ("Ruxsatlar", {
            "fields": (
                "is_superuser",
                "is_staff",
                "is_active",
            )
        }),
        ("Vaqt ma'lumotlari", {
            "fields": (
                "created_at",
                "updated_at",
            )
        }),
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    def save_model(self, request, obj, form, change):
        """
        Agar user yaratilayotgan bo‘lsa yoki parol o‘zgargan bo‘lsa,
        passwordni HASH qilib saqlaydi
        """
        if not change or "password" in form.changed_data:
            obj.password = make_password(obj.password)
        super().save_model(request, obj, form, change)
