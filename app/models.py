class Source:
    '''
    Source class to define Source Objects
    '''

    def __init__(self,id,name,title,description,url,category,language,country,UrlToImage):
        self.id =id
        self.name = name
        self.title = title
        self.description = description
        self.url = url
        self.category=category
        self.language=language
        self.country=country
        self.UrlToImage=UrlToImage


class Article:
    '''
    Article class to define Article Objects
    '''

    def __init__(self,id,name,author,title,description,url,urlToImage,publishedAt):
        self.id =id
        self.name = name
        self.title = title
        self.description = description
        self.url = url
        self.publishedAt=publishedAt
        self.urlToImage=urlToImage
        self.publishedAt=publishedAt