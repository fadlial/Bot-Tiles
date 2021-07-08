from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
'''
Here is the click function:
'''

#Tiles 1 :X:  351 Y:  820 RGB: (  0,   0,   0)
#Tiles 2 :
#Tiles 3 :
#Tiles 4 :


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(651, 400)[0] == 0:
        click(651,400)
    if pyautogui.pixel(651, 400)[0] == 16:
        click(651,400)
    if pyautogui.pixel(651, 400)[0] == 17:
        click(651,400)

        
    if pyautogui.pixel(734, 400)[0] == 0:
        click(734,400)
    if pyautogui.pixel(734, 400)[0] == 16:
        click(734,400)
    if pyautogui.pixel(734, 400)[0] == 17:
        click(734,400)

        
    if pyautogui.pixel(811, 400)[0] == 0:
        click(811,400)
    if pyautogui.pixel(811, 400)[0] == 16:
        click(811,400)
    if pyautogui.pixel(811, 400)[0] == 17:
        click(811,400)

        
    if pyautogui.pixel(892, 400)[0] == 0:
        click(892,400)
    if pyautogui.pixel(892, 400)[0] == 16:
        click(892,400)
    if pyautogui.pixel(892, 400)[0] == 17:
        click(892,400)
    

    
    
    
    
    
