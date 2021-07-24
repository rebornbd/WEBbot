# from celery import shared_task


class URLfrontier():
    def __init__(self, urls=[]):
        if type(urls) != type([]):
            urls = []
        self.urls = urls
    
    # urls prioritizer
    # parameters: 
    # return: 
    def prioritizer(self):
        pass

    # front queue selector & back queue router & maintains prioritization
    # parameters: 
    # return: 
    def frontQueueSelector(self):
        pass
    
    # back queue selector & maintains politeness
    # parameters: 
    # return: 
    def backQueueSelector(self):
        pass
    
    
    """
        frontier all dependency methods
        are implement below
    """
    # method name
    pass


uf = URLfrontier('')

print(type(uf.urls))
