class GameStates:
    WORDPICK = 0
    WINNER   = 1
    LOOSER   = 2

class KeyStates:
    UNKNOWN = 0
    EXACT   = 1
    CLOSE   = 2 # used for keyboard or gamestate
    NOT     = 3
    LEFT    = 4
    RIGHT   = 5

class LengthState:
    EXACT = 0
    SHORTER = 1
    LONGER = 2

def getfgColor(state):
    if state == KeyStates.UNKNOWN:
        return "#ffffff"
    elif state == KeyStates.EXACT:
        return "#ffffff"
    elif state == KeyStates.NOT:
        return "#ffffff"
    else: # state == colorKeyStates.CLOSE:
        return "#ffffff"
def getbgColor(state):
    if state == KeyStates.UNKNOWN:
        return "#828385"
    elif state == KeyStates.EXACT:
        return "#528d4d"
    elif state == KeyStates.NOT:
        return "#3a3a3c"
    else: # state == colorKeyStates.CLOSE:
        return "#b59f3a"