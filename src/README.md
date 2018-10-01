Description of files:-

tweets.py - scrapy spider which extracts 20-25 most recent tweets from the user.

scrape_tweets.sh - A simple shell script which utilises tweets.py and scrapy commandline to output required json file to be used for further analysis.

init.py - Calculates the percentage of tweets marked as "sad" by the toneAnalyzer API. If percentage is more than 50, then generic solutions (Jokes and Song playlist based on mood website) are offered.