class A:
    def __init__(self, a):
        self.a = a
    def __it__(self, other):
        if(self.a<other.a):
            return "ob1 is less than ob2"
        else:
            return "ob2 is less than ob1"
    def __eq__(self, other):
        if(self.a == other.a):
            return "both are equal"
        else:
            return "not equal"
ob1 = A(2)
ob2 = A(3)
print("passed value: ", ob1.a, ob2.a)
print(ob1 < ob2)
ob3 = A(4)
ob4 = A(4)
print("passed values: ", ob3.a, ob4.a)
print(ob3 == ob4)
