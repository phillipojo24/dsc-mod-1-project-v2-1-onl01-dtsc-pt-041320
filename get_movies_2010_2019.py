from selenium import webdriver      
#from selenium.common.exceptions import NoSuchElementException
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
import time
import csv
driver = webdriver.Chrome()
driver.get('https://www.themoviedb.org/movie')

#Get  Sort and FIlters


filterButton = driver.find_element_by_xpath('//*[@id="media_v4"]/div/div/div[2]/div[1]/div[2]/div[1]/span')
filterButton.click()


release_date_start = driver.find_element_by_xpath('//*[@id="release_date_gte"]')
release_date_start.send_keys('1/1/2010')

release_date_end = driver.find_element_by_xpath('//*[@id="release_date_lte"]')
release_date_end.send_keys('12/30/2019')

#Complete Search
searchButton = driver.find_element_by_xpath('//*[@id="media_v4"]/div/div/div[2]/div[3]/p/a')
searchButton.click()

#loadMoreButton = driver.find_element_by_xpath('//*[@id="pagination_page_1"]/p/a')
#loadMoreButton.click()




#Get Data from Webscrapping Start by Retriving Titles

# GETTING SPECIFIC MOVIE URL TO EXTRACT THE DATA AND ADDING IT TO A LIST
movietitleList = driver.find_element_by_id('herf')

    
print('end of process')



import math

millnames = ['',' K',' M',' B',' T']

def millify(n):
    n = float(n)
    millidx = max(0,min(len(millnames)-1,
                        int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))

    return '{:.0f}{}'.format(n / 10**(3 * millidx), millnames[millidx])