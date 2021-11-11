import tkinter
from tkinter import*

question_list = [
    "How many continents are there?",              # pehla question

    "What is the capital of India?",            # doosra question

    "NG mei kaun se course padhaya jaata hai?"    # teesra question
]
options_list = [
    #pehle question ke liye options

    ["1 Four", "2 Nine", "3 Seven", "4 Eight"],

    #second question ke liye options

    ["1 Chandigarh", "2 Bhopal", "3 Chennai", "4 Delhi"],

    #third question ke liye options

    ["1 Software Engineering", "2 Counseling", "3 Tourism", "4 Agriculture"]
]

solution_list=[3, 4, 1]

i=0
def gen():
    global i
    while i<len(question_list):
        print(question_list[i])
        i+=1
        
def startquiz():
    lblQuestion=Label(root,text=question_list[0],font=("consolas",20),width=500,justify="center",wraplength=400)

    lblQuestion.pack()

    radiovar=IntVar()
    radiovar.set(-1)

    r1=Radiobutton(root,text=options_list[0][0],font=("time",15),value=0)
    Variable=radiovar
    r1.pack()

    r2=Radiobutton(root,text=options_list[0][1],font=("time",15),value=1)
    Variable=radiovar
    r2.pack()

    r3=Radiobutton(root,text=options_list[0][2],font=("time",15),value=2)
    Variable=radiovar
    r3.pack()

    r4=Radiobutton(root,text=options_list[0][3],font=("time",15),value=3)
    Variable=radiovar
    r4.pack()


def startIspressed():
    x.destroy()
    y.destroy()
    btn.destroy()
    text.destroy()
    rules.destroy()
    startquiz()
    gen()



root=Tk()

root.title("KBC")

root.geometry("1000x700")

x=Label(root, text="Quizstar",font=("arial",50,"bold"))

x.pack()

y=Label(root,text="welcome to quiz",font=("arial",20,"italic"))

y.place(x=400,y=100)

btn=Button(root,text="start",font=("arial",24,"bold"),bg="blue",command=startIspressed)

btn.place(x=460,y=200)

text=Label(root,text="read the rules and Click start once you are ready",font=("consolas",14))

text.place(x=250,y=300)

rules=Label(root,text="this quiz contains 3 questions",font=("time",14),bg="black",fg="white",width="30",height="2")

rules.place(x=300,y=400)

root.mainloop()