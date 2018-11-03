from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.services.geocoder_service import GeocoderService
from app.views.helpers.custom_exceptions import *

@api_view(["GET"])
def get_location(request):
    latitude, longitude = parse_params(request)
    data = GeocoderService.lookup(latitude, longitude)
    if data:
        output = data
    else:
        output = { "message": "No result found" }

    return Response(output)

def parse_params(request):
    params = request.query_params
    if 'latitude' not in params and 'longitude' not in params:
        raise ParseError("Missing Latitude and Longitude")

    try:
        latitude = float(params['latitude'])
        longitude = float(params['longitude'])
    except ValueError:
        raise ValidationError("Latitude and Longitude must be a number")

    return latitude, longitude
