from django.shortcuts import render
from django.http import HttpResponse
import json

#ideal-guacamole imports
from learn.utils import get_all_domains, get_all_technologies, get_resources_grouped_by_tech, get_resources_grouped_by_domain
# Create your views here.

def hello(request):
    return_data = {}
    return_data['domains_names'] = get_all_technologies()
    return_data['techs_names'] = get_all_technologies()
    print return_data
    return HttpResponse(return_data)

def get_domain_resources_view(request, domain_slug):
    print domain_slug
    return_data = None
    try:
        return_data = get_resources_grouped_by_tech(domain=domain_slug)
    except Exception, e:
        print e
        pass
    print return_data
    return HttpResponse(return_data)

def get_tech_resources_view(request, tech_slug):
    return_data = None
    try:
        return_data = get_resources_grouped_by_domain(tech=tech_slug)
    except Exception, e:
        print e
        pass
    print return_data
    return HttpResponse(return_data)
