"""
Example showing how to read in from a web page
"""

from bs4 import BeautifulSoup
import urllib.request

# Read in the web page
url= "http://simpson.edu"
page = urllib.request.urlopen(url)

# Parse the web page
soup = BeautifulSoup(page.read(), "html.parser")

# Get a list of level 1 headings in the page
headings = soup.findAll("h1")

# Loop through each row
for heading in headings:
    print(heading.text)
