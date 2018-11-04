import requests
import re
from django.conf import settings

class BingResult(object):

    fields_to_process = ['address', 'postal', 'housenumber', 'street', 'neighborhood', 'city', 'state', 'country']

    def __init__(self, json_content):
        self.json = {}
        if len(json_content['resourceSets']) > 0 and json_content['resourceSets'][0]['estimatedTotal'] > 0:
            self._address = json_content['resourceSets'][0]['resources'][0].get('address', {})

            for key in BingResult.fields_to_process:
                value = getattr(self, key)
                if value:
                    self.json[key] = value

            self.status = 'OK'
        else:
            self.status = 'ERROR - No results found'

    @property
    def address(self):
        return self._address.get('formattedAddress')

    @property
    def housenumber(self):
        if self.street:
            expression = r'\d+'
            pattern = re.compile(expression)
            match = pattern.search(self.street, re.UNICODE)
            if match:
                return match.group(0)

    @property
    def street(self):
        return self._address.get('addressLine')

    @property
    def neighborhood(self):
        return self._address.get('neighborhood')

    @property
    def city(self):
        return self._address.get('locality')

    @property
    def state(self):
        return self._address.get('adminDistrict')

    @property
    def country(self):
        return self._address.get('countryRegion')

    @property
    def postal(self):
        return self._address.get('postalCode')

class BingReverseClient:

    URL = 'http://dev.virtualearth.net/REST/v1/Locations/{0}'

    def __init__(self):
        self.key = settings.BING_API_KEY
        self.gen = 8
        self.maxresults = 1

    def reverse_lookup(self, latitude, longitude):
        params = {
            'o': 'json',
            'key': self.key,
            'maxResults': self.maxresults,
        }
        url = BingReverseClient.URL.format('{},{}'.format(latitude, longitude))
        r = requests.get(url, params=params)
        return BingResult(r.json())



