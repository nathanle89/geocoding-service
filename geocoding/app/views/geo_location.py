from rest_framework.decorators import api_view
from rest_framework.response import Response
from geocoding.app.services.geocoder_service import GeoCoderService

@api_view(["GET"])
def get_location(request):
    data = GeoCoderService.lookup(37.375760, -122.026980)
    return Response({
        "neighborhood": data['neighborhood'],
        "district": data['district'],
        "city": data['city'],
        "county": data['county'],
        "postal": data['postal'],
        "state": data['state'],
        "country": data['country']
    })