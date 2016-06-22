from learn.models import Technology, Domain, Resources

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
    return return_resource

def get_resources_grouped_by_tech(domain):
    """
    Given a domain slug, this function will return
    all the resources for that domain group by technologies
    i/p: 'python-web-dev'
    o/p: 
    """
    return_data = {}
    all_resources = Resources.objects.filter(domain__slug=domain)
    for resource in all_resources:
        technologies_in_resource = resource.technology.all()

        for technology in technologies_in_resource:
            tech_name = technology.name
            curr_tech_resources = return_data.get(tech_name, None)

            if not curr_tech_resources:
                curr_tech_resources = [resource_to_data(resource)]
            else:
                print 'adding to an existing tech'
                curr_tech_resources.append(resource_to_data(resource))

            return_data[tech_name] = curr_tech_resources    
    return return_data

def get_resources_grouped_by_domain(tech):
    """
    Given a tech slug, this function will return
    all the resources for that tech grouped by domains
    i/p: 'python-web-dev'
    o/p: 
    """
    return_data = {}
    all_resources = Resources.objects.filter(technology__slug=tech)
    for resource in all_resources:
        domains_in_resource = resource.domain.all()

        for domain in domains_in_resource:
            domain_name = domain.name
            curr_domain_resources = return_data.get(domain_name, None)
            if not curr_domain_resources:
                curr_domain_resources = [resource_to_data(resource)]
            else:
                print 'adding to an existing domain'
                curr_domain_resources.append(resource_to_data(resource))

            return_data[domain_name] = curr_domain_resources    
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