class Animal:
    def __init__(self,value1):
        self.a=value1
d={"k1":1,"k2":2}
Ob=Animal(d)
Ob1=Animal(d)
l=[Ob,Ob1]
def check_value(l):

    for i in l:
        if i.a["k1"]==1:
            print(i.a,"KeyError")
            del i.a['k1']
        print(i)




print(check_value(l))