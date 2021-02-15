from django.apps import AppConfig


class CoinzappConfig(AppConfig):
    name = 'coinzapp'

    def ready(self):
        import coinzapp.signals