#!/usr/bin/python2

import requests
import webbrowser
from bs4 import BeautifulSoup

#Input query to be searched
word=raw_input("Enter input")

#Search url
web_page=requests.get("https://www.google.com/search?q="+word)

#Extracting text only
data=web_page.text

#Parshing data using BS
scraped=BeautifulSoup(data)

#To search for all links-we extract <a> tags
all_links=scraped.find_all('a')

#To get just the links
for i in all_links:	
	link=i.get("href").split('//')[-1].split('/')[0]
	if len(link)!=0 :
		print link




    

