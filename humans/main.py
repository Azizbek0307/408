class Odam ():
    def __init__(self,ism):
        self.first_name = ism
    def metod (self):
        print( f"Salom {self.first_name}")
        print( f" {self.first_name} , sen yugrding")

Odamcha = Odam(input('ismni kiritung :'))

Odamcha.metod()

