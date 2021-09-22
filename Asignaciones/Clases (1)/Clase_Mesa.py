class Mesa:
     color=""
     largo=""
     ancho=""
     def setDatos(self, colorp, largop,anchop):
        self.color=colorp
        self.largo=largop
        self.ancho=anchop
     def getDatos(self):
        return ("\nColor: "+self.color+"\nLargo: "+self.largo+"\nAncho: "+self.ancho)

mesavar=Mesa()        
color=input("Digite Color: ")
largo=input("Digite Largo: ")
ancho=input("Digite Ancho: ")

mesavar.setDatos(color,largo,ancho)
print("\nLos datos son: ",mesavar.getDatos())





