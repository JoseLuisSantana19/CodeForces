n = int(input())
s = input()
i = 0
cont = 0
while i < n:
    if i+1 < n and s[i] == s[i+1]:
        cont += 1
    i += 1
print(cont)
