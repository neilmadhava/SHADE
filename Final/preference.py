from watson_developer_cloud import PersonalityInsightsV3
import json
import os
import sys
from termcolor import colored


personality_insights = PersonalityInsightsV3(
    version='2017-10-13',
    username='',
    password='',
    url='https://gateway.watsonplatform.net/personality-insights/api'
)

with open('snowden.txt') as profile_txt:
    profile = personality_insights.profile(
        profile_txt.read(),
        content_type='text/plain',
        consumption_preferences=True,
        raw_scores=True
    ).get_result()

def consumption():
	os.system('clear')
	ids = ['consumption_preferences_shopping','consumption_preferences_movie',
	'consumption_preferences_music', 'consumption_preferences_reading', 
	'consumption_preferences_health_and_activity', 'consumption_preferences_entrepreneurship',
	'consumption_preferences_environmental_concern', 'consumption_preferences_volunteering']

	names = ['Purchasing Preferences', 'Movie Preferences', 'Music Preferences',
	'Reading Preferences', 'Health & Activity Preferences', 'Entrepreneurship Preferences',
	'Environmental Concern Preferences', 'Volunteering Preferences']

	for name in names:
		print(str(names.index(name) + 1) + '. ' + name + '\n')
	print('*. Back to menu\n')

	choice = input('\nEnter Choice: ')
	index = int(choice) - 1

	print('\n')
	if index in [0, 1, 2, 3, 4, 5, 6, 7]:
		for preference in profile['consumption_preferences']:
			if preference['consumption_preference_category_id'] == ids[index]:
				for x in preference['consumption_preferences']:
					if x['score'] == 1.0:
						print("-> " + colored(x['name'], color="white") + "\n")
	else:
		os.system('clear')
		menu()

	input("Press Enter to continue...")
	os.system('clear')
	consumption()


def personality():
	os.system('clear')
	print(colored('\nName\t\t  Percentile\tRaw Score\n',color="white"))

	for person in profile['personality']:
		if person['name'] == 'Conscientiousness':
			print(person['name'] + '\t' + "%.2f" % person['percentile'] 
				+ '\t' + "%.2f" % person['raw_score'] + '\n')
		else:
			print(person['name'] + '\t\t' + "%.2f" % person['percentile'] 
				+ '\t' + "%.2f" % person['raw_score'] + '\n')

	input("\nPress Enter to continue...")
	os.system('clear')
	menu()


def menu():
	print("\n\tANALYSIS\n")
	print('1. Consumption Preferences\n2. Personality\n*. Exit\n')
	ch = input('\nEnter Choice: ')

	if ch == '1':
		consumption()
	elif ch == '2':
		personality()
	else:
		sys.exit(1)

menu()