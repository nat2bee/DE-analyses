# DE-analyses

Scripts to help in differential expression analyses.

- # Corset_cluster2transcript.py
  Is to be used after running the **Corset** programa (N. M. Davidson and A. Oshlack. Corset: enabling differential gene expression analysis for de novo assembled transcriptomes. Genome Biology 2014, 15:410  doi:10.1186/s13059-014-0410-6). 

  The resulting count matrix in **Corset** are given with the clusters IDs and it might be necessary to recover the transcripts ID (the same usually in the fasta file) after running the DE analyses. This script uses a list of differentially expressed Cluster IDs (one per line) and the ***-clusters.txt*** (output from **Corset**) as inputs and otputs a table (tab delimited) with the DE transcript ID and its cluster.
  
  **Usage:**
  Corset_cluster2transcript.py -c *input1* -r *input2* -o *outputfile*

  **Where:**
- input1 = List of Cluster IDs (one per line)
- input2 = Result table from Corset containing the clusters and transcripts IDs (*-clusters.txt*)
- outputfile = Table with the cluster ID in your Input1 file and the transcript id present in this cluster
 
  **Opitions:**
- h = usage info
  
  
- # Compare_DE.py
  It compares two matrix containing differenttialy expressed data to find similarities between  them. 

  If you run differentially expression analyses in two different programs and want to compare the results this script can be usefull. It takes as input the two files you want to compare and outputs the common and diffferent (optional) transcripts of the input1 in input2.
  
    **Usage:**
  Usage: compare_DE.py -1 *input1* -2 *input2* -o *outprefix* 

  **Where:**
- input1 = File with the transcripts you want to find in the input2 (one per line). It can be another matrix count file or only a list of transcripts ids
- input2 = Matrix file with counts of each transcripts to be compared with input 1
- outprefix = Prefix for the output file(s)

  **Opitions:**
- d = Print an output of counts for the transcripts that are different in both inputs (***-diff.txt***)
- h = usage info


- # ClustersSeq_Corset.py
  Is to be used after running the **Corset** programa (N. M. Davidson and A. Oshlack. Corset: enabling differential gene expression analysis for de novo assembled transcriptomes. Genome Biology 2014, 15:410  doi:10.1186/s13059-014-0410-6). 

  This program is used to recover the nucleotide sequence of the longest transcript in each **Corset** cluster. This script uses as input the fasta file of all the transcripts, a list of  Cluster IDs (one per line) and the ***-clusters.txt*** (output from **Corset**) and otputs a fasta file with the longest transcripts IDs and its nucleotide sequences.

  
  **Usage:**
  ClustersSeq_Corset.py -f *fasta* -l *input1* -c *input2* -o *output*

  **Where:**
- fasta = the fasta file containing all the transcripts used as reference for the realigment of the reads before running the Corset
- input1 = List of Cluster IDs to recover (one per line)
- input2 = Result table from Corset containing the clusters and transcripts IDs (***-clusters.txt)
- outputfile = File in fasta format where the output will be saved i.e. The largest transcript of each Cluster and its nucleotide sequence
 
  **Opitions:**
- h = usage info 


- # Up_Annotation.py
 
Take a list of transcripts names and print their annotation information.

Developed (in my case) to use with a list of deferentially expressed transcripts to find 
the information from an annotation in the **Annocript** program results (Musacchia et al. Annocript: a flexible pipeline for the annotation of transcriptomes able to identify putative long noncoding RNAs. Bioinformatics 2015, 31(13):2199-201. doi: 10.1093/bioinformatics/btv106). 

**Usage:**
Up_Annotation.py -i *list* -a *annotation* -o *output*

**Where:** 
- list = list with all the transcripts Ids to find in the table (one per line)
- output = the name of the output to save the table with the information of the transcripts of interest
- annotation = table result from **Annocript** containing the information from annotation (*...filt_ann_out.txt*)

**Options:**
-h for usage help


- # Up_Annotation2.py

The same as **Up_Annotation.py** but to work with tables after R edition (include cluster info).

**Usage:**
Up_Annotation2.py -i *list* -a *annotation* -o *output*

**Where:** 
- list = list with all the transcripts Ids to find in the table (one per line)
- output = the name of the output to save the table with the information of the transcripts of interest
- annotation = table result from **Annocript** containing the information from annotation (*...filt_ann_out.txt*)

**Options:**
-h for usage help

