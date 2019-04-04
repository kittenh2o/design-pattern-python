from abc import abstractmethod, ABCMeta

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def make_sound(self):
        pass

class Leopard(Animal):
    def make_sound(self):
        print("roar")

class Panda(Animal):
    def make_sound(self):
        print("ah")

class Aligator(Animal):
    def make_sound(self):
        print("huhh")

class SimpleFactory:
    animals = {
        "leopard": Leopard,
        "panda": Panda,
        "aligator": Aligator
    }

    def get_animal(self, animal_type:str):
        return SimpleFactory.animals[animal_type]

# Abstract factory pattern
class VegPizza(metaclass=ABCMeta):
    @abstractmethod
    def prepare(self):
        raise NotImplementedError

class NonVegPizza(metaclass=ABCMeta):
    @abstractmethod
    def serve(self, VegPizza):
        raise NotImplementedError

class DeluxeVeggiePizza(VegPizza):
    def prepare(self):
        print("Prepare {0}".format(type(self).__name__))

class BaconPizza(NonVegPizza):
    def serve(self, veg_pizza):
        print("{0} is served with bacon on {1}".format(
            type(self).__name__, type(veg_pizza).__name__
        ))


class PizzaFactory(metaclass=ABCMeta):

    @abstractmethod
    def create_veg_pizza(self):
        raise NotImplementedError
    
    @abstractmethod
    def create_non_veg_pizza(self):
        raise NotImplementedError

class CanadianPizzaFactory(PizzaFactory):

    def create_veg_pizza(self):
        return DeluxeVeggiePizza()
    
    def create_non_veg_pizza(self):
        return BaconPizza()