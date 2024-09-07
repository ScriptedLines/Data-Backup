import pickle
import ctypes
import tkinter as tp
from tkinter import *
from tkinter import filedialog
import tkinter.font as font
from tkinter import PhotoImage
from PIL import Image, ImageTk
import os
from tkinter import ttk



l=[]
no=1

'''def on_closing():
    # code to save changes before closing
    print("Changes saved!")
    tk.destroy()'''

def new():
    
    desktop_path = os.path.expanduser("~/Desktop")
    file_names = []

    for root, dirs, files in os.walk(desktop_path):
        for file in files:
            file_names.append(file)

    global l
    for i in file_names:
        for x in range(0,1000):
            if i=="backup"+str(x)+".pickle":
                l.append(i)
    n=1
    
    rec =Toplevel(tk)
    rec.geometry("700x500")
    rec.title("Recover")
    rec['background']="#0A0A09"
    listbox=Listbox(rec,height=50,width=100,bg="#0A0A09",fg="#F6F7F7")
    
    
    
    for i in l:
        if i not in listbox.get(0, tp.END):
            listbox.insert(n,i)
            n+=1 
        else:
            continue
    

    def select(event):
    
        desktop_path = os.path.expanduser("~/Desktop")
        file_names = []

        for root, dirs, files in os.walk(desktop_path):
            for file in files:
                file_names.append(file)
        
        no=1
        zx=listbox.get(listbox.curselection())
        x=open(zx,"rb")
        print(file_names)

        restored=x.read()
        o="backup"+str(no)+".txt"
        print(no)
        while True:
            if o in file_names:
                no=no+1
                o="backup"+str(no)+".txt"
            elif o not in file_names:
                y=open(o,"wb")
                break

            
        
        o="backup"+str(no)+".txt"
        
        y=open(o,"wb")
        
        pickle.dump(restored,y)
        x.close()
        y.close()
    listbox.bind("<Double-Button-1>",select) 

    listbox.pack()
    rec.mainloop()
    
def back():
    
    no=1
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
    a=filename
    g=open(a,"rb")
    
    data=g.read()

    while True:
        try:
            f=open("backup"+str(no)+".pickle","wb")
            print("congo")
            break
        except:
            no=no+1   
    
    pickle.dump(data,f)
    g.close()
    f.close()
    hide="backup"+str(no)+".pickle"
    
    
    ctypes.windll.kernel32.SetFileAttributesW(hide, 2)

    desktop_path = os.path.expanduser("~/Desktop")  # Path to the desktop

    file_names = []

    for root, dirs, files in os.walk(desktop_path):
        for file in files:
            file_names.append(file)



    global l
    for i in file_names:
        for x in range(0,1000):
            if i=="backup"+str(x)+".pickle":
                l.append(i)
    

tk=Tk()

def on_enter1(e):
   but1.config(bg='#545eeb')
def on_leave1(e):
   but1.config(bg="#1d29dc",fg="#ffffff")

def on_enter2(e):
   but2.config(bg="#545eeb")
def on_leave2(e):
   but2.config(bg="#1d29dc",fg="#ffffff")




background_image_path = "C:\\Users\\Aaryaman\\Downloads\\image.jpg"
background_image = Image.open(background_image_path)
background_image = ImageTk.PhotoImage(background_image)

canvas = tp.Canvas(tk, width=1000, height=700)  # Set the dimensions to match your window size
canvas.pack()

bi=canvas.create_image(0, 0, anchor=tp.NW, image=background_image)
canvas.tag_lower(bi)
tk.title("Data Backup")
tk.geometry("1000x700+300+50")

canvas = tp.Canvas(tk, width=1000, height=700)  # Set the dimensions to match your window size
canvas.pack()
canvas.create_image(0, 0, anchor=tp.NW, image=background_image)




tk.title("Data Backup")
tk.geometry("1000x700+300+50")















but1font=font.Font(family="Magneto",size=20)
but1=Button(tk,text="Backup",font=but1font,height=1,bg="#121dbe",fg="#ffffff",command=back)
but1.place(x=250,y=400)

but2font=font.Font(family="Magneto",size=20)
but2=Button(tk,text="Recover",font=but2font,height=1,bg="#121dbe",fg="#ffffff",command=new,activebackground="#1283A0")
but2.place(x=500,y=400)

but1.bind('<Enter>', on_enter1)
but1.bind('<Leave>', on_leave1)

but2.bind('<Enter>', on_enter2)
but2.bind('<Leave>', on_leave2)

labfont=font.Font(family="Freestyle Script",size="50",weight="bold")
head=Label(tk,text="Data Backup",font=labfont,bg="#dbf6ff",fg="#4d55e1",highlightthickness=0)
head.place(x=350,y=100)

lab2font=font.Font(family="Arial Rounded MT Bold",size="15")
intro=Label(tk,text="Made by Aaryaman Bisht (XII-A)",font=lab2font,bg="#dbf6ff",fg="#4d55e1")
intro.place(x=500,y=180)

tk.mainloop()





