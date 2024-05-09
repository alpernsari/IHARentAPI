from django.apps import AppConfig

# admin panelinde kiralama modülünü görüntüleyebilmek için
class HiringmoduleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'HiringModule'
