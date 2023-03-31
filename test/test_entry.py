import unittest

from pybangumi.entry.calendar import Calendar
from pybangumi.entry.entry import Entry
from pybangumi.entry.entry_characters import EntryCharacters
from pybangumi.entry.entry_persons import EntryPersons
from pybangumi.entry.entry_relations import EntryRelations


class TestEntry(unittest.TestCase):
    def print_calendar(self) -> None:
        print(Calendar())

    def print_entry(self) -> None:
        print(Entry(326868))

    def print_entry_characters(self) -> None:
        print(EntryCharacters(326868))

    def print_entry_persons(self) -> None:
        print(EntryPersons(326868))

    def print_entry_relations(self) -> None:
        print(EntryRelations(326868))


if __name__ == "__main__":
    unittest.main()
