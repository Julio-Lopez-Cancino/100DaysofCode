import random

def item_randomly(num, lista):
  op = []
  for x in range(num):
    random.seed(random.randint(0, 99999))
    a = random.choice(lista)
    op.append(a)
  return op