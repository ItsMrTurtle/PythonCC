# -*- coding: utf-8 -*-
"""
Created on Wed May 13 00:53:55 2020

@author: Christopher Cheng
"""

# With 2 files, compare how similar they are and give them a rank [0,1] 
# 1 is exactly similar, 0 is no common words 

# Tasks:
# 1. Open and read the files
# 2. Put the words into a list 
# 3. Map the words and frequency (order doesn't matter yet)
# 4. Calculate the similarity via word count 

# Task 1: Read the files and return the content in a useable form 
# Function: to return the contents in form of a long string 

def read_text(file_name):
    """
    Parameters
    ----------
    file_name : string, name of file to read

    Returns
    -------
    line : string of the file contents 
    """
    
    inFile = open(file_name,'r') # Python function to open a file via name
    line = inFile.read() # Function to read contents into a string 
    return line

# Imports all string related functions 
import string
def find_words(text):
    """
    Parameters
    ----------
    text : string
    Parses the long string into separate words 

    Returns
    -------
    LIST of words from the input text 

    """
    text = text.replace("\n"," ") # Replaces new lines with a space
    for char in string.punctuation: #Looks at all punctuations in the string
        text = text.replace(char,"") # Replace punc with empty string
    words = text.split(" ") #Make a list by separating by spaces
    return words

def frequencies(words):
    """
    Parameters
    ----------
    words : LIST 
    Get the frequency each word occurs

    Returns
    -------
    Dictionary of words and its frequency as its value 
    """
    freq_dict = {}
    for word in words:
        if word in freq_dict:
            freq_dict[word] +=  1
        else:
            freq_dict[word] = 1
    return freq_dict

# To calculate: Score = total diff/ total num words in both 
def calculate_similarity(dict1,dict2):
    """
    Parameters
    ----------
    dict1: freq dict for text1
    dict2: freq dict for text2
    Returns
    -------
    float between [0,1] for similarity 
    """
    diff = 0
    total = 0
    # Uses 2 loops. This one goes through all of dictionary 1
    for word in dict1.keys():
        # If the word is in both dictionaries
        if word in dict2.keys():
            diff += abs(dict1[word]-dict2[word]) #Get the diff in frequency in + val
        #Otherwise, just add the count since the word isnt in dict2
        else:
            diff += dict1[word]
    # 2nd loop dictionary 
    for word in dict2.keys():
        if word not in dict1.keys():
            diff += dict2[word] #Add the frequency
    
    # Calculate total: total number of words in both dictionaries 
    total = sum(dict1.values()) + sum(dict2.values())
    difference = diff/total          
    similar = 1.0 - difference
    # Return a number with 2 decimal places 
    return round(similar,2) 
    
text1 = read_text("sonnet18.txt")
text2 = read_text("sonnet19.txt")
words1 = find_words(text1)
words2 = find_words(text2)
freq_dict1 = frequencies(words1)
freq_dict2 = frequencies(words2)
print(calculate_similarity(freq_dict1,freq_dict2))