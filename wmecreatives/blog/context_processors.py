from . models import *

def google_analytics_processor(request):
    analyticscode = AnalyticsCode.objects.all().first()  
    host = request.META['HTTP_HOST']
    scheme = request.scheme          
    return {'analyticscode': analyticscode,
            'host':host,
            'scheme':scheme}



