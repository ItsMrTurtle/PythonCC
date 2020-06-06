# -*- coding: utf-8 -*-
"""
Created on Thu May  7 19:19:32 2020

@author: Christopher Cheng
"""

def read_file (file):
    """
    file is a file object with format:
    Read from a list of names and telephone number in format:
        1 Name
        1 Phone Number
        2 Name
        2 Telephone number 
        ** Seperated by a new line (\n)
        
    Function: To read from a file and allocate to a variable 
    Return: a tuple of 2 tupleS: names and phone numbers 
    """
    
    # The \n newline is implied in each line - we don't want it
    # Use string.replace("a","b") to replace the new line with empty blanks 
    # Can also use the function: word.strip("a") to acheive the same goal 

    # Create placeholder tuples and counter
    even_tuple = ()
    odd_tuple = ()
    line_count = 0
    
    # Go through every character in the string file 
    for line in file: 
        stripped_line = line.strip("\n") #Removes the new lines 
        if line_count % 2 == 0:
            even_tuple += (stripped_line,) #If odd line, add to name
        elif line_count % 2 == 1:
            odd_tuple += (stripped_line,) #If even line, add to number 
        line_count += 1 #Increment the line

    return (even_tuple,odd_tuple) # Return the 2 tuples

def sanitize (tuple_numbers):
    """
    Clean up a tuple of strings passed for irregular formatting of phone numbers
    Whether it's spaces, dashes, or parenthesis
    Return: A clean string with only numbers 
    """
    clean_string = ()
    for st in tuple_numbers:
        # Remove junk characters
        st = st.replace(" ", "")
        st = st.replace("-","")
        st = st.replace("(","")
        st = st.replace(")","")
        clean_string += (st,) #Add in tuple form to the tuple
    return clean_string
    
def analyze_friends (names,phones,all_areacodes,all_places):
    """
    names: tuple of names
    phones: tuple of phone numbers (cleaned)
    all_areacodes: tuple of area codes (3char ints)
    all_places: tuple of places
    Goal: Print out how many friends you have and every unique state 
    """
    
    # For TESTING MAKE THE PHONE NUMBER FIRST 3 DIGITS THE SAME AS THE AREA CODE
    # def get_unique_area_codes():
    #     """
    #     Returns a tuple of all unique area codes
    #     """
    #     area_codes = ()
    #     for ph in phones:
    #         if ph[0:3] not in area_codes:
    #             area_codes += (ph[0:3],)
    #     return area_codes
    
    def get_States(some_areacodes):
        """
        some_areacodes: tuple of area codes
        Return a tuple of states ASSOCIATED with area codes
        """
        states = ()
        for ac in some_areacodes:
            if ac not in all_areacodes:
                states += ("BAD AREA CODE",)
            else:
                index = all_areacodes.index(ac)
                states += (all_places[index],)
        return states
    
    num_friends = len(names) # Gets number of friends
    # unique_areacodes = get_unique_area_codes()
    unique_states = get_States(all_areacodes)
    
    print("You have", num_friends, "friends!")
    print("They live in", unique_states)
    # Function ends with the print, no returns 

friends_file = open('namesnumbers.txt') #Open the text file 
(names,numbers) = read_file(friends_file)

map_file = open('map_area_states.txt')
(area,states) = read_file(map_file)

clean_numbers = sanitize(numbers)
analyze_friends(names,numbers,area,states)

friends_file.close() #Close the text file
map_file.close()
