# SHADE
An attempt at the IBM Hackhathon SHADE (Social-media Health Analysis and Display Engine) solution.

Demonstration Video - https://youtu.be/hTJqiVZv80c

Summary-

The project uses scrapy with python to get the latest tweets of target account. Then an analysis is carried out, which calculates the percentage of tweets with "sad" or "frustrated" tones. If majority of the tone is sad, two generic solutions are provided to help alleviate the mood of the person. However, human psychology is not simple and generic solutions are often unhelpful. Therefore, to provide more custom and personalised solution, a better approach is required. 

To accomplish that, we require more data on the past moods and behaviour. To implement this, Selenium has been used to scrape all tweets of the target user. Then, a list is generated containing tweets with a positive tone. Then, the keywords from each tweet in the list is extracted. These keywords can further be used to implement machine learning algorithms to compute or predict the mood of the person or provide effective solution to the target user.

Why Web Scraping?
Web scraping is more reliable since it doesn't depend on an external API. Also, web scraping can be applied to any website such as facebook, or instagram to extract the required data without the need to use different APIs to accomplish the same.