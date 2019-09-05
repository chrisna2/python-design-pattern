
from abc import ABCMeta, abstractclassmethod

## Command 객체 : 파이썬의 추상 기본 클래스인 인터페이스이며 ConcreteCommand는 이를 기반으로 세부로직을 구현.
class Order(metaclass=ABCMeta):
    # ConcreteCommand 클래스가 Order 클래스를 실행하는 추상 메소드다.
    @abstractclassmethod
    def execute(self):
        pass

## ConcreteCommand 객체 : Order 인터페이스를 구현하는 구상 클래스
# 각 클래스는 증권 거래 시스템 객체를 사용해 주식을을 매수 또는 매도 한다.
# 각 클래스의 execute() 메소드는 주식 객체를 통해 주식을 매수 또는 매도한다.
class BuyStockOrder(Order):
    def __init__(self,stock):
        self.stock = stock
    
    def execute(self): # 리시버에 정의된 buy() 메서드 실행
        self.stock.buy()
        
class SellStockOrder(Order):
    def __init__(self,stock):
        self.stock = stock
        
    def execute(self): # 리시버에 정의된 sell() 메서드 실행
        self.stock.sell()
        
## Receiver 객체: ConcreteCommand 객체가 생성한 주문을 처리하는 여러 메소드를 정의 한다.
# Receiver에 정의된 buy()와 sell()메소드는 BuyStockOrder와 SellStockOrder 클래스가 주식을 매수 또는 매도할 때 호출된다.
class StockTrade:
    def buy(self):
        print("You will buy stocks")
    
    def sell(self):
        print("You will sell stocks")

## Invoker 객체 : 클라이언트와 StockExchange 객체 사이의 중개자이며 클라이언트의 주문을 처리한다.
# Agent에서는 큐를 나타내는 __orderQueue 리스트형 데이터 멤버가 있다 모즌 신규 주문건은 우선 이 큐에 추가한다.
# placeOrder() 메소드는 주문을 큐에 넣고 처리까지 담당한다.
class Agent:
    def __init__(self):
        self.__orderQueue = []
        '''
        if. Redo나 Rollback을 고려할 경우 큐가 아닌 스택을 이용하는 것이 좋다.
        '''
    
    def placeOrder(self, order):
        self.__orderQueue.append(order)
        #order.execute()
    
    ## 내가 추가한 것  ##
    def execute(self):
        for orders in self.__orderQueue:
            orders.execute()
            
    def popOrder(self):
        self.__orderQueue.pop()
        
        
## 클라이언트 부분        
if __name__ == '__main__':
    # Client
    stock = StockTrade() # Receiver 선언
    
    # ConcreteCommand 객체 선언 
    buyStock = BuyStockOrder(stock) # ConcreteCommand 객체 선언시에는 항상 Receiver를 상속하고 선언
    sellStock = SellStockOrder(stock)
    
    # Invoker
    agent = Agent() 
    agent.placeOrder(buyStock)# 구매 요청을 큐에 저장
    agent.placeOrder(sellStock)# 매매 요청을 큐에 저장
    agent.placeOrder(sellStock)# 매매 요청을 큐에 저장
    agent.popOrder()
    agent.placeOrder(buyStock)# 구매 요청을 큐에 저장
    agent.placeOrder(sellStock)# 매매 요청을 큐에 저장
    
    # 이전까지는 실행되지 않고 있음
    agent.execute()# 큐에 저장죈 실행 내역을 한꺼번에 실행
    
'''
[커맨드 패턴의 장단점]
@장점
1)작업을 요청하는 클래스와 실제로 작업을 수행하는 클래스를 분리한다.
2)큐에 커맨드를 순서대로 저장한다.
3)기존코드를 수정하지 않고 새로운 커맨드를 추가할 수 있다.
4)커맨드패넡으로 롤백 시스템을 구현할 수 있다.
@단점
1)클래스와 객체가 많다. 개발자는 신중하게 클래스를 작성해야 한다.
2)모든 작업이 독립적인  ConcreteCommand 클래스이므로 구현 및 유지보수해야 하는 클래스가 많다.
'''
    
    
    
    
    
    
    
