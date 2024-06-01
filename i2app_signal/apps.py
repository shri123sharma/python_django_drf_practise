from django.apps import AppConfig


class I2AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'i2app_signal'

    def ready(self):
        import i2app_signal.signals
