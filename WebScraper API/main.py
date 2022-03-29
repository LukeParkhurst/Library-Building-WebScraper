from webscraper.models.spiderScraper import spiderScraper
from webscraper.helperFunctions import fileCleaner as fc

# here is where user can choose scraper library type. Selenium for more dynamic web pages and BeautifulSoup for simpler web pages
scraperTypeFlag = 1

# flag tells selenium, if used, which web browser to use when scraping so it can select the correct driver
browserUsageFlag = 0

# url of webpage to be scraped
url = "https://oxylabs.io/"

#file location for raw data to be written to
file = "dataFiles/sample.txt"

"""
scraper = spiderScraper()
data = scraper.scrapWebPage(scraperTypeFlag, browserUsageFlag, url, ['span', 'title'])
scraper.writeToFile("webscraper/dataFiles/sample.txt", data)
"""

fc.fileClean('webscraper\dataFiles\sample.txt', 'webscraper\dataFiles\cleanedSample.txt')