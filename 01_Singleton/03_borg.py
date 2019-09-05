
'''
Created on 2019. 3. 19.

@author: TY
'''

''' 모노 스테이트 형태  1 : 초기화 함수를 이용하여 설정
'''
class Borg:
    __shared_state = {"1":"2"}
    
    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state
        pass

''' 모노 스테이트 형태  2 : __new__ 메소드를 이용하여 설정
class Borg(object):
    _shared_state = {}
    def __new__(cls,*args,**kwargs):
        obj = super(Borg, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj
'''
    
b = Borg()
b1 = Borg()
b.x = 4

print("Borg Object 'b': ", b) ## b와 b1은 메모리 주소가 서로 다른 객체다.
print("Borg Object 'b1': ", b1) ## b와 b1은 메모리 주소가 서로 다른 객체다.
print("Object State 'b': ", b.__dict__) ## 싱글톤 객체는 아니지만 서로의 상태를 공유 하는 상태를 모노스테이트 또는 보그 디자인 패턴이라고 한다.
print("Object State 'b1': ", b1.__dict__) 

''' 실행결과
Borg Object 'b':  <__main__.Borg object at 0x0000020FC65705F8>
Borg Object 'b1':  <__main__.Borg object at 0x0000020FC666D128>
Object State 'b':  {'1': '2', 'x': 4}
Object State 'b1':  {'1': '2', 'x': 4}
'''







