'''
Created on 2019. 3. 26.

@author: TY
'''
from abc import ABCMeta, abstractclassmethod

class State(metaclass=ABCMeta):
    @abstractclassmethod
    def doThis(self):
        pass
    
class StartState(State):
    def doThis(self):
        print("TV Switching ON...")
    
    
class StopState(State):
    def doThis(self):
        print("TV Switching OFF...")
 
## 약간 DTO 비슷한 것 같은데?       
class TVContext(State):
    def __init__(self):
        self.state = None
        
    def getState(self):
        return self.state
    
    def setState(self, state):
        self.state = state
        
    def doThis(self):
        self.state.doThis()
        
if __name__ == '__main__':
    context = TVContext()
    context.getState()
    
    start = StartState()
    stop = StopState()
    
    context.setState(stop)
    context.doThis()
