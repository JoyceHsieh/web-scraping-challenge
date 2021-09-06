# web-scraping-challenge
In this assignment, I built a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The following outlines what you need to do.


# Data Sources

All the data were scraped from the following websites:

NASA Mars News Site - Scraped the latest News Title and Paragraph Text
JPL Featured Space Image - Scraped the image url for the current Featured Mars Image
Mars Weather twitter account - Scraped the latest Mars weather tweet
USGS Astrogeology site - Scraped high resolution images for each of Mar's hemispheres
Mars Facts webpage -Scraped the table containing facts about the planet including Diameter, Mass, etc
Web Scraping

Completed an initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter. Jupyter Notebook file called mission_to_mars.ipynb have codes of my scraping and analysis tasks.

# MongoDB and Flask Application

Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

Convered my Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that will execute all of my scraping code from above and return one Python dictionary containing all of the scraped data.

Next, I created a route called /scrape that will import my scrape_mars.py script and call my scrape function. Returned value in Mongo is stored as a Python dictionary.

There is a root route / that will query my Mongo database and pass the mars data into an HTML template to display the data.

Finally I created a template HTML file called index.html that will take the mars data dictionary and display all of the data in the appropriate HTML elements.
