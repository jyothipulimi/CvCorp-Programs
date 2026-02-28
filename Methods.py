class Profile:
    def __init__(self, username):
        self.followers=0
        self.username=username
    def follow(self):
        print("Someone followed you")
        self.followers+=1
    def update_username(self,newusername):
        self.username=newusername
p1=Profile("_jyothi_pulimi")
p1.follow()
print(p1.followers)
p1.update_username("_jyothi_22")
print(p1.username)
