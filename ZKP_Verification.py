
# # Function for calculating the inverse of mod

# In[1]:


def modInverse(a, m) : 
    m0 = m 
    y = 0
    x = 1
  
    if (m == 1) : 
        return 0
  
    while (a > 1) : 
  
        # q is quotient 
        q = a // m 
  
        t = m 
  
        # m is remainder now, process 
        # same as Euclid's algo 
        m = a % m 
        a = t 
        t = y 
  
        # Update x and y 
        y = x - q * y 
        x = t 
  
  
    # Make x positive 
    if (x < 0) : 
        x = x + m0 
  
    return x 
  


# # Importing python libraries

# In[ ]:


from random import randrange

from hashlib import sha256
from math import gcd


# # Key Generation Function for Calculating Discrete Log

# In[ ]:


u=0
def key_generation(p,g):
  x = randrange(2, p-1)
  y = pow(g,x,p)
  return {'secret_key':x,'public_key':y}


# # Sign Function for calculating the varibale r and s used during verification

# In[ ]:


def sign(m, x,p,g):
  s = 0
  while s == 0:
    k = randrange(2, p-1)
    while gcd(k, p-1) !=1:
      k = randrange(2, p-1)
    print("k="+str(k))
    r = pow(g,k,p)
    s = (int.from_bytes(sha256(m.encode('utf-8')).digest(), 'big') - x*r)*modInverse(k,p-1) % (p-1)
  return r,s


# # Various functions for extracting the value and verify function for completing the verification of the Prover

# In[ ]:


def msg2(a,b,p,g,r,s):
    lbl3.config(text="The known values to the verifier are: \nPrime:"+str(p)+"\nGenerator: "+str(g)+"\nr="+str(r)+"\ns="+str(s)+"\nThe verifier has computed the value:\n(Y^r mod p)*(r^s mod p)= "+str(b))
def msg(p,g,h,o,r,s,a):
    lbl2.config(text="The known values to the prover are\n Prime:"+str(p)+"\nGenerator:"+str(g)+"\nSecret Key(X): "+h+"\nG^X mod p: "+o+"\nCalculated r= "+str(r)+"\nCalculated s="+str(s)+"\nThe Prover has calculated the value:\nG^m mod p :"+str(a))
def verify(m, signature_, y,p,g):
  r,s = signature_
  assert 0 < r < p and 0 < s < p-1, 'Signature input are not in the right interval'+str(r)
  left=pow(g, int.from_bytes(sha256(m.encode('utf-8')).digest(), 'big'), p)
  right=pow(y,r,p)*pow(r,s,p)%p
  frame.after(3050,msg2(left,right,p,g,r,s))
  if(left==right):
        frame.after(3100,msg3(True,left))
  else:
        frame.after(31000,msg3(False,left))
  assert pow(g, int.from_bytes(sha256(m.encode('utf-8')).digest(), 'big'), p) == pow(y,r,p)*pow(r,s,p)%p, 'The signature is not valid for the string "{m.decode("utf-8")}".'
  print(f'The signature is valid for the string "{m}"')
  return left
def msg3(ttg,a):
    if ttg==True:
        lbl.config(text = "The Verification has been completed as the prover's and verifier's value has matched!!! ")
    else:
        lbl.config(text = "The verification was unsuccessful for given values. ")


# # print function for calling various other functions used during verification process

# In[2]:


def printInput():
    p=int(entry3.get())
    global a,m
    
    g=int(entry2.get())
    a=g
    m=p
    print("p="+str(p))
    print("g="+str(g))
    keys=key_generation(p,g);
    message=entry4.get()
    h=str(keys['secret_key'])
    print("h="+str(h))
    global u
    o=str(keys['public_key'])
    u=(keys['public_key'])
    print("u="+str(o))
    file=open("info.txt","w")
    file.write(str(a)+"\n"+str(u)+"\n"+str(m))
    file.close()
    signature = sign(message, keys['secret_key'],p,g)
    x3,x4=signature
    print("r="+str(x3))
    print("s="+str(x4))
    ttg=verify(message, signature, keys['public_key'],p,g)
    lbl2.config(text="Wait...The process has been started..")
    frame.after(2000,msg(p,g,h,o,x3,x4,ttg))
   
    #lbl2.config(text="The known values to the prover are\n Prime:"+str(p)+"\nGenerator:"+str(g))
def setTextInput(text1,text2):
    entry2.delete(0,"end")
    entry2.insert(0, text1)    
    entry3.delete(0,"end")
    entry3.insert(0, text2)   


# # Code for creating user interface using python library tkinter

# In[3]:


import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk

# Top level window
frame = tk.Tk()
frame.title("TextBox Input")
frame.geometry('900x700')
canvas= Canvas(frame, width= 1500, height= 1000)
bg = PhotoImage(file = "img2.png")
canvas.create_image( 0, 0, image = bg, 
                     anchor = "nw")
canvas.pack()
# Function for getting Input
# from textbox and printing it
# at label widget

# TextBox Creation

text = Label(frame, text="ZERO KNOWLEDGE PROOF",bg="#000fff000")
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
text2 = Label(frame, text="PROVER",bg="#000fff000")
text2.place(x=160,y=270)
text2.config(font=('Helvetica bold',25))
text3 = Label(frame, text="VERIFIER",bg="#000fff000")
text3.place(x=960,y=270)
text3.config(font=('Helvetica bold',25))
btn = Button(frame, text = 'Start the process of verification!!', bd = '5',command=printInput)
btn.place(x=520, y=300)
btn.config(font=('Helvetica bold',12))

'''entry1 = tk.Entry (frame) 
canvas.create_window(350, 400, window=entry1)'''
text4 = Label(frame, text="Enter The Generator")
text4.place(x=360,y=110)
text4.config(font=('Helvetica bold',12))

entry2 = tk.Entry (frame,font=('Georgia 20')) 
entry2.place(x = 530,
        y = 110,
        width=350,
        height=30)
text5 = Label(frame, text="Enter The Prime")
text5.place(x=360,y=180)
text5.config(font=('Helvetica bold',12))

entry3 = tk.Entry (frame,font=('Georgia 20')) 
entry3.place(x = 530,
        y = 180,
        width=350,
        height=30)
text6= Label(frame, text="Enter The Message")
text6.place(x=360,y=250)
text6.config(font=('Helvetica bold',12))
entry4 = tk.Entry (frame,font=('Georgia 20')) 
entry4.place(x = 530,
        y = 250,
        width=350,
        height=30)
btnSet = Button(frame, text="Set", bd='5',
                    command=lambda:setTextInput(408301515976774063741225363930200775333880949653971216,2337337002729225098572093778426340936344769375016804739))
btnSet.place(x=520, y=550)
btnSet.config(font=('Helvetica bold',12))

lbl = tk.Label(frame, text = "",bg="#000fff000")
lbl.place(x=325,y=600)
lbl.config(font=('Helvetica bold',12))
lbl2 = tk.Label(frame, text = "",bg="#808080")
lbl2.place(x=40,y=350)
lbl2.config(font=('Helvetica bold',12))
lbl3 = tk.Label(frame, text = "",bg="#808080")
lbl3.place(x=700,y=350)
lbl3.config(font=('Helvetica bold',12))



#canvas.create_window(450, 123, window=entry1)
frame.mainloop()


# In[ ]:




