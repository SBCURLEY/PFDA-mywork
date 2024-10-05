# Program to convert a string and read in an integer Lab 1.4 a & b
# This code reads a CSV file and calculates the average of values in the second column, skipping the header row. 
# Author: Sharon Curley

import csv

FILENAME = "data.csv"
DATADIR = "../datafiles/"

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader (fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)       # csv reader returns a list of lists in an enumerator
                                                                                # read from file name,assuming variables seperated by a comma,assuming quotes on non numeric
                                                                                # quoting=csv.QUOTE_ALL  makes everything a string 
    linecount = 0                                                               # ti 
    total = 0
    for line in reader:                                                         # read one line at a time
        if not linecount:                                                       # if linecount is zero, that is false. If True this is the first row.
            pass
            #print(f"{line}\n-------------------")
        else:                                                                   # ll subsequent rows
            total += line[1]                                # why 1             # This line refers to the second column in each row.
        linecount += 1
        
    print (f"average is {total/(linecount-1)}")             # why -1            # The total is divided by linecount - 1 to calculate the correct average 
                                                                                # using only the actual data rows, not the header row.