# Program to read in as a Dictionary object Lab 1.5
# Reads the CSV file into a dictionary where each column is accessed by its header name (e.g., "age").
# Author Sharon Curley

import csv

FILENAME = "data.csv"
DATADIR = "../datafiles/"

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.DictReader (fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)   # if things are not quoted, they are numbers
    total = 0
    count = 0
    for line in reader:
        total += line["age"]   
        count += 1
        
    print (f"average is {total/(count)}")  # why is there no -1
    # with csv.DictReader, the header row is automatically processed by the DictReader, and it doesn't count as part of the data rows.
    # The count variable tracks only the actual data rows.
    # Since the header is already excluded, there's no need to subtract 1 from count—it's already correct. 
    # You can safely divide the total by count to calculate the average of the "age" field.CLS
    