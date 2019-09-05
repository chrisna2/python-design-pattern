
'''
Created on 2019. 3. 26.

@author: TY
'''
# State 인터페이스  : Handle() 추상 메소드를 정의하는 인터페이스다. 이 메소드는 ConcreteState가 구현한다.
class ComputerState(object):
    name = "state"
    allowed = []
    
    # Handle() 메소드 : 객체(컴퓨터)의 상태를 변경하는 switch()메소드를 정의한다.
    def switch(self, state):
        if state.name in self.allowed:
            print("Current:",self," => switched to new state", state.name)
            self.__class__ = state ## ??? -> 단순하다. 말 그대로 현재에  State 클래스 자리에 하위 ConcreteState class 에 정해진 형태 그대로 입력하는 것
            ## 잘보면 알겠지만 하위 ConcreteState는 클래스에 변수만 선언 되었지 매서드로 입력된 것이 없다. name / allowed 변수만 병경 된다.
        else:
            print("Current:",self," => switching to",state.name,'not Possible.')

    
    def __str__(self):
        return self.name

# ConcreteState 클래스 : State 설정에 따라 실행될 각자의 Handle()가 구현된다.
# 여기선 State 인터페이스에서 정의된 switch()메소드가 실행된다. ConcreteState는 인자의 값만 변경함
# 상속 받았기 때문에 굳이 구현 하지 않아도 실행된다...알지?
class Off(ComputerState):
    name = "off"
    allowed = ["on"]

class On(ComputerState):
    name = "on"
    allowed = ["off","suspend","hibernate"]

class Suspend(ComputerState):
    name = "suspend"
    allowed = ["on","off"]
    
class Hibernate(ComputerState):
    name = "hibernate"
    allowed = ["on","off"]
    
# Context 클래스 : 사용자(client)의 요청을 넘겨받는 클래스다. 객체의 현재 상태를 저장하고 요청에 맞는 메소드를 호출한다.
class Computer(object):
    # 객체의 기본상태를 정의하는 메소드    
    def __init__(self,model='HP'):
        self.model = model
        self.state = Off()
    # 객체의 상태를 변경한다. 실제 상태 변경 로직은 ConcreteState(on,off,suspend,hibernate)가 구현한다.
    def change(self, state):
        self.state.switch(state)
        
# client 구현부 ..    
if __name__ == '__main__':
    
    comp = Computer()
    
    #전원을 켠다.
    comp.change(On)
    #전원을 끈다.
    comp.change(Off)
    #전원을 다시켠다.
    comp.change(On)
    #일시 중지
    comp.change(Suspend)
    #절전모드로 변경 불가능
    comp.change(Hibernate)
    #전원을 다시 켠다.
    comp.change(On)
    #절전모드로 변경 가능
    comp.change(Hibernate)
    #전원을  끈다.
    comp.change(Off)
    #전원을 다시 켠다.
    comp.change(On)
    #컴퓨터 상태를 초기화 한다.
    comp.__init__()
    print("초기화  :",comp.state.__str__(),"/",comp.state.allowed)
    
'''
[상태 디자인 패턴의 장단점]
@장점
- 상태 패턴에서 객체의 행위는 해당 상태의 살행 함수의 결과 값과 같다. 행위는 상태에 따라 런타임이 변경된다.
이런 구조는 if/else와 switch/case등의 조건부 연산자를 줄일수 있다. 앞서 다룬 TV리모컨 예제는 주어진 인자에 
따라 TV전원을 켜고 끄는 if/esle로 이뤄진 메소드 하나로도 구현이 가능하다.
- 다형성 구현이 쉬우면 새로운 상태를 쉽게 추가 할 수 있다.
- 상태 관련 행위가 모두 ConcreteState 클래스에 있으므로 응집도가 높아진다.
- 새로운 ConcreteState클래스를 추가해 쉽게 신규 기능을 추가할 수 있다.
- 코드의 유연성이 높아지고 유지 보수가 쉽다.

@단점
- 클래스 남발이 나타난다. 모두 상태를 ConcreteState클래스로 정의하면 쓸데없는 클래스가 많아진다.
- 세로운 행위는 ConcreteState를 새로 추가하면 되지만 Context 클래스도 맞게 수정해야 한다.
- 따라서 Context는 행위가 추가될 때 마다 취약해진다.



'''
    
    
