class camisa:
     color=""
     talla=""
     material=""
     def setDatos(self, colorp, tallap,materialp):
        self.color=colorp
        self.talla=tallap
        self.material=materialp
     def getDatos(self):
        return ("\nColor: "+self.color+"\ntalla: "+self.talla+"\nmaterial: "+self.material)

camisavar=camisa()        
color=input("Digite Color: ")
talla=input("Digite talla: ")
material=input("Digite material: ")

camisavar.setDatos(color,talla,material)
print("\nLos datos son: ",camisavar.getDatos())





