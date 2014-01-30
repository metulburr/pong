#!/usr/bin/env python

import pygame as pg
from data.main import main
import data.tools
import argparse
import sys

parser = argparse.ArgumentParser(description='')
parser.add_argument('-c','--clean', action='store_true', 
    help='Remove all .pyc files and __pycache__ directories')
parser.add_argument('-f' , '--fullscreen', action='store_true',
    help='start program with fullscreen')
parser.add_argument('-d' , '--difficulty',
    help='DIFFICULTY = [hard, medium, easy], change AI difficulty, default is medium, ')
args = vars(parser.parse_args())

if __name__ == '__main__':
    accepted_difficulty = ['hard', 'medium', 'easy']
    difficulty = 'medium'
        
    if args['difficulty'].lower() in accepted_difficulty:
        difficulty = args['difficulty'].lower()
        print('difficulty: {}'.format(difficulty))
    else:
        print('{} is not a valid difficulty option, {}'.format(args['difficulty'], accepted_difficulty))
        sys.exit()
        
    if args['clean']:
        data.tools.clean_files()
    else:
        main(args['fullscreen'], difficulty)
    pg.quit()

