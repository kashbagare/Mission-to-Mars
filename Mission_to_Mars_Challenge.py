#!/usr/bin/env python
# coding: utf-8

# In[208]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[209]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[210]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[211]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[212]:


slide_elem.find('div', class_='content_title')


# In[213]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[214]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# In[215]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[216]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[217]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[218]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[219]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# In[220]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[221]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[222]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[247]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[281]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
# Find the relative image url
html = browser.html
img_soup = soup(html, 'html.parser')
url = img_soup.find('img',class_="thumb").get('src')
title = img_soup.find('h3').get_text()

hemispheres['img_url'] = f'https://marshemispheres.com/{url}'
hemispheres["title"] = title
hemisphere_image_urls.append(hemispheres)


#print(title)


#for link in links:
#    hemispheres = {}
    
#    url = link.find('a', class_= 'itemLink product-items')[href]
    
    #title = i.find("h3")
    #url = i.find()
    
    #hemispheres["title"] = title
    #hemisphere_image_urls.append(hemispheres)

    #url = i.find('img', class_='thumb').get('src')
    
#    html = browser.html
#    img_soup = soup(html, 'html.parser')
#    tag = img_soup.find('div', class_='item')
#    title = img_soup.find('h3').text()
    
#    hemispheres['img_url'] = f'https://marshemispheres.com/{url}'
 #   hemisphere_image_urls.append(hemispheres)
        
#    browser.back()
    
#browser.quit()



#    html = browser.html
#    img_soup = soup(html, 'html.parser')
    

#img_url = f'https://marshemispheres.com/{tag}'
#img_url

#title = img_soup.find('h3').get_text()
#title


# In[282]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[19]:


# 5. Quit the browser
browser.quit()


# In[ ]:




