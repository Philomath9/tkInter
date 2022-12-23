class gameStates:
    WORDPICK = 0
    WINNER   = 1
    LOOSER   = 2

class colorKeyStates:
    UNKNOWN = 0
    EXACT   = 1
    CLOSE   = 2
    NOT     = 3

def getfgColor(state):
    if state == colorKeyStates.UNKNOWN:
        return "#ffffff"
    elif state == colorKeyStates.EXACT:
        return "#ffffff"
    elif state == colorKeyStates.NOT:
        return "#ffffff"
    else: # state == colorKeyStates.CLOSE:
        return "#ffffff"
def getbgColor(state):
    if state == colorKeyStates.UNKNOWN:
        return "#828385"
    elif state == colorKeyStates.EXACT:
        return "#528d4d"
    elif state == colorKeyStates.NOT:
        return "#3a3a3c"
    else: # state == colorKeyStates.CLOSE:
        return "#b59f3a"