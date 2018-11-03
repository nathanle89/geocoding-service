from django.conf import settings
from app.views.helpers.custom_exceptions import ServiceUnavailable
from urllib3.exceptions import HTTPError, ConnectionError
from .here_client import HereReverseClient
from .bing_client import BingReverseClient

class GeocoderService:

    @classmethod
    def lookup(cls, latitude, longitude):
        here_client = HereReverseClient()
        bing_client = BingReverseClient()

        try:
            response = here_client.reverse_lookup(latitude, longitude)

            if response.status == 'ERROR - No results found':
                # Try with Bing to see if it works
                response = bing_client.reverse_lookup(latitude, longitude)

        except (HTTPError, ConnectionError):
            try:
                # Network/Connectivity Issue fall back to secondary service
                response = bing_client.reverse_lookup(latitude, longitude)

            except (HTTPError, ConnectionError):
                # Both services are down, give up
                raise ServiceUnavailable()

        result = {}
        json_result = response.json
        if json_result:
            if 'address' in json_result:
                result["address"] = json_result['address']
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
