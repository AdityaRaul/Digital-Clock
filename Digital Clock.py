#!/usr/bin/env python
# coding: utf-8

# In[12]:


from tkinter import *
from time import strftime
def time():
    string=strftime('%I:%M:%S  %p')
    L.configure(text=string)
    L.after(1000,time)
w=Tk()
w.title("Clock")
L=Label(w,font=('Arial',50,'bold'),bg='purple',fg='light gray')
L.pack(anchor='center')
time()
w.mainloop()


# In[ ]:




