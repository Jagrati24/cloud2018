#!/usr/bin/python2

print "Press 1 for word search"

import webbrowser 
 
ch= raw_input()

if ch == "1":
	string=raw_input("Enter the string to be searched:")
	string=string.strip()
	search=string.split()
	for i in search:
           webbrowser.open("https://www.google.com/search?q="+i)
 
else:
	print "Something went wrong"
