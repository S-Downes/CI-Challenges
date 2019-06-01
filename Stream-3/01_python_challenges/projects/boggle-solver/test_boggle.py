import unittest
import boggle
from string import ascii_uppercase

# Test cases to make sure our boggle.py functions are working

class test_boggle(unittest.TestCase):
    def test_is_this_thing_on(self):
        self.assertEqual(1, 1)
        
class TestBoggleSolver(unittest.TestCase):
    """
    Our suite of boggle solver test cases
    """
    def test_can_create_empty_grid(self):
        """
        Test case for creating an empty grid
        """
        zero_grid = boggle.make_grid(0, 0)
        self.assertEqual(len(zero_grid), 0)
        
    def test_grid_returns_correct_size(self):
        """
        Test case to ensure size of grid returned is correct
        """
        grid = boggle.make_grid(2, 3)
        self.assertEqual(len(grid), 6)
        
    def test_grid_coordinates(self):
        """
        Test case to verify that given coordinates are contained or not contained within
        a given grid
        """
        grid = boggle.make_grid(2, 2)
        self.assertIn((0, 0), grid)
        self.assertIn((0, 1), grid)
        self.assertIn((1, 0), grid)
        self.assertIn((1, 1), grid)
        self.assertNotIn((2, 2), grid)
        
    def test_grid_contains_uppercase_letters(self):
        """
        Test case to verify that the grid letters are uppercase
        """
        grid = boggle.make_grid(2, 2)
        for letter in grid.values():
            self.assertIn(letter, ascii_uppercase)
            
    def test_neighbours_of_grid_position(self):
        """
        Test case to verify that a position contains 8 neighbours
        """
        coords = (1, 2)
        neighbours = boggle.position_neighbours(coords)
        self.assertIn((0, 1), neighbours)
        self.assertIn((0, 2), neighbours)
        self.assertIn((0, 3), neighbours)
        self.assertIn((1, 1), neighbours)
        # Current coordinates (1, 2)
        self.assertIn((1, 3), neighbours)
        self.assertIn((2, 1), neighbours)
        self.assertIn((2, 2), neighbours)
        self.assertIn((2, 3), neighbours)
        
    def test_all_grid_neighbours(self):
        """
        Test case to verify all grid positions have neighbours
        """
        grid = boggle.make_grid(2, 2)
        neighbours = boggle.all_grid_neighbours(grid)
        self.assertEqual(len(grid), len(neighbours))
        for position in grid:
            adjacents = list(grid)
            # Remove the current grid position to leave only the adjacent positions
            adjacents.remove(position)
            self.assertListEqual(sorted(neighbours[position]), sorted(adjacents))
            
    def test_path_to_word(self):
        """
        Test case to verify a path can be converted into words
        """
        grid = boggle.make_grid(2, 2)
        oneLetterWord = boggle.path_to_word(grid, [(0, 0)])
        twoLetterWord = boggle.path_to_word(grid, [(0, 0), (1, 1)])
        self.assertEqual(oneLetterWord, grid[(0, 0)])
        self.assertEqual(twoLetterWord, grid[(0, 0)] + grid[(1, 1)])
        
    def test_search_grid_for_words(self):
        """
        Test case to verify that a pattern of words can be found
        """
        grid = { (0, 0): "A", (0, 1): "B",  (1, 0): "C", (1, 1): "D" }
        twoLetterWord = "AB"
        threeLetterWord = "ABC"
        wordNotInGrid = "EEE"
        
        full_words = [twoLetterWord, threeLetterWord, wordNotInGrid]
        stems = ["A", "AB", "E", "EE"]
        dictionary = full_words, stems
        
        wordMatch = boggle.search(grid, dictionary)
        
        self.assertTrue(twoLetterWord in wordMatch)
        self.assertTrue(threeLetterWord in wordMatch)
        self.assertTrue(wordNotInGrid not in wordMatch)
        
    def test_load_dictionary(self):
        """
        Test case to verify that a list of words returned using get_dictionary()
        is greater than 0
        """
        dictionary = boggle.get_dictionary("words.txt")
        self.assertGreater(len(dictionary), 0)
    
        
        
    
    