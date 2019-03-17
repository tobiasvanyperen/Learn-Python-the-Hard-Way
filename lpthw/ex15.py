# The line below allows you to pass arguments to Python from the command line to argv
from sys import argv

# The line below creates a list called argv the contains two values. The name of the script and another argument passed from the command line
script, filename = argv

# The line below takes a file, reads it and sets the value as the text variable
txt = open(filename)

# The line below prints a string with a variable and prints the file with the text.read command
print(f"Here's your file {filename}:")
# The line below
print(txt.read())

txt.close()

# The line below prompts to insert the filename again and creates a variable from it
print("Type the filename again:")
# The line below
file_again = input("> ")

# The line below opens the file previously prompted with open() and puts it into the variable txt_again
txt_again = open(file_again)

# The line below reads the opened file in the variable txt_again and prints it.
print(txt_again.read())

txt_again.close()