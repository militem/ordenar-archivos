from tkinter import *
from tkinter import filedialog
from ficheros import *

class Gui:
    
    filename = ""
    
    def __init__(self, window):
        self.window = window
        self.window.title("ORDENAR ARCHIVOS")
        self.window.resizable(0, 0)
        self.window.geometry("300x150")
        self.window.iconphoto(False, PhotoImage(file='./icono.png'))
        button_explore = Button(self.window, text = "Buscar Carpeta", command = self.browseFiles)
        button_ordenar = Button(self.window, text = "Ordenar", command = self.ordenar)
        
        button_explore.place(x = 90, y = 30, width = 120, heigh = 25)
        button_ordenar.place(x = 100, y = 80, width = 100, heigh = 25)
        
    def browseFiles(self):
        self.filename = filedialog.askdirectory()
        
    def ordenar(self):
        archivos = ficheros(self.filename)
    


def main():
    
    root = Tk()
    app = Gui(root)
    root.mainloop()

if __name__ == '__main__':
    main()
