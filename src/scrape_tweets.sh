#!/bin/bash

cd /home/citizen/Documents/\(7\)\ System/virtual_environments/v1/ && source bin/activate && cd
cd /home/citizen/Documents/\(2\)\ Programs/Python\ Programming/Scrapy/twitter/
read -p "Enter filename to store tweets: " FILE
scrapy crawl tweets -o $FILE --nolog
deactivate
cd