import geocoder
from django.conf import settings
from app.views.helpers.custom_exceptions import ServiceUnavailable
from urllib3.exceptions import HTTPError, ConnectionError

class GeoCoderService:

    @classmethod
    def lookup(cls, latitude, longitude):
        try:
            g = geocoder.here([latitude, longitude], method='reverse',
                              app_id=settings.HERE_APP_ID, app_code=settings.HERE_APP_CODE)
        except (IndexError, ValueError):
            try:
                # Try with Bing to see if it works
                g = geocoder.bing([latitude, longitude], method='reverse', key=settings.BING_API_KEY)
                if g.status == 'ERROR - No results found':
                    return {}

            except (IndexError, ValueError):
                # Give up. return no result
                return {}

        except (HTTPError, ConnectionError):
            try:
                # Network/Connectivity Issue fall back to secondary service
                g = geocoder.bing([latitude, longitude], method='reverse', key=settings.BING_API_KEY)
                if g.status == 'ERROR - No results found':
                    return {}

            except (HTTPError, ConnectionError):
                # Both services are down, give up
                raise ServiceUnavailable()

        result = {}
        json_result = g.json
        if g.json:
            if 'neighborhood' in json_result:
                result["neighborhood"] = json_result['neighborhood']
            if 'district' in json_result:
                result["district"] = json_result['district']
            if 'city' in json_result:
                result["city"] = json_result['city']
            if 'county' in json_result:
                result["county"] = json_result['county']
            if 'postal' in json_result:
                result["postal"] = json_result['postal']
            if 'state' in json_result:
                result["state"] = json_result['state']
            if 'country' in json_result:
                result["country"] = json_result['country']

        return result
