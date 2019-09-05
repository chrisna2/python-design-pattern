
'''
생성패턴
    -> Singleton
        -> 생성 패턴에서는 객체가 생성되는 방식이 중요하다. 
        -> 객체가 생성되는 세부 과정은 숨기고 생성하려면 생성하려는 객체 형과 독립적인 구조를 지원한다.
구조패턴
    -> Facade, Proxy
        -> 구조 패턴은 객체와 클래스를  합쳐 더 큰 기능을 구현한다.
        -> 구조를 간소화하고 클래스와 객체사이의 관계를 찾는 것이 주목적
행위패턴
    -> Observer
        -> 객체의 역황(행위)에 초점을 둠
        -> 더 큰 기능을 구현하기 위한 객체 간의 상호 작용을 중요시
        -> 행동 패턴에서 객체는 상호작용하지만 느슨하게 결합됨  a.k.a "느슨한 결합"
        
[옵저버 패턴]        
@목적 
1> 객체 간 일대다(1:N) 관계를 형성하고 객체의 상태를 다른 종속 객체에 자동으로 알린다.
2> 서브젝트의 핵심 부분을 캡슣화 한다.
@적합활용도 
1> 분산시스템의 이벤트 서비스를 구현할 때
2> 뉴스 에이전시 프레임워크
3> 주식 시장 모델
'''
## 1. Subject 클래스 ##
class Subject:
    def __init__(self):
        self.__observers = []
    
    def register(self, observer):
        self.__observers.append(observer)
    
    def notifyAll(self, *args, **kwargs):
        for observer in self.__observers:
            observer.notify(self,*args,**kwargs)
            
## 2. Observer 클래스 ##           
class Observer1:
    def __init__(self,subject):
        subject.register(self)

    def notify(self,subject,*args):
        print(type(self).__name__,':: GOT',args,'From',subject)

class Observer2:
    def __init__(self,subject):
        subject.register(self)
        
    def notify(self,subject,*args):
        print(type(self).__name__,':: GOT',args,'From',subject)

class Observer3:
    def __init__(self,subject):
        subject.register(self)
        
    def notify(self,subject,*args):
        print(type(self).__name__,':: GOT',args,'From',subject)
        
 
if __name__ == '__main__':
    # 서브젝트 객체 호출 -> 생성자로 해당 배열 초기화
    subject = Subject()
    
    observer1 = Observer1(subject)#상속 형태로 클래스를 호출하게 되면 생성자에서 해당 클래스를 등록 1
    observer2 = Observer2(subject)#상속 형태로 클래스를 호출하게 되면 생성자에서 해당 클래스를 등록 2
    observer3 = Observer3(subject)#상속 형태로 클래스를 호출하게 되면 생성자에서 해당 클래스를 등록 3
    
    # 서브젝트에 옵저버가 등록이 된 경우 
    subject.notifyAll('notification','1> java is doomed','2> python is king','3> goodbye oracle!')
