#!/usr/bin/python2.7

#############################################################################################
#Change the filtered maf file generated by R and output as a snp call type file
#############################################################################################

import sys
import os
import csv

def average(value1, value2):
    addtion = value1 + value2
    result = addtion/2
    return result

#set up script
os.chdir('/Users/d.brown6/Documents/FredCSC/reformattedFiles/preranked')
inFile = sys.argv[1]
data = []

#read in the files
f = open(inFile, 'U')
files = csv.reader(f, delimiter='\t')
for row in files:
    data.append(row)
    
#get the header row then remove it from data
dataHeader = data[0][:]
data = data[1:]

newDict = {}
for line in data:
    #fix empty values and NAs with a try except clause
    try: 
        line[1] = float(line[1])
    except ValueError:
            pass
    #if the gene already exists in the dictionary average the values
    if line[0] in newDict:
        dupGene = line[0]
        newDict[dupGene] = average(newDict[dupGene], line[1])
        #print "duplicate " + dupGene + ' new value ' + str(newDict[dupGene])
    #Append new genes to the dictionary
    else:
        newDict[line[0]] = line[1]

#get rid of the empty key        
del newDict['']
del newDict['NA']
        
print '#ignoreThis'+'\t'+' '        
for entry in newDict:
    print entry+'\t'+str(newDict[entry])


 
    