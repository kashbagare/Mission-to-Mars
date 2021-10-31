#!/usr/bin/env python
# coding: utf-8

# In[22]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[23]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[24]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[26]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[27]:


slide_elem.find('div', class_='content_title')


# In[28]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[29]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# In[30]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[31]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[32]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[33]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[34]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# In[35]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[36]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[37]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[38]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[39]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
# Find the relative image url
html = browser.html
img_soup = soup(html, 'html.parser')
elements = img_soup.find_all('div', class_='item')


for i in elements:
    hemisphere = {}

    link = url + i.find('a', class_='itemLink product-item').get('href')
    browser.visit(link)
    
    html = browser.html
    img_soup = soup(html, 'html.parser')
    
    hemisphere['title'] = img_soup.find('h2').get_text()

    img_url = img_soup.find('img', class_='wide-image').get('src')
    hemisphere['url'] = url + img_url  

    hemisphere_image_urls.append(hemisphere)

    browser.back()


# In[40]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[41]:


# 5. Quit the browser
browser.quit()


# In[ ]:




