# django imports
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# standart imports
import json
from pprint import pprint

#aurora imports
from learn.models import Domain, Technology, Resources, QualityFeedback
from learn.utils.aurora_utils import get_all_domains, get_all_technologies, get_resources_grouped_by_tech, get_resources_grouped_by_domain, get_domains_and_slugs, get_tech_and_slugs
from learn.utils.wikipedia_utils import get_wiki_modal_data
# Create your views here.

def hello(request):
    return_data = {}
    return_data['Domains'] = get_domains_and_slugs()
    return_data['Technology'] = get_tech_and_slugs()
    return render(request, 'hello.html', {'data': return_data})

def get_domain_resources_view(request, domain_slug):
    return_data = {}
    try:
        slug_data = Domain.objects.get(slug=domain_slug)
        return_data['slug_name'] = slug_data.name
        return_data['slug_desc'] = slug_data.desc
        return_data['all_resources'] = get_resources_grouped_by_tech(domain=domain_slug)
        return_data['mode'] = 'domain'
        pprint(return_data)
    except Exception, e:
        return HttpResponse(json.dumps("500 error"))
    pprint(return_data)
    return render(request, 'resource_layout.html', {'return_data': return_data})

def get_tech_resources_view(request, tech_slug):
    return_data = {}
    try:
        slug_data = Technology.objects.get(slug=tech_slug)
        return_data['slug_name'] = slug_data.name
        return_data['slug_desc'] = slug_data.desc
        return_data['all_resources'] = get_resources_grouped_by_domain(tech=tech_slug)
        return_data['mode'] = 'tech'
        pprint(return_data)
    except Exception, e:
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

@csrf_exempt
def get_wiki_view(request):
    wiki_data = False
    if request.method == 'POST' and request.is_ajax():
        json_string = request.body.decode(encoding='UTF-8')
        data = json.loads(json_string)
        search_term =  str(data['search-term'])
        wiki_data = get_wiki_modal_data(term=search_term)
    return HttpResponse(json.dumps(wiki_data))

@csrf_exempt
def resource_quality_ratings(request):
    if request.method == 'POST' and request.is_ajax():
        json_string = request.body.decode(encoding='UTF-8')
        data = json.loads(json_string)
        pprint(data)
        resource_id =  str(data['resource_id'])
        helpfulness =  str(data['helpfulness'])
        simplicity =  str(data['simplicity'])
        placement =  str(data['placement'])
        recommendation =  str(data['recommendation'])
        try:
            resource = Resources.objects.get(id=resource_id)
            new_resource_feedback = QualityFeedback()
            new_resource_feedback.resource = resource
            new_resource_feedback.helpfulness = helpfulness
            new_resource_feedback.simplicity = simplicity
            new_resource_feedback.placement = placement
            new_resource_feedback.recommendation = recommendation
            new_resource_feedback.save()

        except Exception as e:
            print e
    return HttpResponse(True)
