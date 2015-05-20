####################################################################################### 
#
# Get the nucleotide sequence of the largest transcript in each Corset cluster
#
# Usage: ClustersSeq_Corset.py -f <fasta> -l <input1> -c <input2> -o <output>
#
# Where:
#
# fasta = the fasta file containing all the transcripts used as reference for the realigment 
#         of the reads before running the Corset
# input1 = List of Cluster IDs to recover (one per line)
# input2 = Result table from Corset containing the clusters and transcripts IDs (***-clusters.txt)
# outputfile = File in fasta format where the output will be saved i.e. The largest transcript 
#              of each Cluster and its nucleotide sequence
# 
#######################################################################################

#!/usr/bin/python

import sys, getopt
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord


genes_size = dict()
genes_seq = dict()
cluster_dic = dict()

clusters = list()
Ids = list()

fasta = ""
input1 = ""
input2 = ""
outputfile = ""

# Check for the arguments and print useful help messages

try:
    opts, args = getopt.getopt(sys.argv[1:],"hf:l:c:o:",["fasta=","ifile1=","ifile2=","output="])
except getopt.GetoptError:
    print '\n', '####     Invalid use     ####', '\n'
    print 'Usage: ClustersSeq_Corset.py -f <fasta> -l <input1> -c <input2> -o <output>'
    print 'For help use ClustersSeq_Corset.py -h'
    sys.exit(99)
    
if len(args) != 1:
        print '\n', '###    Arguments are missing   ###', '\n', '\n' 'Use -h option for help'
        sys.exit(1)

for opt, arg in opts:
    if opt == '-h':
        print '\n', 'Get the nucleotide sequence of the largest transcript in each Corset cluster', '\n'
        print 'Usage: ClustersSeq_Corset.py -f <fasta> -l <input1> -c <input2> -o <output>', '\n'
        print 'Where: fasta = the fasta file containing all the transcripts used as reference for the realigment of the reads before running the Corset'
        print 'input1 = List of Cluster IDs to recover (one per line)'
        print 'input2 = Result table from Corset containing the clusters and transcripts IDs (***-clusters.txt)'
        print 'outputfile = File in fasta format where the output will be saved i.e. The largest transcript of each Cluster and its nucleotide sequence'
        sys.exit()
    elif opt in ("-f", "--fasta"):
        fasta = open(arg)
    elif opt in ("-l", "--ifile1"):
        input1 = open(arg)
    elif opt in ("-c", "--ifile2"):
        input2 = open(arg)
    elif opt in ("-o", "--output"):
        outname = arg + ".fasta"
        outputfile = open(outname,"w")
    else:
        assert False, "unhandled option"


## Make a list of the cluster IDs    
for id in input1:
    clusters.append(id)

## Open the fasta file and save the information to be used later
for seq_record in SeqIO.parse(fasta, "fasta"):
    gene_id = seq_record.id
    seq_length = (len(seq_record))
    bases = (seq_record.seq)
    genes_size[gene_id]= seq_length
    genes_seq[gene_id]= bases

## Find the transcript ID foreach clusterID in the list and check which transcripts are larger within the same cluster
for line in input2:
    table_line = line.split("\t")
    trans_ID = table_line[0]
    cluster_ID = table_line[1]
    if cluster_ID in clusters and cluster_ID not in cluster_dic:
        cluster_dic[cluster_ID] = trans_ID
    elif cluster_ID in cluster_dic:
        old_trans = cluster_dic[cluster_ID]
        new_trans = trans_ID
        if genes_size[new_trans] > genes_size[old_trans]:
            cluster_dic[cluster_ID] = trans_ID
             

## Save the Ids of the longest transcripts in a list
for k,v in cluster_dic.items():
    Ids.append(v)
 
## Recover the nucleotide sequence of the longest transcripts and save it in the output fasta file    
for k,v in genes_seq.items():
    if k in Ids:
        fasta_format_string = SeqRecord(v, id=k)
        outputfile.write(fasta_format_string.format("fasta"))



outputfile.close() 
