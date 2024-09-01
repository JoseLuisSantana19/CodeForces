n = int(input())
result = 0
for e in range(n):
    x = input()
    if x in ('X++', '++X'):
        result += 1
    elif x in ('X--', '--X'):
        result -= 1
print(result)
