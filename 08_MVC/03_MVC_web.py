v
import tornado.web
import tornado.ioloop
import tornado.httpserver
import sqlite3
'''
<!> 파이썬 모듈 설치법  <!>
---------------------------------------
1> 파이썬 설치 경로 찾기
2> 파이썬 설치 경로에 CMD실행
3> CMD> python -m pip install tornado
4> 설치가 완료되면 버전 확인 해볼것
---------------------------------------
'''
## <주의!> 책에서는 생략됨 : DB에 접속 해야한다. DB 파일이 있었음 ㅠ_ㅠ  
conn = sqlite3.connect(r"C:\Users\chris\pythonPractice\DesignPattern\08_MVC\db")
cursor = conn.cursor()


## [1] MODEL ##################################
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        query = "select * from task"
        # <!이거아님> todos = _execute(query) 
        # _execute() 정의 되지 않았다고 에러 발생함
        
        
        todos = cursor.execute(query)
        self.render('index.html', todos=todos)
    
class NewHandler(tornado.web.RequestHandler):
    def post(self):
        name = self.get_argument('name', None)
        query = "create table if not exists task (id INTEGER PRIMARY KEY, name TEXT, status NUMERIC) "
        cursor.execute(query)
        query = "insert into task (name, status) values ('%s', %d) " %(name, 1)
        cursor.execute(query)
        self.redirect('/')
        
    def get(self):
        self.render('new.html')
        
class UpdateHandler(tornado.web.RequestHandler):
    def get(self, id, status):
        query = "update task set status=%d where id=%s" %(int(status), id)
        cursor.execute(query)
        self.redirect('/')
        
class DeleteHandler(tornado.web.RequestHandler):
    def get(self,id):
        query = "delete from task where id=%s" % id
        cursor.execute(query)
        self.redirect('/')
################################################

### [2] VIEW : base.html / index.html / new.html

### [3] Controller #############################
class RunApp(tornado.web.Application):
    def __init__(self):
        # 파이썬에서는 링크설정을 이렇게 하는 듯?
        Handlers = [
                (r'/', IndexHandler),
                (r'/todo/new', NewHandler),
                (r'/todo/update/(\d+)/status/(\d+)',UpdateHandler),
                (r'/todo/delete/(\d+)', DeleteHandler),
                ]
        
        Settings = dict(
            debug=True,
            template_path='templates',
            static_path='static',
        )
        
        tornado.web.Application.__init__(self,Handlers,**Settings)

################################################

if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(RunApp())
    http_server.listen(5000)
    tornado.ioloop.IOLoop.instance().start()
    # 실행시 : localhost:5000 웹브라우저로 접속

'''
@MVC의 장점
+ MVC를 사용하면 애플리케이션을 모델과 뷰, 컨트롤러 총 3개의 파트로 나눌수 있다.
이 구조는 유지보수가 쉽고 요소간의 독립성이 높아져 복잡성이 줄어든다.
+ 백앤드 로직을 거의 건드리지 않고 독립적으로 프론트앤드를 수정할 수 있다.
+ 모델이나 비즈니스 로직도 마찬가지로 뷰와 상관없이 수정될 수 있다.
+ 컨트롤러 또한 뷰와 모델과는 독립적으로 수정될수 있다.
+ 플랫폼 개발자와 UI개발자 같이 특정 분야의 전문가들이 독립적으로 일할수 있는 환경을 제공한다.
'''

        
