# -*- coding: utf-8 -*-
"""
Created on Wed May 15 22:09:40 2019

@author: Nitanshu
"""

# import nlkt
# nltk.download('punkt')
import glob
import re
from textblob import TextBlob
from collections import Counter


#replace with personal merged file
tfc2 = open("tfc2.txt", "w+")
#replace with location of webscrapped files
tfc_files2 = glob.glob('D:/Stevens/595/Assignments/Task-4/*.txt')
with tfc2 as outfile:
    for filename in tfc_files2:
        with open(filename) as infile:
            for line in infile:
                line = str(line)
                #gets rid of extra spaces
                line = line.strip()
                #edits all female sentences
                if "She's" in line:
                    x = re.split("She", line)
                    #checks for strings with multiple sentences
                    if len(x) >= 3:
                        line = ""
                        for sentence in x:
                            #only adds lines with actual sentences and not just empty brackets
                            if len(sentence) > 10:
                                if "She's" not in sentence:
                                    sentence = "She" + sentence
                                #converts first letter to uppercase
                                if sentence[0].islower():
                                    if "she's" in sentence:
                                        sentence = "S" + sentence[1:]
                                #clears random characters at the end of sentences and adds periods if necessary
                                while not re.search(r'(\w|[.])$', sentence):
                                    sentence = sentence[:-1]
                                    sentence = sentence.strip()
                                if re.search(r'\w$', sentence):
                                    sentence += "."
                                if re.search(r'They fight crime!', sentence):
                                    x = re.split("They", sentence)
                                    sentence = x[0]
                                    sentence = sentence.strip()
                                while re.search(r'^\W', sentence):
                                    sentence = sentence[1:]
                                    sentence = sentence.strip()
                                line += sentence + '\n'
                    else:
                        #converts first letter to uppercase
                        if line[0].islower():
                            if "she's" in line:
                                line = "S" + line[1:]
                        #clears random characters at the end of sentences and adds periods if necessary
                        if re.search(r'\w$', line):
                            line += "."
                        if re.search(r'They fight crime!', line):
                            x = re.split("They", line)
                            line = x[0]
                            line = line.strip()
                        if re.search(r'^\W', line):
                            line = line[1:]
                            line = line.strip()
                #does the same process for male sentences
                elif "He's" in line:
                    x = re.split("He", line)
                    if len(x) >= 3:
                        line = ""
                        for sentence in x:
                            if len(sentence) > 10:
                                if "He's" not in sentence:
                                    sentence = "He" + sentence
                                if sentence[0].islower():
                                    if "he's" in sentence:
                                        sentence = "H" + sentence[1:]
                                while not re.search(r'(\w|[.])$', sentence):
                                    sentence = sentence[:-1]
                                    sentence = sentence.strip()
                                if re.search(r'\w$', sentence):
                                    sentence += "."
                                while re.search(r'^\W', sentence):
                                    sentence = sentence[1:]
                                    sentence = sentence.strip()
                                line += sentence + '\n'
                    else:
                        if line[0].islower():
                            if "she's" in line:
                                line = "S" + line[1:]
                        if re.search(r'\w$', line):
                            line += "."
                        if re.search(r'They fight crime!', line):
                            x = re.split("They", line)
                            line = x[0]
                            line = line.strip()
                        if re.search(r'^\W', line):
                            line = line[1:]
                            line = line.strip()
                else:
                    if line[0].islower():
                        if "she's" in line:
                            line = "S" + line[1:]
                    if re.search(r'\w$', line):
                        line += "."
                    if re.search(r'They fight crime!', line):
                        x = re.split("They", line)
                        line = x[0]
                        line = line.strip()
                    if re.search(r'^\W', line):
                        line = line[1:]
                        line = line.strip()
                line += "\n"
                outfile.write(line)

text = open("tfc2.txt", "r")
words = text.read()
des = TextBlob(words)
best_male = " "
best_female = " "
worst_male = " "
worst_female = " "
female = ""
male = ""
for sentence in des.sentences:
    #checks polarity of female sentences
    if "She's" in sentence:
        sentP = sentence.polarity
        #stores best and worst polarity
        bF = TextBlob(best_female).polarity
        wF = TextBlob(worst_female).polarity
        if sentP > bF:
            best_female = str(sentence)
        if sentP < wF:
            worst_female = str(sentence)
    else:
        #repeats process for male sentences
        sentP = sentence.polarity
        bM = TextBlob(best_male).polarity
        wM = TextBlob(worst_male).polarity
        if sentP > bM:
            best_male = str(sentence)
        if sentP < wM:
            worst_male = str(sentence)
#prints the best and worst characters in the joke form (male + female + They fight crime!)
print("Best: " + best_male + " " + best_female + " They fight crime!")
print("Worst: " + worst_male + " " + worst_female + " They fight crime!")


female = ""
male = ""
words = words.splitlines()
for lines in words:
    if "She's" in lines:
        female += lines
        female += "\n"
    elif "He's" in lines:
        male += lines
        male += "\n"
#counts number of each description occurance and prints the 10 most common for males and females
counterF = Counter(female.splitlines())
print("10 Most Common Female: ")
print(counterF.most_common(10))
counterM = Counter(male.splitlines())
print("10 Most Common Male: ")
print(counterM.most_common(10))