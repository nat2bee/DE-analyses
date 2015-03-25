####################################################################################### 
#
# Comparing two DE matrix to search for shared transcripts on them
#
# Usage: compare_DE.py -1 <input1> -2 <input2> -o <outprefix> 
#
# Where:
# input1 = File with the transcripts you want to find in the input2. It can be another matrix
#          count file or only a list of transcripts ids
# input2 = Matrix file with counts of each transcripts to be compared with input 1
# outprefix = Output of counts for the transcripts that are common to both inputs
#
# Options:
# -d = Print an output of counts for the transcripts that are different in both inputs (***-diff.txt)
# 
#######################################################################################

#!/usr/bin/python

import sys, getopt

transcripts = list()
input1 = ''
input2 = ''
outputfile = ''
outputfile2 = ''
n = 0

try:
    opts, args = getopt.getopt(sys.argv[1:],"h1:2:o:d",["ifile1=","ifile2=","outprefix=","diff="])
except getopt.GetoptError:
    print 'compare_DE.py -1 <input1> -2 <input2> -o <outprefix> -d'
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print 'compare_DE.py -1 <input1> -2 <input2> -o <outprefix> -d'
        sys.exit()
    elif opt in ("-1", "--ifile1"):
        input1 = open(arg)
    elif opt in ("-2", "--ifile2"):
        input2 = open(arg)
    elif opt in ("-o", "--outprefix"):
        outname = arg + "-common.txt"
        outputfile = open(outname,"w")
    elif opt in ("-d", "--diff"):
        for o, a in opts:
            if o in ("-o", "--outprefix"):
                outname2 = a + "-diff.txt"
                outputfile2 = open(outname2,"w")


## Make a list of the IDs of transcripts   
for id in input1:
    table_line = id.split("\t")
    trans_ID = table_line[0]
    transcripts.append(trans_ID)

## Find the transcript in the count table and print it
for line in input2:
    if n == 0:
        outputfile.write(line)
        n = n + 1
    else:
        table_line = line.split("\t")
        trans_ID2 = table_line[0]
        if trans_ID2 in transcripts:
            outputfile.write(line)
        elif opt in ("-d", "--diff"):
            outputfile2.write(line)
            
outputfile.close()
if opt in ("-d", "--diff"):  
    outputfile2.close()  
