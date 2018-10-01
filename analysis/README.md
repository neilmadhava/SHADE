Description of files:-

tweet_all.py - gets all tweets from target user using selenium webdriver in CSV format.

csvtojson.py - converts output of tweet_all.py [CSV file] to JSON file.

watson_keyword.py - uses JSON file from csvtojson.py as input and applies toneAnalyzer and NaturalLanguageUnderstanding from IBM Watson. All tweets are analyzed and only tweets with positive tones are extracted. Furthermore, keywords from each of the positive tweets are analysed. 

The keywords can be scrutinised and an algorithm can be formulated to predict moods during specific months. Also, a customised solution can be presented for each user rather than generic ones.