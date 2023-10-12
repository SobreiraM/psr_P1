#!/usr/bin/env python3
#shebang line

#import modules
from pprint import pprint
import argparse
from collections import namedtuple
from math import sqrt
import colorama 
from colorama import Fore, Back, Style

def main():
    
    # usei a seguinte linha no terminal para testar o programa
    # python3 main.py -utm 3 -mv 3 -wl word 
    
        parser = argparse.ArgumentParser(description='Typing test')
        parser.add_argument('-utm','--use_time_mode',type=int, help='Max number of seconds for the test.') 
        parser.add_argument('-mv','--maximum_value',type=int, help='Max number of inputs for the test')
        parser.add_argument ('-wl', '--word_letter', type=str, help='Word mode or letter mode')
        
        args = vars(parser.parse_args()) #cria um dicionário 
        
        print(args['maximum_value']) #para aceder a valores especificos no dicionario faz-se args['NOME'];
        print(args['use_time_mode']) #caso não se saiba NOME pode-se dar print ao dicionário todo com print(args) e ver o nome que é imprimido no terminal
        print(args['word_letter'])
        

if __name__ == '__main__':
    main()
