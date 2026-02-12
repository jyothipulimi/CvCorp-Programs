from functools import reduce
r = [1,2,4,6,10,18,95,10,4,6,7]
print(reduce(lambda x,y:x if x > y else y, r))