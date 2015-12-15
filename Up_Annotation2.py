#!/usr/local/bin/python


"""
The same as Up_Annotation.py but to work with tables after R edition (include cluster info)

Usage = Up_Annotation2.py -i <list> -a <annotation> -o <output>

Where: 
list = list with all the transcripts Ids to find in the table (one per line)
output = the name of the output to save the table with the information of the transcripts of interest
annotation = table result from Annocript containing the information from annotation (...filt_ann_out.txt)

Options: -h for usage help
"""

import sys, getopt

# Check for the arguments, open the inputs and print useful help messages

try:
    opts, args = getopt.getopt(sys.argv[1:],"hi:a:o:",["list=","annotation","output="])
except getopt.GetoptError:
    print '\n', '####     Invalid use     ####', '\n'
    print 'Usage = Up_Annotation2.py -i <list> -a <annotation> -o <output>'
    print 'For help use Up_Annotation2.py -h'
    sys.exit(99)
    
for opt, arg in opts:
    if len(arg) < 3 and opt == '-h':
        print '\n', 'Take a list of transcripts names and print their annotation information.', '\n'
        print 'Usage = Up_Annotation2.py -i <list> -a <annotation> -o <output>'
        print 'Where: list = list with all the transcripts Ids to find in the table (one per line)'
        print 'output =  the name of the output to save the table with the information of the transcripts of interest'
        print 'annotation = table result from Annocript containing the information from annotation (...filt_ann_out.txt)'
        sys.exit()
    elif len(arg) > 3:
        if opt in ("-i", "--list"):
            list = open(arg)
        if opt in ("-a", "--annotation"):
            annotation = open(arg)
        if opt in ("-o", "--output"):
            output = open(arg,"w")
    elif len(arg) < 3:
        print '\n', '###    Arguments are missing   ###', '\n', '\n' 'Use -h option for help\n'
        sys.exit(1)
    else:
        assert False, "unhandled option"


transcripts = []
teste = []
n = 0

# Open the list of transcripts IDs and save them in a list

for ids in list:
    transcript = ids.split("\n")
    transcript = str(transcript[0])
    transcripts.append(transcript)



# Check if the transcript of interest is in the line of the annotation table and if so save it in the output

for line in annotation:
    elements = line.split("\t")
    transcript_id = elements[1]
    transcript_id = transcript_id.split('"')
    transcript_id = str(transcript_id[1])
    if n == 0:
        output.write(line)
        n = n + 1
    if transcript_id in transcripts:
        output.write(line)

   

output.close()
