from __future__ import print_function
from watson_developer_cloud import ToneAnalyzerV3
import json
import subprocess
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features, EntitiesOptions, KeywordsOptions, RelationsOptions

# CALLING TONE ANALYSER API

tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    username='',
    password='',
    url='https://gateway.watsonplatform.net/tone-analyzer/api'
)

texts = []  

with open('tweets.json') as f:
    utterances = json.load(f)

utterance_analyses = tone_analyzer.tone_chat(utterances)

# GETTING TWEETS WITH POSITIVE TONE

for entity in utterance_analyses['utterances_tone']:
    for tones in entity['tones']:
        if (tones['tone_id'] == 'satisfied') or (tones['tone_id'] == 'excited'):
            texts.append(entity['utterance_text'])


# APPLYING NATURAL LANGUAGE UNDERSTANDING ALGORITHM TO GET POSITIVE KEYWORDS IN POSITIVE TWEETS
# CALLING NATURAL LANGUAGE UNDERSTANDING API

natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2018-03-16',
    username='',
    password='',
    url='https://gateway.watsonplatform.net/natural-language-understanding/api'
)

for text in texts:
    response = natural_language_understanding.analyze(
      text=text,
      features=Features(
        keywords=KeywordsOptions(
          emotion=True,
          sentiment=True)))
    print('\nText: ' +text + "\nKeywords:-")

    # PRINTING KEYWORDS WITH POSITIVE SENTIMENT 
    for keys in response['keywords']:
        if keys['sentiment']['label'] == 'positive':
            print(keys['text'])