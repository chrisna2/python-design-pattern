
'''
장남감 공장 과  CEO 

장남감 공장 = 인터페이스
CEO = 클라이언트
장남감 공장에서 생성된 장남감 = 객체

@example
CEO가 자동차 장남감에서 인형을 추가 생산하려고 공장에 지시를 했다.
클라이언트가 조회프로그램에서 검색프로그램을 추가 하려고 인터페이스에 추가했다.
'''

from abc import ABCMeta, abstractmethod
# ABCMeta는 파이썬에서 특정 클래스를 Abstract로 선언하는 특수 메타클래스 

class Animal(metaclass = ABCMeta):
    @abstractmethod
    def do_say(self):
        pass #??
    
class Dog(Animal): # 추상 클래스를 먹고 
    def do_say(self): # 여기서 추상 클래스의 do_say 메서드 변경
        print("멍멍멍 멍멍멍")
        
class Cat(Animal): # 추상 클래스를 먹고 
    def do_say(self): # 여기서 추상 클래스의 do_say 메서드 변경
        print("야옹 야옹 야옹")

class Cow(Animal): # 추상 클래스를 먹고 
    def do_say(self): # 여기서 추상 클래스의 do_say 메서드 변경
        print("음매 음매 음매")

## forest factory 정의
class ForestFactory(object):
    def make_sound(self, object_type):
        return eval(object_type)().do_say()
## eval 함수 => 자바스크립트와 마찮가지로 문자열로 받은 값을 프로그램 안에서 동적으로 행동하게 하는 함수라고 한다. eval("2+2") -> 4  

    
## 클라이언트 코드
if __name__ == '__main__': #이게 메인 선언이다.... 자바는 public static void main(String[] args)
    ff = ForestFactory()
    animal = input("클래스명 입력 : ")
    ff.make_sound(animal)
        
        
        
        
        

