#!/usr/bin/env python3
#shebang line

#function descriptions...

#import modules
import random
import readchar
from time import time, ctime
from datetime import datetime
import sys
from pprint import pprint
import argparse
from collections import namedtuple
from math import sqrt
import colorama 
from colorama import Fore, Back, Style

def Statistics(inputs, t_start, t_end):
        
        n_hits = 0 
        thad = 0
        tmad = 0
        duration = t_end - t_start 
        
        for input in inputs:
                if input[0] == input[1]: # caso requested == received
                        n_hits += 1
                        thad += input[2]
                else:
                        tmad += input[2]
        
        accuracy = n_hits/len(inputs) * 100
           
        tad = (thad + tmad) / len(inputs)  
        
        if n_hits == len(inputs): #evitar divisões por 0 caso utilizador acerte tudo
                tmad = 0
        else:
                tmad = tmad / (len(inputs) - n_hits)
                
        if n_hits == 0: #evitar divisões por 0 caso utilizador erre tudo
                thad = 0
        else:
                thad = thad / n_hits
        
        start = datetime.fromtimestamp(t_start).strftime("%A, %B %d, %Y %I:%M:%S") # parece complicado mas faz o que time.ctime() deveria fazer mas não estava a funcionar de outra forma
        end = datetime.fromtimestamp(t_end).strftime("%A, %B %d, %Y %I:%M:%S")     # aplica o formato de data tendo o numero de segundos
        
        data = {'accuracy': accuracy, 'inputs': inputs, 'number_of_hits': n_hits, 'number_of_types': len(inputs), 'test_duration': duration, 'test_end' : end, 'test_start': start,
                'type_average_duration' : tad, 'type_hit_average_duration' : thad, 'type_miss_average_duration':tmad}
    
        pprint(data)
        sys.exit()

# Function to generate words from a text, in a logical order and check if the user introduces them correctly
def GenerateWords(numwords):
        Input = namedtuple('Input', ['requested', 'received', 'duration'])
        inputs = []

        with open('The zen of python - Tim Peters.txt', 'r', encoding='utf-8') as textfile: # Opening the txt file in 'read' mode
              text = textfile.read()                # Funtion to read txt file

        if numwords == 0:                           # For the first word in the typing test
            words = text.plit()                     # Splits the text in a word list
            randomword = random.choice(words)       # Chooses a random letter from the word list
            wordnum = words.index(randomword)       # Returns the index from the random word in the list

            letters_word = list(randomword)         # Divides the word in a letter list

        else:
            wordnum += 1                            # The index of the word is now the index of the next word

            if wordnum < len(words) - 1:            # Makes sure the word is not the last word in the text
                   randomword = words[wordnum+1]      # Increments the word index so that there is a logic evolution of the sentence
                   letters_word = list(randomword)    # Divides the new word in a letter list

            else:                                         # If the last word was the last word in the txt, generates a new random word
                    randomword = random.choice(words)       # Chooses a random letter from the word list
                    wordnum = words.index(randomword)       # Returns the index from the random word in the list
                    letters_word = list(randomword)         # Divides the new word in a letter list

        print('Type ' + randomword + Fore.BLUE + Style.RESET_ALL)   # Giving the new word

        t_request = time()                              # Input - time duration
        while len(word_pressed) < len(letters_word):    # Stops reading when the word being typed and the word show have the same number of letters
                
                letter = readchar.readkey()              # Reads keys (letters) being typed
                word_pressed += letter                   # Adds new letters to the word being typed
                print (letter, end = '' , flush = True)  # Shows the user what they are typing

        t_deliver = time()                               # End of time duration for input
                
        inputs.append(Input(randomword, word_pressed, t_deliver - t_request))   #Appending the data to the dictionary
        return inputs, word_pressed, randomword    

# Time mode for word typing test
def Time_Words(seconds):
        
        t_start = time()
        duration = t_start + seconds
        numwords = 0      
            
        while time() < duration:

            inputs, word_pressed, randomword = GenerateWords(numwords)

            if word_pressed == randomword:
                print('You typed letter ' + Fore.GREEN + word_pressed + Style.RESET_ALL)  
            else:
                print('You typed letter ' + Fore.RED + word_pressed + Style.RESET_ALL)
                        
            numwords += 1

        t_end = time()
        print('Current test duration (' + Fore.CYAN + (str(t_end - t_start)) + Style.RESET_ALL + ") exceeds maximum of " + str(seconds))
        Statistics(inputs, t_start, t_end)

