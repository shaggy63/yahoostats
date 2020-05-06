import unittest
from selenium import webdriver
from yahoostats.selenium_stats import Webscraper, ys_run, tr_run
from yahoostats.selenium_stats import BROWSER_OPT
from yahoostats.evaluator import combine_stats


class TestMethods(unittest.TestCase):
    def test_zero(self):
        print("Sample test to test the testings :)")
        self.assertEqual(":)", ":)")

    def test_webscrapertestrun(self):
        """
        Test Webscraper class-testrun()
        """
        ys = Webscraper(BROWSER_OPT)
        self.assertTrue(ys.test_run())

    def test_yahoo_ticker_stats(self):
        """
        Test of getting data for list of stocks in df.
        """
        stock_list = 'GOOGL'
        self.assertTrue(ys_run(stock_list) is not None)

    def test_tipranks_stats(self):
        """
        Test of getting data for list of stocks in df.
        """
        stock_list = 'GOOGL'
        self.assertTrue(tr_run(stock_list) is not None)

    def test_evaluator(self):
        """
        Test of merging requests with selenium data
        """
        stock_list = ['GOOGL', 'MU']
        self.assertTrue(combine_stats(stock_list) is not None)


# if __name__ == '__main__':
#     unittest.main()
