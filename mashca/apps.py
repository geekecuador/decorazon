from __future__ import unicode_literals

from django.apps import AppConfig


class MashcaConfig(AppConfig):
    name = 'mashca'
    def ready(self):
        import mashca.signals