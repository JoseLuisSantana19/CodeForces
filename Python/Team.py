n = int(input())
output = 0
for e in range(n):
    array = input().split()
    count = 0
    for e in array:
        if e == '1':
            count += 1
    if count > 1:
        output += 1
print(output)
