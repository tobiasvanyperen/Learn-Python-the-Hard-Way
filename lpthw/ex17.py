from sys import argv
from os.path import exists

script, from_file, to_file = argv

indata = open(from_file).read()

print("Hit RETURN to continue copy files, CTRL-C to abort.")
input()

out_file = open(to_file, 'w').write(indata)

print("Done.")