from abc import ABCMeta, abstractmethod

class Compiler(metaclass=ABCMeta):
    @abstractmethod
    def collect_source(self):
        pass
    
    @abstractmethod
    def compile_to_object(self):
        pass

    @abstractmethod
    def run(self):
        pass
    
    def compile_and_run(self):
        """ Template method defining algorithm"""
        self.collect_source()
        self.compile_to_object()
        self.run()

# Concrete class
class iOSCompiler(Compiler):
    def collect_source(self):
        print("Collecting Swift source code")

    def compile_to_object(self):
        print("Compiling Swift code to LLVM bitcode")

    def run(self):
        print("Program running on runtime env")


class Trip(metaclass=ABCMeta):

    def __init__(self):
        self.transpot= None

    @abstractmethod
    def set_transpot(self):
        pass

    @abstractmethod
    def day1(self):
        pass
    
    @abstractmethod
    def day2(self):
        pass

    @abstractmethod
    def day3(self):
        pass

    @abstractmethod
    def return_home(self):
        pass
    
    def itinerary(self):
        """ template method"""
        self.set_transpot()
        self.day1()
        self.day2()
        self.day3()
        self.return_home()


class VeniceTrip(Trip):
    def set_transpot(self):
        self.transpot = "boat"
    
    def day1(self):
        pass

    def day2(self):
        pass

    def day3(self):
        pass

    def return_home(self):
        pass


class MaldiveTrip(Trip):
    def set_transpot(self):
        self.transpot = "foot"
    
    def day1(self):
        pass

    def day2(self):
        pass

    def day3(self):
        pass

    def return_home(self):
        pass


class TravelAgency:

    def __init__(self):
        self.trip = None

    def arrange_trip(self):
        choice = input("Maldive or Venice?")
        class_str = choice + "Trip"
        if class_str not in globals().keys():
            raise Exception("No class named " + class_str)

        EvaledClass = eval(class_str)
        self.trip = EvaledClass()
        self.trip.itinerary()
