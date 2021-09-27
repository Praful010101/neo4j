from django.conf.urls import url 
from django.urls import path,re_path
from . import views
 
urlpatterns = [ 
    re_path(r"^test_neo4j_connection/?$", views.TestNeo4jConnectionView.as_view(), name='test-neo4j-data-view'),
    url(r'^api/symptom_template$', views.SymptomTemplate.as_view(),name="symptom-template"),
]