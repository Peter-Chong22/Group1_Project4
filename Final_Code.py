'''
Group 1 Project 3
This program will attain a specific HTTP log file from a server on the internet.
The program will then check that the log file is where it needs to be.
Using this log file, it will be parsed to show the total number of logs in the past 6 months, as well as all time logs.

'''
#necessary modules for program to run correctly
from itertools import count
import pip._vendor.requests 
import os 
from os.path import exists 
from datetime import datetime
import re

cwd = os.getcwd() # obtain file path 
cwd += '\http_access_log.txt' # Make sure file path is appended to reflect where the HTTP log is stored

file_exists = exists(cwd) # check if file exists


if file_exists == False: # conditional statement so the program will be able to determine if it needs to fetch the file or not. 

    url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
    r = pip._vendor.requests.get(url, allow_redirects = True) # create object to pass web file into

    f = open('http_access_log.txt', 'wb')
    for chunk in r.iter_content(chunk_size = 8192):
        if chunk:
            f.write(chunk)
    f.close() # Creates the file, writes the data from the object to it, then closes and saves itself.

# Get a count of how many total requests are in the entire log
file = open('http_access_log.txt') 
data = file.read()
requests = data.count("GET")
#prints the first output of the program, the total requests from the log
print ('TOTAL REQUESTS IN LOG :', requests)


# Split file into a list of lines
with open('http_access_log.txt', 'r') as sixmon:
    lines = sixmon.readlines()

with open('six_months_access_log.txt', 'w') as sixmon2:
    for number, line in enumerate(lines):
        if number not in range(0, 166364):
            sixmon2.write(line)
# Write last six months to the file only using the known range generated from parsing earlier

file = open('six_months_access_log.txt') 
data = file.read()
lastsixrequests = data.count("GET")
#prints the final output of the program, the number of requests from the last six months, according to the log (11 OCT 1995)
print ('TOTAL NUMBER OF REQUESTS OVER LAST SIX MONTHS FROM 11 OCT 1995 :', lastsixrequests)

#import collections
import collections
logfile =  open("http_access_log.txt", "r")
clean_log=[]
clean_log.append(line[line.index("GET")+4:line.index("HTTP")])
#print most requested file
counter = collections.Counter(clean_log)
print(str(count[1]) + "\t" + str(count[0]))
