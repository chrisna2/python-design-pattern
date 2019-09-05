
'''
프록시 패턴 -> 배우와 소속사의 관계
프록시(proxy) -> 요청자와 공급자 사이에 중계자
ex) 클라이언트  <-> 프록시 서버  <-> 메인 서버

+ Proxy클래스는 객체의 인터페이스 역활을 수행 (반환해 사용할 실제 객체를 감싸는 포장지 또는 에이전트)
+ 프록시패턴의 주목적 : 실제 객체에 접근할 수 있는 대리 객체나 껍데기를 제공하는 것
+ 프록시 패턴의 역활
    1) 복잡한 시스템을 간단하게 표현할 수 있다. 
    2) 객체에 대한 보안을 제공
    3) 다른 서버에 존제하는 외부 객체에 대한 로컬 인터페이스 제공
    4) 메모리 사용량이 높은 객체를 다루는 기벼운 핸들러 역활을 함

'''

## 객체 클래스 
class Actor(object):
    def __init__(self):
        self.isBusy = False
    
    def occupied(self):
        self.isBusy = True
        print(type(self).__name__, "is occupied with current movie") #다른 영화 촬영중
        
    def available(self):
        self.isBusy = False
        print(type(self).__name__, "is free for the movie") #출연가능
    
    def getStatus(self):
        #self.isBusy = True
        return self.isBusy

## 프록시 클래스
class Agent(object):
    def __init__(self):
        self.principal = None
        
    def work(self):
        self.actor = Actor()
        if self.actor.getStatus():
            self.actor.occupied()
        else:
            self.actor.available()

## 메인 : 클라이언트 구현부 
if __name__ == '__main__':
    r = Agent()
    r.work()
    
"""
+ 특정 객체의 대리 객체를 제공해 접근을 제어
+ 분산 구조를 지원하기 위한 레이어 또는 인터페이스 제공
+ 의도하지 않은 케이스로부터 객체를 보호

"""
