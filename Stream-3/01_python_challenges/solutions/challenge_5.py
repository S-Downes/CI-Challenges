# File I/O

# Open file with 'w+'

with open('challenges/data/data.txt', 'w+') as file:
    # Write to data
    file.write("\nIt is an ancient Mariner, And he stoppeth one of three.\n\'By thy long grey beard and glittering eye,\nNow wherefore stopp\'st thou me?")
    lines = file.read()
    # Note once read the cursor position has shifted to 132
    print (file.tell())
    print (lines)

file.closed

# Open file with 'r+' 

with open('challenges/data/data.txt', 'r+') as file:
    # Read data
    lines = file.read()
    # Move cursor to 0 and write
    file.seek(0)
    file.write("This is my new first line!\n")
    # Change line three
    file.seek(50)
    file.write("\nAnd this is my new third line!")
    # Use read() to shift the cursor position to the end so we can append
    file.read()
    file.write("\nAnd this has been appended!")
    print (lines)
    
file.closed
