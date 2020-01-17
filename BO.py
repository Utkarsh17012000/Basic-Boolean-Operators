import tkinter
from tkinter import *
from tkinter import messagebox
window=Tk()
window.geometry("1366x768")
window.title("Validation")
window.config(bg='PaleGreen4') 

def delete():
    window1.destroy()

def success():
    introwindow=Toplevel(window)
    introwindow.geometry('1366x768')
    introwindow.title('Introduction')
    introwindow.config(bg='lemon chiffon')
    
    def and_def():
        def and_execution():
            conv1=int(A_value.get())
            conv1=bin(conv1)
            conv1=conv1[2:]
            conv2=int(B_value.get())
            conv2=bin(conv2)
            conv2=conv2[2:]
            
            Ans=int(A_value.get()) & int(B_value.get())
            rname["text"]="Result                     " + str(Ans)

            conv3=bin(Ans)
            conv3=conv3[2:]
            bin1["text"]="Operand in Binary:        " + str(conv1)
            bin2["text"]="Operand in Binary:        " + str(conv2)
            bin3["text"]="Result in Binary:        " + str(conv3)
            
             
        and_window=Toplevel(introwindow)
        and_window.geometry('1366x768')
        and_window.title('AND OPERATION WINDOW')
        and_window.config(bg='green')
    
        Label(and_window,text='Enter 1 Operand: ',cursor='arrow',bd=10,font=('Times New Roman',20,'bold','underline'),height=2,width=15,anchor=W,relief=GROOVE).place(x=100,y=50)
        bin1=Label(and_window,text='Operand in Binary: ',cursor='arrow',bd=10,font=('Times New Roman',20,'bold','underline'),height=2,width=25,anchor=W,relief=GROOVE)
        bin1.place(x=750,y=50)
        A_value=Entry(and_window,cursor='arrow',bd=10,font=('Times New Roman',20,'bold','underline'),width=10,relief=SUNKEN)
        A_value.place(x=500,y=60)
        Label(and_window,text='Enter 2 Operand: ',cursor='arrow',bd=10,font=('Times New Roman',20,'bold','underline'),height=2,width=15,anchor=W,relief=GROOVE).place(x=100,y=150)
        bin2=Label(and_window,text='Operand in Binary: ',cursor='arrow',bd=10,font=('Times New Roman',20,'bold','underline'),height=2,width=25,anchor=W,relief=GROOVE)
        bin2.place(x=750,y=150)
        B_value=Entry(and_window,cursor='arrow',bd=10,font=('Times New Roman',20,'bold','underline'),width=10,relief=SUNKEN)
        B_value.place(x=500,y=160)
        bin3=Label(and_window,text='Operand in Binary: ',cursor='arrow',bd=10,font=('Times New Roman',20,'bold','underline'),height=2,width=25,anchor=W,relief=GROOVE)
        bin3.place(x=750,y=400)

        Button(and_window,text='AND',bd=10,font=('Times New Roman',20,'bold'),width=8,relief=SUNKEN,command=and_execution).place(x=500,y=260)
        
        rname=Label(and_window,bd=10,font=('Times New Roman',20,'bold'),relief=SUNKEN,text='Result: ')
        rname.place(x=100,y=400)

    def or_def():
        def or_execution():
            conv1=int(A_value.get())
            conv1=bin(conv1)
            conv1=conv1[2:]
            conv2=int(B_value.get())
            conv2=bin(conv2)
            conv2=conv2[2:]

            Ans=int(A_value.get()) | int(B_value.get())
            rname["text"]="Result                     " + str(Ans)

            conv3=bin(Ans)
            conv3=conv3[2:]
            
            bin1["text"]="Operand in Binary:        " + str(conv1)
            bin2["text"]="Operand in Binary:        " + str(conv2)
            bin3["text"]="Result in Binary:        " + str(conv3)
                
        or_window=Toplevel(introwindow)
        or_window.geometry('1366x768')
        or_window.title('OR OPERATION WINDOW')
        or_window.config(bg='RED')
        
        Label(or_window,text='Enter 1 Operand: ',cursor='arrow',bd=10,font=('Times New Roman',20,'bold','underline'),height=2,width=15,anchor=W,relief=GROOVE).place(x=100,y=50)
        bin1=Label(or_window,text='Operand in Binary: ',cursor='arrow',bd=10,font=('Times New Roman',20,'bold','underline'),height=2,width=25,anchor=W,relief=GROOVE)
        bin1.place(x=750,y=50)
        A_value=Entry(or_window,cursor='arrow',bd=10,font=('Times New Roman',20,'bold','underline'),width=10,relief=SUNKEN)
        A_value.place(x=500,y=60)
        Label(or_window,text='Enter 2 Operand: ',cursor='arrow',bd=10,font=('Times New Roman',20,'bold','underline'),height=2,width=15,anchor=W,relief=GROOVE).place(x=100,y=150)
        bin2=Label(or_window,text='Operand in Binary: ',cursor='arrow',bd=10,font=('Times New Roman',20,'bold','underline'),height=2,width=25,anchor=W,relief=GROOVE)
        bin2.place(x=750,y=150)
        B_value=Entry(or_window,cursor='arrow',bd=10,font=('Times New Roman',20,'bold','underline'),width=10,relief=SUNKEN)
        B_value.place(x=500,y=160)
        bin3=Label(or_window,text='Operand in Binary: ',cursor='arrow',bd=10,font=('Times New Roman',20,'bold','underline'),height=2,width=25,anchor=W,relief=GROOVE)
        bin3.place(x=750,y=400)

        Button(or_window,text='OR',bd=10,font=('Times New Roman',20,'bold'),width=8,relief=SUNKEN,command=or_execution).place(x=500,y=260)
        
        rname=Label(or_window,bd=10,font=('Times New Roman',20,'bold'),relief=SUNKEN,text='Result: ')
        rname.place(x=100,y=400)
    
    def xor_def():
        def xor_execution():
            conv1=int(A_value.get())
            conv1=bin(conv1)
            conv1=conv1[2:]
            conv2=int(B_value.get())
            conv2=bin(conv2)
            conv2=conv2[2:]

            Ans=int(A_value.get()) ^ int(B_value.get())
            rname["text"]="Result                     " + str(Ans)

            conv3=bin(Ans)
            conv3=conv3[2:]
            
            bin1["text"]="Operand in Binary:        " + str(conv1)
            bin2["text"]="Operand in Binary:        " + str(conv2)
            bin3["text"]="Result in Binary:        " + str(conv3)
                
        xor_window=Toplevel(introwindow)
        xor_window.geometry('1366x768')
        xor_window.title('XOR OPERATION WINDOW')
        xor_window.config(bg='blue')

        Label(xor_window,text='Enter 1 Operand: ',cursor='arrow',bd=10,font=('Times New Roman',20,'bold','underline'),height=2,width=15,anchor=W,relief=GROOVE).place(x=100,y=50)
        bin1=Label(xor_window,text='Operand in Binary: ',cursor='arrow',bd=10,font=('Times New Roman',20,'bold','underline'),height=2,width=25,anchor=W,relief=GROOVE)
        bin1.place(x=750,y=50)
        A_value=Entry(xor_window,cursor='arrow',bd=10,font=('Times New Roman',20,'bold','underline'),width=10,relief=SUNKEN)
        A_value.place(x=500,y=60)
        Label(xor_window,text='Enter 2 Operand: ',cursor='arrow',bd=10,font=('Times New Roman',20,'bold','underline'),height=2,width=15,anchor=W,relief=GROOVE).place(x=100,y=150)
        bin2=Label(xor_window,text='Operand in Binary: ',cursor='arrow',bd=10,font=('Times New Roman',20,'bold','underline'),height=2,width=25,anchor=W,relief=GROOVE)
        bin2.place(x=750,y=150)
        B_value=Entry(xor_window,cursor='arrow',bd=10,font=('Times New Roman',20,'bold','underline'),width=10,relief=SUNKEN)
        B_value.place(x=500,y=160)
        bin3=Label(xor_window,text='Operand in Binary: ',cursor='arrow',bd=10,font=('Times New Roman',20,'bold','underline'),height=2,width=25,anchor=W,relief=GROOVE)
        bin3.place(x=750,y=400)

        Button(xor_window,text='XOR',bd=10,font=('Times New Roman',20,'bold'),width=8,relief=SUNKEN,command=xor_execution).place(x=500,y=260)
        
        rname=Label(xor_window,bd=10,font=('Times New Roman',20,'bold'),relief=SUNKEN,text='Result: ')
        rname.place(x=100,y=400)

    def not_def():
        def not_execution():
            conv1=int(A_value.get())
            conv1=bin(conv1)
            conv1=conv1[2:]
            Ans=~(int(A_value.get()))
            rname["text"]="Result                     " + str(Ans)
            
            conv2=bin(Ans)
            conv2=conv2[3:]
            bin1["text"]="Result                     " + str(conv2)

        not_window=Toplevel(introwindow)
        not_window.geometry('1366x768')
        not_window.title('NOT OPERATION WINDOW')
        not_window.config(bg='yellow')
        
        Label(not_window,text='Enter  Operand: ',cursor='arrow',bd=10,font=('Times New Roman',20,'bold','underline'),height=2,width=15,anchor=W,relief=GROOVE).place(x=100,y=50)
        bin1=Label(not_window,text='Operand in Binary: ',cursor='arrow',bd=10,font=('Times New Roman',20,'bold','underline'),height=2,width=25,anchor=W,relief=GROOVE)
        bin1.place(x=750,y=50)
        A_value=Entry(not_window,cursor='arrow',bd=10,font=('Times New Roman',20,'bold','underline'),width=10,relief=SUNKEN)
        A_value.place(x=500,y=60)

        Button(not_window,text='NOT',bd=10,font=('Times New Roman',20,'bold'),width=15,relief=SUNKEN,command=not_execution).place(x=800,y=160)
        
        rname=Label(not_window,bd=10,font=('Times New Roman',20,'bold'),relief=SUNKEN,text='Result: ')
        rname.place(x=500,y=250)

    Label(introwindow,text='Introduction',cursor='arrow',bd=10,font=('Times New Roman',20,'bold','underline'),fg='green',height=2,width=10,anchor=W,relief=SUNKEN).place(x=8,y=10)
    Label(introwindow,cursor='pencil',bg='black',fg='white',bd=2,font=('Times New Roman',16),height=6,width=105,anchor=NW,justify=LEFT,relief=RAISED,wraplength=1250,text="In electronics, a logic gate is an idealized or physical device implementing a Boolean function; that is, it performs a logical operation on one or more binary inputs and produces a single binary output. Depending on the context, the term may refer to an ideal logic gate, one that has for instance zero rise time and unlimited fan-out, or it may refer to a non-ideal physical device. Logic gates are primarily implemented using diodes or transistors acting as electronic switches, but can also be constructed using vacuum tubes, electromagnetic relays (relay logic), fluidic logic, pneumatic logic, optics, molecules, or even mechanical elements. With amplification, logic gates can be cascaded in the same way that Boolean functions can be composed, allowing the construction of a physical model of all of Boolean logic, and therefore, all of the algorithms and mathematics that can be described with Boolean logic.").place(x=50,y=130)

    Label(introwindow,text='History',cursor='arrow',bd=10,font=('Times New Roman',20,'bold','underline'),fg='green',height=2,width=10,anchor=W,relief=SUNKEN).place(x=8,y=290)
    Label(introwindow,cursor='pencil',bg='black',fg='white',bd=2,font=('Times New Roman',16),height=10,width=105,anchor=NW,justify=LEFT,relief=RAISED,wraplength=1250,text="The binary number system was refined by Gottfried Wilhelm Leibniz (published in 1705), influenced by the ancient I Ching's binary system. Leibniz established that, by using the binary system, the principles of arithmetic and logic could be combined.In an 1886 letter, Charles Sanders Peirce described how logical operations could be carried out by electrical switching circuits. Eventually, vacuum tubes replaced relays for logic operations. Lee De Forest's modification, in 1907, of the Fleming valve can be used as a logic gate. Ludwig Wittgenstein introduced a version of the 16-row truth table of Tractatus Logico-Philosophicus (1921). Walther Bothe, inventor of the coincidence circuit, got part of the 1954 Nobel Prize in physics, for the first modern electronic AND gate in 1924. Konrad Zuse designed and built electromechanical logic gates for his computer Z1 (from 1935–38).From 1934 to 1936, NEC engineer Akira Nakashima introduced switching circuit theory in a series of papers showing that two-valued Boolean algebra, which he discovered independently, can describe the operation of switching circuits. His work was later cited by Claude E. Shannon, who elaborated on the use of Boolean algebra in the analysis and design of switching circuits in 1937. Using this property of electrical switches to implement logic is the fundamental concept that underlies all electronic digital computers. Switching circuit theory became the foundation of digital circuit design, as it became widely known in the electrical engineering community during and after World War II, with theoretical rigor superseding the ad hoc methods that had prevailed previously.").place(x=50,y=420)

    menubar=Menu(introwindow)

    operationmenu=Menu(menubar,tearoff=0)
    operationmenu.add_command(label="AND",command=and_def)
    operationmenu.add_command(label="OR",command=or_def)
    operationmenu.add_separator()                          
    operationmenu.add_command(label="NOT",command=not_def)
    operationmenu.add_command(label="XOR",command=xor_def)
    menubar.add_cascade(label='Operation',menu=operationmenu)

    exitmenu=Menu(menubar,tearoff=0)
    exitmenu.add_command(label='Quit',command=introwindow.destroy)
    menubar.add_cascade(label='Exit',menu=exitmenu)

    introwindow.config(menu=menubar)

    introwindow.mainloop()


