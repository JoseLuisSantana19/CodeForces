distinctChar = []
nick = input()
for e in nick:
    if e not in distinctChar:
        distinctChar.append(e)
if len(distinctChar) % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')
