import geocoder
from django.conf import settings

class GeoCoderService:

    @classmethod
    def lookup(cls, latitude, longitude):
        g = geocoder.here([latitude, longitude], method='reverse',
                          app_id=settings.HERE_APP_ID, app_code=settings.HERE_APP_CODE)
        return g.json
