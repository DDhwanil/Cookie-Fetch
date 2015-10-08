from annobrowser import *
from BeautifulSoup import BeautifulSoup

url=raw_input('Enter url (In form of http:// or https://) :http')
url='http'+url
no=int(raw_input('Enter the number of time to fetch cookie :'))
a=annobrowser(proxies=[],user_agents=[('User-agent','whatever')])
for aa in range(no):
    a.anonymize()
    res=a.open(url)
    print '\n'
    for cooki in a.cookie_jar:
        print cooki
    print '\n'
