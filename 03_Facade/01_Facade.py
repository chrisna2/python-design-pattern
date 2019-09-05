'''
구조 디자인 패턴 
-------------
1) 파사드 패턴 
    -> 복잡한 내부 시스템 로직을 감추고 클라이언트다 쉽게 시스템에 접근할 수 있는 인터패이스 제공

2) 퍼사드 디자인 패턴의 목적
    1> 서브시스템의 인터페이스를 통합시킨 단일 인터페이스를 제공해 클라이언트가 쉽게 서브시스템에 접근랗 수 있게 한다.
    2> 단일 인터페이스 객체로 복잡한 서브시스템을 대체 한다. 서브시스템을 캡슐화하는 것이 아니라 모든 서브시스템을 결합한다.
    3> 클라이언트와 내부 구현을 분리한다.
    4> 클라이언트와 서브시스템을 분리하는 역활도 수행

3) 퍼사드 디자인 패턴의 3개 구조
    1> 퍼사드(facade) : 외부에서 보기에 깔끔하도록 복잡한 서브시스템을 감싸는 역활을 한다.
        -> 어떤 서브시스템이 요청에 알맞는지 알고 있는 인터페이스다.
        -> 컴포지션을 통해 클라이언트의 요청을  적합한 서브 시스템 객체에 전달한다.
    2> 시스템(system) : 전체 시스템을 하나의 복잡한 복합체로 만드는 여러 서브시스템의 집합
        -> 서브시스템의 기능을 구현하는 클래스다. 이상적으로 시스템은 각기 다른 역활을 하는 클래스의 집합
        -> 퍼사드 객체가 지시한 이름을 담당하지만 퍼사드의 존재도 모르며 참조하지도 않음
    3> 클라이언트(client) : 퍼사드를 통해 서브시스템과 통신한다. 복잡한 시스템 구조에 대해 전혀 알 필요없다.
        -> 클라이언트는 퍼사드를 인스턴스화하는 클래스
        -> 퍼사드에서 서브시스템을 통해 작업을 수행하도록 요청
'''


## 퍼사드 부분 : 외부에서 보기에 깔끔하도록 복잡한 서브시스템을 감싸는 역활 => 웨딩플래너
class EventManager(object):
    # EventManager는 You 클래스를 위해 인터페이스를 간소화 해주는 퍼사드
    # EventManager는 컴포지션을 통해 Hotelier와 Florist둥울 서브시스템 객체를 생성함
    def __init__(self):
        print("Event Manager :: Let me talk to the folk\n")

    def arrange(self):
        self.hotelier = Hotelier()
        self.hotelier.bookHotel()

        self.florist = Florist()
        self.florist.setFlowerRequirements()

        self.caterer = Caterer()
        self.caterer.setCuisine()

        self.musician = Musician()
        self.musician.setMusicType()


## 서브시스템 부분 : 전체 시스템을 하나의 복잡한 복합체로 만드는 여러 서브시스템의 집합 => 호텔리어, 플로어리스트, 음식공급자, 뮤지션
class Hotelier(object):
    def __init__(self):
        print("Arranging the Hotel for Marriage? --")

    def __isAvailable(self):
        print("Is the Hotel free for the event on given day?")

    def bookHotel(self):
        print("Registered the Booking\n\n")


class Florist(object):
    def __init__(self):
        print("Flower Decorations for the Event? --")

    def setFlowerRequirements(self):
        print("Carnations, Roses and Lilies would be used for Decorations\n\n")


class Caterer(object):
    def __init__(self):
        print("Food Arrangements for the Event --")

    def setCuisine(self):
        print("Chinese & Continental Cuisine to be served\n\n")


class Musician(object):
    def __init__(self):
        print("Musical Arrangements for the Marriage --")

    def setMusicType(self):
        print("Jazz and Classical will be played\n\n")

    ## 클라이언트 부분 : 퍼사드를 통해 서브시스템과 통신한다. 복잡한 시스템 구조에 대해 전혀 알 필요없다. => 결혼을 앞둔 사용자


class You(object):
    def __init__(self):
        print("YOU:: Whoa! Marriage Arrangement?!!")

    def askEventManager(self):
        print("YOU:: Let's Contact the Event Manger\n\n")
        em = EventManager()
        em.arrange()

    def __del__(self):  ## 소멸자 : 객체가 소멸될때 자동으로 실행되는 함수
        print("YOU:: Thanks to Event Manager, all preparations done! phew!")


if __name__ == '__main__':
    you = You()  ## 자바에서는  You you = new You()
    you.askEventManager()  ## 이거 하나만 수행하면 처리 완료.

'''
최소 지식의 원칙 (== 데메테르 법칙, 느슨한 결합을 원칙)
-----------------------------------------------------------------
+ 시스템을 설계할 때 생성하는 모든 객체가 몇개의 클래스와 연관되며 어떤식으로 대화하는지 알아야 한다.
+ 원칙에 따라 지나치게 서로 얽혀있는 클래스를 만드는 것을 지양해야 한다.
+ 클래스 간의 의존도가 높아질수록 시스템의 유지 보수가 힘들어진다. 
    시스템의 한 부분을 수정하면 다른 부분이 의도치 않게 변경될 수 있다.
    이런 회귀적인 구조는 피해야 한다.
-----------------------------------------------------------------
데메테르 법칙
-----------------------------------------------------------------
1> 각 유닛은 시스탬 내의 다른 유닛에 대해 최소한의 지식만을 가져야 한다.
2> 유닛은 주변의 친구와만 대화를 해야한다.
3> 유닛은 자신이 다루는 객체의 세부사항에 대해 알 필요가 없다.
'''
