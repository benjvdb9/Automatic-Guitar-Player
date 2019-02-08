import re
from time import sleep

class Note:
    def __init__(self, s_note):
        self.note = s_note
        self.notes= self.getNotes()

    def getNotes(self):
        #import pdb; pdb.set_trace()
        regex = r'([=_^]?[a-zA-Z][,\']?\d?)\/(\d)'

        if self.note[0] == '[':
            notes = []
            matches = re.finditer(regex, self.note, re.MULTILINE)
            for matchnum, match in enumerate(matches):
                notes += [match.group()]
        else:
            pattern = re.compile(regex)
            note = pattern.match(self.note)
            notes = [note.group(0)]
        return notes

    def __str__(self):
        return '<Note Object: {}>'.format(self.note)

pattern = re.compile(r'(.): (.+)')
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
            all_notes = []
            notes = line.split(' ')
            all_notes += notes
            running = False

    else:
        notes = line.split(' ')
        all_notes += notes

print(attributes)
all_Notes = []
for num in range(len(all_notes)):
    if all_notes[num] != '' and all_notes[num] != '\n':
        all_Notes += [Note(all_notes[num])]

for num in range(len(all_Notes)):
    print(all_Notes[num].getNotes())
abc.close()