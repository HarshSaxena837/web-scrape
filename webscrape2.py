


import httplib2
from bs4 import BeautifulSoup, SoupStrainer


url = "https://www.yelp.com/biz/berd-and-klauss-new-york-4"


http = httplib2.Http()

response, content = http.request(url)


links= []

for link in BeautifulSoup(content).find_all('a', href=True):

  links.append(link['href'])



for link in links:
  print(links)

