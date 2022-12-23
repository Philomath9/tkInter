import tkinter as tk
from tkinter import messagebox
from gameboard import *
from keyboard import *
from gamelogic import *

class App:      
    def __init__(self, root):
        self.root = root
        self.keyboardObject = keyboard()
        self.gameObject = gameBoard()  

        self.frameTop = tk.Frame(self.root, bg="#121214")
        self.frameTop.pack(side="top", fill=tk.BOTH, expand=1)  
        tk.Label(self.frameTop,text = "", width = 100, bg="#121214").grid(column = 1, row = 0, columnspan = 18)
        tk.Button(self.frameTop, text = "New Word", bg="grey", width = 12,command=self.newWord).grid(column = 0, row = 0, columnspan = 3, sticky="ew")        
        self.gameObject.createGameboard(self.frameTop) 
        
        self.frameBottom = tk.Frame(self.root, bg="#121214")
        self.frameBottom.pack(side="bottom", fill=tk.BOTH, expand=1)
        self.keyboardObject.createKeyboard(self.keyPressed, self.frameBottom)                
 
    def keyPressed(self, keyElem):
        key = keyElem.getKey()        
        if(not(self.gameObject.getState() == gameStates.WORDPICK)):
            return # we are either in win or loss state here        
        if(key == 'ENTER'):
            if self.gameObject.enterButton():
                # ok the input was valid
                # update the keyboard letter colors
                states = self.gameObject.getKeyStates() # hey states are a dict with 'char' and UNKNOWN EXACT or CLOSE
                self.keyboardObject.updateKeyStates(states)
                if(self.gameObject.getState() == gameStates.WINNER):
                    ret = messagebox.askquestion("You win!","Another round?")
                    if ret == 'yes':
                        self.newWord()
                    else:
                        quit()
                if(self.gameObject.getState() == gameStates.LOOSER):
                    str = "The answer was " + self.gameObject.winword + "\nAnother round?"
                    ret = messagebox.askquestion("Cough...loser...cough!", str)
                    if ret == 'yes':
                        self.newWord()
                    else:
                        quit()
            else:
                pass # we were not valid
        elif(key == 'Back'):
            self.gameObject.delChar()
        else: # it must be a letter
            self.gameObject.addChar(key)            
   
    def newWord(self): # button handler
        self.gameObject.resetBoard()   
        self.keyboardObject.resetLetters() 
   
root = tk.Tk()
app = App(root)
root.mainloop()