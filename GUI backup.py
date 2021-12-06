from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os
from ImageEndecrypt import image_proc as ip

root = Tk()
root.geometry("550x300+300+150")
root.resizable(width=True, height=True)
image = None

def openfn():
    filename = filedialog.askopenfilename(title='open')
    return filename
    
def open_image():
    global image
    x = openfn()
    fname.set('当前文件:' + x)
    image = Image.open(x)
    y = int(root.winfo_height() *0.5)
    x = int(image.size[0]*y/image.size[1])
    show = image.resize((x,y), Image.ANTIALIAS)
    show = ImageTk.PhotoImage(show)
    panel.config(image = show)
    panel.image = show

	
def encrypt():
    global image
    image = ip(image,password.get(),'e')
    y = int(root.winfo_height() *0.5)
    x = int(image.size[0]*y/image.size[1])
    show = image.resize((x,y), Image.ANTIALIAS)
    show = ImageTk.PhotoImage(show)
    panel.config(image = show)
    panel.image = show
    
    
def decrypt():
    global image
    image = ip(image,password.get(),'d')
    y = int(root.winfo_height() *0.5)
    x = int(image.size[0]*y/image.size[1])
    show = image.resize((x,y), Image.ANTIALIAS)
    show = ImageTk.PhotoImage(show)
    panel.config(image = show)
    panel.image = show

def save():
    image.save('./'+path.get())
	
fname = StringVar()
password = StringVar()
path = StringVar()
fname.set("文件路径在这-w-")
password.set('0.14725')
path.set('处理结果.png')
Label(root,textvariable = fname).pack()
panel = Label(root)
panel.pack()
btn1 = Button(root, text='打开', command=open_image)
btn1.pack()
ent1 = Entry(textvariable = password)
ent1.pack()
btn2 = Button(root,text = '解密',command = decrypt)
btn3 = Button(root,text = '加密',command = encrypt)
btn2.pack()
btn3.pack()
ent2 = Entry(root, textvariable = path)
ent2.pack()
btn4 = Button(root, text = '保存', command = save)
btn4.pack()
root.mainloop()
