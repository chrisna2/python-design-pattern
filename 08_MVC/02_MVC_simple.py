

# Model 클래스 : 비지니스 로직이나 Client의 요청을 수행하는 작업을 정의한다.
class Model(object):
    def logic(self):
        data = "Got it!"
        print("Model: Crunching data as per business logic")
        return data
    
# View 클래스 : Client가 보게 되는 뷰 또는 시각적 표현을 정의함
# 모델은 비지니스 로직에 따라 데이터를 뷰에 전달한다.    
class View(object):
    def update(self,data):
        print("View: Updating the view with results: ",data)
        
# Controller 클래스 : 뷰와 모델 사이의 인터페이스 역활을 한다.Client의 요청을 뷰에서 모델로 보낸다.
class Controller(object):
    def __init__(self):
        self.model = Model()
        self.view = View()
        
    def interface(self):
        print("Controller: Relayed the client asks")
        data = self.model.logic()
        self.view.update(data)
        
## ?? 이게 바로 실행되네?
class Client(object):
    print("Client: asks for certain information") 
    controller = Controller()
    controller.interface()       


    
