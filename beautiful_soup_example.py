# WEBSCRAPING SCRIPT
# ScarlettOhara -- 2017

# You will need the BeautifulSoup module
# You can pip install
import bs4

from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

# I since I was only scraping seach results I have this URL input here
my_url = input('Please enter a URL: ')

# Grab the HTML of the page
client = urlopen(my_url)
page_html = client.read()
client.close()

# Parse that shizz
page_soup = soup(page_html, "html.parser")

# This is an example of how i would search the html soup for the specific info
# i needed. the below finds all the classes named "item-conainer" within div
# tags and then grabs the the brand data from those tags.
containers = page_soup.findAll("div", {"class":"item-container"})
for container in containers:
    brand = container.div.div.a.img["title"]
    # the above would grab the brand from the div/div/a/img tag named 'title'
    # but you could also use the same findAll method as seen above
    print('Brand: ' + str(brand))

