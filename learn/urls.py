from django.conf.urls import url
from learn import views

urlpatterns = [
   url(r'^$', views.hello),
   # site core urls
   # rhs data
   url(r'get_domain_resource/(?P<domain_slug>.+)$', views.get_domain_resources_view),
   url(r'get_tech_resource/(?P<tech_slug>.+)$', views.get_tech_resources_view),
   # lhs data (capture clicks for generating wiki in html hover label via ajax)
   url(r'get_label_data/(?P<term>.+)$', views.get_label_data_view),   
   # extra
   url(r'get_all_domains/$', views.get_all_domains_view),
   url(r'get_all_technologies/$', views.get_all_technologies_view),
   url(r'get_domains_and_slugs/$', views.get_domains_and_slugs_view),
   # download data
   url(r'download_all_domain_data/(?P<domain_slug>.+)$', views.download_all_domain_data_view),
   url(r'download_all_tech_data/(?P<tech_slug>.+)$', views.download_all_tech_data_view),
   # extract info from wiki
   url(r'get_wiki/(?P<term>.+)$', views.get_wiki_view),
   ]
