
'''
@컴파운드패턴
여러가지 형태의 패턴을 섞어서 사용하는 디자인 패턴의 형태

@MVC 
-사용자는 뷰를 통해 요청을 보낸다. 뷰는 사용자에게 보여지는 웹사이트다.
뷰에있는 버튼을 클릭하면 뷰는 컨트롤러에 요청을 전달한다.
-컨트롤러는 뷰에 전달 받은 인풋을 모델로 보낸다.모델은 요청에 맞는 작업을
수행한다.
-컨트롤러는 사용자의 요청에 따라 버튼 교체 및 UI 추가등을 뷰에 지시할 수 있다.
-모델은 뷰에 상태변경을 알린다. 내부 로직 또는 버튼 클릭 등의 외부 트리거에
의한 상태 변경이다.
-뷰는 모델이 전달한 상태를 출력한다. 예를 들어 사용자가 웹사이트에 로그인하면
대시보드를 표시한다. 대시보드의 세부 내용은 모델이 뷰에 전달한다.

@모델 : 데이터를 저장하고 조작하는 클래스
    -> model 클래스는 데이터의 생성과 수정, 소멸 등 데이터에 관한 작업을 정의하고 
    data에 관한 모든 작업을 정의하고 데이터를 사용하는 메소드를 제공한다.
@뷰 : 유저 인터페이스와 데이터의 시각적 표현을 담당하는 클래스
    -> view 클래스는 유저 인터페이스를 담당한다. 애플리케이션에 필요한 웹이나 
    GUI를 생성하는 메소드를 포함한다. 
    -> 전달받은 데이터를 시각적으로 표현하는 기능외 개별적인 로직은 포함하지 않아야 한다.
@컨트롤러 : 모델과 뷰를 연결하는 클래스
    -> controller 클래스는 데이터를 받고 전달한다. 요청을 라우팅하는 메소드를 포함한다.
@클라이언트 : 목적에 따라 정보를 요청하는 클래스

@MVC의 적합 용도
+비지니스 로직을 건들지 않고 표현 계층만 수정해야 하는 경우
+유저인터페이스를 수정하는데 다수의 컨츠롤러와 뷰가 사용될수도 있다.
+모델은 뷰를 수정하지 않아도 변경될 수 있으므로 독립적이다.

@MVC의 목적
+데이터 조작과 표현의 분리
+쉬운 유지보수와 구현
+유연한 데이터 저장과 표현방식의 수정
    -> 서로 독립적이기에 쉽게 수정이 가능
'''
class Model(object):
    ## ???
    services = {
                'email':{'number':1000, 'price':2,},
                'sms':{'number':1000, 'price':10,},
                'voice':{'number':1000, 'price':15,},
    }
    
class View(object):
    def list_services(self, services):
        for svc in services:
            print(svc, ' ')
    
    def list_pricing(self, services):
        for svc in services:
            print("For", Model.services[svc]['number'],
                  svc, "message you pay $", Model.services[svc]['price'])
            
class Controller(object):
    def __init__(self):
        self.model = Model()
        self.view = View()
        
    def get_services(self):
        services = self.model.services.keys()# 모델 클래스에서 데이터를 호출하고
        return(self.view.list_services(services))# 뷰 클래스에 데이터를 불러온다.
    
    def get_pricing(self):
        services = self.model.services.keys()
        return(self.view.list_pricing(services))
    
class Client(object):
    controller = Controller()
    print("Services Provided : ")
    controller.get_services()
    print("Pricing for Services : ")
    controller.get_pricing()
