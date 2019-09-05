'''
Created on 2019. 3. 18.

# 자바에서는 생성자를 private로 선언하고 객체를 초기화하는 static 함수를 만들면 간단하게 싱글톤 구현가능
# 파이썬에서는 생성자를 private를 선언할 수 없기 때문에 다른 방법이 필요하다.

@author: 나현기
'''
class Singleton(object):
    def __new__(cls):   #  __new__ 함수 (파이썬 전용 특수 생성자) 오버라이드
        if not hasattr(cls, 'instance'):    
            # hasattr 함수  : 해당객체가 명시한 속성을 가지고 있는지 확인 하는 파이썬 함수
            # cls 객체가 instance 속성을 가지고 있는지 확인, 클래스객체가 이미 존재하는지 확인하는 과정
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance
    
s = Singleton()
print("object created", s)

s1 = Singleton()
print("object created", s1)

'''
[실행 결과]

s = Singleton()
print("object created", s)
    ->    object created <__main__.Singleton object at 0x0000016C8A318550>

s1 = Singleton()
print("object created", s1)
    ->    object created <__main__.Singleton object at 0x0000016C8A318550>
'''
