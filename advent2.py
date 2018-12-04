import re
import itertools
with open("freq.txt") as freq:

    seen = set()
    contact = 0
    contacts = []
    dupes = [x for x in contacts if contacts.count(x) > 1]
    pat = re.compile(r'(\D)(\d*)(\n)')

    if len(dupes) == 0:
        for num in itertools.cycle(freq.readlines()):
            match = re.findall(pat, num)
            pref = match[0][0]
            value = match[0][1]
            if pref == '+':
                if contact not in contacts:
                    contacts.append(contact)
                    seen.add(contact)
                elif contact in contacts:
                    print(contact)
                    break
                contact += int(value)

            elif pref == '-':
                if contact not in contacts:
                    contacts.append(contact)
                    seen.add(contact)
                elif contact in contacts:
                    print(contact)
                    break
                contact -= int(value)
