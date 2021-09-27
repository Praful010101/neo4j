from django.conf.urls import url, include 
 
urlpatterns = [ 
    url(r'^', include('mica-services.apps.symptom_template.urls')),
]