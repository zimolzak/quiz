## usage: python3 quiz.py state capital 10

from re import sub
from sys import argv
from random import choice

## Determine which datfile to open

index = open('./datfiles/index.in').read().splitlines()
filename = ''
fields = ''
for line in index:
    ## simplify
    line = line.replace('@quiz_dir@/', '')
    line = line.replace('{', '')
    line = line.replace('}', '')
    line = line.replace('[', '')
    line = line.replace(']', '')
    line = sub('\|.*?:', ':', line)
    ## parse
    this_list = line.split(':')
    filename = this_list[0]
    fields = this_list[1:]
    if argv[1] in fields and argv[2] in fields:
        break

## Open datfile and parse argv options

datfile = open('./datfiles/'+filename).read().splitlines()

a = fields.index(argv[1])
b = fields.index(argv[2])
try:
    reps = int(argv[3])
except(IndexError):
    reps = 5

## Do the quiz

for i in range(reps):
    d_fields = choice(datfile).split(':')
    print(d_fields[a])
    input('Think hard...')
    print(d_fields[b])
    print()
