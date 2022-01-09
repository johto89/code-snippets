'''
Python parsing a .srt file with regex - Remove all, keep only text
'''
import re


# remove the shortest line from statements.txt
with open("test.srt",'r') as read_file:
    lines = read_file.readlines()

shortest = 10000 # used to compare line length
lineToDelete = " " # the line we want to remove

for line in lines:
    if len(line) < shortest:
        shortest = len(line)
        lineToDelete = line

with open("test.srt",'w') as write_file:
    for line in lines:
        if line == lineToDelete:
            pass
        elif re.findall("^[0-9]+$", line):
            pass
        elif re.findall("(?:--> )", line):
            pass
        else:
            write_file.write(line)
print("done")
