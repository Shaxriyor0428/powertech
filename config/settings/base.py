from pathlib import Path
from datetime import timedelta
from django.conf.global_settings import AUTH_USER_MODEL

from config.env import get_env, REQUIRED_ENVS

for env in REQUIRED_ENVS:
    get_env(env, required=True)


# Keyin ENV qiymatlarni o‘qib olamiz
SECRET_KEY = get_env("DJANGO_SECRET")
DEBUG = get_env("DJANGO_DEBUG", cast=bool, default=False)
BOT_TOKEN = get_env("BOT_TOKEN")
TELEGRAM_GROUP_ID = get_env("TELEGRAM_GROUP_ID")
BASE_URL = get_env("BASE_URL", required=True)

BASE_DIR = Path(__file__).resolve().parent.parent.parent



ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # third-party
    "django_extensions",
    "rest_framework",
    "django_filters",
    "rest_framework_simplejwt",
    "corsheaders",
    "drf_spectacular",
    "drf_spectacular_sidecar",

    # "local apps"
    "apps.users",
    "apps.category",
    "apps.product",
    "apps.busket",
    "apps.contact"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# =====================
# DATABASE (PostgreSQL)
# =====================
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": get_env("DB_NAME"),
        "USER": get_env("PG_USER"),
        "PASSWORD": get_env("PG_PASSWORD"),
        "HOST": get_env("PG_HOST", default="localhost"),
        "PORT": get_env("PG_PORT", default="5432"),
    }
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=10),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=20),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,

    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": "",
    "AUDIENCE": None,
    "ISSUER": None,
    "JSON_ENCODER": None,
    "JWK_URL": None,
    "LEEWAY": 0,

    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",

    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",

    "JTI_CLAIM": "jti",

    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),

    "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
    "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
    "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
    "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
    "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
    "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
}


# =====================
# REST Framework
# =====================
REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}


# settings.py

JAZZMIN_SETTINGS = {
    # THESE THREE LINES ARE THE MOST IMPORTANT
    "site_title": "Powertech",      # removes "Aksessuar" from browser tab
    "site_header": "Powertech",     # removes text from the main header
    "site_brand": "Powertech",      # removes text from sidebar & top-left

    "welcome_sign": "Welcome back!",

    # Your logo (path is relative to STATICFILES_DIRS or static/ folder)
    "site_logo": "logo1.png",      # shows in header and sidebar
    "login_logo": "logo1.png",     # login screen
    # "site_icon": "img/favicon.ico",

    # Optional – makes logo a bit bigger and centered nicely
    "site_logo_classes": "img-fluid",   # or "img-circle" if you want round logo

    # Your theme settings (keep them as you like)
    "dark_mode_theme": "darkly",
    "default_theme": "darkly",
    "navbar": "navbar-dark navbar-navy",
    "sidebar": "sidebar-dark-navy",
    "accent": "accent-navy",

    "show_ui_builder": True,
    "related_modal_active": True,

    "custom_css": "jazzmin/custom.css",
}

# This makes the UI builder show dark themes nicely too
# This makes the UI builder show dark themes nicely too
JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-navy",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-light-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "pulse",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    }
}

SPECTACULAR_SETTINGS = {
    "TITLE": "My Project API",
    "DESCRIPTION": "Django REST API documentation with Swagger & Redoc",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "SWAGGER_UI_SETTINGS": {
        "deepLinking": True,
        "persistAuthorization": False,  # tokenni saqlamasin
    },
    "COMPONENT_SPLIT_REQUEST": True,
    "SERVE_PERMISSIONS": ["rest_framework.permissions.AllowAny"],
    "SECURITY": [{"bearerAuth": []}],
    "COMPONENTS": {
        "securitySchemes": {
            "bearerAuth": {
                "type": "http",
                "scheme": "bearer",
                "bearerFormat": "JWT",
            }
        }
    },
}


# =====================
# CORS
# =====================
CORS_ALLOW_ALL_ORIGINS = True

# =====================
# AUTH PASSWORD VALIDATORS
# =====================
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Tashkent"
USE_I18N = True
USE_TZ = True

AUTH_USER_MODEL = "users.User"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
