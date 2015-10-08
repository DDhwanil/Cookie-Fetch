from annobrowser import *
from BeautifulSoup import BeautifulSoup

url=raw_input('Enter url (In form of http:// or https://) :http')
url='http'+url
no=int(raw_input('Enter the number of time to fetch cookie :'))
a=annobrowser(proxies=[],user_agents=[('User-agent','whatever')])
try:
    for aa in range(no):
        a.anonymize()
        res=a.open(url)
        print '\n'
        for cooki in a.cookie_jar:
            print cooki
        print '\n'
except Exception, e:

    if 'HTTP Error 403: Forbidden' in str(e):
        print "Firewall Block or Url not accessible"
