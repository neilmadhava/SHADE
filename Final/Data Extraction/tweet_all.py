from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from csv import writer
# import requests

twitter_id = input('Enter twitter id: ')

driver = webdriver.Chrome('/home/citizen/Downloads/chromedriver_linux64/chromedriver')

# For demonstration purposes, default set to twitter account "@sosadtoday".
# Change substring "sosadtoday" to suitable string to get tweets from another account.
# Example: driver.get('https://twitter.com/realdonaldtrump/')

driver.get('http://twitter.com/' + twitter_id + '/')
sleep(2)

SCROLL_PAUSE_TIME = 2
last_height=driver.execute_script("return document.body.scrollHeight")

# GETTING ALL TWEETS
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)");

    sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height==last_height:
    	break
    else:
    	last_height = new_height

# After scrolling to the bottom, the page source is passed to BeautifulSoup for 
# extracting tweet texts

soup = BeautifulSoup(driver.page_source, "html.parser")
sleep(5)
tweets = soup.findAll('div', {'class':'js-tweet-text-container'})

# WRITING TWEETS TO A CSV FILE

# with open("tweets.txt", "w") as file:
# 		csv_writer = writer(file)
# 		csv_writer.writerow(["content"])

f_name = input('Enter file name: ')

file = open(f_name, "w")
file.close()

for tweet in tweets:
    text = tweet.find('p').getText()
    
    with open(f_name, "a") as file:
    	file.write(text + "\n\n")

driver.close() 