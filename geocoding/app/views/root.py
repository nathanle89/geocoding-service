from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def root(request):
    return Response({
        "Name": "Geo Coding Service",
        "Version": "1.0"
    })