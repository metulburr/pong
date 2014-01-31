#!/usr/bin/env python

import pygame as pg
from data.main import main
import data.tools
import argparse
import sys

parser = argparse.ArgumentParser(description='Pong Arguments')
parser.add_argument('-c','--clean', action='store_true', 
    help='Remove all .pyc files and __pycache__ directories')
parser.add_argument('-f' , '--fullscreen', action='store_true',
    help='start program with fullscreen')
parser.add_argument('-d' , '--difficulty', default='medium',
    help='where DIFFICULTY is one of the strings [hard, medium, easy], set AI difficulty, default is medium, ')
parser.add_argument('-s' , '--size', nargs=2, default=[800,600], metavar=('WIDTH', 'HEIGHT'),
    help='set window size to WIDTH HEIGHT, defualt is 800 600')
args = vars(parser.parse_args())

if __name__ == '__main__':
    accepted_difficulty = ['hard', 'medium', 'easy']
    
    if args['difficulty']:
        if args['difficulty'].lower() in accepted_difficulty:
            difficulty = args['difficulty'].lower()
            print('difficulty: {}'.format(difficulty))
        else:
            print('{} is not a valid difficulty option, {}'.format(args['difficulty'], accepted_difficulty))
            sys.exit()
    if args['size']:
        size = args['size']
        print('window size: {}'.format(size))
        
    if args['clean']:
        data.tools.clean_files()
    else:
        main(args['fullscreen'], difficulty, size)
    pg.quit()

