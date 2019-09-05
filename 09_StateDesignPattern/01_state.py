'''
상태디자인 패턴  -> AM/FM라디오 변경 스위치

@구조
1> State : 객체의 행위를 캡슐화하는 인터페이스다. 행위는 객체의 상태에 따라 변한다.
2> ConcreteState : State인터페이스를 구현하는 서브클래스다. 특정 상태의 객체의 행위를 구현한다.
3> Context : 사용자가 선택한 인터페이스 정의한다. 특정 상태의 객체를 구현한 ConcreteState 서브클래스의 인스턴스를 가지고 있다.

'''
from abc import ABCMeta, abstractmethod

class State(metaclass=ABCMeta):
    @abstractmethod
    def Handle(self):
        pass
    
class ConcreteStateB(State):
    def Handle(self):
        print("ConcreteStateB")
        
class ConcreteStateA(State):
    def Handle(self):
        print("ConcreteStateA")
        
class Context(State):
    def __init__(self):
        self.state = None
        
    def getState(self):
        return self.state
    
    def setState(self, state):
        self.state = state
        
    def Handle(self):
        self.state.Handle()
        
if __name__ == '__main__':
    context = Context()
    
    stateA = ConcreteStateA()
    stateB = ConcreteStateB()
    
    # 상태를 설정 -> stateA
    context.setState(stateA)
    context.Handle()
