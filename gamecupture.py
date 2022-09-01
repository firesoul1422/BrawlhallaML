# Bring in mss
from mss import mss
# Bring in opencv for rendering 
import cv2
import numpy as np
import time 
import uuid
import os 
# bring in pynput for keypress capture
from pynput.keyboard import Key, Listener 


class GameCupture():

    def __init__(self) -> None:
        self.gamearea = {"left": 0, "top": 35, "width": 960, "height": 530}
        self.capture = mss()
        self.current_keys = None


    def collect_game(self):
        # for keystroks
        listener = Listener(on_press=self.on_keypress, on_release=self.on_keyrelease)
        listener.start()

        # for collecting game frames
        filename = os.path.join("data", str(uuid.uuid1()))
        gamecap = np.array(self.capture.grab(self.gamearea))
        cv2.imwrite(f"{filename}.png", gamecap)

        if self.current_keys:
            np.savetxt(f"{filename}.txt" , np.array([str(self.current_keys)]), fmt="%s")

    def on_keypress(self, key):
        if self.current_keys == key:
            print(self.current_keys)
            return self.current_keys

        else:
            print(self.current_keys)
            self.current_keys = key
            return self.current_keys


    def on_keyrelease(self, key):
        self.current_keys = None
        if key == Key.esc:
            return False





if __name__ == "__main__":
    time.sleep(10)
    game = GameCupture()
    while True:
        game.collect_game()
