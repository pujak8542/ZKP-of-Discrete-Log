#!/usr/bin/env python
# coding: utf-8

# # Importing various libraries and implementing functions for printing output on user ingerface

# In[1]:


from datetime import datetime, timedelta
import math
def msg(ans):
        lbl2.config(text="Adversary got the Secret Key..\nThe secret key is:"+str(ans))
def msg2():
    with open("info.txt") as file_in:
            lines = []
            for line in file_in:
                lines.append(line)
    a=int(lines[0])
    b=int(lines[1])
    m=int(lines[2])
    lbl.config(text="Adversary captured the values:\nPrime="+str(m)+"\nGenerator="+str(a)+"\nG^X mod P="+str(b))
def capture():
        lbl.config(text="Capturing has been started...")
        frame.after(2000,msg2)


# # Discrete Logarithm function which will compute the value of X when value of prime, generator are given

# In[ ]:


def discreteLogarithm():
    with open("info.txt") as file_in:
                lines = []
                for line in file_in:
                    lines.append(line)
    a=int(lines[0])
    b=int(lines[1])
    m=int(lines[2])
    end_time = datetime.now() + timedelta(seconds=10)
    flag=0
    while datetime.now() < end_time and flag==0:
        n = int(math.sqrt (m) + 1);

        
        an = 1;
        for i in range(n):
            if datetime.now() > end_time:
                  break
            an = (an * a) % m;
        if datetime.now() > end_time:
              break
        value = [0] * m;

       
        cur = an;
        for i in range(1, n + 1):
            if datetime.now() > end_time:
                  break
            if (value[ cur ] == 0):
                value[ cur ] = i;
            cur = (cur * an) % m;

        cur = b;
        if datetime.now() > end_time:
              break
        for i in range(n + 1):
            if datetime.now() > end_time:
                  break
            
            if (value[cur] > 0):
                ans = value[cur] * n - i;
                if (ans < m):
                    print(ans);
                    frame.after(2000,msg(ans))
                    flag=1
            cur = (cur * a) % m;

        
    if(flag==0):
        print("Cant find")
        lbl2.config(text="Too large to get within the specified time period")


# # For creating user interface for the adversary attack

# In[2]:


import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk

# Top level window
frame = tk.Tk()
frame.title("TextBox Input")
frame.geometry('700x500')
canvas= Canvas(frame, width= 1500, height= 1000)
bg = PhotoImage(file = "img2.png")
canvas.create_image( 0, 0, image = bg, 
                     anchor = "nw")
canvas.pack()
# Function for getting Input
# from textbox and printing it
# at label widget

# TextBox Creation

text = Label(frame, text="What in presence of ADVERSARY?",bg="#000fff000")
text.place(x=420,y=10)
text.config(font=('Helvetica bold',25))
#Load an image in the script
img= (Image.open("img3.png"))

#Resize the Image using resize method
resized_image= img.resize((200,205), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)

#Add image to the Canvas Items
canvas.create_image(130,60, anchor=NW, image=new_image)
img2= (Image.open("img3.png"))

#Resize the Image using resize method
resized_image2= img.resize((200,205), Image.ANTIALIAS)
new_image2= ImageTk.PhotoImage(resized_image2)

#Add image to the Canvas Items
canvas.create_image(930,60, anchor=NW, image=new_image2)
img3= (Image.open("img5.png"))

#Resize the Image using resize method
resized_image3= img3.resize((200,205), Image.ANTIALIAS)
new_image3= ImageTk.PhotoImage(resized_image3)

#Add image to the Canvas Items
canvas.create_image(530,60, anchor=NW, image=new_image3)
text2 = Label(frame, text="PROVER",bg="#000fff000")
text2.place(x=160,y=270)
text2.config(font=('Helvetica bold',25))
text3 = Label(frame, text="VERIFIER",bg="#000fff000")
text3.place(x=960,y=270)
text3.config(font=('Helvetica bold',25))
text4 = Label(frame, text="ADVERSARY",bg="#000fff000")
text4.place(x=530,y=270)
text4.config(font=('Helvetica bold',25))
btn = Button(frame, text = 'Capture the public values of Prover', bd = '5',command=capture)
btn.place(x=500, y=350)
btn.config(font=('Helvetica bold',12))
btn2 = Button(frame, text = 'Get the Secret Key', bd = '5',command=discreteLogarithm)
btn2.place(x=890, y=350)
btn2.config(font=('Helvetica bold',12))
'''entry1 = tk.Entry (frame) 
canvas.create_window(350, 400, window=entry1)'''

lbl = tk.Label(frame, text = "",bg="#808080")
lbl.place(x=500,y=410)
lbl.config(font=('Helvetica bold',15))
lbl2 = tk.Label(frame, text = "",bg="#808080")
lbl2.place(x=500,y=590)
lbl2.config(font=('Helvetica bold',15))
lbl3 = tk.Label(frame, text = "",bg="#808080")
lbl3.place(x=890,y=350)
lbl3.config(font=('Helvetica bold',15))



#canvas.create_window(450, 123, window=entry1)
frame.mainloop()


# In[ ]:





# In[ ]:




