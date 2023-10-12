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
        
def  Tempo_Letras(segundos):
        Input = namedtuple('Input', ['requested', 'received', 'duration'])
        inputs = [] #lista para namedtuple
        #t = ctime() penso que isto não é preciso
        t_start = time()
        duration = t_start + segundos        
        
        while time() < duration :
                num = random.randint(97,122)
                key_requested = chr(num)
                
                print('Type letter ' + Fore.BLUE + key_requested + Style.RESET_ALL)
                
                t_request = time()               #usado para calcular a duração de cada input
                key_pressed = readchar.readkey()
                t_deliver = time()         #usado para calcular a duração de cada input                                      
                inputs.append(Input(key_requested, key_pressed, t_deliver - t_request))
                
                if key_pressed == key_requested:
                        print('You typed letter ' + Fore.GREEN + key_pressed + Style.RESET_ALL)  
                else:
                        print('You typed letter ' + Fore.RED + key_pressed + Style.RESET_ALL)
                        
        t_end = time()
        print('Current test duration (' + Fore.CYAN + (str(t_end - t_start)) + Style.RESET_ALL + ") exceeds maximum of " + str(segundos))
        
        Statistics(inputs, t_start, t_end)
                
def  Inputs_Letras(max_letras):
        Input = namedtuple('Input', ['requested', 'received', 'duration'])
        inputs = []
        #t = ctime()
        t_start = time()
        n_letras = 0
        
        while n_letras < max_letras :
                num = random.randint(97,122)
                key_requested = chr(num)
                print('Type letter ' + Fore.BLUE + key_requested + Style.RESET_ALL)
                t_request = time()               #usado para calcular a duração de cada input
                key_pressed = readchar.readkey()
                t_deliver = time()         #usado para calcular a duração de cada input                                      
                inputs.append(Input(key_requested, key_pressed, t_deliver - t_request))
                
                if key_pressed == key_requested:
                        print('You typed letter ' + Fore.GREEN + key_pressed + Style.RESET_ALL)
                else:
                        print('You typed letter ' + Fore.RED + key_pressed + Style.RESET_ALL)
                
                n_letras += 1
        
        t_end = time()
        
        print(str(n_letras) + ' inputs submitted when the maximum was ' + str(max_letras))
        Statistics(inputs, t_start, t_end)
                
                                   

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
                print("Calling Time mode")
                
                if args['word_letter'] == 'word':
                        print("calling word")
                        
                elif args['word_letter'] == 'letter':
                        print('calling letter')
                        Tempo_Letras(args['maximum_value'])
                        
                else:
                        sys.exit("Bad inputs")
                        
        else:
                print("Calling Input")
                
                if args['word_letter'] == 'word':
                        print("calling word")
                        
                elif args['word_letter'] == 'letter':
                        print('calling letter')
                        Inputs_Letras(args['maximum_value'])
                        
                else:
                        sys.exit("Bad inputs")        

if __name__ == '__main__':
    main()
