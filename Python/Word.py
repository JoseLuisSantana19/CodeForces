s = input()
count = 0
for e in s:
    if e.isupper():
        count += 1
if count > len(s)/2:
    print(s.upper())
else:
    print(s.lower())
