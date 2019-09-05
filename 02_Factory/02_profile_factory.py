
'''
Created on 2019. 3. 20.

@author: TY
'''
from abc import ABCMeta, abstractmethod

# product 인터페이스 ===================

class Section(metaclass=ABCMeta): ## 추상클래스
    @abstractmethod
    def describe(self):
        pass    ## 아무것도 안하는 매서드 생성
    
class PersonalSection(Section): ## Section 클래스 상속
    def describe(self):
        print("personal section")
        
class AlbumSection(Section):
    def describe(self):
        print("album section")
        
class PatentSection(Section):
    def describe(self):
        print("patent section")
        
class PublicatinSection(Section):
    def describe(self):
        print("publication section")
        
## creator 추상클래스 ===================

class Profile(metaclass=ABCMeta):
    def __init__(self): ## 파이썬에서의 생성자(constructor)
        self.sections = [] ## 생성자에서 선언이 되어버림
        self.createProfile()
    
    def __del__(self): ## 파이썬에서의 소멸자(constructor)
        pass
    
    @abstractmethod
    def createProfile(self):
        pass
    def getSections(self):
        return self.sections
    def addSections(self, section):
        self.sections.append(section)
        
class linkedin(Profile): ## Profile 클래스 상속
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(PatentSection())
        self.addSections(PublicatinSection())
        
class facebook(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(AlbumSection())

### 클라이언트 섹션 부분 =======================
if __name__ == '__main__':
    profile_type = input("which profie you'd like to create? [linkedIn or facebook]")
    profile = eval(profile_type.lower())() ## linkedin + () 따라서 linkedin() 클래스가 실행됨
    print("creating profile..", type(profile).__name__)
    print("Profile has section --", profile.getSections())       
    
'''
팩토리 메서드의 장점
-> 유연성과 포괄성을 갖추며 한 클래스에 종속되지 않는다. ConcreteProduct가 아닌 인터페이스에 의존한다.
-> 객체를 생성하는 코드와 활용하는 코드를 분리해 의존성이 줄어든다.클라이언트는 인자나 어떤 클래스가 생성되는지 알필요가 없다.
       새로운 클래스 추가 등의 유지보수가 쉽다.
       
팩토리메소드 
-> 객체 생성에 필요한 메소드가 사용자에게 노출된다.
-> 어떤 객체를 생성할지 결정하는 상속과 서브클래스가 필요하다.
-> 한 개의 객체를 생성하는 팩토리 메소드를 사용한다.

추상 팩토리 메소드
-> 관련된 객체 집단을 생성하기 위해 한 개 이상의 팩토리 메소드가 필요
-> 다른 클래스 객체를 생성하기 위해 컴포지션을 사용한다.
-> 관련된 객체 집단을 생성한다.
'''
    
    
    
    
