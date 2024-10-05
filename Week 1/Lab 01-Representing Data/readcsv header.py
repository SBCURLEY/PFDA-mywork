# Program to create a header in a csv file  Lab 1.3
# Author: Sharon Curley

import csv

FILENAME = "data.csv"
DATADIR = "../datafiles/"

with open (DATADIR + FILENAME, "rt") as fp:          # opening a file with file/path and mode as a variable
    reader = csv.reader (fp, delimiter=",")
    linecount = 0
    for line in reader:                             # go through the lines one by one
        if not linecount:    # first row is header row
            print(f"{line}\n-------------------")
        else:  #all subsequent rows
            print (line)
        linecount += 1
