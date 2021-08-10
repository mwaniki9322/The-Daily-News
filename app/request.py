
import urllib.request,json
from .models import Source,Article


# Getting api key
api_key = None

# Getting the news base url
base_url=None

#getting articles base url
article_url=None

def configure_reques(app):
    global api_key,base_url,article_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    article_url=app.config['ARTICLES_BASE_URL']

def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = base_url.format(api_key) #construct the news api url

    with urllib.request.urlopen(get_source_url) as url: #sending request as url
        get_sources_data = url.read() #reading the response and storing in a get_sources_data variable
        get_sources_response = json.loads(get_sources_data) #converting the JSON response to a Python dictionary

        sources_results = None

        if get_sources_response['sources']: #checking if response has any data
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources(sources_results_list)  

    return sources_results #return a list of sources objects

def process_sources(sources_list):
    '''
    Function  that processes the sources result and transform them to a list of Objects
    Args:
        sources_list: A list of dictionaries that contain sources details
    Returns :
        sources_results: A list of sources objects
    '''
    sources_results = [] #to store our newly created sources objects
    for sources_item in sources_list:
        id = sources_item.get('id')
        name = sources_item.get('name')
        title=sources_item.get('title')
        description = sources_item.get('description')
        url = sources_item.get('url')
        category = sources_item.get('category')
        language = sources_item.get('language')
        country=sources_item.get('country')
        UrlToImage=sources_item.get('UrlToImage')


        sources_object = Source(id, name,title, description, url, category, language,country,UrlToImage)
        sources_results.append(sources_object)
    return sources_results


def article_source(id):
    article_source_url = article_url.format(id,api_key)
    print(article_source_url)
    with urllib.request.urlopen(article_source_url) as url:
        article_source_data = url.read()
        article_source_response = json.loads(article_source_data)

        article_source_results = None

        if article_source_response['articles']:
            article_source_list = article_source_response['articles']
            article_source_results = process_articles_results(article_source_list)


    return article_source_results


def process_articles_results(articles_list):
    '''
    function that processes the json files of articles from the api key
    '''
    article_source_results = []
    for article in articles_list:
        id = article.get('id')
        name = article.get('name')
        author = article.get('author')
        title = article.get('title')
        description= article.get('description')
        url = article.get ('url')
        urlToImage=article.get('urlToImage')
        publishedAt=article.get('publishedAt')

        
        article_objects = Article(id,name,author,title,description,url,urlToImage,publishedAt)
        article_source_results.append(article_objects)

    return article_source_results


#search request

def search_source(source_name):
    search_source_url = 'http://newsapi.org/v2/search/sources?&apiKey={}&query={}'.format(api_key,source_name)
    with urllib.request.urlopen(search_source_url) as url:
        search_source_data = url.read()
        search_source_response = json.loads(search_source_data)

        search_source_results = None

        if search_source_response['results']:
            search_source_list = search_source_response['results']
            search_source_results = process_sources(search_source_list)


    return search_source_results


    