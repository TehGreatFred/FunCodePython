#mouse moving troll
import pyautogui
import time
from tkinter import *

def mouseMoveDetect():
    orgPos = pyautogui.position()
    pyautogui.hotkey('winleft', 'd') #turns to desktop
    x,y= pyautogui.position()
    pyautogui.hotkey('winleft', 'd')
    while True:
        noPos = pyautogui.position()
        if noPos != orgPos:
            pyautogui.moveTo(x,y)
            #time.sleep(0.001)
            
def windowPop():
    root = Tk()
    root.title("WARNING!!!!")
    S = Scrollbar(root)
    T = Text(root, height=4, width=50)
    S.pack(side=RIGHT, fill=Y)
    T.pack(side=LEFT, fill=Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    quote = "Do not close"
    T.insert(END, quote)
    mainloop(  )

def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)





if __name__ == '__main__':
    install_and_import('pyautogui')
    windowPop()
    pyautogui.FAILSAFE = False
    pyautogui.hotkey('winleft', 'd') #turns to desktop
    mouseMoveDetect()
            
