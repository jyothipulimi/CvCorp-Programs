nums = [12,15,7,18,20,21,25]
print(list(filter(lambda x:(x%3==0 or x%5==0) is not (x%3==0 and x%5==0),nums)))