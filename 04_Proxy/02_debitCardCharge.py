
'''
'''
from _py_abc import ABCMeta
from abc import abstractmethod

### 클라이언트 클래스 : 작업을 수행하기 위해 Proxy클래스에 접근한다.###
class You: 
    def __init__(self): # 생성자 -> 프록시를 호출하고  생성
        print("You:: Lets buy the Denim shirt")
        self.debitCard = DebitCard()
        self.isPurchased = None
        
    def make_payment(self):
        self.isPurchased = self.debitCard.do_pay()
        
    def __del__(self):
        if self.isPurchased:
            print("You:: Wow! Denim shirt is mine :-) ")
        else:
            print("You:: I should earn more :-( ")

### Subject 클래스 : Proxy와 RealSubject를 정의하는 인터페이스 ###
class Payment(metaclass=ABCMeta):   # 추상 기본 클래스이며 인터페이스
    # proxy와 realsubjet가 구현해야할 do_pay() 메서드를 정의
    @abstractmethod
    def do_pay(self):
        pass
    
### RealSubject 클래스 : Subject의 실 구현체다. 클라이언트가 사용할 기능을 제공한다.###
class Bank(Payment): # payment 상속
    
    def __init__(self):
        self.card = None
        self.account = None
        
    def __getAccount(self):
        self.account = self.card # 카드 번호와 계좌 번호는 같다고 가정
        return self.account
        
    def __hasFunds(self):
        tmpAcnt = self.__getAccount()
        if "123123".__eq__(tmpAcnt):
            print("Bank:: Checking if Account", tmpAcnt, "has enough funds")
            return True
        else:
            print("Bank:: Checking if Account", tmpAcnt, "has not enough funds")
            return False              

    def setCard(self, card):
        self.card = card
    
    def do_pay(self):
        if self.__hasFunds():
            print("Bank:: paying the merchant")
            return True
        else:
            print("Bank:: Sorry, not enough funds!")
            return False
        
### Proxy 클래스 : Realsubject 클래스의 접근을 제어하는 클래스다. 크라이언트의 요청을 처리하고 Realsubject를 생성 및 소멸한다. (프록시는 Realsubject를 대체 할 수 있다.)###
# DebitCard 클래스는 RealSubject인 Bank의 대리 객체다.
class DebitCard(Payment): # payment 상속
    def __init__(self):
        self.bank = Bank()
    
    def do_pay(self):
        card = input("Proxy:: punch in card Number: ")
        self.bank.setCard(card)
        return self.bank.do_pay()

## 메인 구현부 ##     
if __name__ == '__main__':
    you = You()
    you.make_payment()
    
"""
프록시 패턴의 종류

1)가상 프록시 : 인스턴스화 하기에는 무거운 객체의 플레이스 홀더 역활을 수행 , 클라이언트가 객체를 처음 요청하거나 접근했을때 실객체를 생성
    ex> 웹사이트에서 큰이미지를 불러와야 하는 경우 이미지가 있는 아이콘으로 대채하고 클릭시 이미지를 로드

2)원격 프록시 : 원격 서버나 다른 주소 공간에 존재하는 객체에 대한 로컬 인스턴스를 생성한다.
    ex> 다수의 웹서버와 데이터베이스서버, 작업서버, 캐시서버 등으로 구성된 애플리케이션 모니터링 시스템을 구현
        -> 각 서버의 CPU와 디스크 사용량을 모니터링하려면 모니터링 서버에서 각 서버의 실제 사용량 수치를 얻는 원격 명령을 수행 필요
            -> 이 경우 원격 개체를 로컬에서 제어할 수 있는 원격 프록시 객체를 생성하면 유용하다.

3)보호 프록시 : RealSubject의 중요한 부분에 대한 접근을 제어
    ex> 사용자의 인증과 허가를 담당라는 인증 서비스를 제공
    
4)스마트 프록시 : 사용자가 객체에 접근하였을 때 추가적인 행동을 취하는 프록시
    ex> 상태를 중앙 서버에 저장하는 핵심 기능이 있는 서비스
        -> 시스템 내의 여라 서비스가 동시에 이 기능을 호출하는 바람에 리소스 공유에 문제가 발생
            -> 이 경우 각 서비스가 이 기능을 직접 호출하는 대신 스마트 프록시가 객체의 잠금 상태를 확인 하는 기능을 추가로 수행해 접근을 제어

[구조 패턴]
프록시 vs 퍼사드
*프록시 패턴
1) 실 객체의 대리 객체를 제동해 접근을 제어한다.
2) 타겟 객체가 동일한 인터페이스 구조를 가지며 타겟에 대한 참조를 가지고 있다.
3) 클라이언트와 감싸고 있는 객체 사이에 중재자 역활읗 수행한다.
*퍼사드 패턴
1) 클래스의 서브시스템에 대한 인터페이스를 제공한다.
2) 서브시스템 간의 의존도와 통신을 최소화한다.
3) 퍼사드 객체는 하나의 통합된 간단한 인터페이스를 제공한다.

프록시 패턴의 단점
-> 프록시 패턴으로 인해서 응답시간이 늘어날 수 있다. 
-> 프록시가 제대로 설계되지 않았다면 realSubject의 응답 시간에 영향을 줄 수 있다.
-> 즉, 성능에 문제가 없게 프록시를 구현해야 한다.

"""    

    
