import requests
import socket
import ssl
from urllib.request import urlopen as urlOPEN
from urllib3.exceptions import InsecureRequestWarning


# check if a web page is live or not
# return: True | False
def webpageIsLive(url, withoutSSL=False):
    ok = False
    
    context = ssl.create_default_context()
    if withoutSSL is True:
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
    
    try:
        code = urlOPEN(url=url, context=context).getcode()
        if code == 200:
            ok = True
    except Exception as err:
        pass
    return ok



# get request response text
# return: str | None
def webpageResponseText(url, withoutSSL=False):
    res = None

    # without ssl then disable warning
    if withoutSSL is True:
        requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
    
    try:
        if withoutSSL is True:
            # without ssl
            response = requests.get(url=url, verify=False)
        else:
            # with ssl
            response = requests.get(url=url)
        
        if response is not None:
            if response.status_code == 200:
                res = response.text
    except Exception as err:
        pass

    return res



# =========================================
url = "https://github.com/"
# web = webpageIsLive(url)

web = webpageResponseText(url, withoutSSL=False)
# web = webpageIsLive(url, withoutSSL=True)


print(web)

