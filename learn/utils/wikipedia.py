import wikipedia
import json

def get_wiki_data(term):
    """
    Input: term, a string
    Output: return_data, a dictionary
    Returns page title, page url, page content for term
    Returns None if it encounters a ConnectionError
    """
    return_data = {}
    try:
        term_data = wikipedia.page(term)
        return_data['title'] = term_data.title
        return_data['url'] = term_data.url
        return_data['content'] = term_data.content
    except ConnectionError:
        return None

def get_similar_search(term):
    """
    Input: term, a string
    Output: return_data, a list
    Returns a list containing strings which are similar to the current search term
    Returns None if it encounters a ConnectionError
    """
    try:
        return_data = wikipedia.search(term)
    except ConnectionError:
        return None

def get_wiki_summary(term, sentences=3):
    """
    Input: term, a string. sentences, an interger
    Output: string
    Returns the summary for term with a constraint on the number of sentences. Default = 3
    Returns None if it encounters a ConnectionError
    """
    try:
        return_data = wikipedia.summary(term, sentences)
    except ConnectionError:
        return None