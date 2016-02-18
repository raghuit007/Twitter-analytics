# Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import csv
import json
import re

# added importing PDB to help debug
import pdb

#Variables that contains the user credentials to access Twitter API
access_token = "141867598-d6haSz20y5ZOLRXng1NBZpPCLsU6i0Hn4Iol3hC3"
access_token_secret = "0fKZeqNHyU2FazH4sthIeZlCSSj4y2aOtEQJvEmtsbHpu"
consumer_key = "m9Pe1MYO7pgZ0jUsZsdqWpGw1"
consumer_secret = "UlL77f4Vsh0Y61cZljg3RTarHwyj9PXfArmsw2Jx7Ux2GkIMxL"

# Lists of keywords, company names & tickers, twitter handles credible sources
search_keywords = []
company_list = []
source_twtr = []

# read the company list from a text file. Each company on a seperate line
# store the company names in a list of strings
company_file = open("company_names.txt", "r")
line1 = company_file.readline()
# Strip out the new line character at the end.
line1 = line1[:-1]
while line1 != "":
        company_list.append(line1)
        line1 = company_file.readline()
        line1 = line1[:-1]

company_file.close()


# Code Below reads the keywords file and stores in a list of keyword strings.
# This keyword list is passed to tweepy
keywords_file = open("twtr_keywords.txt", "r")
line1 = keywords_file.readline()
# Strip out the new line character at the end.
#line1 = line1[:-1]
while line1 != "":
        search_keywords.append(line1)
        line1 = keywords_file.readline()
#        line1 = line1[:-1]

keywords_file.close()

print search_keywords


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        output_file = open('raw_output.txt','a')
        d= json.loads(data)
        for x in company_list:
            if re.search(r"\b" + re.escape(x) + r"\b", d['text']):
                print "------------->", x, "<------------"
                print d['text']
                #output_file.write(data)

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=search_keywords)






# xxxxxxxxxxxxxx---------- UNUSED CODE ----------xxxxxxxxxxxxxxxxxx

# Raghu - I commented out your code reading from a CSV file.
"""
a = []

# read the company list from CSV file
with open('companylist.csv') as f:
    reader = csv.reader(f, delimiter=",")
    for i in reader:
        a.append(i[0])     

print a
"""

"""
# Just some test code to see how many keywords to copy to the keyword array "a"
i=0
while i < 10:
    a.append(company_list[i])
    i+=1

print "# of SEARCH KEYWORDS:", i, a
"""

