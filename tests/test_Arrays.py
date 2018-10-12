import unittest
from tests.test_utils import captured_output
import Arrays


class ArrayTest(unittest.TestCase):
    def test_missing_several(self):
        total_nums = 100
        a = [i+1 for i in range(total_nums)]
        a.pop(20)
        a.pop(30)
        a.pop(80)
        with captured_output() as out:
            Arrays.print_missing(a, total_nums)
        self.assertEqual('21\n32\n83\n', out.getvalue())

    def test_numbers_that_sum_up(self):
        a = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
        result = Arrays.pair_that_sums_to_num(a, 7)
        result.sort()
        solution = [(2, 5), (4, 3), (3, 4), (-2, 9)]
        solution.sort()
        self.assertEqual(solution, result)
