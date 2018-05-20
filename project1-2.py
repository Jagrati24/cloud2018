#!/usr/bin/python2

import webbrowser

search=raw_input("Enter data to be searched")
search=search.strip()
word=search.split()

for i in word:
	webbrowser.open_new_tab("https://www.google.com/images?q="+i)
