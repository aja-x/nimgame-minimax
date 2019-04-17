class Game:
    state = type(None)
    move = ""

    def __init__(self, state, move):
        self.state = state
        self.move = move
        if move == 1:
            self.move = 'human'
        else:
            self.move = 'agent'
    
    def getState(self):
        return self.state
    
    def setState(self, state):
        self.state = state

    def start():
        if move == 'human':
            humanMove()
        else:
            agentMove()
    
    def humanMove(self):
        showState()
        if isStateHasChild():
            try:
                print('Masukkan pilihan state\t: ')
                choice = input()
                choosenState = getState().getChildList().get(0)
                setState(choosenState)
                print(choosenState)
                agentMove()
            except:
                print('this is an error message')
        else:
            showWin('agent')

    def agentMove(self):
        showState()
        if isStateHasChild():
            try:
                choosenState = getState().getChildList().get(0)
                if(getState().getMinimax() > 0):
                    for childState in getState().getChildList():
                        if childState.getValue == 1:
                            choosenState = childState
                else:
                    for childState in getState().getChildList:
                        if childState.getValue() == 0:
                            choosenState = childState
                setState(choosenState)
                print(choosenState)
                humanMove()
            except:
                print('this is an error message')

    def showState(self):
        i = 1
        for state in getState().getChildList():
            print(i + '. ' + state)
            i = i + 1

    def isStateHasChild(self):
        if(self.state.getChildList().size() > 0):
            return True
        return False

    def showWin(self, winner):
        if winner == 'human':
            print('Congratulations! You Win')
        else:
            print('Sorry! You Lose!')
