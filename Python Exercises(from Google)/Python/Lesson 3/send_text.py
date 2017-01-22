# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 16:47:17 2016

@author: HenryYu
"""
import os 

import urllib
# now as read text 

def read_text():
    quotes = open("/Users/HenryYu/Google Drive/Data Analyst Nanocourse/Python/Lesson 3/movie_quotes.txt", "r")
    content = quotes.read()
    print(content)
    quotes.close()
    check_profanity(content)

def check_profanity(text):
    connect = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text)
    output = connect.read()
    # print(output)
    connect.close()
    if "true" in output:
        print("Profanity Alert!")
    elif "false" in output:
        print("No profanity detected!")
    else:
        print("Error Occured")
        
    
    
os.chdir("/Users/HenryYu/Google Drive/Data Analyst Nanocourse/Python")

read_text()



