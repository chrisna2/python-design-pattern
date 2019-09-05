
'''
[옵져버 패턴의 메서드]
+ 풀 (pull)모델 
    -> Subject는 변경사항이 있음을 등록된 Observer에 브로드캐스팅한다.
    -> Observer는 직접 게시자에게 변경사항을 요청하고 끌어와야 한다.
    -> 풀(pull) 모델은 Subject가 Observer에 알리는 단게와 
       Observer가 Subject로 부터 필요한 데이터를 받아오는 두 단계가 필요하므로 비효율적이다.
+ 푸쉬(push)모델
    -> 풀 모델과는 달리 Subject가 Observer에 데이터를 보낸다.
    -> Subject는 Observer가 필요로 하지 않는 데이터까지 보낼수 있다.
    -> 따라서 쓸데없이 많은 양의 데이터를 전송해 응답시간이 늦어질 수 있다.
    -> 성능을 위해 Subject는 오직 필요한 데이터만 보내야 된다.

[느슨한 결합 : 싱호작용하는 객체간의 관계를 최대한 느슨하게 구성하는 것이 목적, 독립적]
@효과
1> 한 부분에 대한 수정이 예기치 않게 다른 부분까지 영향을 끼치는 위험을 줄인다.
2> 테스트와 유지 보수 및 장애 처리가 쉽다.
3> 시스템을 쉽게 여러 부분으로 분리할 수 있다.
@옵저버패턴_느슨한결합
1> Subject는 정확히 Observer가 어떤 인터페이스를 구현하는지 모름
2> 언제든지 새로운 Observer를 추가할 수 있다.
3> 새로운 Observer를 추가해도 Subject는 수정할 필요가 없다.아래에 적용하는 예제에서
   Subject를 수정하지 않고도 AnyOtherObserver를 추가/제거 할 수 있다.
4> Subject 또는 Observer는 독립적이다.
   Observer는 필요시 어디에서도 사용이 가능하다.
5> Subject 또는 Observer에 대한 수정이 서로에게 아무런 영향을 주지않는다. 완전 독립성 또는 느슨한 결합 덕분애 걱정없이 수정이 가능하다.

[옵저버 패턴의 장단점]
@장점
1> 객체 간의 느슨한 결합 원칙을 따른다.
2> Subject 또는 Observer 클래스를 수정하지 않고 객체 간 자유롭게 데이터를 주고 받을 수 있다.
3> 새로운 Observer를 언제든지 추가 할 수 있다.
@단점
1> ConcreteObserver는 상속을 통해  Observer 인터페이스를 구현한다. 컴포지션에 대한 선택권이 없다.
2> 제대로 구현되지 않은 Observer클래스는 복잡도를 높이고 성능저하의 원인이 될수 있다.
3> 애플리케이션에서 알림(Notification)기능은 간혹 신뢰할 수 없으며 레이스 상태(Race Condition) 또는 비일관성을 초래 할 수 있다.
'''
from abc import ABCMeta, abstractmethod

## Subject 클래스 : Subject는 Observer를 관리한다. ##
class NewsPublisher:
    
    def __init__(self): #생성자
        self.__subscribers = []
        self.__latestNews = None 
        
    def attach(self,subscriber): # attach() 메소드를 호출해 자신(subscriber)을 등록한다.
        self.__subscribers.append(subscriber)
        
    def detach(self): # detach() 메소드를 호출해 자신(subscriber)을 등록을 취소한다.
        return self.__subscribers.pop()
    
    def subscribers(self):
        return [type(x).__name__ for x in self.__subscribers]
    
    def notifySubscribers(self):
        for sub in self.__subscribers:
            sub.update()
            
    def addNews(self, news):    # 새로운 뉴스 등록
        self.__latestNews = news
        
    def getNews(self):
        return "Got News:", self.__latestNews
    
## Observer : Subject를 감시하는 객체를 위한 인터페이스를 제공한다. ## 
## -> Subject의 상태를 알 수 있도록 ConcreteObserver가 구현해야 하는 메소드를 정의한다. ##    
class Subscriber(metaclass=ABCMeta):    # 모든 ConcreteObserver의 추상 기본 클래스다.
    @abstractmethod
    def update(self):   # ConcreteObserver는 update()를 구현해 Subject(Newspublisher)로 부터 새로운 뉴스 알림을 받는다.
        pass
  
