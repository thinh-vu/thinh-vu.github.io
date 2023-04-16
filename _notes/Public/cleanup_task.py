import re

with open('How to take smart notes.md', 'r') as f:
    lines = f.readlines()

with open('How to take smart notes.md', 'w') as f:
    for line in lines:
        if not re.match(r'.*Highlight \(yellow\) - Location \d+', line):
            f.write(line)
