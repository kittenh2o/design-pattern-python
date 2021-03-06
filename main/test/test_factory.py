import unittest

from src.factory import CanadianPizzaFactory, Panda, SimpleFactory


class TestSimpleFactory(unittest.TestCase):
    def test_simple_factory(self):
        animal = SimpleFactory().get_animal("panda")()
        self.assertIsInstance(animal, Panda)

class TestAbstractFactory(unittest.TestCase):
    def test_pizza_factory(self):
        factory = CanadianPizzaFactory()
        veg_pizza = factory.create_veg_pizza()
        veg_pizza.prepare()

        non_veg_pizza = factory.create_non_veg_pizza()
        non_veg_pizza.serve(veg_pizza)

if __name__ == "__main__":
    unittest.main(exit=False)
