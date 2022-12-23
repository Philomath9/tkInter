import tkinter as tk
from tkinter import ttk
from states import *
from PIL import Image, ImageTk

class keyboardKey:
    def __init__(self, key, col, row, span, keyState):
        self.key = key
        self.row = row
        self.col = col
        self.span = span
        self.keyState = keyState
    def getKey(self):
        return self.key
    def getRow(self):
        return self.row
    def getCol(self):
        return self.col
    def getSpan(self):
        return self.span

class testAnim:
    def __init__(self, root, row, col):
               #example of compositing use this for animated letters
        self.root = root
        img = Image.open('Assets/A.png').convert("RGBA")
        back = Image.open('Assets/Nope.png').convert("RGBA")
        back2 = Image.open('Assets/Yup.png').convert("RGBA")
        c = Image.alpha_composite(back, img)
        d = Image.alpha_composite(back2, img)
        self.stateofanim = 0
        #c.show()
        self.image1 = ImageTk.PhotoImage(c)        # must keep a reference...wierd
        self.image2 = ImageTk.PhotoImage(d)        # must keep a reference...wierd
        self.label = tk.Label(root, image = self.image1)                
        self.label.grid(column = 0, row = 2, ipadx = 0, ipady = 0)  
        self.root.after(500, lambda:self.swapmeout()) 
        #command=lambda lelem = elem: kpfunc(lelem)

    def swapmeout(self):
        if(self.stateofanim == 0):
            self.label.configure(image = self.image2) 
            self.stateofanim = 1
        else:   
            self.label.configure(image = self.image1) 
            self.stateofanim = 0
        self.root.after(500, lambda:self.swapmeout())  

class keyboard:    
    def __init__(self):
        self.letters = []  
        self.buttons = {}
    def resetLetters(self):           
        for key in self.letters: # all the letters and the enter and backspace
            key.ketState = KeyStates.UNKNOWN     
        for key in self.buttons:
            self.buttons[key].configure(bg=getbgColor(KeyStates.UNKNOWN), fg=getfgColor(KeyStates.UNKNOWN))   
    def updateKeyStates(self, states): # states is a dictionary with 'char' and UNKNOWN EXACT or CLOSE
        for key, state in states.items():
            self.buttons[key].configure(bg=getbgColor(state), fg=getfgColor(state))        
    def createKeyboard(self, kpfunc, frame):
        # setup keyboard
        # Row 1                             Key,   Col,   Row,   Span,      State
        self.letters.append(keyboardKey(    'Q',     0,     1,      2,      KeyStates.UNKNOWN))
        self.letters.append(keyboardKey(    'W',     2,     1,      2,      KeyStates.UNKNOWN)) 
        self.letters.append(keyboardKey(    'E',     4,     1,      2,      KeyStates.UNKNOWN)) 
        self.letters.append(keyboardKey(    'R',     6,     1,      2,      KeyStates.UNKNOWN)) 
        self.letters.append(keyboardKey(    'T',     8,     1,      2,      KeyStates.UNKNOWN)) 
        self.letters.append(keyboardKey(    'Y',    10,     1,      2,      KeyStates.UNKNOWN)) 
        self.letters.append(keyboardKey(    'U',    12,     1,      2,      KeyStates.UNKNOWN)) 
        self.letters.append(keyboardKey(    'I',    14,     1,      2,      KeyStates.UNKNOWN)) 
        self.letters.append(keyboardKey(    'O',    16,     1,      2,      KeyStates.UNKNOWN)) 
        self.letters.append(keyboardKey(    'P',    18,     1,      2,      KeyStates.UNKNOWN)) 
        # Row 2                             Key,   Col,   Row,   Span,      State
        self.letters.append(keyboardKey(    'A',     1,     2,      2,      KeyStates.UNKNOWN)) 
        self.letters.append(keyboardKey(    'S',     3,     2,      2,      KeyStates.EXACT)) 
        self.letters.append(keyboardKey(    'D',     5,     2,      2,      KeyStates.UNKNOWN)) 
        self.letters.append(keyboardKey(    'F',     7,     2,      2,      KeyStates.UNKNOWN)) 
        self.letters.append(keyboardKey(    'G',     9,     2,      2,      KeyStates.UNKNOWN)) 
        self.letters.append(keyboardKey(    'H',    11,     2,      2,      KeyStates.CLOSE)) 
        self.letters.append(keyboardKey(    'J',    13,     2,      2,      KeyStates.UNKNOWN)) 
        self.letters.append(keyboardKey(    'K',    15,     2,      2,      KeyStates.UNKNOWN)) 
        self.letters.append(keyboardKey(    'L',    17,     2,      2,      KeyStates.UNKNOWN)) 
        # Row 3                             Key,   Col,   Row,   Span,      State
        self.letters.append(keyboardKey('ENTER',     0,     3,      3,      KeyStates.UNKNOWN)) # enter
        self.letters.append(keyboardKey(    'Z',     3,     3,      2,      KeyStates.UNKNOWN)) 
        self.letters.append(keyboardKey(    'X',     5,     3,      2,      KeyStates.UNKNOWN)) 
        self.letters.append(keyboardKey(    'C',     7,     3,      2,      KeyStates.UNKNOWN)) 
        self.letters.append(keyboardKey(    'V',     9,     3,      2,      KeyStates.UNKNOWN)) 
        self.letters.append(keyboardKey(    'B',    11,     3,      2,      KeyStates.UNKNOWN)) 
        self.letters.append(keyboardKey(    'N',    13,     3,      2,      KeyStates.UNKNOWN)) 
        self.letters.append(keyboardKey(    'M',    15,     3,      2,      KeyStates.UNKNOWN)) 
        self.letters.append(keyboardKey( 'Back',    17,     3,      3,      KeyStates.UNKNOWN)) #backspace
        for elem in self.letters:            
            bt = tk.Button(frame, \
                width=4 * elem.getSpan(), \
                bg = getbgColor(KeyStates.UNKNOWN), \
                fg = getfgColor(KeyStates.UNKNOWN), \
                text=elem.getKey(), \
                command=lambda lelem = elem: kpfunc(lelem))
            bt.grid(column=elem.getCol(), row = elem.getRow(), columnspan = elem.getSpan(), sticky="ew")     
            self.buttons[elem.getKey()] = bt

        #example of compositing use this for animated letters
        self. ta = testAnim(frame, 2, 0)
        '''
        img = Image.open('Assets/A.png').convert("RGBA")
        back = Image.open('Assets/Nope.png').convert("RGBA")
        c = Image.alpha_composite(back, img)
        #c.show()
        self.useme = ImageTk.PhotoImage(c)        # must keep a reference...wierd
        bt = tk.Button(frame, bd = 0, image=self.useme)
        #bt = tk.Button(frame, image=self.useme)
        bt.grid(column = 0, row = 2, ipadx = 0, ipady = 0)  
        '''
