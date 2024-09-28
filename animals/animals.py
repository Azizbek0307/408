class Dog :
    def __init__ (self, laqabi):
        self.nickname = laqabi
    def woof(self):
        print(f"{self.nickname} : Woof ")
    def eat(self,food):
        print(f"{self.nickname} is eating {food}")

dog1 = Dog(input("name :"))

dog1.woof() 
dog1.eat("suyak")