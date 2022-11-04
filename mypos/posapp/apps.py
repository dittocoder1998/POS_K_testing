from django.apps import AppConfig


class PosappConfig(AppConfig):
    #default_auto_field = 'django.db.models.BigAutoField'
    name = 'posapp'

class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'html_templates'