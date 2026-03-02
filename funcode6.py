# Movie class with attributes and methods

class Movie:
    lang="Telugu"
    def __init__(self,director,hero,tp):
        self.director=director
        self.hero=hero
        self.ticket_price=tp
    def collections(self,tickets):
        return self.ticket_price*tickets
    def Dub(self,new_lang):
        self.lang=new_lang
bahubali=Movie("SSR","PB", 350)
bahubali.collections(10000000000)
bahubali.lang
bahubali.Dub("Hindi")
bahubali.lang
spirit=Movie("SRV","PB",500)