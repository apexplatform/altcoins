#!/bin/sh

date >> /tmp/MyLaunchdTest.out

#python3 /Users/huazhao/altcoins/collectaltcoinData.py

date=$(date);
btcdata=$(curl "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD");
adadata=$(curl "https://min-api.cryptocompare.com/data/price?fsym=ADA&tsyms=USD");

echo "{date:\"$date\",BTC:$btcdata}" >> /Users/huazhao/altcoins/altcoinsData.txt
echo "{date:\"$date\",ADA:$adadata}" >> /Users/huazhao/altcoins/altcoinsData.txt