def error():
    
    global window1
    window1=Toplevel(window)
    window1.geometry("500x500")
    window1.title("Warning")
    Label(window1,text="All fields required//Gmail is Incorrect",fg="red").pack()
    Button(window1,text="OK",command=delete).pack()
    window1.mainloop()
def Submit():
    name_text=name.get()
    Gmail_text=Gmail.get()
    import sqlite3
    x=sqlite3.connect("xyz.db")
    print("Success")
    #x.execute("create table dataa(name stringvar,Gmail stringvar)")
    x.execute("insert into dataa values(?,?)",(name_text,Gmail_text))
    x.commit()
    x.close()
    c=sqlite3.connect("xyz.db")
    cursor=c.execute("select name,Gmail from dataa")
    for i in cursor:
        print(i)

    if name_text=="":
        error()
    elif Gmail_text=="":
        error()
    else:
        success()
       

Label(window,text='Basic Logic Gates Calculations',cursor='arrow',bd=10,font=('Times New Roman',40,'bold','underline'),fg='bisque2',bg='cadetblue',height=3,width=40,anchor=CENTER,relief=SUNKEN).place(x=35,y=10)
Label(window,text='Name: ',cursor='arrow',bd=10,font=('Times New Roman',20,'bold','underline'),height=2,bg='dark orange',width=15,anchor=W,relief=GROOVE).place(x=50,y=300)
Label(window,text='Gmail: ',cursor='arrow',bd=10,font=('Times New Roman',20,'bold','underline'),height=2,bg='dark orange',width=15,anchor=W,relief=GROOVE).place(x=50,y=400)
'''
canvas=Canvas(window).pack()
Imagee=PhotoImage(file="E:\\my2.png")
canvas.create_image(10,20, anchor=SE,image=Imagee)
'''
name=StringVar()
Gmail=StringVar()

Entry(window,textvariable=name,cursor='arrow',bd=10,fg='azure',font=('Times New Roman',15,'bold'),bg='black',width=20,relief=SUNKEN).place(x=350,y=325)
Entry(window,textvariable=Gmail,cursor='arrow',fg='azure',bd=10,font=('Times New Roman',15,'bold'),bg='black',width=20,relief=SUNKEN).place(x=350,y=425)

Button(window,text='Submit',cursor='spider',bg='black',fg='red',bd=10,font=('Times New Roman',20,'bold'),width=15,relief=SUNKEN,command=Submit).place(x=700,y=500)

