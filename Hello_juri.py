import requests
#import BeautifulSoup4 as bs4

print ("Hallo Juri")

session = requests.Session()
req = session.get("https://www.google.com")

print req
print req.content

print(' Leo codet hart ab! ')

print 'Leoo lernt branch'