import random
from tkinter import *
import emoji 

root=Tk()
root.geometry("700x450")

l1=Label(root,font=("roboto",200))

def compchoice():
    l=['Rock','Paper','Scissor']
    b=l[random.randint(0,2)]
    g_dict={'rock':1,'paper':2,'scissor':3}
    A=g_dict.get(b.lower())
    return(A)
    #computer choice is returned

def printcmpchoice(cmpchoice):
    T= Label(root, text="Computer's Choice: ",font=100)
    T.place(x=160,y=215)
    if(cmpchoice==1):
        dd=Button(root,text=emoji.emojize(":fist:", use_aliases=True),font=100,width=6,height=2)
        dd.place(x=340,y=200)
    elif(cmpchoice==2):
        dd2=Button(root,text=emoji.emojize(":raised_hand:"),font=100,width=6,height=2)
        dd2.place(x=340,y=200)
    elif(cmpchoice==3):
        dd3=Button(root,text=emoji.emojize(":v:", use_aliases=True),font=100,width=6,height=2)
        dd3.place(x=340,y=200)
    

def game(a):
    userchoice=a
    cmpchoice=compchoice()
    
    l=['Rock','Paper','Scissor']
    print (l[cmpchoice-1])

    printcmpchoice(cmpchoice)

    dif=userchoice-cmpchoice

    if(dif==0):
        L1 = Label(root, text='         MATCH IS DRAW :-/      ',font=100)
        L1.place(x=225,y=300)
    elif(dif== 1 or dif==-2):
        L1 = Label(root, text='        YOU WIN!! :-)        ',font=100)
        L1.place(x=265,y=300)
    elif(dif==-1 or dif==2):
        L1 = Label(root, text='   COMPUTER WINS :-(',font=100)
        L1.place(x=265,y=300)

def rock():
    game(1)
    return()

def paper():
    game(2)
    return()

def scissor():
    game(3)
    return()

#the fn
def rolld():
    Rock=Button(root,text=emoji.emojize(":fist:", use_aliases=True),font=100,width=6,height=2,command=rock)
    Rock.place(x=240,y=100)
    Paper=Button(root,text=emoji.emojize(":raised_hand:"),font=100,width=6,height=2,command=paper)
    Paper.place(x=340,y=100)
    Scissor=Button(root,text=emoji.emojize(":v:", use_aliases=True),font=100,width=6,height=2,command=scissor)
    Scissor.place(x=440,y=100)


def resetAll():
    root.destroy()


#button code+postion
b1=Button(root,text="Lets Play!!",command=rolld,font=300)
b1.place(x=320,y=20)
ff = Button(root, text='EXIT', command=resetAll)
ff.place(x=350,y=400)


root.mainloop()