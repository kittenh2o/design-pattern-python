from abc import ABCMeta, abstractmethod


class Receiver:
    def action(self):
        print("Do stuff...")


class Command(metaclass=ABCMeta):
    def __init__(self, recv:Receiver):
        self.recv = recv
    
    @abstractmethod
    def execute(self):
        raise NotImplementedError


class ConcreteCommand(Command):
    def execute(self):
        self.recv.action()


class Invoker:
    def command(self, cmd):
        self.cmd = cmd
    
    def execute(self):
        self.cmd.execute()
    

# Stock Market Example
class Order(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        raise NotImplementedError


class StockTrade:
    def buy(self):
        print("Buying stock...")
    
    def sell(self):
        print("Selling stock...")


class BuyStockOrder(Order):
    def __init__(self, stock:StockTrade):
        self.stock = stock
    
    def execute(self):
        self.stock.buy()


class SellStockOrder(Order):
    def __init__(self, stock:StockTrade):
        self.stock = stock
    
    def execute(self):
        self.stock.sell()


class Agent:
    def __init__(self):
        self.__orders = list()
    
    def add_order(self, order:Order):
        self.__orders.append(order)
    
    def place_orders(self):
        while self.__orders:
            order = self.__orders.pop()
            order.execute()
