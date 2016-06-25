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

def get_related_technologies(resource):
    """
    returns related technologies for a resource
    used in the related technology section of the resource page
    """
    required_resource = Resources.objects.get(id=resource.id)
    related_technologies = {tech.name: tech.slug for tech in required_resource.technology.all()}
    return related_technologies

def get_related_domains(resource):
    """
    returns related domains and slugs for a resource
    used in the related domains sections of the resource layout page
    """
    required_resource = Resources.objects.get(id=resource.id)
    related_domains = {domain.name: domain.slug for domain in required_resource.domain.all()}
    return related_domains

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

    return_resource['related_technologies'] = get_related_technologies(resource)
    return_resource['related_domains'] = get_related_domains(resource)

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
                curr_tech_data.resources.append(resource_to_data(resource))

            return_data[tech_name] = curr_tech_data
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
                curr_domain_data.resources.append(resource_to_data(resource))

            return_data[domain_name] = curr_domain_data
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