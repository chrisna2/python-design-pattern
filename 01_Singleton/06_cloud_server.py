
'''
클라우드 DB서버 구조는 싱글톤 패턴의 구조와 유사하다. 
여러 서비스가 한 개의 DB릃 공유하는 구조다 보니 안정된 클라우드 서비스를 설계하려면 다음과 같은 사항들을 명심해야 한다.

1) 데이터이스의 일관성을 보존해야 한다. -> 언제 어디서 사용되더라도 항상 상태를 공유 해야 한다.
2) 다수의 DB 연산을 처리하려면 메모리와 CPU를 효율적으로 사용해야 한다. -> 메모리를 한개만 차지 한다. 다른 작업을 한다고 해도 새로 생성되지 않는다.
 
@author: TY
'''
import sqlite3

## 메타클래스 생성
'''
클래스는 메타클래스가 정의 한다.
class Database 구문으로 클래스를 셍성하면 

파이썬은
Database = type(name, bases, dict)를 실행한다.

+ name : 클래스명
+ base : 베이스 클래스
+ dict : 속성값

만약 여기서  이미 정의된 메타클래스가 있다면
Database = MetaSingleton(name, bases, dict)를 실행한다.

'''
class MetaSingleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs): # [1] 싱글톤 생성
        if cls not in cls._instances: # [2] 단 한개의  database 클래스객체만 생성된다. -> 매타클래스의 객체가 존재 하지 않는 경우 메타클래스를 생성한다.
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args,**kwargs) 
        return cls._instances[cls]
    
## 클라우드 데이터베이스 모형
class Database(metaclass=MetaSingleton):
    # 클래스의 인자, 변수
    connetion = None
    
    # 메서드  
    def connect(self):
        if self.connetion is None:
            self.connetion = sqlite3.connect("db.sqlite3")
            self.cursorobj = self.connetion.cursor()
        return self.cursorobj
    
    def checkPunc(self):
        print("Hello world -> ",self.cursorobj)  
        return

# [3] 웹 앱이 DB 연산을 요청할때마다 Database 클래스를 생성하지만 내부적으로 한개의 객체만 생성된다.
db1 = Database().connect()
print("Database Object DB1", db1)
Database().checkPunc()
db2 = Database().connect() 
print("Database Object DB2", db2)
   
'''
※ 단잏 웹 앱 형태가 아닌 여러 웹앱이 같은 DB에 접속하는 경우  (DB동기화가 어렵고 리소스 사용량이 많은 경우)
 -> 각 웹엡이 싱글론을 생성하기 때문에 싱글톤 패턴에 적합하지 않다.
 -> 연결 풀링 기법을 사용하는 것이 효과적이다. 
     -> 자바에서는 DBConnectionPool이라거나 ConnectionManager이라고 들어 봤을 것이다.
     
※ 싱글톤 패턴의 단점
1] 클래스의 전역변수 값이 실수로 변경된 것을 모르고 애플리케이션에서 사용이 가능하다. -> 값이 공유 되기 때문에.. 초기화를 따로 하지 않았을 경우
2] 같은 객체에 대한 여러 참조자가 생길수 있다. -> 같은 객체에 대한 여러개의 참조자가 생긴 경우 참조자 별로 별도의 메모리 분리가 필요하다.
3] 싱글톤 패턴 클래스는 전역변수가 변경되서는 곤란하다. -> 클래스안에서 수정이 이루어 질 경우 의도치않게 다른 클래스에 영향을 줄수 있다.
4] 사용하는 구조에 따라서 리소스를 많이 사용하는 구조가 될수 되 있다.
'''
