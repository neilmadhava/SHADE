from __future__ import print_function
from watson_developer_cloud import ToneAnalyzerV3
import json
import subprocess
import requests
from termcolor import colored
from random import choice
from selenium import webdriver
import sys

# Getting most recent tweets of target twitter account using scrape_tweets.sh script
# which calls the "tweets" spider in "Twitter" scrapy project.
subprocess.call(['/home/citizen/Documents/(2) Programs/Scripts/scrape_tweets.sh'])

tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    username='fb45a89b-4f77-46b0-a339-bde58755df55',
    password='ZBhsW1nVlXpt',
    url='https://gateway.watsonplatform.net/tone-analyzer/api'
)

file = input("\nEnter json file name with tweets: ")


with open('/home/citizen/Documents/(2) Programs/Python Programming/Scrapy/twitter/' + file) as f:
	utterances = json.load(f)

utterance_analyses = tone_analyzer.tone_chat(utterances)

sad=0
count=0

# The following for loop gets the tone of each tweet and increments the 'sad'
# variable by 1 if 'sad' tone is encountered. The 'count' variable tracks the number
# of tweets analysed but decrements the counter by 1 when the tone is not analused.

for entity in utterance_analyses['utterances_tone']:
    count+=1
    print("\n\nText: " + entity['utterance_text'] + "\nTones: ", end='', flush=True)
    if(len(entity['tones']) == 0):
    	print("None", end=' ', flush=True);count-=1
    else:
    	for tones in entity['tones']:
            if (tones['tone_name']=='Sad') or (tones['tone_name']=='Frustrated'):
                sad+=1
    		
            print(tones['tone_name'], end=' ', flush=True)

# Calculating the percentage of sad tweets
print("\nThe percentage of sad tweets = "+ str(sad/count*100) + "%")

# Function to print jokes. Utilises the API offered by icanhazdadjoke.com
def joke():
    url = "https://icanhazdadjoke.com"
    valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")
    usr_input = ' '

    while usr_input[0] != "n":
        response = requests.get(
            url, 
            headers={"Accept":"application/json"},
            ).json()

        print(colored(response['joke'], color=choice(valid_colors)))
        usr_input = input("Print Another (y/n)? ").lower()
        print("")


# Function to display menu of possible solutions
def menu():
    print("\n\nSolutions:-\n1. Print random joke.\n2. Play songs based on mood.\n3. Exit")
    ch = input("Enter Choice: ")

    if ch == '1':
        joke()
    elif ch=='2':
        driver = webdriver.Chrome('/home/citizen/Downloads/chromedriver_linux64/chromedriver')
        driver.get('https://moodfuse.com/')
    else:
        sys.exit(1)

    menu()

# Display menu if the target twitter account has majority percentage of sad/frustrated tweets

if (sad/count*100)>50:
    menu()