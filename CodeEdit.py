try:
    # Python2
    from Tkinter import *
except ImportError:
    # Python3
    import tkinter as tk
    from tkinter import *
    

root = Tk("CodeEdit")
root.title("CodeEdit")
root.configure(bg="#59584c")

lbl1 = Label(root, text="CodeEdit", font=("Avenir Next", 30))
lbl1.configure(bg="#59584c")

text = Text(root, padx=30, pady=30)

def saveas():
    global text

    t = text.get("1.0", "end-1c")

    saveLocation = filedialog.asksaveasfilename()

    file1 = open(saveLocation, "w+")
    file1.write(t)
    file1.close
saveAsButton = Button(root, text="Save File As", command=saveas)

def save():
    global text
    
    t = text.get("1.0", "end-1c")
    
    saveLocation = filedialog.saveasfilename()
    
    file1 = open(saveLocation, "w+")
    file1.write(t)
    file1.close
saveButton = Button(root, text="Save File", command=save)

def openfile():
    filename = filedialog.askopenfilename()
    with open(filename) as filename:
        file_data = filename.read()

    text.delete('1.0', 'end')
    text.insert('end', file_data)
openButton = Button(root, text="Open File", command=openfile)

class TextLineNumbers(tk.canvas):
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs)
        self.textwidget = None

    def attach(self, text_widget):
        self.textwidget = text_widget

    def redraw(self, *args):
        '''redraw line numbers'''
        self.delete("all")

        i = self.textwidget.index("@0,0")
        while True :
            dline= self.textwidget.dlineinfo(i)
            if dline is None: break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(2,y,anchor="nw", text=linenum)
            i = self.textwidget.index("%s+1line" % i)

tln = TextLineNumbers(canvas)
tln.redraw()

saveButton.grid()
openButton.grid()
lbl1.grid()
saveAsButton.grid()
root.grid()
text.grid()

root.mainloop()