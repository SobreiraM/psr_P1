#!/usr/bin/env python3
# Shebang line

# PSR Typing Test - Universidade de Aveiro - 23/24
# Miguel Sobreira - 110045
# Ricardo Baptista - 40170

######################      IMPORT MODULES      ######################

import random
import json
import readchar
from time import time, ctime, sleep
from datetime import datetime
import sys
from pprint import pprint
import argparse
from collections import namedtuple
from math import sqrt
import colorama 
from colorama import Fore, Back, Style

######################      GLOBAL VARIABLES      ######################      

Input = namedtuple('Input', ['requested', 'received', 'duration', 'correct_letters'])
inputs = []

######################      FUNCTIONS      ######################  

######## START TEST FUNCTION
# If any key is pressed the test starts, if the key is the space bar, the test stops
def Start_Test():
    print('Press any key to start the test or press key "Space" to abort the test!\n')
        
    key_pressed = readchar.readkey()     

    if key_pressed == chr(32):                                                  # If space key is pressed the program stops
        print( Back.RED + 'Test interrupted!' + Style.RESET_ALL)
        exit()                                                                  #Exit the test

    else:
        for i in range(1,4):
            print( Back.GREEN + 'Starting the test in '+ str(4-i) +' seconds' + Style.RESET_ALL, end="\r")
            sleep(1)
            print("\033[K", end="\r" )

######## LETTER MODE FUNCTIONS
# Function to generate letters and check if the user introduces them correctly
def GenerateLetter():

    num = random.randint(97,122)                                                 # Chooses a random number from the ASCII table
    key_requested = chr(num)                                                     # Transforms int to char

    print('Type letter ' + Fore.BLUE + key_requested + Style.RESET_ALL)          # Asks user for input

    t_start = time()                                                             # Starts timer
    t_request = time()                                                           # Saving time stamps for data purposes
    key_pressed = readchar.readkey()
    t_deliver = time()                                                           # Calculates de duration of each input

    if key_pressed == chr(32):                                                   # If space key is pressed the program stops              
        print( Back.RED + '\nTest interrupted!' + Style.RESET_ALL)
        t_end = time()
        Statistics(t_start, t_end)
        exit()

    if(key_pressed == key_requested):                                            # Records how many tries were hits and misses
        hit = 1
    else:
        hit = 0
            
    inputs.append(Input(key_requested, key_pressed, round(t_deliver - t_request,4), hit)) # Appends data

    return key_pressed, key_requested                               


# 'Test duration' mode for word typing test
def Time_Letters(segundos):
        
    t_start = time()
    duration = t_start + segundos        
        
    while time() < duration:                    # Until the maximum time limit is reached, the program runs

        key_pressed, key_requested = GenerateLetter()

        if key_pressed == key_requested:        # When the letter pressed corresponds to the letter given prints the answer in green
            print('You typed letter ' + Fore.GREEN + key_pressed + Style.RESET_ALL) 

        else:                                   # When the letter pressed is not the given letter and prints the answer in red
            print('You typed letter ' + Fore.RED + key_pressed + Style.RESET_ALL)
                        
    t_end = time()
    print('Current test duration (' + Fore.CYAN + (str(t_end - t_start)) + Style.RESET_ALL + ") exceeds maximum of " + str(segundos))
    Statistics(t_start, t_end)


# 'Maximum number of inputs' mode for letter typing test
def  Inputs_Letters(max_letters):
        
    t_start = time()
    n_letters = 0

    while n_letters < max_letters:              # While the number of letters printed is not the max number of letter the program runs

        key_pressed, key_requested = GenerateLetter()

        if key_pressed == key_requested:        # When the letter pressed corresponds to the letter given prints the answer in green
            print('You typed letter ' + Fore.GREEN + key_pressed + Style.RESET_ALL)

        else:                                   # When the letter pressed is not the given letter and prints the answer in red
            print('You typed letter ' + Fore.RED + key_pressed + Style.RESET_ALL)
        
        n_letters += 1
    
    t_end = time()

    # Ends the typing test and prints statistics
    print(str(n_letters) + ' inputs submitted when the maximum was ' + str(max_letters))
    Statistics(t_start, t_end)
        

