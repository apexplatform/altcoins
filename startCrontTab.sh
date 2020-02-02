#!/bin/sh

# note that on macosx the following command loads that file into the launch list
# meaning it will automatically be run periodically
# also note that the file actually periodically calls a shellscript file in users bin folder 
# and the shellscript file runs a python script which does the webscrape of data and appends 
# into a text file 

launchctl load /Users/huazhao/Library/LaunchAgents/com.haumartin.altcoin.plist
