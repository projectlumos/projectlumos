from django.shortcuts import render
from django.http import HttpResponse
import json
from pprint import pprint

#ideal-guacamole imports
from learn.utils import get_all_domains, get_all_technologies, get_resources_grouped_by_tech, get_resources_grouped_by_domain, get_domains_and_slugs, get_tech_and_slugs
# Create your views here.

def hello(request):
    return_data = {}
    return_data['Domains'] = get_domains_and_slugs()
    return_data['Technology'] = get_tech_and_slugs()
    return render(request, 'hello.html', {'data': return_data})

def get_domain_resources_view(request, domain_slug):
    print domain_slug
    return_data = None
    try:
        return_data = get_resources_grouped_by_tech(domain=domain_slug)
    except Exception, e:
        print e
        pass
    pprint(return_data)
    return HttpResponse(return_data)

def get_tech_resources_view(request, tech_slug):
    return_data = None
    try:
        return_data = get_resources_grouped_by_domain(tech=tech_slug)
    except Exception, e:
        print e
        pass
    pprint(return_data)
    return HttpResponse(return_data)

def get_label_data_view(request):
    pass

def get_all_domains_view(request):
    pass

def get_all_technologies_view(request):
    pass
def get_domains_and_slugs_view(request):
    pass
def download_all_domain_data_view(request):
    pass
def download_all_tech_data_view(request):
    pass

def get_wiki_view(request):
    pass