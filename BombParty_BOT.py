from pynput.keyboard import Key, Controller as KeyboardController

from pynput.mouse import Button, Controller as MouseController

import pyperclip, time, random

from pynput import keyboard

# SETTINGS
posOfChars = 835, 575 # POSITION OF FIELD WITH CHARS IN CENTER

posOfEnter = 841, 1023 # POSITION OF ENTER FIELD

timer = random.uniform(0.1, 0.18) # RANDOM INTERVAL OF ENTERING CHARS

def split(word):

    return [char for char in word]

# LOAD WORD LIBRARY OF WORDS

with open("library.txt", "r") as r:

    content = r.readlines()

send = KeyboardController()

mouse = MouseController()

def _parseChars():
    mouse.position = (posOfChars)

    mouse.press(Button.left)
    mouse.release(Button.left)

    mouse.press(Button.left)
    mouse.release(Button.left)

    send.press(Key.ctrl)
    send.press('c')

    time.sleep(0.01)

    send.release('c')
    send.release(Key.ctrl)

    Chars = pyperclip.paste()

    return Chars.lower()

def _findWord():

    chars = _parseChars()

    words = []

    for i in content:

        if (i.find(chars) != -1):

            words.append(i.split())

    return random.choice(words)

def _typeWord():

    word = _findWord()

    splittedWord = split(word[0])

    print(word[0] + "\n")

    mouse.position = (posOfEnter)

    mouse.press(Button.left)
    mouse.release(Button.left)

    for i in range(len(splittedWord)):

        send.press(splittedWord[i])
        send.release(splittedWord[i])

        time.sleep(timer)

    send.press(Key.enter)
    send.release(Key.enter)



def main():

    hotkey = keyboard.HotKey(keyboard.HotKey.parse('<f8>'), _typeWord)

    LtThread = keyboard.Listener(on_press=hotkey.press, on_release=hotkey.release)
    LtThread.start()
    LtThread.join()

if __name__ == "__main__":
    main()
