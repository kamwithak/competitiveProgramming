import random

def giveMeAColor():
  possibleValues = '0123456789ABCDEF'
  n = len(possibleValues)
  arr = ['#']
  for i in range(6):
    arr.append(possibleValues[random.randint(0,255) % n])
  return ''.join(arr) 

print(giveMeAColor())


n = 4
for i in range(150):
  if ((random.randint(0,255) % n) >= 6):
    print('END - the compression law has been broken')
    break
  print(random.randint(0,255) % n)


