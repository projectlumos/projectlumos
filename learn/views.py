from django.shortcuts import render
from django.http import HttpResponse
import json
from pprint import pprint

#aurora imports
from learn.models import Domain, Technology
from learn.utils.aurora_utils import get_all_domains, get_all_technologies, get_resources_grouped_by_tech, get_resources_grouped_by_domain, get_domains_and_slugs, get_tech_and_slugs
# Create your views here.

def hello(request):
    return_data = {}
    return_data['Domains'] = get_domains_and_slugs()
    return_data['Technology'] = get_tech_and_slugs()
    return render(request, 'hello.html', {'data': return_data})

def get_domain_resources_view(request, domain_slug):
    print domain_slug
    return_data = {}
    try:
        slug_data = Domain.objects.get(slug=domain_slug)
        return_data['slug_name'] = slug_data.name
        return_data['slug_desc'] = slug_data.desc
        return_data['all_resources'] = get_resources_grouped_by_tech(domain=domain_slug)
        return_data['mode'] = 'domain'
        pprint(return_data)
    except Exception, e:
        print e
        return HttpResponse(json.dumps("500 error"))
    pprint(return_data)
    return render(request, 'resource_layout.html', {'return_data': return_data})

def get_tech_resources_view(request, tech_slug):
    print tech_slug
    return_data = {}
    try:
        slug_data = Technology.objects.get(slug=tech_slug)
        return_data['slug_name'] = slug_data.name
        return_data['slug_desc'] = slug_data.desc
        return_data['all_resources'] = get_resources_grouped_by_domain(tech=tech_slug)
        return_data['mode'] = 'tech'
        pprint(return_data)
    except Exception, e:
        print e
        return HttpResponse(json.dumps("500 error"))
    pprint(return_data)
    return render(request, 'resource_layout.html', {'return_data': return_data})

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
