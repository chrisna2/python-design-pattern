
'''
02.게으른 초기화
@author: 나현기

※ '_' (파이썬 언더스코어)에 대하여
1. 인터프리터에서 사용되는 경우
    -> 파이썬 인터프리터에선 마지막으로 실행된 결과값이 _라는 변수에 저장된다. 
                이는 표준 CPython 인터프리터에서 먼저 사용되었으며 다른 파이썬 인터프리터 구현체에서도 
                똑같이 사용할 수 있다.
2. 값을 무시하고 싶은 경우
3. 특별한 의미의 네이밍을 하는 경우
4. 국제화(i18n)/지역화(ㅣ10n) 함수로 사용되는 경우
5. 숫자의 리터럴값의 자릿수 구분을 위한 구분자로써 사용할 때
'''
class Singleton:
    
    __instance = None # None = (java)Null
    
    def __init__(self):
        if not Singleton.__instance:# 현재 인스턴스가 생성되지 않았으면
            print("__init__ method called.")
        else:
            print("Instance already created:",self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance: # 현재 인스턴스가 생성되지 않았으면
            cls.__instance = Singleton()
        return cls.__instance
    
print("check_1")
s = Singleton() ## 클래스를 초기화 했지만 객체는 생성되지 않음

print("check_2")
print("Object created", Singleton.getInstance()) # 객체생성 : Singleton.getInstance()

print("check_3")
s1 = Singleton() ## 객체는 이미 생성됐음