## ConcreteObserver 클래스 ##    
'''
1) EmailSubscriber와 SMSSubscriber는 Subject의 인터페이스를 구현하는 옵저버다.
2) AnyOtherSubscriber는 Observer와 Subject의 느슨한 관계를 나타내는 또 다른 옵져버다.
3) 각 ConcreteObserver의 __init__()메소드는 attach()메소드를 통해 자신을 NewsPublisher에 등록한다.
4) NewsPublisher는 내부적으로 ConcreteObserver의 update()메소드를 호출해 새로운 뉴스를 알린다.
'''
#1) EmailSubscriber와 SMSSubscriber는 Subject의 인터페이스를 구현하는 옵저버다.
class SMSSubscriber:
    def __init__(self, publisher):
        self.publisher = publisher
        # 3) 각 ConcreteObserver의 __init__()메소드는 attach()메소드를 통해 자신을 NewsPublisher에 등록한다.
        self.publisher.attach(self)
    
    # 4) NewsPublisher는 내부적으로 ConcreteObserver의 update()메소드를 호출해 새로운 뉴스를 알린다. 
    def update(self):
        print(type(self).__name__, self.publisher.getNews())
        
#1) EmailSubscriber와 SMSSubscriber는 Subject의 인터페이스를 구현하는 옵저버다.    
class EmailSubscriber:
    def __init__(self, publisher):
        self.publisher = publisher
        # 3) 각 ConcreteObserver의 __init__()메소드는 attach()메소드를 통해 자신을 NewsPublisher에 등록한다.
        self.publisher.attach(self)

    # 4) NewsPublisher는 내부적으로 ConcreteObserver의 update()메소드를 호출해 새로운 뉴스를 알린다.         
    def update(self):
        print(type(self).__name__, self.publisher.getNews())
        
# 2) AnyOtherSubscriber는 Observer와 Subject의 느슨한 관계를 나타내는 또 다른 옵져버다. 이런 식으로 여러개의 옵저버를 추가 할 수 있다.
class AnyOtherSubscriber:
    def __init__(self,publisher):
        self.publisher = publisher
        # 3) 각 ConcreteObserver의 __init__()메소드는 attach()메소드를 통해 자신을 NewsPublisher에 등록한다.
        self.publisher.attach(self)
    
    # 4) NewsPublisher는 내부적으로 ConcreteObserver의 update()메소드를 호출해 새로운 뉴스를 알린다.         
    def update(self):
        print(type(self).__name__, self.publisher.getNews())
        
## Subject와 Observer의 상호 작용 구현한 코드 ##    
if __name__ == '__main__':
    
    # subject클래스는 딱 한번만 호출되어야 함! -> 생성자에서 기본 변수 초기화!
    news_publisher = NewsPublisher()
    
    # (명심!) Subscribers는 그냥 배열에 나열된 클래스를 담을 그릇에 불과하다. 
    for Subscribers in [SMSSubscriber, EmailSubscriber, AnyOtherSubscriber]:
        '''
        for문을 돌 경우 (3회전)
            1) SMSSubscriber(news_publisher)
            2) EmailSubscriber(news_publisher)
            3) AnyOtherSubscriber(news_publisher) -> NewsPublisher클래스를 상속받는 각각의  ConcreteObserver클래스 호출
        '''
        Subscribers(news_publisher) # 생성자 -> ConcreteObserver 자동등록!
    
    print("\nSubscribers:",news_publisher.subscribers())
    
    news_publisher.addNews("Hello World! My first news!")
    news_publisher.notifySubscribers() ## 뉴스 전파!
    
    print("\nDetached:",type(news_publisher.detach()).__name__) ## 구독자 1명 제거 pop
    print("\nSubscribers:",news_publisher.subscribers())
    
    news_publisher.addNews("My Second news!")
    news_publisher.notifySubscribers() ## 뉴스 전파!
    
    AnyOtherSubscriber(news_publisher) # 생성자 -> ConcreteObserver 자동등록!
    print("\nAttached:",AnyOtherSubscriber.__name__) ## 구독자 1명 
    print("\nSubscribers:",news_publisher.subscribers())
    
    news_publisher.addNews("My Third news!")
    news_publisher.notifySubscribers() ## 뉴스 전파!
    
