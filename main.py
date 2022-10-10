# In order to read xml format, you need to install lxml by using pip install lxml
from bs4 import BeautifulSoup
import requests
url = requests.get('https://realpython.com/atom.xml')

#soup = BeautifulSoup(url.content, 'xml')
#if we use XML parser - error is comins as ->  bs4.FeatureNotFound: Couldn't find a tree builder with the features you requested: xml. Do you need to install a 
#parser library?
# so change to html.parser - its working

soup = BeautifulSoup(url.content, "html.parser")
entries = soup.find_all('entry')
rss = []
for i in entries:
  title = i.title.text
  link = i.link['href']
  summary = i.summary.text
  print('Title: ', title, '\n\nSummary: ', summary, '\n\nLink: ', link,'\n\n------------------------\n')  
