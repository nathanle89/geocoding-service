import requests
from django.conf import settings

class HereResult(object):

    fields_to_process = ['address', 'postal', 'housenumber', 'street', 'neighborhood', 'district', 'city', 'county', 'state', 'country']

    def __init__(self, json_content):
        self.json = {}

        if len(json_content['Response']['View']) > 0:
            # We know for sure that we only want the best match so only look for 0 item
            address_json = json_content['Response']['View'][0]['Result'][0]['Location']
            self._address = address_json.get('Address', {})

            for key in HereResult.fields_to_process:
                value = getattr(self, key)
                if value:
                    self.json[key] = value
            self.status = 'OK'
        else:
            self.status = 'ERROR - No results found'

    @property
    def address(self):
        return self._address.get('Label')

    @property
    def postal(self):
        return self._address.get('PostalCode')

    @property
    def housenumber(self):
        return self._address.get('HouseNumber')

    @property
    def street(self):
        return self._address.get('Street')

    @property
    def neighborhood(self):
        return self.district

    @property
    def district(self):
        return self._address.get('District')

    @property
    def city(self):
        return self._address.get('City')

    @property
    def county(self):
        return self._address.get('County')

    @property
    def state(self):
        return self._address.get('State')

    @property
    def country(self):
        return self._address.get('Country')

class HereReverseClient:

    URL = 'http://reverse.geocoder.cit.api.here.com/6.2/reversegeocode.json'

    def __init__(self):
        self.app_id = settings.HERE_APP_ID
        self.app_code = settings.HERE_APP_CODE
        self.gen = 8
        self.maxresults = 1

    def reverse_lookup(self, latitude, longitude):
        params = {
            'mode': 'retrieveAddresses',
            'gen': 8,
            'app_id': self.app_id,
            'app_code': self.app_code,
            'prox': '{},{}'.format(latitude, longitude),
            'maxresults': self.maxresults
        }

        r = requests.get(HereReverseClient.URL, params=params)
        return HereResult(r.json())



