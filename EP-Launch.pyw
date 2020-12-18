from tkinter import *
from tkinter import filedialog
from io import open
from os import system
from os import chdir
from os import remove
from os import pardir
from os import getcwd
from os.path import dirname
from os.path import abspath
from os.path import exists
from os.path import basename
from os.path import splitext

programpath = getcwd()
strTypeFile = ["Weather", "Input", "Python Plug-In"]
strExtnFile = ["*.epw", "*.idf", "*.py"]
def exit():
    chdir(programpath)
    if (exists("log.txt")):
        remove("log.txt")
    bw = open("log.txt", 'w')
    bw.write(strWeather.get() + '\n')
    bw.write(strFile.get())
    bw.close()
    myRoot.destroy()

def get_dir(ref:int = 0):
    if (ref == 0):
        myfile = dirname(strWeather.get())
    else: #ref == 1
        myfile = dirname(strFile.get())
    return myfile

def searchFile(ref:int = 0):
    myFile = filedialog.askopenfilename(
      title = strTypeFile[ref]+" File",
      initialdir = get_dir(ref),
      filetypes = [(strTypeFile[0] + " files",strExtnFile[ref])]
      )
    if(len(myFile) != 0):
        if (ref == 0):
            strWeather.set(myFile)
        else: #ref == 1
            strFile.set(myFile)

def runEP():
    parent = dirname(abspath(strFile.get())) 
    chdir(parent)
    system("energyplus -r -w {} -p {} {}".format(
      strWeather.get(),
      splitext(basename(strFile.get()))[0],
      strFile.get()
      ))
myRoot = Tk()
mainForm = Frame(myRoot, width=1200, height=600)
mainForm.pack()

strWeather = StringVar()
strFile = StringVar()
if (exists("log.txt")):
    br = open("log.txt", 'r')
    str1 = br.read().splitlines()
    strWeather.set(str1[0])
    strFile.set(str1[1])
    br.close()
lblWeather = Label(mainForm, text="Weather file:")
lblWeather.grid(row=0, column=0, padx=5, pady=5)
txtWeather = Entry(mainForm, textvariable=strWeather)
txtWeather.grid(row=0, column=1, padx=5, pady=5)
btnWeather = Button(mainForm, text="Search", command=lambda:searchFile(0))
btnWeather.grid(row=0, column=2, padx=5, pady=5)
lblFile = Label(mainForm, text="IDF File:")
lblFile.grid(row=1, column=0, padx=5, pady=5)
txtFile = Entry(mainForm, textvariable=strFile)
txtFile.grid(row=1, column=1, padx=5, pady=5)
btnFile = Button(mainForm, text="Search", command=lambda:searchFile(1))
btnFile.grid(row=1, column=2, padx=5, pady=5)
btnExit = Button(mainForm, text="Exit", command=exit)
btnExit.grid(row=2, column=1, padx=5, pady=5)
btnSimulate = Button(mainForm, text="Run", command=runEP)
btnSimulate.grid(row=2, column=2, padx=5, pady=5)

myRoot.mainloop()

