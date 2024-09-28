import time

class Odam():
    def __init__(self,ism):
        self .name = ism 
    def yugurish(self):
        print(f"{self.name} yugurayapti")
    
    def yiqilish(self):
        time.sleep(3)
        print(f"{self.name},yiqilib tushdi ") 

Odam1 = Odam(input("ism kirting :"))

Odam1.yugurish()
Odam1.yiqilish()

