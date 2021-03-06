#!/usr/bin/python2.7
#A script to parse 96 well files and transpose to column vector

import argparse, string, itertools, csv
import aUsefulFunctionsFiltering
from locale import str


def main():
    parser = argparse.ArgumentParser(description="""Reads an input file that is a 96 well plate and transposes it
        to yield the column letter.""")
    parser.add_argument('-i', '--inputData', required=True, help='''The file containing elements you want to change.
        The input file should just contain data and no column/ row headers etc''')
    parser.add_argument('-o', '--outputData', required=False, help='The file you get at the end')
    args = parser.parse_args()

    plateMap = aUsefulFunctionsFiltering.readAfile(args.inputData)
    # Remove the header of the file
    #plateMap = plateMap[1:]

    # Flatten the list of lists data structure using itertools
    plateMap2 = list(itertools.chain.from_iterable(plateMap))

    # Write in the well names
    letters = list(string.ascii_uppercase)
    letters = letters[0:8]
    number = range(1, 13)

    wells = []
    for letter in letters:
        for num in number:
            x = letter + str(num)
            wells.append(x)

    # Write out to file if one is provided on cammand line
    if args.outputData == True:
        w = open(args.outputData, 'w')
        writer = csv.writer(w ,delimiter="\t")
        ###################################### Fix the iteration of this
        writer.writerow(zip(wells, plateMap2))
    ######################################


    for well, gene in zip(wells, plateMap2):
        #writer.writerow(well + '\t' + gene)
        print well + '\t' + gene

if __name__ == '__main__':
    main()