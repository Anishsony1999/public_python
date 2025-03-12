
class Math:

    def adding(self,x,y):
        print(x+y)

class MathChils(Math):

    def adding(self,x,y):
        print(x*y)
    

child = MathChils()

child.adding(3,3)


def adding(x=0,y=0,z=0):
    print(x+y+z)


adding(2,2,2)
