from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^$', views.hello),
   url(r'get_domain_resource/(?P<domain_slug>.+)$', views.get_domain_resources_view),
   url(r'get_tech_resource/(?P<tech_slug>.+)$', views.get_tech_resources_view),
   ]
