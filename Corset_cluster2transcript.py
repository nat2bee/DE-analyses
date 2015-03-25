####################################################################################### 
#
# Recovering transcripts ID based on the Clusters ID present in the Corset counts output
#
# Usage: Corset_cluster2transcript.py -c <input1> -r <input2> -o <outputfile>
#
# Where:
# input1 = List of Cluster IDs (one per line)
# input2 = Result table from Corset containing the clusters and transcripts IDs (***-clusters.txt)
# outputfile = Table with the cluster ID in your Input1 file and the transcript id present in this
# cluster
# 
#######################################################################################

#!/usr/bin/python

import sys, getopt


clusters = list()
input1 = ""
input2 = ""
outputfile = ""


try:
    opts, args = getopt.getopt(sys.argv[1:],"hc:r:o:",["ifile1=","ifile2=","ofile="])
except getopt.GetoptError:
    print 'Corset_cluster2transcript.py -c <input1> -r <input2> -o <outputfile>'
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print 'Corset_cluster2transcript.py -c <input1> -r <input2> -o <outputfile>'
        sys.exit()
    elif opt in ("-c", "--ifile1"):
        input1 = open(arg)
    elif opt in ("-r", "--ifile2"):
        input2 = open(arg)
    elif opt in ("-o", "--ofile"):
        outputfile = open(arg,"w")



## Make a list of the cluster IDs    
for id in input1:
    clusters.append(id)


## Find the transcript ID foreach clusterID in the list
for line in input2:
    table_line = line.split("\t")
    trans_ID = table_line[0]
    cluster_ID = table_line[1]
    if cluster_ID in clusters:
        outputfile.write(trans_ID)
        outputfile.write("\t") 
        outputfile.write(cluster_ID)
    

outputfile.close()  
