import re
from time import sleep

pattern = re.compile(r'(.): (.+)')
note = re.compile(r'(?:[^_=]?[a-zA-Z][,\']?/[0-9]?)+')
abc = open('resources/StayinAlive.abc', 'r')

attributes = {}
running = True
for line in abc:
    if running:
        try:
            match = pattern.match(line)
            values = match.groups()
            attributes[values[0]] = values[1] 
        except:
            t = note.match(line)
            print(t.groups())
            running = False

    else:
        break


abc.close()
