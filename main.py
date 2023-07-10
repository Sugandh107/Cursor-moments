import pyautogui as pag
import random
import time


cords=pag.position()
afk=0
while True:
    if pag.position()==cords:
        afk+=1
    else:
        afk=0
        cords=pag.position()
        
    if afk>1:
        x=random.randint(2560,5120)
        y=random.randint(1,1440)
        pag.moveTo(x,y,0.5)
        cords=pag.position()
    print(afk)
    
    time.sleep(2)