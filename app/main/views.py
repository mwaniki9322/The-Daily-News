from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources,article_source,search_source

# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    #Getting sources
    sources = get_sources()
    title = 'The Daily News'

    search_source = request.args.get('source_query')

    if search_source:
        return redirect(url_for('main.search',source_name=search_source))
    else:
   
     return render_template('index.html', title = title, sources=sources)

@main.route('/article/<id>')
def article(id):

    '''
    View article page function that returns the various article details page and its data
    '''
    # title= 'Articles'
    articles = article_source(id)
    return render_template('article.html',articles= articles,id=id )


@main.route('/article/<source_name>')
def search(source_name):
    '''
    View function to display the search results
    '''
    source_name_list = source_name.split(" ")
    source_name_format = "+".join(source_name_list)
    searched_sources = search_source(source_name_format)
    title = f'search results for {source_name}'
    return render_template('search.html',sources = searched_sources)