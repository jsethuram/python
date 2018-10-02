# Coded by Jaisimha Sethuram

import json
import urllib.request
import time
import re
    
#creating a new empty list
newList = []
#request a web URL, get json data and store in list
earthQuakeWebUrlList = json.load(urllib.request.urlopen("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"))
#calculate length of the list
totalNumberOfQuakes = len(earthQuakeWebUrlList['features'])
print ("Total number of earthquakes: ",totalNumberOfQuakes)
# initialize i to 0, to be used later in for loop
i = 0
#for i in range 0 to total number of quakes minus 1 of 
for i in range(0,totalNumberOfQuakes):
    #get necessary json object entries for feature i property value i, title value for it and store that for variable entry
    entry = earthQuakeWebUrlList['features'][i]['properties']['title']
    #split the entry at comma to get state
    entryStateSplit = entry.split(",")
    #get the last part of the split which is state for every entry
    state = entryStateSplit[-1]
    #check if state value is either california or CA, as both are same state
    if ('California' in state) or ('CA' in state):
        #Now conver time into milliseconds or epoch time feature i property value i, time value
        timeInEpoch = earthQuakeWebUrlList['features'][i]['properties']['time']
        #append the value to a new list created earlier
        newList.append(str(timeInEpoch) + " - " + entry)       
#sort the list items
newList.sort()
#initialize j to 0 to be used in for loop next
j = 0
#for every element of new list
for j in newList:
    #split entry at - 
    listSplit = j.split("-")
    #select first part as epoch time
    justEpochTime = listSplit[0]
    #convert epoch or time in milliseconds time to normal time, by diving epoch time by 1000
    earthQuakeDate = time.strftime('%Y-%m-%dT%H:%M:%S+00:00', time.localtime(float(justEpochTime)/1000))
    #get region part
    region = listSplit[2]
    # get magnitude part
    magnitude = listSplit[1]
    #regular expression to match charected of M
    magnitude = re.sub('[M]', 'Magnitude:', magnitude)
    #display in the required format
    print (earthQuakeDate + " | " + region + " | " + magnitude)
