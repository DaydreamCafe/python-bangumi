import unittest

from src.BangumiAPI.entry.Entry import Entry


class TestEntry(unittest.TestCase):
    def print_entry(self):
        print(Entry(326868))

if __name__ == "__main__":
    unittest.main()