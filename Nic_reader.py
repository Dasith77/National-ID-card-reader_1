from tkinter import*
#from PIL import ImageTk,Image
          
window =Tk()

window.title(" NIC card reader from #Dasith#")

window.configure(background="black")

def click():
     
     x=textentry.get()
     if len(x)<=10:
         a=int(1900+int(x[0:2]))
         k=int(x[2:5])
     else:
         a=int(x[0:4])
         k=int(x[4:7])
     if k<500:
         aaa=("Male")
         cc=k
     else:
         aaa=("Female")
         cc=(k-500)
     if 0<cc<=31:
         b=1
         c=cc
     elif 31<cc<=60:
         b=2
         c=(cc-31)
     elif 60<cc<=91:
         b=3
         c=(cc-60)
     elif 91<cc<=121:
         b=4
         c=(cc-91)
     elif 121<cc<=152:
         b=5
         c=(cc-121)
     elif 152<cc<=182:
         b=6
         c=(cc-152)
     elif 182<cc<=213:
         b=7
         c=(cc-182)
     elif 213<cc<=244:
         b=8
         c=(cc-213)
     elif 244<cc<=274:
         b=9
         c=(cc-244)
     elif 274<cc<=305:
         b=10
         c=(cc-274)
     elif 305<cc<=335:
         b=11
         c=(cc-305)
     else:
         b=12
         c=(cc-335)
     ccc=(a,"/",b,"/",c)
     import datetime
     d=datetime.datetime(a,b,c)
     dt=datetime.datetime.today()
     ddd=(dt-d)
     tdelta=datetime.timedelta(days=365.25)
     t1delta=datetime.timedelta(days=30.5)
     s=((dt-d)//tdelta)
     u=((dt-d)%tdelta)
     ss=((u)//t1delta)
     zz=(u%t1delta)
     kk=datetime.timedelta(days=1)
     eee=("year=",s, "month=",ss)
     if s>=18:
          fff=("you are an elder")
     else:
          fff=("child")
    
     x1.set(aaa)
     x2.set(ccc)
     x3.set(ddd)
     x4.set(eee)
     x5.set(fff)
     
Label(window,text="NIC Reader",bg="green",fg="white",font="none 22 bold").grid(row=0,column=1,sticky=W)
#create lable
Label(window,text="Enter your NIC number:",bg="light yellow",fg="black",font="none 12 bold").grid(row=1,column=1,sticky=W)

#create atext entry box
textentry=Entry(window,font="none 12 bold",width=20,bg="white",fg="black")
textentry.grid(row=2,column=1)

#add a submit button
Button(window,text="SUBMIT",width=6,bg="yellow",command=click).grid(row=3,column=1)
def deletx():
     textentry.delete(0,END)
     #a1.delete(0,END)
     #a2.delete(0,END)
     #a3.delete(0,END)
     #a4.delete(0,END)
     #a5.delete(0,END)
Button(window,text="RESET",width=6,bg="yellow",command=deletx).grid(row=3,column=2)






#create another lable



x1=StringVar()
x2=StringVar()
x3=StringVar()
x4=StringVar()
x5=StringVar()
#create a text box
Label(window,width=50,font="none 12 bold",text="Gender:",bg="black",foreground="white").grid(row=5,column=1,columnspan=1)
a1=Label(window,width=100,font="none 10 bold",textvariable=x1,height=2,background="red",foreground="white")
a1.grid(row=6,column=1,columnspan=1,sticky=W)
Label(window,width=50,font="none 12 bold",text="Your Birthday is:",bg="black",foreground="white").grid(row=7,column=1)
a2=Label(window,width=100,font="none 10 bold",textvariable=x2,height=2,background="orange",foreground="white")
a2.grid(row=8,column=1,columnspan=1,sticky=W)
Label(window,width=50,font="none 12 bold",text="You Have Lived:",bg="black",foreground="white").grid(row=9,column=1)
a3=Label(window,width=100,font="none 10 bold",textvariable=x3,height=2,background="blue",foreground="white")
a3.grid(row=10,column=1,columnspan=1,sticky=W)
Label(window,width=50,font="none 12 bold",text="Now Your Age:",bg="black",foreground="white").grid(row=11,column=1)
a4=Label(window,width=100,font="none 10 bold",textvariable=x4,height=2,background="indigo",foreground="white")
a4.grid(row=12,column=1,columnspan=1,sticky=W)
Label(window,width=50,font="none 12 bold",text="Your Current Situation:",bg="black",foreground="white").grid(row=13,column=1)
a5=Label(window,width=100,font="none 10 bold",textvariable=x5,height=2,background="purple",foreground="white")
a5.grid(row=14,column=1,columnspan=1,sticky=W)


Label(window,text="Click here to exit:",bg="black",fg="white",font="none 12 bold").grid(row=15,column=0,sticky=W)
def cl():
     window.destroy()
     exit()




Button(window,text="EXIT",width=12,command=cl).grid(row=16,column=0,sticky=W)










window.mainloop()




















    


