
class shape:
    def __init__(self,x,y):#constructor
        self.x=x
        self.y=y

class Circle(shape): #inheritence is done by passing the super class as an argument to the class
    def __init__(self,x,y, r):
        super().__init__(x,y)#super constructor just like in java
        self.radius=r

    def compute_area(self):
        return self.radius*self.radius*3.1415

    def __str__(self) -> str:#toString method of python
        return "Circle at " + str(self.x) + "," + str(self.y)+ " has area: " + str(self.compute_area())

if __name__=='__main__':
    c=Circle(10,10,4.5)
    print(c)