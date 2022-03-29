import requests
from selenium.webdriver import Chrome
from bs4 import BeautifulSoup


"""
class: The spiderScraper class holds the basic tools for scraping a webpage and writing it to a raw file
"""
class spiderScraper:

    def __init__(self, id = 1):
        self.id = id

    """
    Function to scrape a single webpage
    scraperLibrary: allows user to switch between BeautifulSoup (input = 0) and Selenium (input = 1) libraries
    browserToBeUsed: allows user to switch which browser to scrape with if using Selenium library
    url: the url of the webpage the user is trying to scrape
    customBrowserDriver: allows the user to use own browser driver in the case of none common browser or different browser version, can be ignored
    """
    def scrapWebPage(self, scraperLibrary, browserToBeUsed, url, tagsToLookFor = [], customBrowserDriver = ""):
        # use Soup
        if scraperLibrary == 0:
            # pull the html content from the website
            response = requests.get(url)

            # if a form is needed to be filled, can fill a dictionary that is posted to the website
            #form_data = {'key1': 'value1', 'key2': 'value2'}
            #response = requests.post("https://oxylabs.io/ ", data=form_data)
            #print(response.text.encode("utf-8"))

            # create variable with soup to retrieve html
            soup = BeautifulSoup(response.text, 'html.parser')
            # if no desired tags to be retrieved has been input, take all text of html
            if len(tagsToLookFor) == 0:
                data = soup.get_text()
                return data
            else:
                data = []
                for tag in tagsToLookFor:
                    tagData = soup.findAll(tag)
                    data.append(list(tagData))
                print(data)
                return data

        # use Selenium
        else:
            if customBrowserDriver != "":
                    try:
                        driver = Chrome(executable_path=customBrowserDriver)
                        data = driver.get(url)
                        print(data)
                        return "check"
                    except:
                        print("Driver not found")
            else:
                match browserToBeUsed: # used to switch browser driver for grabbing information from
                    case 0:
                        driver = Chrome(executable_path='webscraper\webDrivers\chromedriver.exe')
                        data = self.seleniumGetData(url, driver, tagsToLookFor)
                    case 1:
                        print("to be used with Edge driver")
                    case 2:
                        print("to be used with FireFox driver")
                    case 3:
                        print("to be used with Safari Driver")
                    case _:
                        print("Not a correct webDriver selection, please select from the folowing.")
                        print("0 - Chrome, 1 - Edge, 2 - FireFox, 3 - Safari")
                        return
                driver.quit() # closing the browser driver
                return data

    """
    Function for Selenium to find data from website, written to follow DRY for multiple drivers
    driver: driver being used for the webpage scraping
    tagsToLookFor: optional list of html elements tags to look for and grab data from
    """
    def seleniumGetData(self, url, driver, tagsToLookFor = []):
        driver.get(url)
        # if no desired tags to be retrieved has been input, take all of the html
        if len(tagsToLookFor) == 0:
            data = driver.page_source
            data = str(data)
            return data
        else:
            data = []
            for tag in tagsToLookFor:
                tagData = driver.find_elements_by_tag_name(tag)
                #print(tagData)
                for dataPiece in tagData:
                    print(dataPiece.text, tag)
                    data.append([dataPiece.text])
            #print(data)
        return data

    """
    Function to write raw data to a file
    fileWriteLocation: parameter on where the file to write into is, or to create a new file at the chosen location
    data: the chosen data to be written to the file
    """
    def writeToFile(self, fileWriteLocation, data):
            try:
                #print(type(data))
                # if the data is in an array due to choosing specific elements
                if isinstance(data, list):
                    with open(fileWriteLocation, "w", newline="", encoding="UTF-8") as file:
                        for dataPiece in data:
                            file.writelines("%s\n" % singleDataPiece for singleDataPiece in dataPiece)

                # otherwise if all text is gathered, then write the data to the file
                else:
                    with open(fileWriteLocation, "w", newline="", encoding="UTF-8") as file:
                        file.write(data)

            except:
                print("Unable to write to file")
