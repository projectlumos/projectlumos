import wikipedia
import json

def wiki_term_to_url(terms_list):
    """
    takes a term list and returns a dict
    which contains the term and the wikipedia url
    """
    wiki_data = {curr_term: 'http://www.wikipedia.org/wiki/' + curr_term.lower().replace(' ','_') for curr_term in terms_list}
    return wiki_data

def get_wiki_data(term):
    """
    Input: term, a string
    Output: return_data, a dictionary
    Returns page title, page url, page content for term
    Returns False if it encounters a ConnectionError
    """
    return_data = {}
    try:
        term_data = wikipedia.page(term)
        return_data['title'] = term_data.title
        return_data['url'] = term_data.url
        return_data['content'] = term_data.content
    except Exception as e:
        print e
        return_data = None
    return return_data

def get_similar_search(term):
    """
    Input: term, a string
    Output: return_data, a dict
    Returns a dict containing related term asa key and the wiki url as valuege
    Returns False if it encounters a ConnectionError
    """
    return_data = None
    try:
        all_terms = wikipedia.search(term)
        return_data = wiki_term_to_url(all_terms)
    except Exception as e:
        print e
        return_data = None
    return return_data

def get_wiki_summary(term, sentences=3):
    """
    Input: term, a string. sentences, an interger
    Output: string
    Returns the summary for term with a constraint on the number of sentences. Default = 3
    Returns a dict of approx links with their wikipedia urls
    """
    return_data = {}
    try:
        return_data['summary_present'] = True
        return_data['summary_content'] = wikipedia.summary(term, sentences)
    except wikipedia.exceptions.DisambiguationError as e:
        return_data['summary_present'] = False
        approx_links = e.options
        return_data['other_links'] =  wiki_term_to_url(approx_links)
    return return_data

def get_wiki_modal_data(term):
    """
    runs the wikiperdia helper functions and created the
    wikipedia data ready for the modal
    """
    return_data = False
    summary_data = get_wiki_summary(term=term)
    related_terms = get_similar_search(term=term)
    if summary_data:
        return_data = {
                'wiki_term': term,
                'summary_data': summary_data,
                'related_terms': related_terms
        }
    return return_data
