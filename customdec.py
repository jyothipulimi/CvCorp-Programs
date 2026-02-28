def Extra_feature(f):
    def x(*args, **kwargs):
        print("Starting function")
        result=f(*args,**kwargs)
        print("Ending function")
        return result
    return x
@Extra_feature
def fun(a,b):
    return a * b
print(fun(5,3))
