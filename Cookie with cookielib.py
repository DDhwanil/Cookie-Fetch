import cookielib,mechanize
b=mechanize.Browser()
b.set_handle_robots(False)
c=cookielib.LWPCookieJar()
b.set_cookiejar(c)
url=raw_input('Enter url (In form of http:// or https://) :http')
url='http'+url
op=b.open(url)
print '\n',c
