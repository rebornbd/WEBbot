import requests
from bs4 import BeautifulSoup
from django.core.validators import URLValidator
from urllib.parse import urlparse, urlsplit, urljoin


class Crawl:
    def __init__(self, url=None):
        self.url = url
    
    def __getSource(self):
        return requests.get(self.url).text
    
    def __getSoup(self):
        source = self.__getSource()
        return BeautifulSoup(source, 'lxml')

    def __urlValidator(self, url=None):
        validate = URLValidator()
        try:
            validate(url)
            return True
        except Exception as err:
            pass
        return False
    
    def show(self):
        soup = self.__getSoup()

        links = []
        invalidLinks = []
        for link in soup.find_all('a'):
            myurl = link.get('href')
            join_url = urljoin(base=self.url, url=myurl)
            if (self.__urlValidator(join_url)):
                links.append(join_url)
            else:
                invalidLinks.append(myurl)
        
        print("Valid links:")
        for indx in range(0, len(links)):
            print(f"link {indx+1}: {links[indx]}")

        print("\n\nInvalid links:")
        for indx in range(0, len(invalidLinks)):
            print(f"link {indx+1}: {invalidLinks[indx]}")


# c = Crawl("https://github.com")
# c.show()


import requests
from urllib.request import urlopen

url = "https://github.com"

# conn = urlopen(url=url).getcode()
conn = requests.head(url)

print(conn)

# request = requests.get(url)
# if request.status_code == 200:
#     print('Web site exists')
# else:
#     print('Web site does not exist')

# host = "https://github.com"
# paths = ["/login", "logout", "/about/", "https://cloud.com/list/10?param=some-params#io=testio"]

# for i in range(0, len(paths)):
#     link = urljoin(base=host, url=paths[i])
#     link = urlparse(link)

#     print(link.geturl())

