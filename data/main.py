

from .control import Control

def main(fullscreen, difficulty, size):
    app = Control(fullscreen, difficulty, size)
    app.run()
