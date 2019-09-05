
'''
추상 팩토리 패턴
-> 클래스를 직접호출하지 않고 관련된 객체를 생성하는 인터페이스를 제공


'''
from abc import ABCMeta, abstractmethod

## 1. AbstractFactory [최상위 인터페이스 : Interface] =========
class PizzaFactory(metaclass=ABCMeta):
    ## 추상 메서드 구성
    @abstractmethod
    def createVegPizza(self):
        pass
    ## 추상 메서드 구성
    @abstractmethod
    def createNonVegPizza(self):
        pass
    
## 2. ConcreteFactory [인터페이스 상속받음] ===============
class IndianPizzaFactory(PizzaFactory):
    ## 상위 인터페이스 메서드 구현
    def createVegPizza(self):
        return DeluxVeggiePizza()
    ## 상위 인터페이스 메서드 구현
    def createNonVegPizza(self):
        return ChickenPizza()
    
class USPizzaFactory(PizzaFactory):
    ## 상위 인터페이스 메서드 구현
    def createVegPizza(self):
        return MexicanVegPizza()
    ## 상위 인터페이스 메서드 구현
    def createNonVegPizza(self):
        return HamPizza()

## 3. AbstractProduct [상위의 product 클래스, 다른 ConcreteProduct에 상속됨, 관련된 객체의 집합] ======
class VegPizza(metaclass=ABCMeta):
    @abstractmethod
    def prepare(self, VegPizza):
        pass

class NonVegPizza(metaclass=ABCMeta):
    @abstractmethod
    def serve(self, VegPizza):
        pass

## 4. ConcreteProduct [AbstractProduct 상속받음] ========
class DeluxVeggiePizza(VegPizza): ## 어떤 AbstractProduct 클래스를 상속받는냐에 따라 제품을 구분함
    ## 상위 인터페이스 메서드 구현
    def prepare(self):
        print("Prepare", type(self).__name__)

class ChickenPizza(NonVegPizza): ## 어떤 AbstractProduct 클래스를 상속받는냐에 따라 제품을 구분함
    ## 상위 인터페이스 메서드 구현
    def serve(self, VegPizza):
        print(type(self).__name__, "is served with Chicken on ", type(VegPizza).__name__)    
        
class MexicanVegPizza(VegPizza):
    ## 상위 인터페이스 메서드 구현
    def prepare(self):
        print("Prepare ", type(self).__name__)
        
class HamPizza(NonVegPizza):
    ## 상위 인터페이스 메서드 구현
    def serve(self, VegPizza):
        print(type(self).__name__, "is served with Ham on ", type(VegPizza).__name__)  

### 클라이언트 섹션 부분 =======================
class PizzaStore:
    def __init__(self):
        pass
    
    def makePizza(self):
        '''
            'for in'
            for item in iterable
            + iterable : 반복가능한 객체
                -> collections.Iterable에 속한 instance면 모두 가능함
                
        for factory in [IndianPizzaFactory(), USPizzaFactory()]:
            ## 간단하게 말하면 그냥 배열이다. 배열안에 클래스가 있으니 클래스를 차례 차례 실행한 것이다.
            # print("현재 실행되는 클래스 메모리주소_",factory)
            ## for문은 2번 회전한 것임, 파이썬은 이게 된다. 자바는 어떻게 될지 모르겠네..   
            
            # 클래스 객체 MOVE
            self.factory = factory
            # 그냥피자 객체 생성 후 MOVE
            self.NonVegPizza = self.factory.createNonVegPizza()
            # 야채피자 객체 생성 후 MOVE
            self.VegPizza = self.factory.createVegPizza()
            ## 여기서 생성됱 객체는 상위  ConcreteFactory클래스가 무엇인가에 따라서 구분되어 생성됨
            self.VegPizza.prepare()
            self.NonVegPizza.serve(self.VegPizza)
        '''
        
        ''' 내가 변경해 본것
        '''
        switchKey = input("1)인도피자 or 2)미국피자 : ")  # 주의! 여기서 나오는 출력 값은 String 형태이다. 파이썬이라도 형변환이 없는게 아님
        
        if "1" == switchKey:
            factory = IndianPizzaFactory()
        elif "2" == switchKey :
            factory = USPizzaFactory()
            
        # 클래스 객체 MOVE
        self.factory = factory
        # 그냥피자 객체 생성 후 MOVE
        self.NonVegPizza = self.factory.createNonVegPizza()
        # 야채피자 객체 생성 후 MOVE
        self.VegPizza = self.factory.createVegPizza()
        ## 여기서 생성됱 객체는 상위  ConcreteFactory클래스가 무엇인가에 따라서 구분되어 생성됨
        self.VegPizza.prepare()
        self.NonVegPizza.serve(self.VegPizza)

## main 실행부       
if __name__ == '__main__':
    pizza = PizzaStore() ## PizzaStore 클래스 호출 선언 -> 이렇게 해야 'self'가 생성됨
    pizza.makePizza()
    
'''
팩토리 메소드 
-> 객체 생성에 필요한 메소드가 사용자에게 노출된다.
-> 어떤 객체를 생성할지 결정하는 상속과 서브클래스가 필요하다.
-> 한 개의 객체를 생성하는 팩토리 메소드를 사용한다.

추상 팩토리 메소드
-> 관련된 객체 집단을 생성하기 위해 한 개 이상의 팩토리 메소드가 필요
-> 다른 클래스 객체를 생성하기 위해 컴포지션을 사용한다.
-> 관련된 객체 집단을 생성한다.

<<정리>>
-> 심플 팩토리 : 런타임에 클라이언트가 인자로 넘긴 객체형을 기반으로 인스턴스를 생성
-> 팩토리 메소드 : 인터페이스를 통해 객체를 생성하지만 실재 생성은 서브클래스가 담당
-> 추상 팩토리 메소드 : 콘크리트 클래스를 명시하지 않고 관련된 객체의 집단울 생성한다.
 
'''
    
