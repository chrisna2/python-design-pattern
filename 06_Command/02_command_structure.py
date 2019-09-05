
'''
Created on 2019. 3. 25.

@author: TY
'''
from abc import ABCMeta, abstractmethod

## Command : 연산을 수행할 인터패이스를 정의한다
class Command(metaclass=ABCMeta):
    def __init__(self, recv):
        self.recv = recv
        
    def execute(self):
        pass
    
## ConcreteCommand : Receiver 객체와 연산 간 바인딩을 정의한다.
class ConcreteCommand(Command):
    def __init__(self, recv):
        self.recv = recv
        
    def execute(self):
        self.recv.action()
        
## Receiver : 요청에 관련된 연산을 관리한다
class Receiver:
    def action(self):
        print("Receiver Action")

## Invoker : ConcreteCommand에 수행을 요청한다.
class Invoker:
    def command(self, cmd):
        self.cmd = cmd
    
    def execute(self):
        self.cmd.execute()

## 클라이언트 실행부
if __name__=='__main__':
    recv = Receiver()
    cmd = ConcreteCommand(recv)
    invoker = Invoker()
    invoker.command(cmd)
    invoker.execute()
    
    
