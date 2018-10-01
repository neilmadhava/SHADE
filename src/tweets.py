# -*- coding: utf-8 -*-
import scrapy

id = input("Enter twitter ID: ")
url = 'twitter.com/'

class TweetsSpider(scrapy.Spider):
    name = 'tweets'
    allowed_domains = [url+id]
    start_urls = ['http://' + url + id + '/']

    def parse(self, response):
        tweets = response.xpath('//*[@class="content"]')
        
        for tweet in tweets:
        	text = tweet.xpath('.//p//text()').extract()
        	text = "".join(text)
        	time = tweet.xpath('.//small/.//*/span/text()').extract()

        	if(len(time)>1):
        		time = time[1]

        	yield {
        		'text': text,
        		'Time': time
        	}