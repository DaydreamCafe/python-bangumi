import unittest

from test.test_entry import TestEntry

# from test.test_entry import TestEntry

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestEntry("print_entry"))
    runner = unittest.TextTestRunner()
    runner.run(suite)