######## WORD MODE FUNCTIONS

# Function to generate words from a text, in a logical order and check if the user introduces them correctly
def GenerateWords(t_start,numwords):

    # Global variables
    global word_n
    global words


    with open('The zen of python - Tim Peters.txt', 'r', encoding='utf-8') as textfile: # Opening the txt file in 'read' mode
        text = textfile.read()                  # Funtion to read txt file

    if numwords == 0:                           # For the first word in the typing test

        words = text.split()                    # Splits the text in a word list
        randomword = random.choice(words)       # Chooses a random letter from the word list
        word_n = int(words.index(randomword))   # Returns the index from the random word in the list

        letters_word = list(randomword)          # Divides the word in a letter list
        
    else:
        
        word_n += 1                              # The index of the word is now the index of the next word

        
        if word_n < len(words) - 1:              # Makes sure the word is not the last word in the text
            randomword = words[word_n]           # Increments the word index so that there is a logic evolution of the sentence
            letters_word = list(randomword)    

        else:                                    # If the last word was the last word in the txt, generates a new random word
            randomword = random.choice(words)       
            word_n = words.index(randomword)        
            letters_word = list(randomword)         

    print('Type ' + Fore.BLUE + randomword + Style.RESET_ALL)   # Giving the new word

    t_request = time()                           # Time duration
    word_pressed = ''

    while len(word_pressed) < len(letters_word): # Stops reading when the word being typed and the word shown have the same number of letters
        letter = readchar.readkey()              # Reads keys (letters) being typed

        if letter == chr(32):                    # When the key "Space" is pressed                   
            print( Back.RED + '\nTest interrupted!' + Style.RESET_ALL)
            t_end = time()
            Statistics(t_start, t_end)
            exit()

        word_pressed += letter                   # Adds new letters to the word being typed
        print (letter, end = '' , flush = True)  # Shows the user what they are typing

    t_deliver = time()                           # End of time duration for input

    equal_letters = 0                            # Will count equal letters
    for letter in randomword:
        if letter in word_pressed:
            equal_letters += 1

    inputs.append(Input(randomword, word_pressed, round(t_deliver - t_request,4), equal_letters))   #Appending the data to the dictionary
    return word_pressed, randomword


# 'Test duration' mode for word typing test
def Time_Words(seconds):
    
    # Initializing variables
    t_start = time()
    duration = t_start + seconds
    numwords = 0      

    while time() < duration:                                    # The typing test should only work until the time is up

        word_pressed, randomword = GenerateWords(t_start, numwords)      # Calling GenerateWords() function

        if word_pressed == randomword:                          # When the word pressed corresponds to the word given prints the answer in green

            print('')
            print('You typed ' + Fore.GREEN + word_pressed + Style.RESET_ALL)  

        else:                                                   # When the word pressed is not the word given prints the answer in red
    
            print('')
            print('You typed ' + Fore.RED + word_pressed + Style.RESET_ALL)
                    
        numwords += 1                                           # Increments word index

    t_end = time()

    # Ends the typing test and prints statistics
    print('Current test duration (' + Fore.CYAN + (str(t_end - t_start)) + Style.RESET_ALL + ") exceeds maximum of " + str(seconds))
    Statistics(t_start, t_end)


# 'Maximum number of inputs' mode for word typing test
def  Inputs_Words(max_words):
        
    t_start = time()
    numwords = 0

    while numwords < max_words: # The test runs until the max number of words is met

        word_pressed, randomword = GenerateWords(t_start, numwords)

        if word_pressed == randomword:          # When the word pressed corresponds to the word given prints the answer in green

            print('')
            print('You typed letter ' + Fore.GREEN + word_pressed + Style.RESET_ALL)

        else:                                   # When the word pressed is not the word given prints the answer in red

            print('')
            print('You typed letter ' + Fore.RED + word_pressed + Style.RESET_ALL)

        numwords += 1
    
    t_end = time()

    # Ends the typing test and prints statistics
    print(str(numwords) + ' inputs submitted when the maximum was ' + str(max_words))
    Statistics(t_start, t_end)
                       

