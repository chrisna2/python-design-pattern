
'''
커맨드 디자인 패턴
-> 커맨드 패턴은 객체가 특정 기능을 바로 수행 하거나 나중에 트리거할 때 필요한 모든 정보를 캡슐화하는 행동 패턴이다.
-> 캡슐화 하는 정보는 [메소드명/메소드를 소유하는 객체/메소드 인자]
-> Command 객체를 통해 실행 후 사용자가 단계별로 선택한 설정을 Command 객체에 저장 후 excute()를 실행하여 설치 함수 실행

커맨드 패턴 구성요소 : Command와 Receiver,Invoker,Client 클래스로 구성된다.
-> Command 객체는 Receiver 객체에 대해 알고 있으며 Receiver객체의 함수를 호출한다.
-> Receiver 함수의 인자는 Command 객체에 저장되어있다.
-> Invoker는 명령을 수행한다.
-> Client는 Command 객체를 생성하고 Receiver를 정한다.

커맨드 패턴의 목적
-> 요청을 객체 속에 캡슐화 한다.
-> 클라이언트의 다양한 요청을 매개변수화 한다.
-> 요청을 큐에 저장한다.
-> 객체지향 콜백을 지원한다.

커맨드 패턴의 적합 사용처
-> 수행할 명령에 따라 객체를 변수화 할 때
-> 요청을 큐에 저장하고 각기 다른 시점에 수행을 해야 하는 경우
-> 작은 단위의 연산을 기반으로 하는 상위 연산을 만들때

'''

## 인스톨 위자드
class Wizard():
    def __init__(self, src, rootdir):
        self.choices = []
        self.rootdir = rootdir
        self.src = src
        
    def preferences(self, command):
        self.choices.append(command)
        
    def execute(self):
        for choice in self.choices:
            if list(choice.values())[0]:
                print("Copying binaries --", self.src, " to ", self.rootdir)
            else:
                print("No Operation")
    
if __name__ == '__main__':
    ## 클라이언트 코드
    wizard = Wizard('python3.5.gzip', '/usr/bin/')
    ## 사용자는 파이썬을 선택 (헸다고 가정) -> 각 단계에서 사용자가 선택한 정보를 저장한다.
    wizard.preferences({'python':True})
    wizard.preferences({'java':False})
    
    print(wizard.choices) ## 상위 커맨드 클래스 인자에 저장됨
    
    wizard.execute() ## 메소드는 저장된 설정을 불러오고 설치를 진행 한다.
