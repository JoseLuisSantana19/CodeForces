s = sorted(list(map(int, input().split('+'))))
for e in range(len(s)):
    if e != len(s)-1:
        print(s[e], end='+')
    else:
        print(s[e])
