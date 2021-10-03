# Wikipedia title web scapper using Python3
# Made by- Snehomoy100 (https://github.com/Snehomoy100/)

import requests
from bs4 import BeautifulSoup
import random

def scrapeWikiArticle(url): # for creating an endless scraper
	response = requests.get(
		url=url,
	)
	
	soup = BeautifulSoup(response.content, 'html.parser')

	title = soup.find(id="firstHeading")
	print(title.text)

	allLinks = soup.find(id="bodyContent").find_all("a") # for finding random <a></a> tags
	random.shuffle(allLinks)
	linkToScrape = 0

	for link in allLinks:
		# only for the wiki articles
		if link['href'].find("/wiki/") == -1: 
			continue

		# linking to scrape 
		linkToScrape = link
		break

	scrapeWikiArticle("https://en.wikipedia.org" + linkToScrape['href'])

scrapeWikiArticle("https://en.wikipedia.org/wiki/Web_scraping")