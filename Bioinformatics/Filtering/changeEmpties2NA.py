#!/usr/bin/python

import argparse, csv

def readAfile(filenameString):
    'Reads the input file into a dictionary object where the key is the first row'
    fileA = open(filenameString, 'U')
    inputA = csv.reader(fileA, delimiter='\t')
    data = []
    for row in inputA:
        data.append(row)
    fileA.close()
    return data

def writeAfile(fileName, data2Bwritten):
    w = open(fileName, 'w')        
    writer = csv.writer(w ,delimiter="\t")
    for row in data2Bwritten:
        writer.writerow(row)
    w.close()


def fixVariables(inputFile, find, replace):
    'Read in a list of lists and if there is a match with find the replace it with replace!'
    result = []
    for entry in inputFile:
        [replace if i==find else i for i in entry]
        result.append(entry)
    return result

def main():
    parser = argparse.ArgumentParser(description="Reads an input file and changes whatever matches the second argument to NA for use in R")
    parser.add_argument('-i', '--inputData', required=True, help='The file containing elements you want to change')
    parser.add_argument('-v', '--valueToChange', required=True, help='The value you want to change. For example null or 0')
    parser.add_argument('-r', '--valueToReplace', required=True, help='The value you want to replace it with. For example NA')
    parser.add_argument('-o', '--outputData', required=False, help='The file you get at the end')
    args = parser.parse_args()

    # The variables
    rawData = readAfile(args.inputData)
    val2Change = args.valueToChange
    val2Replace = args.valueToReplace
    fileOut = args.outputData

    # Use the variables
    outcome = fixVariables(rawData, val2Change, val2Replace)
    writeAfile(fileOut, outcome)

if __name__ == '__main__':
    main()