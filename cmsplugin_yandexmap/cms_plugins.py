from django.conf import settings
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from django.utils.translation import ugettext_lazy as _
from models import YandexMap
from django.forms.widgets import Media


class YandexMapPlugin(CMSPluginBase):
    model = YandexMap
    name = _("Yandex Map")
    render_template = "cmsplugin_yandexmap/yandexmap.html"
    
    def render(self, context, instance, placeholder):
        context.update({
            'object': instance, 
            'placeholder': placeholder, 
            'settings': settings,
        })
        return context
    
    #def get_plugin_media(self, request, context, plugin):
    #    return Media(js = ('http://maps.google.com/maps/api/js?sensor=true',))

plugin_pool.register_plugin(YandexMapPlugin)
