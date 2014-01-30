

from .control import Control

def main(fullscreen, difficulty):
    app = Control(fullscreen, difficulty)
    app.run()
