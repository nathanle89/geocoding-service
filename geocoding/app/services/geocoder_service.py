import geocoder
from django.conf import settings
from app.views.helpers.custom_exceptions import ValidationError, ServiceUnavailable
from urllib3.exceptions import HTTPError, ConnectionError

class GeoCoderService:

    @classmethod
    def lookup(cls, latitude, longitude):
        try:
            g = geocoder.here([latitude, longitude], method='reverse',
                              app_id=settings.HERE_APP_ID, app_code=settings.HERE_APP_CODE)
        except (IndexError, ValueError):
            raise ValidationError("Invalid latitude and longitude")
        except (HTTPError, ConnectionError):
            raise ServiceUnavailable()

        return g.json
