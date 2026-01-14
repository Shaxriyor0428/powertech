from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

# DEBUG = False
# ALLOWED_HOSTS = ["yourdomain.com", "www.yourdomain.com"]

# STATIC & MEDIA - production server uchun
STATIC_URL = "/static/"
MEDIA_URL = "/media/"

STATIC_ROOT = "/var/www/powertech/staticfiles"
MEDIA_ROOT = "/var/www/powertech/mediafiles"

CORS_ALLOW_ALL_ORIGINS = True
