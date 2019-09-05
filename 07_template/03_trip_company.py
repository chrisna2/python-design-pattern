
from abc import ABCMeta, abstractclassmethod

# AbstractClass 구현부
class Trip(metaclass=ABCMeta):
    
    @abstractclassmethod
    def setTransport(self):
        pass
    
    @abstractclassmethod
    def day1(self):
        pass
    
    @abstractclassmethod
    def day2(self):
        pass
    
    @abstractclassmethod
    def day3(self):
        pass
    
    @abstractclassmethod
    def returnHome(self):
        pass
    
    # template_method() 구현부 :
    def itinerary(self):
        self.setTransport()
        self.day1()
        self.day2()
        self.day3()
        self.returnHome()
        
# ConcreteClass 구현부 1:     
class VeniceTrip(Trip):
    def setTransport(self):
        print("Take a boat and find your way in the Grand Canal")
        
    def day1(self):
        print("Visit St Mark's Basilica in St Mark's Square")
    
    def day2(self):
        print("Appreciate Doge's Palace")
    
    def day3(self):
        print("Enjoy the food near the Rialto Bridge")
        
    def returnHome(self):
        print("Get souveniers for friends and get back")

# ConcreteClass 구현부2:
class MaldivesTrip(Trip):
    def setTransport(self):
        print("On foot, on any island, Wow!")
        
    def day1(self):
        print("Enjoy the marine life of Banana Reef")
    
    def day2(self):
        print("Go for the water sports and snorkelling")
    
    def day3(self):
        print("Relax on the beach and enjoy the sun")
        
    def returnHome(self):
        print("Dont feel like leaving the beach..")
        
## 클라이언트 호출부
class TravelAgency:
    def arrange_trip(self):
        choice = input("whot kind of place you'd like to go historical or to a beach? :")
        if "historical" == choice:
            self.trip = VeniceTrip()
            self.trip.itinerary()
        elif "beach" == choice:
            self.trip = MaldivesTrip()
            self.trip.itinerary()
    
if __name__ == '__main__':
    TravelAgency().arrange_trip()
