import pyautogui
import keyboard
import time
import os

pyautogui.PAUSE = 0.01

# ================= CONFIGURATIONS =================
TEXT_FILE = 'texts.txt' 

TRIGGER_KEY = '/' 
# ==================================================

try:
    with open(TEXT_FILE, 'r', encoding='utf-8') as file:
        lines = file.readlines()
except FileNotFoundError:
    print(f"Error: The file '{TEXT_FILE}' was not found.")
    exit()

keyboard.wait(TRIGGER_KEY)

def clear_keys():
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('option')
    pyautogui.keyUp('shift')
    pyautogui.keyUp('command')
    pyautogui.press('esc')
    time.sleep(0.1)

def m_solve(words):
     for letter in words:
        if (letter == 'm' or letter =='M'):
            pyautogui.press('esc')
            pyautogui.write(letter.lower(),interval=.01)
        pyautogui.write(letter.lower(),interval=.01)

for line in lines:
    text = line.strip()
    if not text:
        continue
    time.sleep(0.1)
    pyautogui.hotkey('option', 'c')
    pyautogui.press('down', presses=3, interval=0.1)
    pyautogui.press('enter')
    ### CLEAN MENU ###
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('option') 
    time.sleep(0.1)
    pyautogui.press('l')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('option')
    pyautogui.keyDown('shift')
    time.sleep(0.1)
    pyautogui.press('tab',presses=4, interval=0.1)
    pyautogui.keyUp('shift')
    pyautogui.press('down', interval=0.1)
    pyautogui.press('up', presses=2, interval=0.1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('tab', presses=2, interval=0.1)
    clear_keys()
    m_solve('munic')
    pyautogui.press('tab', interval=0.1)
    m_solve(line[:-1])
    pyautogui.press('down', interval=0.1)
    pyautogui.press('enter')
    # SEARCH
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('option')  
    time.sleep(0.1)     
    pyautogui.press('p')
    pyautogui.keyUp('option')
    pyautogui.keyUp('ctrl')
    keyboard.wait(TRIGGER_KEY)
    pyautogui.keyDown('ctrl') 
    time.sleep(0.1)
    pyautogui.press('f4')
    pyautogui.keyUp('ctrl')
 
    
