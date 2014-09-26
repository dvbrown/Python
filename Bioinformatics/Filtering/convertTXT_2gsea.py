#!/usr/bin/python2.7

import aUsefulFunctionsFiltering
import argparse

def convertGEMtoGCT(data):
    '''Takes as input a gene expression matrix with samples as columns and genes as rows
    and adds the first 2 lines that GSEA requires for parsing
    '''
    # Measure the number of samples and genes
    header = data[0]
    gctFile = data[:]
    probeNumber = str(len(data))
    sampleNumber = str(len(header))
    # Copy the data so that entries can be pushed
    # Insert NA into the description
    for line in gctFile:
        line.insert(1, 'NA')
        
    gctFile[0] = '#1.2'
    gctFile[1] = probeNumber + '\t' + sampleNumber
    return gctFile

def convertLabelstoCLS(data):
    '''Takes as input the list of phenotypes which will be a column vector generated by R
    Returns a file that can be parsed by GSEA to generate phenotype labels
    '''
    return None

def main():
    parser = argparse.ArgumentParser(description="""Reads an input file that is either a gene expression matrix or a list of 
    phenotype labels and returns a file suitable for analysis with GSEA""")
    parser.add_argument('-i', '--inputData', required=True, help='The file containing the data to be converted')
    parser.add_argument('-o', '--outputData', required=False, help='The file you get at the end')
    parser.add_argument('-t', '--typeOfFile', required=True, help='Either gem for gene expression matrix or phenotype for phenotype list')
    args = parser.parse_args()
    
    
    data = aUsefulFunctionsFiltering.readAfile(args.inputData)
    

    # The switch that calls either of the helper functions
    if args.typeOfFile == 'gem':
        result = convertGEMtoGCT(data)
    elif args.typeOfFile == 'phenotype':
        result = convertLabelstoCLS(data)
    else:
        print 'You have specified the wrong type of argument to type of file'

    for entry in result:
        print entry    
    
if __name__ == '__main__':
    main()