import re

emailFile = open('read.txt', 'r').read()
outputFile = open('output.txt', 'w')
emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", emailFile)
outputFile.write('\n'.join(emails))