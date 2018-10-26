from __future__ import print_function
from watson_developer_cloud import ToneAnalyzerV3
import json
import sys
import os
from termcolor import colored
# import subprocess
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
    import Features, EntitiesOptions, KeywordsOptions, RelationsOptions, SemanticRolesOptions

# CALLING TONE ANALYSER API

tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    username='',
    password='',
    url='https://gateway.watsonplatform.net/tone-analyzer/api'
)

texts_pos = []
texts_neg = []

with open('tweets.json') as f:
    utterances = json.load(f)

utterance_analyses = tone_analyzer.tone_chat(utterances).get_result()

# GETTING TWEETS WITH POSITIVE AND NEGATIVE TONE

for entity in utterance_analyses['utterances_tone']:
    for tones in entity['tones']:
        if tones['tone_id'] in ['polite', 'satisfied', 'sympathetic', 'excited']:
            if entity['utterance_text'] not in texts_pos:
                texts_pos.append(entity['utterance_text'])
        if tones['tone_id'] in ['sad', 'frustrated']:
            if entity['utterance_text'] not in texts_neg:
                texts_neg.append(entity['utterance_text'])

# APPLYING NATURAL LANGUAGE UNDERSTANDING ALGORITHM TO GET POSITIVE KEYWORDS IN POSITIVE TWEETS
# CALLING NATURAL LANGUAGE UNDERSTANDING API

natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2018-03-16',
    username='',
    password='',
    url='https://gateway.watsonplatform.net/natural-language-understanding/api'
)


def key_Pos():
    os.system('clear')
    for text in texts_pos:
        response = natural_language_understanding.analyze(
            text=text,
            features=Features(
                keywords=KeywordsOptions(
                    emotion=True,
                    sentiment=True))).get_result()
        print('\nText: ' + text + "\nKeywords:-")

        # PRINTING KEYWORDS WITH POSITIVE SENTIMENT
        for keys in response['keywords']:
            if keys['sentiment']['label'] == 'positive':
                print(colored(keys['text'], color="red"))
    input("\n\nPress Enter to continue...")
    os.system('clear')
    menu()


def key_Neg():
    os.system('clear')
    for text in texts_neg:
        response = natural_language_understanding.analyze(
            text=text,
            features=Features(
                keywords=KeywordsOptions(
                    emotion=True,
                    sentiment=True))).get_result()
        print('\nText: ' + text + "\nKeywords:-")

        # PRINTING KEYWORDS
        for keys in response['keywords']:
            print(colored(keys['text'], color="red"))
    input("\n\nPress Enter to continue...")
    os.system('clear')
    menu()


def sem_role():
    os.system('clear')
    for text in texts_pos:
        response = natural_language_understanding.analyze(
            text=text,
            features=Features(
                semantic_roles=SemanticRolesOptions(
                    entities=True,
                    keywords=True
                ))).get_result()
        print('\nText: ' + text + "\nActions:-")

        for x in response["semantic_roles"]:
            if x["subject"]["text"].lower() == 'i':
                print(colored(x["action"]["text"], color="red"))
    input("\n\nPress Enter to continue...")
    os.system('clear')
    menu()

    # print("\n\n" + json.dumps(response, indent=5))


def menu():
    print('\tMENU')
    print('\n1. Display Keywords in positive tweets')
    print('2. Display Keywords in negative tweets')
    print('3. Display Action words in positive tweets')
    print('*. Exit')

    ch = input('\nEnter Choice: ')

    if ch == '1':
        key_Pos()
    elif ch == '2':
        key_Neg()
    elif ch == '3':
        sem_role()
    else:
        sys.exit(1)


menu()

# OUTPUT
# {
#  "semantic_roles": [
#       {
#            "subject": {
#                 "text": "everyone"
#            },
#            "action": {
#                 "verb": {
#                      "tense": "present",
#                      "text": "be"
#                 },
#                 "normalized": "be",
#                 "text": "is"
#            },
#            "sentence": "seems like everyone is a professional selfie taker and i'm just eating cereal",
#            "object": {
#                 "keywords": [
#                      {
#                           "text": "professional selfie taker"
#                      }
#                 ],
#                 "text": "a professional selfie taker"
#            }
#       },

#       {
#            "subject": {
#                 "text": "i"
#            },
#            "action": {
#                 "verb": {
#                      "tense": "present",
#                      "text": "be"
#                 },
#                 "normalized": "be",
#                 "text": "am"
#            },
#            "sentence": "seems like everyone is a professional selfie taker and i'm just eating cereal",
#            "object": {
#                 "keywords": [
#                      {
#                           "text": "cereal"
#                      }
#                 ],
#                 "text": "just eating cereal"
#            }
#       },

#       {
#            "subject": {
#                 "text": "i"
#            },
#            "action": {
#                 "verb": {
#                      "tense": "present",
#                      "text": "eat"
#                 },
#                 "normalized": "eat",
#                 "text": "eating"
#            },
#            "sentence": "seems like everyone is a professional selfie taker and i'm just eating cereal",
#            "object": {
#                 "keywords": [
#                      {
#                           "text": "cereal"
#                      }
#                 ],
#                 "text": "cereal"
#            }
#       }
#  ],

#  "language": "en",

#  "usage": {
#       "text_characters": 77,
#       "features": 1,
#       "text_units": 1
#  }
# }
