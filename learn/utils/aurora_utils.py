from learn.models import Technology, Domain, Resources
from collections import Counter

def get_all_domains():
    """
    returns all the domain names
    """
    domain_names = Domain.objects.filter(active=1).values_list('name', flat=True)
    return domain_names

def get_all_technologies():
    """
    returns all the technology names
    """
    tech_names = Technology.objects.filter(active=1).values_list('name', flat=True)
    return tech_names

def get_domains_and_slugs():
    """
    returns all the domain names and slugs as dictionary
    {domain_name: slug}
    """
    return_data = {}
    domain_slugs = Domain.objects.filter(active=1).order_by('name')
    if domain_slugs:
        for domain in domain_slugs:
            return_data[domain.name] = domain.slug
    return return_data

def get_tech_and_slugs():
    """
    returns all the technology names and slugs as dictionary
    {domain_name: slug}
    """
    return_data = {}
    technology_slugs = Technology.objects.filter(active=1).order_by('name')
    if technology_slugs:
        for technology in technology_slugs:
            return_data[technology.name] = technology.slug
    return return_data

def extract_related_info(raw_data):
    print raw_data
    return_data = []
    for key, value in raw_data.items():
        curr_data = {}
        curr_data['name'] = key.name
        curr_data['slug'] = key.slug
        curr_data['freq'] = value
        return_data.append(curr_data)
    # return_data = sorted(return_data, key=lamba x: int(x['freq']), reverse=True)[:9]
    return return_data

def get_aggr_related_data(resources):
    """
    takes in a array of resources 
    and returns a dict of related tech name and domains sorted on the basis of freq
    o/p: {
        tech: [{tech_object: 12}, {tech_object: 10}],
        domain: [{domain_object: 12}, {domain_object: 10}]
    } 
    This function is for the tech and domain
    """
    related_data = {}
    all_techs = []
    all_domains = []
    for resource in resources:
        curr_techs = resource.technology.all()
        all_techs.extend(curr_techs)
        curr_domains = resource.domain.all()
        all_domains.extend(curr_domains)
    all_techs = dict(Counter(all_techs))
    all_domains = dict(Counter(all_domains))

    all_techs = extract_related_info(all_techs)
    all_domains = extract_related_info(all_domains)
    return all_techs, all_domains


def get_related_data(resource):
    """
    identical to the above function but used for resource level
    """

    related_data = {}
    all_techs = []
    all_domains = []
    curr_techs = resource.technology.all()
    all_techs.extend(curr_techs)
    curr_domains = resource.domain.all()
    all_domains.extend(curr_domains)
    all_techs = dict(Counter(all_techs))
    all_domains = dict(Counter(all_domains))

    all_techs = extract_related_info(all_techs)
    all_domains = extract_related_info(all_domains)
    
    return all_techs, all_domains

def resource_to_data(resource):
    """
    Converts a resource queryset into essential fields only
    """
    return_resource = {}
    return_resource['name'] = resource.name
    return_resource['link'] = resource.link
    return_resource['desc'] = resource.desc
    return_resource['diff_level'] = resource.diff_level
    return_resource['diff_sort'] = resource.diff_sort
    return_resource['media_type'] = resource.media_type
    return_resource['slug'] = resource.slug

    return_resource['related_technologies'], return_resource['related_domains'] = get_related_data(resource)

    return return_resource

def get_resources_grouped_by_tech(domain):
    """
    Given a domain slug, this function will return
    all the resources for that domain group by technologies
    i/p: 'android-dev'
    o/p: 
    """
    return_data = {}
    all_resources = Resources.objects.filter(domain__slug=domain)
    for resource in all_resources:
        technologies_in_resource = resource.technology.all()

        for technology in technologies_in_resource:
            tech_name = technology.name
            curr_tech_data = return_data.get(tech_name, None)

            if not curr_tech_data:
                curr_tech_data = {}
                # curr_tech_data['related_domains'] = domains_for_tech(tech_name)
                # figure out the related domains using smart querying
                curr_tech_data['resources'] = [resource_to_data(resource)]
                curr_tech_data['desc'] = technology.desc
            else:
                print 'adding to an existing tech'
                curr_tech_data['resources'].append(resource_to_data(resource))
            
            return_data[tech_name] = curr_tech_data
    
    # return_data['related_technologies'], return_data['related_domains'] = get_aggr_related_data(all_resources)
    return return_data

def get_resources_grouped_by_domain(tech):
    """
    Given a tech slug, this function will return
    all the resources for that tech grouped by domains
    i/p: 'python'
    """
    return_data = {}
    all_resources = Resources.objects.filter(technology__slug=tech)
    for resource in all_resources:
        domains_in_resource = resource.domain.all()

        for domain in domains_in_resource:
            domain_name = domain.name
            curr_domain_data = return_data.get(domain_name, None)

            if not curr_domain_data:
                curr_domain_data = {}
                # curr_domain_data['related_technologies'] = techs_for_domain(domain_name)
                # figure out the related techs using smart querying
                curr_domain_data['resources'] = [resource_to_data(resource)]
                curr_domain_data['desc'] = domain.desc
            else:
                curr_domain_data['resources'].append(resource_to_data(resource))

            return_data[domain_name] = curr_domain_data
        
    # return_data['related_technologies'], return_data['related_domains'] = get_aggr_related_data(all_resources)
    return return_data

def get_info_by_slug(slug):
    """
    get's information nased on the slug
    """
    all_domains = get_all_domains_slugs()
    all_technologies = get_all_technologies_slugs()
    return_data = None

    if name in all_domains:
        return_data = Domain.objects.get(name=name)
    elif name in all_technologies:
        return_data = Technology.objects.get(name=name)

    return return_data