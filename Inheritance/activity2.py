class person( object ):
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)
class employee( person ):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.past = post
        person.__init__(self, name, idnumber)
a = employee('rahul',886012, 200000, "intern")
a.display()