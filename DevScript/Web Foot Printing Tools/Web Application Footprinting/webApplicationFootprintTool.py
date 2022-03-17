import urllib
from bs4 import BeautifulSoup

targetURL = input("Enter the target URL: ")
page = urllib.urlopen(targetURL)
htmlPage = page.read()

# create Soup object from html page
soupObject = BeautifulSoup(htmlPage)

# getting title name with and without tag
print(f"Title with tags: {soupObject.title}")
print(f"Title without tags: {soupObject.title.text}")

# a searches for all <a></a> tags
for link in soupObject.find_all('a'):
	# href has the URL of the link
	print(link.get('href'))