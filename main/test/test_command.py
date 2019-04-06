import unittest
import sys
from os.path import dirname

sys.path.insert(0, dirname(dirname(__file__)))
from src.command import (Invoker, ConcreteCommand, Receiver,
                         Agent, BuyStockOrder, SellStockOrder, StockTrade)

class TestCommand(unittest.TestCase):
    def test_command(self):
        recv = Receiver()
        cmd = ConcreteCommand(recv)
        invoker = Invoker()
        invoker.command(cmd)
        invoker.execute()


class TestStockTrade(unittest.TestCase):
    def setUp(self):
        self.stock = StockTrade()
        self.agent = Agent()

    def test_buy_stock(self):
        buy_order = BuyStockOrder(self.stock)
        self.agent.add_order(buy_order)
        self.agent.place_orders()

    def test_sell_stock(self):
        sell_order = SellStockOrder(self.stock)
        self.agent.add_order(sell_order)
        self.agent.place_orders()


if __name__ == "__main__":
    suites = (
        unittest.TestLoader().loadTestsFromTestCase(case) for case in (TestCommand, TestStockTrade)
    )
    for suite in suites:
        unittest.TextTestRunner(verbosity=2).run(suite)
