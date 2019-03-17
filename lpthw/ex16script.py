from sys import argv

script, filename = argv

txt = open(filename)

print(f"Opening {filename} now...")
print(txt.read())