# Maximum number of words mode for word typing test
def  Inputs_Words(max_words):
        
        t_start = time()
        numwords = 0

        while numwords < max_words:

                inputs, word_pressed, randomword = GenerateWords(numwords)
    
                if word_pressed == randomword:
                        print('You typed letter ' + Fore.GREEN + word_pressed + Style.RESET_ALL)
                else:
                        print('You typed letter ' + Fore.RED + word_pressed + Style.RESET_ALL)

                numwords += 1
        
        t_end = time()
        print(str(numwords) + ' inputs submitted when the maximum was ' + str(max_words))
        Statistics(inputs, t_start, t_end)
                       


def Tempo_Letras(segundos):
        
        t_start = time()
        duration = t_start + segundos        
            
        while time() < duration:

            inputs, key_pressed, key_requested = GenerateLetter()
            if key_pressed == key_requested:
                print('You typed letter ' + Fore.GREEN + key_pressed + Style.RESET_ALL)  
            else:
                print('You typed letter ' + Fore.RED + key_pressed + Style.RESET_ALL)
                            
        t_end = time()
        print('Current test duration (' + Fore.CYAN + (str(t_end - t_start)) + Style.RESET_ALL + ") exceeds maximum of " + str(segundos))
        Statistics(inputs, t_start, t_end)


def  Inputs_Letras(max_letras):
        
        t_start = time()
        n_letras = 0

        while n_letras < max_letras:

                inputs, key_pressed, key_requested = GenerateLetter()
    
                if key_pressed == key_requested:
                        print('You typed letter ' + Fore.GREEN + key_pressed + Style.RESET_ALL)
                else:
                        print('You typed letter ' + Fore.RED + key_pressed + Style.RESET_ALL)
                
                n_letras += 1
        
        t_end = time()
        print(str(n_letras) + ' inputs submitted when the maximum was ' + str(max_letras))
        Statistics(inputs, t_start, t_end)
                
def GenerateLetter():
    Input = namedtuple('Input', ['requested', 'received', 'duration'])
    inputs = []

    num = random.randint(97,122)
    key_requested = chr(num)
    print('Type letter ' + Fore.BLUE + key_requested + Style.RESET_ALL)
    t_request = time()                                                          #usado para calcular a duração de cada input
    key_pressed = readchar.readkey()
    t_deliver = time()                                                          #usado para calcular a duração de cada input                                      
    inputs.append(Input(key_requested, key_pressed, t_deliver - t_request))

    return inputs, key_pressed, key_requested                               

def main():
    
        # usei a seguinte linha no terminal para testar o programa
        # python3 main.py -utm 3 -mv 3 -wl word 
    
        parser = argparse.ArgumentParser(description='Typing test')
        parser.add_argument('-utm','--use_time_mode', help='Max number of seconds for the test.', action="store_true") 
        parser.add_argument('-mv','--maximum_value',type=int, help='Max number of inputs or seconds for the test', required=True)
        parser.add_argument ('-wl', '--word_letter', type=str, help='Word mode or letter mode',required=True)
        
        args = vars(parser.parse_args()) #cria um dicionário
        
        #check parameters 
        
        if args['use_time_mode']:
                print("Calling time mode")
                
                if args['word_letter'] == 'word':
                        print('calling word mode')
                        Time_Words(args['maximum_value'])
                        
                elif args['word_letter'] == 'letter':
                        print('calling letter mode')
                        Tempo_Letras(args['maximum_value'])
                        
                else:
                        sys.exit("Bad inputs")
                        
        else:
                print("Calling Input")
                
                if args['word_letter'] == 'word':
                        print('calling word mode')
                        Inputs_Words(args['maximum_value'])
                        
                elif args['word_letter'] == 'letter':
                        print('calling letter mode')
                        Inputs_Letras(args['maximum_value'])
                        
                else:
                        sys.exit("Bad inputs")        

if __name__ == '__main__':
    main()
