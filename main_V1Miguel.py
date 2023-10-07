#!/usr/bin/env python3
#shebang line

#function descriptions...

#import modules
import random
import readchar
from time import time, ctime
import sys
from pprint import pprint
import argparse
from collections import namedtuple
from math import sqrt
import colorama 
from colorama import Fore, Back, Style


############## Variáveis Globais ##############
hit = [] 
miss = []
time_hit = []
time_miss = []

#def Statistics(): #vai receber parametros e calcular estatisticas pedidas para dps enviar
    
def Print_End(inputs, stats_dict): #será enviado um dicionário (criado na função de estatiticas) com os elementos, da seguinte forma -> stats_dict = {'accuracy': x, ....}
                                  #onde depois serão inseridos no dicionario data da seguinte forma -> data = {'accuracy': stats_dict['accuracy']}
    data = {'accuracy': 0, 'inputs': inputs, 'number_of_hits': 0, 'number_of_types': 0, 'test_duration': 0, 'test_end' : 0, 'test_start': 0,
            'type_average_duration' : 0, 'type_hit_average_duration' : 0, 'type_miss_average_duration':0}
    
    pprint(data)
    
    """ Relacionado com testes da função Print_End - REMOVER DEPOIS
    Input = namedtuple('Input', ['requested', 'received', 'duration'])
    I1 = Input('a','b','time')
    I2 = Input('c','d','time')
    I3 = Input('f','e','time')
    inputs = []
    inputs.append(I1)
    inputs.append(I2)
    inputs.append(I3)
    
    data = {'accuracy': 0, 'inputs': inputs, 'number_of_hits': 0, 'number_of_types': 0, 'test_duration': 0, 'test_end' : 0, 'teste_start': 0,
            'type_average_duration' : 0, 'type_hit_average_duration' : 0, 'type_miss_average_duration':0}
    
    
    print('dictionary')
    pprint(data)
    """
   
"""
def  Tempo_Palavras(segundos):
        t = ctime()
        t_start = time()
        duration = t_start + segundos
        
        hit = [] # talvez tenham que ser vars globais?
        time_hit = []
        miss = []
        time_miss = []
        
        
        while time() < duration :
        
        FALTA PREENCHER AQUI COM O CÓDIGO QUE GERA PALAVRAS
        
        t_end = time()
        print('Current test duration (' + Fore.CYAN + (str(t_end - t_start)) + Style.RESET_ALL + ") exceeds maximum of " + str(segundos))
        sys.exit()
"""                
#def  Inputs_Palavras(): 

        
def  Tempo_Letras(segundos):
        t = ctime()
        t_start = time()
        duration = t_start + segundos        
        
        while time() < duration :
                num = random.randint(97,122)
                key_requested = chr(num)
                print('Type letter ' + Fore.BLUE + key_requested + Style.RESET_ALL)
                key_pressed = readchar.readkey()
                
                if key_pressed == key_requested:
                        print('You typed letter ' + Fore.GREEN + key_pressed + Style.RESET_ALL)
                        hit.append(key_pressed)
                        time_hit.append(time())
                else:
                        print('You typed letter ' + Fore.RED + key_pressed + Style.RESET_ALL)
                        miss.append(key_pressed)
                        time_miss.append(time())
        
        t_end = time()
        print('Current test duration (' + Fore.CYAN + (str(t_end - t_start)) + Style.RESET_ALL + ") exceeds maximum of " + str(segundos))
        sys.exit()
                
def  Inputs_Letras(max_letras):
        n_letras = 0
        
        while n_letras < max_letras :
                num = random.randint(97,122)
                key_requested = chr(num)
                print('Type letter ' + Fore.BLUE + key_requested + Style.RESET_ALL)
                key_pressed = readchar.readkey()
                
                if key_pressed == key_requested:
                        print('You typed letter ' + Fore.GREEN + key_pressed + Style.RESET_ALL)
                        hit.append(key_pressed)
                        time_hit.append(time())
                else:
                        print('You typed letter ' + Fore.RED + key_pressed + Style.RESET_ALL)
                        miss.append(key_pressed)
                        time_miss.append(time())
                
                n_letras += 1
        
        print(str(n_letras) + ' inputs submitted when the maximum was ' + str(max_letras))
        sys.exit()                
                
                                

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