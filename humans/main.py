class Odam ():
    def __init__(self,ism):
        self.first_name = ism
    def metod (self):
        print( f"Salom {self.first_name}")
    def yugurish(self):
        print(f"siz yugurdiz {self.first_name}")

Odamcha = Odam(input('ismni kiritung :'))

Odamcha.metod()
Odamcha.yugurish()


