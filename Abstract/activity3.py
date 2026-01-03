class india():
    def capital(self):
        print("new delhi is the capital of india.")
    def lang(self):
        print("hindi is the most widely spoken language in india.")
    def type(self):
        print("india is a developing country.")
class usa():
    def capital(self):
        print("washington D.C. is the capital of usa.")
    def lang(self):
        print("english is the primary language of usa.")
    def type(self):
        print("usa is a developed country.")
obj_ind = india()
obj_usa = usa()
for country in (obj_ind, obj_usa):
    country.capital()
    country.lang()
    country.type()