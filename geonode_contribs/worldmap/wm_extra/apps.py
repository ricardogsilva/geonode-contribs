from django.apps import AppConfig


class WMExtraConfig(AppConfig):
    name = 'geonode_contribs.worldmap.wm_extra'
    verbose_name = 'WM Extras'

    def ready(self):
        from geonode_contribs.worldmap.wm_extra import signals  # noqa
