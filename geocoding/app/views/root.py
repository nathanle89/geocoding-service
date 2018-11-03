from rest_framework.decorators import api_view
from rest_framework.response import Response

'''
This endpoint can be used to describe the service
'''
@api_view(["GET"])
def root(request):
    return Response({
        "Name": "Geo Coding Service",
        "Version": "1.0"
    })