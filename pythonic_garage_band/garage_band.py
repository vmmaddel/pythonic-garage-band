from abc import ABC, abstractmethod
#should be abstract
class Musician(ABC):
    def __init__(self,name,instrument):
        self.name = name
        self.instrument = instrument
    
    @abstractmethod
    def play_solo(self):
        pass

class Guitarist(Musician):
    def __init__(self,name):
        #now call init on the super class and pass in guitar
        super().__init__(name,"guitar")
    
    def play_solo(self):
        return "face melting guitar wailing"

class Bassist(Musician):
    def __init__(self,name):
        #now call init on the super class and pass in guitar
        super().__init__(name,"bass")
    
    def play_solo(self):
        return "thump, thumpty thump"

class Drummer(Musician):
    def __init__(self,name):
        #now call init on the super class and pass in guitar
        super().__init__(name,"drums")
    
    def play_solo(self):
        return "rattle crash boom"

class Band:
    def __init__(self,name, members):
        self.name = name
        self.members = members
    def play_solos(self):
        pass

    @classmethod
    def to_list(cls):
        pass
    @staticmethod
    def create_from_data(data):
        #create from some data source
        pass
    
    def function(self):
        print("This message inside the class")

myObject = Band()
print(Band.name)
myObject.function()