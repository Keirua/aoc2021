import d1_2021
import unittest
from hypothesis import given, strategies as st

class TestFuzzDay1_2021(unittest.TestCase):
    def test_part1_and_2(self):
        test_input = """199
        200
        208
        210
        200
        207
        240
        269
        260
        263"""
        test_ints = d1_2021.parse(test_input)

        self.assertEqual(d1_2021.part1(test_ints), 7)
        self.assertEqual(d1_2021.part_2(test_ints), 5)

    @given(ints=st.lists(st.integers()))
    def test_fuzz_part_1(self, ints):
        d1_2021.part1(ints=ints)

    @given(ints=st.lists(st.integers()))
    def test_fuzz_part_2(self, ints):
        d1_2021.part_2(ints=ints)

if __name__ == "__main__":
    unittest.main()