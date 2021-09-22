### create a list of buttons
### show click values in an entry
##try:
##    # Python2
##    import Tkinter as tk
##except ImportError:
##    # Python3
##    import tkinter as tk
##def click(val):
##    s = "Button " + val + " clicked"
##    root.title(s)
##    entry.insert('end', val)
##
##
##root = tk.Tk()
### create the list of button objects
##button_list = [
##tk.Button(root, text=" 1 ", bg='red', command=lambda: click('1')),
##tk.Button(root, text=" 2 ", bg='green', command=lambda: click('2')), 
##tk.Button(root, text=" 3 ", bg='white', command=lambda: click('3'))
##]
### show buttons
##for button in button_list:
##    button.pack(side='left', padx=10)
### create an entry to show button values
##entry = tk.Entry(root)
##entry.pack(padx=3, pady=3)
##root.mainloop()
# create multiple Tkinter buttons using a dictionary:
##import tkinter as tk
##def text_update(animal,f):
##    text.delete(0, tk.END)
##    text.insert(0, animal+str(f))
##    print(f)
##root = tk.Tk()
##text = tk.Entry(root, width=35, bg='yellow')
##text.grid(row=0, column=0, columnspan=5) 
##btn_dict = {}
##col = 0
##words = ["Dog", "Cat", "Pig", "Cow", "Rat"]
##for i in range(3):
##    for animal in words:
##        # pass each button's text to a function
##        action = lambda x = animal: text_update(x,i)
##        # create the buttons and assign to animal:button-object dict pair
##        btn_dict[animal] = tk.Button(root, text=animal, command=action) 
##        btn_dict[animal].grid(row=1, column=col, pady=5) 
##        col += 1
##
### run the GUI event loop
##root.mainloop()

import tkinter as tk

class SimpleTableInput(tk.Frame):
    def __init__(self, parent, rows, columns):
        tk.Frame.__init__(self, parent)

        self._entry = {}
        self.rows = rows
        self.columns = columns

        # register a command to use for validation
        vcmd = (self.register(self._validate), "%P")

        # create the table of widgets
        for row in range(self.rows):
            for column in range(self.columns):
                index = (row, column)
                e = tk.Entry(self, validate="key", validatecommand=vcmd)
                e.grid(row=row, column=column, stick="nsew")
                self._entry[index] = e
        # adjust column weights so they all expand equally
        for column in range(self.columns):
            self.grid_columnconfigure(column, weight=1)
        # designate a final, empty row to fill up any extra space
        self.grid_rowconfigure(rows, weight=1)

    def get(self):
        '''Return a list of lists, containing the data in the table'''
        result = []
        for row in range(self.rows):
            current_row = []
            for column in range(self.columns):
                index = (row, column)
                current_row.append(self._entry[index].get())
            result.append(current_row)
        return result

    def _validate(self, P):
        '''Perform input validation. 

        Allow only an empty value, or a value that can be converted to a float
        '''
        if P.strip() == "":
            return True

        try:
            f = float(P)
        except ValueError:
            self.bell()
            return False
        return True

class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.table = SimpleTableInput(self, 3, 4)
        self.submit = tk.Button(self, text="Submit", command=self.on_submit)
        self.table.pack(side="top", fill="both", expand=True)
        self.submit.pack(side="bottom")

    def on_submit(self):
        print(self.table.get())


root = tk.Tk()
Example(root).pack(side="top", fill="both", expand=True)
root.mainloop()
