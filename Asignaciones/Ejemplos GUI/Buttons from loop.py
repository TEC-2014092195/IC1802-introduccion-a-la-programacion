from tkinter import *

class ButtonParam ( Button ):
        
        def __init__ ( self, param, parent, **kw ):
                        Button.__init__ ( self, parent, kw )
                        self.Param = param
        def launch ( self ):
                        print ('My Param:', self.Param)
                        

if __name__ == '__main__':
        tk = Tk ()
        for bspec in [('text1','par1'),('text2','par2'),('text3','par3')]:
                b = ButtonParam ( bspec [1], tk, text=bspec [0] )
                b.configure ( command=b.launch )
                b.pack ()
        tk.mainloop ()
