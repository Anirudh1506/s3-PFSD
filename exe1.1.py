class Det:
    def disp(self):
        print("Ticket has been booked for",self.name,self.age,self.gender)
class Book(Det):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
c=60
c1=30
c2=40
a=int(input("Enter 1.Genral 2.First Class 3.Second Class\n"))
ch='y'
while ch=='y':
    if a==1:
        if c==0:
            print("Sorry, All tickets have booked")
        else:
            nam=input("Enter name:")
            ag=input("Enter age:")
            gen=input("Enter gender:")
            b=Book(nam,ag,gen)
            b.disp()
            c-=1
    elif a==2:
        if c1==0:
            print("Sorry, All tickets have booked")
        else:
            nam=input("Enter name:")
            ag=input("Enter age:")
            gen=input("Enter gender:")
            b=Book(nam,ag,gen)
            b.disp()
            c1-=1
    else:
        if c2 == 0:
            print("Sorry, All tickets have booked")
        else:
            nam = input("Enter name:")
            ag = input("Enter age:")
            gen = input("Enter gender:")
            b = Book(nam, ag, gen)
            b.disp()
            c2-=1
    print("If you want to continue booking enter y or else n")
    ch=input()




