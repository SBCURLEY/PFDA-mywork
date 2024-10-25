# This is code anonymise the sub domains of ip addresses 
# Author: Sharon Curley

import re

#regex = "\d{1,3}\.\d{1,3} " # this will find other numbers apart from ips
regex =  r"(\d{1,3}\.\d{1,3}\.)\d{1,3}\.\d{1,3}"  # we make a group at the beginning to keep
replacementText=r"\1XXX.XXX " # note the space at the end to match above
filename ="./sample-files/smallerAccess.log"
outputFileName = "anonymisedIPs.txt"

with open(filename) as inputFile:
    with open(outputFileName, 'w') as outputFile:
        for line in inputFile:
            # for debugging
            #foundText = re.search(regex, line).group()
            #print(foundText)
            newLine = re.sub(regex, replacementText, line)
            outputFile.write(newLine)

# It reads a log file line by line, replaces the last two segments of any IP addresses with "XXX.XXX" for anonymization, 
# and writes the modified lines to a new file. However, if there are lines that do not match the pattern, using re.search().group() 
# as it is may raise an error. 

