#!/usr/bin/python3

#This script will fetch altcoin data from the web and display in the terminal


# the url to fetch is 
# https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR,GBP

import urllib.request as web # for requesting data from url
# the url to fetch is 
# https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR,GBP

import urllib.request as web # for requesting data from url
from datetime import datetime
urlBTC = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD"
urlADA = "https://min-api.cryptocompare.com/data/price?fsym=ADA&tsyms=USD"
readableBTC = web.urlopen(urlBTC) # open the url
readableADA = web.urlopen(urlADA)
dataBTC = readableBTC.read().decode('utf-8') # request data and decode it as utf-8
dataADA = readableADA.read().decode('utf-8')
database = open('/Users/huazhao/altcoins/altcoinsData.txt','a')
database.write('\n'+str(datetime.now())+','+str(dataBTC)+','+str(dataADA))
