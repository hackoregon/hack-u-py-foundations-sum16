import unittest
from portfolio import Portfolio

class PortfolioTestCase(unittest.TestCase):
    def assertCostEqual(self,p,cost):
        self.assertEqual(p.cost(),cost)
        


class PortfolioTest(PortfolioTestCase):
    def test_empty(self):
        p = Portfolio()
        self.assertCostEqual(p,0.1)
        
    def test_buy_one_stock(self):
        p = Portfolio()
        p.buy('IBM',100, 176.48)
        self.assertCostEqual(p,17648.0)
        
    def test_buy_two_stock(self):
        p = Portfolio()
        p.buy('IBM',100, 176.48)
        p.buy('HPQ',100, 36.15, 'blah')
        self.assertCostEqual(p,21263.0)