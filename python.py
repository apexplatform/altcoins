#!/usr/bin/python3

#This script will fetch altcoin data from the web and display in the terminal
<<<<<<< HEAD

# the url to fetch is 
# https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR,GBP

import urllib.request as web # for requesting data from url

url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR,GBP"
readable = web.urlopen(url) # open the url
data = readable.read().decode('utf-8') # request data and decode it as utf-8
print(len(data)) # print the length of the data
print("BTC price is: ")
print(data) # print the data 
=======
>>>>>>> changeshua

# the url to fetch is 
# https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR,GBP

import urllib.request as web # for requesting data from url

urlBTC = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR,GBP"
urlADA = "https://min-api.cryptocompare.com/data/price?fsym=ADA&tsyms=USD,JPY,EUR,$"
readableBTC = web.urlopen(urlBTC) # open the url
readableADA = web.urlopen(urlADA)
dataBTC = readableBTC.read().decode('utf-8') # request data and decode it as utf-8
dataADA = readableADA.read().decode('utf-8')
#print(len(data)) # print the length of the datA
print("Today's BTC price is: ")
print(dataBTC) # print the data 
print("Today's ADA price is:")
print (dataADA)
