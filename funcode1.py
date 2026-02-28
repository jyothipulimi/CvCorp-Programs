class Building:
    total_rooms=10
    def __init__(self,name,roadno):
        self.name=name
        self.roadno=roadno
    def change_rooms(self,trooms):
        self.total_rooms=trooms
b1=Building("MB",1)
b2=Building("PB",2)
b1.change_rooms(20)
print(b1.total_rooms)
print(b2.total_rooms)