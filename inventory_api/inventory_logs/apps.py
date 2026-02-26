from django.apps import AppConfig

class InventoryLogsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'inventory_logs'

    def ready(self):
        import inventory_logs.signals