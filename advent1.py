import re

start = 0

freq = open("freq.txt", "r")

pat = re.compile(r'(\D)(\d*)(\n)')

for num in freq:
    match = re.findall(pat, num)
    pref = match[0][0]
    value = match[0][1]
    if pref == '+':
        start += int(value)
    elif pref == '-':
        start -= int(value)

print(start)

