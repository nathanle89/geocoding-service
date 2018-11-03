# Geocoding Service

We create a simple Network Service that can resolve the provided latitude and longitude into an address using third party geocoding services.

The third party services used are HERE and Bing:

- HERE: `https://developer.here.com/documentation/geocoder/topics/quick-start.html`
- Bing: `https://msdn.microsoft.com/en-us/library/ff701713.aspx`

Our Network Service will use HERE as the primary service and it will fall back to Bing in case no result is found or Network Error

## Required Softwares:
- Python 3.6
- Django = 2.1.3 
- djangorestframework = 3.8.2
- django-environ = 0.4.5