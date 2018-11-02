from django.http import HttpResponse
from geocoding.app.services import GeoCoderService

def get_location(request):
    return HttpResponse("Hello, world. You're at the geocoding index.")