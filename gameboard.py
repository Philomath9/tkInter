import tkinter as tk
from tkinter import ttk
from gamelogic import *
from states import *

class wordGuess:
    def __init__(self):
        self.word = ""
        self.state = []
        self.labels = []
        self.resetWord()
        
    def getWord(self):
        return self.word

    def resetWord(self):
        self.word = ""
        self.state.clear()        
        for i in range(5):            
            self.state.append(colorKeyStates.UNKNOWN)       

    def addChar(self, char):
        self.word += char
        if(len(self.word)>5):
            self.word = self.word[0:5]

    def delChar(self):
        if(len(self.word)>0):
            self.word = self.word[0:len(self.word)-1]

    def createWord(self, frame, row):        
        for idx in range(5):  
            lb = tk.Label(frame,text ="", width = 8, height = 2, borderwidth = 3, relief="raised", \
                fg = getfgColor(self.state[idx]), bg = getbgColor(self.state[idx]))
            lb.grid(column = 4 + idx*2, row = row+1, columnspan = 2)  
            self.labels.append(lb)              

    def updateWord(self):
        wlen = len(self.word) 
        for idx in range(5):
            if idx < wlen: 
                self.labels[idx].configure(text = self.word[idx], bg=getbgColor(self.state[idx]), fg=getfgColor(self.state[idx]))
            else:
                self.labels[idx].configure(text = "", bg=getbgColor(self.state[idx]), fg=getfgColor(self.state[idx]))

class gameBoard:  
    def __init__(self):
        self.letterStates = {} # does not exist = unknown
        self.currentState = gameState()
        self.words = []
        for idx in range(6):
            self.words.append(wordGuess())  
        self.winword = getNewWord()  
    def createGameboard(self, frame):            
        for guessNum in range(6):
            self.words[guessNum].createWord(frame, guessNum)
        sep = ttk.Separator(frame,orient='horizontal').grid(column = 0,row=7, columnspan = 20, sticky="ew")
    def getState(self):
        return self.currentState.getState()
    def addChar(self, char):        
        self.words[self.currentState.getWordGuess()].addChar(char)     
        self.words[self.currentState.getWordGuess()].updateWord()   
    def delChar(self):
        self.words[self.currentState.getWordGuess()].delChar()
        self.words[self.currentState.getWordGuess()].updateWord()   
    def resetBoard(self):
        for idx in range(6):
            self.words[idx].resetWord()
        self.currentState.resetState()
        self.letterStates.clear()
        self.winword = getNewWord()  # get new word
        for i in range(6):
            self.words[i].updateWord() 
    def updateLetterDictionary(self, letter, state):
        if letter in self.letterStates:
            old = self.letterStates[letter]
            if old == colorKeyStates.NOT:
                self.letterStates[letter] = state
            elif state == colorKeyStates.EXACT:
                self.letterStates[letter] = state
            elif not (old == colorKeyStates.EXACT):
                self.letterStates[letter] = state
        else:
            self.letterStates[letter] = state

    def enterButton(self):
        wordobj = self.words[self.currentState.getWordGuess()]
        gword = wordobj.getWord()
        lgwlen = len(gword)
        if not(lgwlen == 5):
            return False
        for idx in range(5):
            if self.winword[idx] == gword[idx]:
                wordobj.state[idx] = colorKeyStates.EXACT
                self.updateLetterDictionary(gword[idx], colorKeyStates.EXACT)                
            else:
                found = False                
                for CH in self.winword:                    
                    if CH == gword[idx]:
                        wordobj.state[idx] = colorKeyStates.CLOSE                        
                        self.updateLetterDictionary(gword[idx], colorKeyStates.CLOSE)
                        found = True
                        break
                if not found:
                    wordobj.state[idx] = colorKeyStates.NOT
                    self.updateLetterDictionary(gword[idx], colorKeyStates.NOT)
        wordobj.updateWord()
        if gword == self.winword:
            self.currentState.changeState(gameStates.WINNER)
        else:
            if self.currentState.getWordGuess() == 5:
                self.currentState.changeState(gameStates.LOOSER)
            else:
                self.currentState.nextGuess()
        return True
        
    def getKeyStates(self):
        #return key value dictionary of key and state
        return self.letterStates        
