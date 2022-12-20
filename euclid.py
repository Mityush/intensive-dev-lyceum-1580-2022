def euclidForTwo(x,y):
  if (y == 0):
    return x
  else: return(nod(y,x % y))

from functools import reduce

def euclid(list):
    for item in list:
        if not isinstance(item, int) or int(item) <= 0:
            return -1
    return reduce(lambda x,y: nod(x,y), list)
