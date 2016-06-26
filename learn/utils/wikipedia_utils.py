import wikipedia
import json

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
    Output: return_data, a list
    Returns a list containing strings which are similar to the current search term
    Returns False if it encounters a ConnectionError
    """
    return_data = None
    try:
        return_data = wikipedia.search(term)
    except Exception as e:
        print e
        return_data = None
    return return_data

def get_wiki_summary(term, sentences=3):
    """
    Input: term, a string. sentences, an interger
    Output: string
    Returns the summary for term with a constraint on the number of sentences. Default = 3
    Returns False if it encounters a ConnectionError
    """
    return_data = None
    try:
        return_data = wikipedia.summary(term, sentences)
    except Exception as e:
        print e
        return_data = None
    return return_data

def get_wiki_modal_data(term):
    """
    runs the wikiperdia helper functions and created the
    wikipedia data ready for the modal
    """
    return_data = False
    summary = get_wiki_summary(term=term)
    related_terms = get_similar_search(term=term)
    if summary:
        return_data = {
                'wiki_term': term,
                'summary': summary,
                'related_terms': related_terms
        }
    return return_data
