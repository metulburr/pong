
import pygame as pg
from data.main import main
import data.tools
import argparse

parser = argparse.ArgumentParser(description='')
parser.add_argument('-c','--clean', action='store_true', 
    help='Remove all .pyc files and __pycache__ directories')
args = vars(parser.parse_args())

if __name__ == '__main__':
    if args['clean']:
        data.tools.clean_files()
    else:
        main()
        pg.quit()
