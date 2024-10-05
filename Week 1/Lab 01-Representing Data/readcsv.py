# Program to read csv file Lab 1.2
# Author Sharon Curley

import csv

FILENAME = "data.csv"
DATADIR  = "../datafiles/"

with open (DATADIR + FILENAME, "rt") as fp:    # open the file as read mode text 
    reader = csv.reader(fp, delimiter=",")     #pass in file pointer & set delmiter will be a comma
    for line in reader:
        print (line)
