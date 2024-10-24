# this is code for for the quiz
import re

regex = "^Hello [A-Z]"
filename = "./sample-files/quiz.txt"

with open(filename) as quizFile:
    for line in quizFile:
        searchResult = re.search(regex, line)
        if (searchResult):
            matchingLine = line
            # I set the end to blank because each line will already have a \n
            print (matchingLine, end="")
            
            

# a. hello      Line 1
# b. Hello      Line 2  3  5
# c. ^Hello     Line 2  3
# d. ^Hell*o    Line 2  3  6   On the quiz, for d. Why is 4 included in the answer? 'Helo John'
# e. ^Hell+o    Line 2  3  6
# f. ^Hell?o    
# g. ^hello [A-Z] 
# h. ^Hello [A-Z]
# i. =
# j. #
# k. [
# l. ^$
