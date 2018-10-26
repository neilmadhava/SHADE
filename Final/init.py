from __future__ import print_function
from watson_developer_cloud import ToneAnalyzerV3
import json
import subprocess
import requests
from termcolor import colored
from random import choice
from selenium import webdriver
import sys
import os
from bs4 import BeautifulSoup

os.system('clear')
in_ch = input("1. Use existing file\n2. Scrape new data\n\nEnter Choice [1/2]: ")

if in_ch == '2':
	# Getting most recent tweets of target twitter account using scrape_tweets.sh script
	# which calls the "tweets" spider in "Twitter" scrapy project.
	subprocess.call(
	    ['/home/citizen/Documents/(2) Programs/Scripts/scrape_tweets.sh'])

tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    username='',
    password='',
    url='https://gateway.watsonplatform.net/tone-analyzer/api'
)

file = input("\nEnter json file name with tweets: ")


with open('/home/citizen/Documents/(2) Programs/Python Programming/Scrapy/twitter/' + file) as f:
    utterances = json.load(f)

utterance_analyses = tone_analyzer.tone_chat(utterances).get_result()
print(utterance_analyses)
sad = 0
count = 0

# The following for loop gets the tone of each tweet and increments the 'sad'
# variable by 1 if 'sad' tone is encountered. The 'count' variable tracks the number
# of tweets analysed but decrements the counter by 1 when the tone is not analused.


def analyze():
    # sad = 0
    # count = 0
    flag = 0
    for entity in utterance_analyses['utterances_tone']:
        # count += 1
        flag=0
        if(len(entity['tones']) == 0):
            print("\n\nText: " +
                  entity['utterance_text'] + "\nTones: ", end='', flush=True)
            print("None", end=' ', flush=True)
            # count -= 1
        else:
            for tones in entity['tones']:
                if (tones['tone_name'] == 'Sad') or (tones['tone_name'] == 'Frustrated'):
                    # sad += 1
                    flag = 1

            if flag:
                print("\n\nText: " + colored(entity['utterance_text'],
                                             color="red") + "\nTones: ", end='', flush=True)
            else:
                print(
                    "\n\nText: " + entity['utterance_text'] + "\nTones: ", end='', flush=True)

            for tones in entity['tones']:
                print(tones['tone_name'], end=' ', flush=True)


for entity in utterance_analyses['utterances_tone']:
    count += 1
    if(len(entity['tones']) == 0):
        count -= 1
    else:
        for tones in entity['tones']:
            if (tones['tone_name'] == 'Sad') or (tones['tone_name'] == 'Frustrated'):
                sad += 1

# Calculating the percentage of sad tweets
percent = sad/count*100

os.system('clear')
print("\nThe percentage of sad tweets = " + "%.2f" % percent + "%")

# Function to print jokes. Utilises the API offered by icanhazdadjoke.com


def joke():
    os.system('clear')
    valid_colors = ("red", "green", "yellow", "blue",
                    "magenta", "cyan", "white")
    print("1. Search Joke\n2. Print Random Joke\n3. Exit to Main Menu\n")
    ch = input("\n\nEnter choice [1/2/3]: ")
    os.system('clear')

    if ch == '2':
        url = "https://icanhazdadjoke.com"
        usr_input = ' '

        while usr_input[0] != "n":
            response = requests.get(
                url,
                headers={"Accept": "application/json"},
            ).json()

            print(colored(response['joke'], color=choice(valid_colors)))
            usr_input = input("Print Another (y/n)? ").lower()
            print("")

        input("Press Enter to continue...")
        os.system('clear')
        menu()
    elif ch == '1':
        usr_in = input("Search Term: ")
        url = "https://icanhazdadjoke.com/search"
        res = requests.get(
            url,
            headers={"Accept": "application/json"},
            params={"term": usr_in}
        ).json()
        results = res['results']
        total_jokes = res['total_jokes']
        if total_jokes > 1:
            print(
                "I've got {0} jokes about {1}. Here's one:\n".format(
                    total_jokes, usr_in)
            )
            print(colored(choice(results)['joke'], color=choice(valid_colors)))
            input("Press Enter to continue...")
            os.system('clear')
            menu()
        elif total_jokes == 1:
            print("I've got one joke about {0}. Here it is:\n".format(usr_in))
            print(colored(results[0]['joke'], color=choice(valid_colors)))
            input("Press Enter to continue...")
            os.system('clear')
            menu()
        else:
            print(
                "Sorry, I don't have any jokes about {0}! Please try again.".format(usr_in))
            joke()
    elif ch == '3':
        menu()
    else:
        print("Wrong Input. Try Again.")
        joke()


# Function to display an Explosm comic
def explosm():
    os.system('clear')
    usr_input = ' '

    while usr_input[0] != "n":
        response = requests.get("http://explosm.net/comics/random")
        soup = BeautifulSoup(response.text, "html.parser")

        random_img_url = "http:" + str(soup.find(id="main-comic")["src"])
        subprocess.run(["eog", random_img_url])
        usr_input = input("Print Another (y/n)? ").lower()

    input("Press Enter to exit to main menu...")
    os.system('clear')
    menu()


# Function to display menu of possible solutions
def menu():
    print("\n\nSolutions:-\n1. Display joke\n2. Play songs based on mood\n" +
          "3. Display a 'Cyanide and Happiness' comic\n4. Exit")
    ch = input("Enter Choice: ")

    if ch == '1':
        joke()
    elif ch == '2':
        driver = webdriver.Chrome(
            '/home/citizen/Downloads/chromedriver_linux64/chromedriver')
        driver.get('https://moodfuse.com/')
    elif ch == '3':
        explosm()
    else:
        sys.exit(1)

    menu()


# View Detailed analysis of each tweet
in_detail = input("View detailed analysis of each tweet? [y/n]: ")
if in_detail[0].lower() == 'y':
    os.system('clear')
    analyze()
    input("\n\nPress Enter to continue...")
    os.system('clear')

# Display menu if the target twitter account has majority percentage of sad/frustrated tweets
if percent > 50:
    menu()
