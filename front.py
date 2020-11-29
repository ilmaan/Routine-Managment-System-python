from tkinter import *
import back

def getselrow(event):
    global selrow 
    index = list.curselection()[0]
    selrow = list.get(index)
    e1.delete(0,END)
    e1.insert(END,selrow[1])
    e2.delete(0,END)
    e2.insert(END,selrow[2])
    e3.delete(0,END)
    e3.insert(END,selrow[3])
    e4.delete(0,END)
    e4.insert(END,selrow[4])
    e5.delete(0,END)
    e5.insert(END,selrow[5])
    e6.delete(0,END)
    e6.insert(END,selrow[6])
    
def deletecom():
    back.delete(selrow[0])


def viewcom():
    list.delete(0,END)
    for row in back.view():
        list.insert(END,row)

def searchcom():
    list.delete(0,END)
    for row in back.search(datev.get(),wakev.get(),grev.get(),majorv.get(),univ.get(),ielv.get()):
        list.insert(END,row)

def addcom():
    back.insert(datev.get(),wakev.get(),grev.get(),majorv.get(),univ.get(),ielv.get())

    list.delete(0,END)
    list.insert(END,(datev.get(),wakev.get(),grev.get(),majorv.get(),univ.get(),ielv.get()))



win = Tk()

win.wm_title('Routine Managment System')

l1 = Label(win,text='Date')
l1.grid(row=1,column=1)

l2 = Label(win,text='Wake Time')
l2.grid(row=1,column=3)

l3 = Label(win,text='GRE PREP')
l3.grid(row=2,column=1)

l4 = Label(win,text='Major Project')
l4.grid(row=2,column=3)

l5 = Label(win,text='University Search')
l5.grid(row=3,column=1)

l6 = Label(win,text='IELTS/TOEFL PREP')
l6.grid(row=3,column=3)


datev = StringVar()
e1 = Entry(win,textvariable=datev)
e1.grid(row=1,column=2)

wakev = StringVar()
e2 = Entry(win,textvariable=wakev)
e2.grid(row=1,column=4)

grev = StringVar()
e3 = Entry(win,textvariable=grev)
e3.grid(row=2,column=2)

majorv = StringVar()
e4 = Entry(win,textvariable=majorv)
e4.grid(row=2,column=4)

univ = StringVar()
e5 = Entry(win,textvariable=univ)
e5.grid(row=3,column=2)

ielv = StringVar()
e6 = Entry(win,textvariable=ielv)
e6.grid(row=3,column=4)


list = Listbox(win,height=8,width=50)
list.grid(row=4,column=1,rowspan=9,columnspan=2)

# sb= Scrollbar(win)
# sb.grid(row=4,column=3,rowspan=9)

list.bind('<<ListboxSelection>>',getselrow)

b1 = Button(win,text="ADD",width=12,pady=5,padx=5,command=addcom)
b1.grid(row=5,column=4)

b2 = Button(win,text="Search",width=12,pady=5,padx=5,command=searchcom)
b2.grid(row=6,column=4)

b3 = Button(win,text="Delete",width=12,pady=5,padx=5,command=deletecom)
b3.grid(row=7,column=4)

b4 = Button(win,text="View All",width=12,pady=5,padx=5,command=viewcom)
b4.grid(row=8,column=4)

b5 = Button(win,text="Close",width=12,pady=5,padx=5,command= win.destroy)
b5.grid(row=9,column=4)










win.mainloop()