######## STATISTIC FUNCTIONS

# Function to processo data and generate statistics
def Statistics(t_start, t_end):
        
    # Variable initialization
    n_hits = 0                                  # Number of hits
    thad = 0                                    # Average duration of a correct try
    tmad = 0                                    # Average duration of a miss try
    duration = t_end - t_start                  # Duration of the typing test
    
    # Cycle to count the number of correct and wrong answers
    for input in inputs:
            
        if input[0] == input[1]:                # In case input requested is equal to input received
            n_hits += 1
            thad += input[2]

        else:                                   # In case input requested is different to input received
            tmad += input[2]

    if len(inputs) == 0:
        accuracy = 0
        tad = 0
    
    else:           
        accuracy = n_hits / len(inputs) * 100 # Accuracy calculation
        tad = (thad + tmad) / len(inputs)     # Average duration of any type of answer
    
    if n_hits == len(inputs):                 # In case the user gets everything right, avoids division by 0
        tmad = 0

    else:
        tmad = tmad / (len(inputs) - n_hits)

        
    if n_hits == 0:                           # In case the user gets everything wrong, avoids division by 0
        thad = 0

    else:
        thad = thad / n_hits                  # Average duration of right answers
              
    
    start = datetime.fromtimestamp(t_start).strftime("%A, %B %d, %Y %I:%M:%S") # Timestamp for the beginning
    end = datetime.fromtimestamp(t_end).strftime("%A, %B %d, %Y %I:%M:%S")     # Timestamp for the end
    
    # Data registry input
    data = {'number_of_types': len(inputs), 'number_of_hits': n_hits, 'accuracy': round(accuracy,2),
        'test_duration': round(duration,4), 'test_start': start, 'test_end' : end,'type_average_duration' : round(tad,4),
        'type_hit_average_duration' : round(thad,4), 'type_miss_average_duration':round(tmad,4), 'inputs': inputs}

    # Printing data
    pprint(data, sort_dicts=False)

    # History save file
    history = open('history.txt', 'a')          # Open the file history.txt and save report
    history.write('User: ')
    json.dump(user, history)
    history.write(' Test duration: ')
    json.dump(data['test_duration'], history)   # Convert dictionary data into str
    history.write(' Score: ')
    json.dump(data['accuracy'], history)        # Convert dictionary data into str
    history.write('\n')
    history.close
    sys.exit()


######## MAIN FUNCTION

# Main funtion defines the order, logic and conditions behind the sequence each function is called in
def main():
    global user
    # Argparse description and arguments
    parser = argparse.ArgumentParser(description='Typing test')

    parser.add_argument('-utm','--use_time_mode', help='Use time mode for the test.', action="store_true") 
    parser.add_argument('-mv','--max_value', type=int, help='Max number of inputs or seconds for the test', required=True)
    parser.add_argument('-uw', '--use_word_mode', help='Use word mode for the test', action="store_true")
    parser.add_argument('-user', type = str, help = "Set a user name to record your test score!")
    
    args = vars(parser.parse_args()) # Creates a dictionary
    print(args)

    if args['user'] is None:
        user = 'Default'
    else:
        user = args['user']
    Start_Test()
    #check parameters 
    
    if args['use_time_mode']:                   # Runs 'time mode' typing test
        if args['use_word_mode']:               # Runs 'word mode' type of test
            Time_Words(args['max_value'])
                
        else:                                   # Runs 'letter mode' type of test
            Time_Letters(args['max_value'])

                    
    else:                                       # Runs 'maximum input mode' typing test
        if args['use_word_mode']:               # Runs 'word mode' type of test
            Inputs_Words(args['max_value'])
                    
        else:                                   # Runs 'letter mode' type of test
            Inputs_Letters(args['max_value'])
                    

######################      MAIN CODE      ######################   

# Main program body, calls main function
if __name__ == '__main__':
      main()
