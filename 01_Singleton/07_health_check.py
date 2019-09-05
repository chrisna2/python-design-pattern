
'''
인프라의 상태를 확인하는 서비스 구현

@author: TY
'''
class HealthCheck:
    _instance = None
    def __new__(cls, *args, **kwargs): # 여기서 싱글톤 객체 생성 확인 
        if not HealthCheck._instance:
            HealthCheck._instance = super(HealthCheck, cls).__new__(cls,*args,**kwargs)
        return HealthCheck._instance
    
    def __init__(self):
        self._servers = []
        
    def addServer(self):
        self._servers.append("Server 1")
        self._servers.append("Server 2")
        self._servers.append("Server 3")
        self._servers.append("Server 4")
        
    def changeServer(self):
        self._servers.pop()
        self._servers.append("Server 5")
        
hc1 = HealthCheck()
hc2 = HealthCheck()

hc1.addServer()
print("서버1의 상태를 체크합니다..")
for i in range(4):
    print(hc1._servers[i], "... 체크 중...")

# 초기화가 끼어 든다면..
hc1.__init__()

hc2.addServer()
hc2.changeServer()
print("서버2의 상태를 체크합니다..")
for i in range(4):
    print(hc2._servers[i], "... 체크 중...")

