from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250')

#button = driver.find_element(By.ID, 'list-view-option-detailed')
#button.click()

soup = BeautifulSoup(driver.page_source, 'html.parser')
#soup

movies_list = soup.find_all('li',{'class':'ipc-metadata-list-summary-item'})
#movies_list[0]

len(movies_list)

titles = []
images = []
years = []
durations=[]
imdb_ratings = []
descs=[]

for movie in movies_list:
    title =  movie.h3.text
    titles.append(title)
    image = movie.img['src']
    images.append(image)
    year = movie.find_all('span',{'class':'sc-b189961a-8 kLaxqf cli-title-metadata-item'})[0].text
    years.append(year)
    duration =  movie.find_all('span',{'class':'sc-b189961a-8 kLaxqf cli-title-metadata-item'})[1].text
    durations.append(duration)
    imdb_rating = movie.find('span',{'class':'ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating'}).text
    imdb_ratings.append(imdb_rating)
    desc = movie.find('div',{'class':'ipc-html-content-inner-div'})
    descs.append(desc)

    #print(descs)
    break

import pandas as pd
data =  pd.DataFrame({'titles':titles, 'year':years,'duration':durations,'images':images,'description':descs,'imdb_ratings':imdb_ratings})
data

data.to_csv('IMDB top 250 movies.csv')
