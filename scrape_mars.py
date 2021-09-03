import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import requests
from webdriver_manager.chrome import ChromeDriverManager


def scrape():
    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Set up url
    nasa_url = "https://mars.nasa.gov/news/"
    browser.visit(nasa_url)

    # NASA Mars latest News
    # Scrape html and fine item list
    nasa_html = browser.html
    nasa_soup = bs(nasa_html, "html.parser")
    nasa_results = nasa_soup.find("ul", class_="item_list")

    news_title = nasa_results.find("div", class_="content_title").text
    news_p = nasa_results.find("div", class_="article_teaser_body").text

    #___________________________________________________________
    # Set up url
    #JPL Mars Space Images - Featured Image
    jpl_url = "https://spaceimages-mars.com"
    browser.visit(jpl_url)


    # Find figure to retrieve section that has image url
    jpl_html = browser.html
    jpl_soup = bs(jpl_html, "html.parser")
    jpl_img = jpl_soup.find("img", class_="headerimage fade-in")

    img_src=jpl_img['src']
    featured_image_url = 'https://spaceimages-mars.com/' + img_src


    #___________________________________________________________
    #Mars Facts
    # Set up url and scrape latest tweets
    facts_url = "https://galaxyfacts-mars.com"
    tables = pd.read_html(facts_url)
    Comparison_df = tables[0]
    Comparison_df.columns =["Comparison", "Mars", "Earth"]
    Comparison_df = Comparison_df.iloc[1:]
    Comparison_df.set_index('Comparison', inplace=True)
    Comparison_html_table = Comparison_df.to_html()

    #___________________________________________________________
    # Mars Hemispheres
    # Visit the USGS Astrogeology site 
    h_url = "https://marshemispheres.com"
    browser.visit(h_url)

    # Scrape the site and visit each hemisphere page
    title_list = []
    url_list = []

    for result in range(1):
        h_html = browser.html
        h_soup = bs(h_html, "html.parser")
        h_results = h_soup.find_all("div", class_="item")
        
        # Get url for each hemisphere
        for item in h_results:
            item_url = item.find("h3").text.split(' ')[0].lower()
            if item_url=="syrtis":
                item_full_url='https://marshemispheres.com/images/' + item_url + '_major' +'_enhanced.tif'
            elif item_url=="valles":
                item_full_url='https://marshemispheres.com/images/' + item_url + '_marineris' +'_enhanced.tif'
            else:
                item_full_url = 'https://marshemispheres.com/images/' + item_url +'_enhanced.tif'
            url_list.append(item_full_url)
            title = item.find("h3").text
            title_list.append(title)

    hemisphere_image_urls = []

    for url,title in zip(url_list,title_list):
        hemisphere_image_dict = {}
        hemisphere_image_dict["title"] = title
        hemisphere_image_dict["img_url"] = url
        hemisphere_image_urls.append(hemisphere_image_dict)

    # Return all results as one dictionary
    mars_data_dict = {
        "news_title" : news_title,
        "news_p" : news_p,
        "featured_image_url" : featured_image_url,
        "table":Comparison_html_table,
        "hemisphere_image" : hemisphere_image_urls
    }


    # Close the browser after scraping
    browser.quit()

    # Return results
    return(mars_data_dict)

