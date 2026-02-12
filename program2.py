d = {"apple": 100, "banana": 40, "cherry": 150}
keys = d.keys()
print(list(filter(lambda x:d[x]>50, keys)))