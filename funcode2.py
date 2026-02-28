class A:
    x=20
    def __init__(self,a,b):
        self.x=a
        self.x=b
    def m1(self,k):
        self.x=k
    @classmethod
    def m2(cls):
        cls.x=50
obj=A(30,40)
obj.m1(60)
print(obj.x)
print(A.x)
A.m2()
print(obj.x)
print(A.x)