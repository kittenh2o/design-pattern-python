import unittest

from src.singleton import (LazySingleton, MetaSingleton, SingletonClassDecor,
                           singleton)


class TestSingleton(unittest.TestCase):
    def test_lazy_singleton(self):
        s1 = LazySingleton()
        s2 = LazySingleton()
        self.assertIs(s1, s2)


class TestMetaSingleton(unittest.TestCase):
    def test_meat_singleton(self):
        class A(metaclass=MetaSingleton):
            pass
        
        a1 = A()
        a2 = A()
        self.assertIs(a1, a2)

class TestSingletonDecorator(unittest.TestCase):
    @singleton
    class B:
        pass
    
    class B2:
        """POPO"""
        pass

    def test_singleton_decorator(self):
        b1 = TestSingletonDecorator.B()
        b2 = TestSingletonDecorator.B()
        self.assertIs(b1, b2)

    def test_popo(self):
        b3 = TestSingletonDecorator.B2()
        b4 = TestSingletonDecorator.B2()
        self.assertIsNot(b3, b4)

class TestSingletonClassDecorator(unittest.TestCase):
    def test_singleton_class_decorator(self):
        @SingletonClassDecor
        class C:
            pass
        
        c1 = C()
        c2 = C()
        self.assertIs(c1, c2)

