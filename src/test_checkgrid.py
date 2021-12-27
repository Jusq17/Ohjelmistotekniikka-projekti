
import unittest
import sudoku_answers

from modules import functions

class test_gridfunctions(unittest.TestCase):

    def test_check_correct(self):

        functions.sudoku_grid = sudoku_answers.answer5

        self.assertEqual(functions.check_grid(), True)

    def test_check_incorrect(self):

        functions.sudoku_grid = sudoku_answers.incorrect_grid
        self.assertEqual(functions.check_grid(), False)

        functions.sudoku_grid = sudoku_answers.incomplete_grid
        self.assertEqual(functions.check_grid(), False)

        functions.sudoku_grid = sudoku_answers.empty_grid
        self.assertEqual(functions.check_grid(), False)

        functions.sudoku_grid = sudoku_answers.empty_list
        self.assertEqual(functions.check_grid(), False)


if __name__ == "__main__":

    unittest.main()

