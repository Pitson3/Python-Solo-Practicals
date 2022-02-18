from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    name = 'profiles'

    def read(self):
        import profiles.signals
