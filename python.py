#!/usr/bin/python3

#This script will fetch altcoin data from the web and display in the terminal

# the url to fetch is 
# https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR,GBP

import urllib.request as web # for requesting data from url

url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR,GBP"
readable = web.urlopen(url) # open the url
data = readable.read().decode('utf-8') # request data and decode it as utf-8
print(len(data)) # print the length of the data
print("BTC price is: ")
print(data) # print the data 

