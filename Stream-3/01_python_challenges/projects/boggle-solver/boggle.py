from string import ascii_uppercase
from random import choice

# Define our function(s) for testing

def make_grid(w, h):
    """
    Our make_grid() function returns a grid of given dimensions width and height
    """
    return {(row, col): choice(ascii_uppercase) for row in range(h) for col in range(w)}
    
def position_neighbours(coordinates):
    """
    Returns the neighbour coordinates for a given position on the grid
    """
    row = coordinates[0]
    col = coordinates[1]
    
    """ 
    Assign the neighbours
    """
    # Top grid
    top_left = (row - 1, col - 1)
    top_center = (row - 1, col)
    top_right = (row - 1, col + 1)
    
    # Middle grid
    middle_left = (row, col - 1)
    # Current grid position (1, 2)
    middle_right = (row, col + 1)
    
    # Bottom grid
    bottom_left = (row + 1, col - 1)
    bottom_center = (row + 1, col)
    bottom_right = (row + 1, col + 1)
    
    return [top_left, top_center, top_right, middle_left, middle_right, bottom_left, bottom_center, bottom_right]
    
def all_grid_neighbours(grid):
    """
    Find and return all neighbours for a given position on the grid
    """
    neighbours = {}
    for position in grid:
        position_of_neighbours = position_neighbours(position)
        neighbours[position] = [p for p in position_of_neighbours if p in grid]
    
    return neighbours
    
def path_to_word(grid, path):
    """
    Join each letter in the path to form a string
    """
    return "".join([grid[p] for p in path])
   
def search(grid, dictionary):
    """
    Finds words contained in paths on the grid and matches these to words in a dictionary
    """
    neighbours = all_grid_neighbours(grid)
    paths = []
    full_words, stems = dictionary
    
    def do_search(path):
        word = path_to_word(grid, path)
        # If a word is present, add the path
        if word in full_words:
            paths.append(path)
        # If the stems needed to make a word are not in the dictionary, we keep searching
        if word not in stems:
            return
        for nextPosition in neighbours[path[-1]]:
            if nextPosition not in path:
                do_search(path + [nextPosition])
                
    for position in grid:
        do_search([position])
            
    words = []
    for path in paths:
        words.append(path_to_word(grid, path))
    
    return set(words)
        
def get_dictionary(dictionary):
    """
    Load dictionary of words
    """
    full_words = set()
    stems = set()
    
    with open(dictionary) as f:
        for word in f:
            word = word.strip().upper()
            full_words.add(word)
            
            for i in range(1, len(word)):
                stems.add(word[:i])
                
    # Return set (more performant than list data structure)
    return full_words, stems
        
def main():
    """
    Our main function runs the boggle solver project
    """
    grid = make_grid(3, 3)
    dictionary = get_dictionary("words.txt")
    words = search(grid, dictionary)
    
    def display_words(words):
        """
        Display words found in grid
        """
        print ("The following words were found in the grid: ")
        for word in words:
            print ("# " + word)
        print ("Found %s words" % len(words))
    
    display_words(words)

# Running our boggle solver

if __name__ == "__main__":
    main()
        