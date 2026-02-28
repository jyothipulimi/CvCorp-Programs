class A:
    def __init__(self,q,r):
        self.q=q 
        self.r=r 
    @classmethod
    def divideby10(cls,n):
        return cls(n//10,n%10)
obj=A.divideby10(25)
print(obj.q)
print(obj.r)
