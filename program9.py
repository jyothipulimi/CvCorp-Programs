from functools import reduce
num = [5, 10, 15, 20, 25, 30]
print(reduce(lambda x,y:x+y, filter(lambda x: x%5 == 0, map(lambda x:x**2, num))))