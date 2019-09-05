
'''
04 싱글톤 패턴 : 메타 클래스 


@author: TY
'''

class MyInt(type):
    def __call__(cls, *args, **kwargs):
        print("***** Here is my Int *****", args)
        print("Now do Whatever you want with these object...")
        return type.__call__(cls, *args, **kwargs)
        
        
class int(metaclass=MyInt):
    def __init__(self, x ,y):
        self.x = x
        self.y = y

i = int(4,5)
