
# import the time module
import time
import pyautogui
from time import sleep

# input time in seconds
t = 20000

# define the countdown func.
def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
       
        pyautogui.click(x=860, y=372)
        pyautogui.click(x=1283, y=754)
                        
      
    print('Finish')

def  actionneur():
                                                    
        pyautogui.click(x=1264, y=421)
        time.sleep(2)

        pyautogui.click(x=1681, y=684)
        print("ok")
 
# function call
pyautogui.FAILSAFE = False
countdown(int(t))
actionneur()

