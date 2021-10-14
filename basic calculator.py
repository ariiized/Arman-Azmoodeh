from tkinter import *

def btnClick(number):
    global operator
    operator= operator+ str(number) 
    text_input.set(operator)

def btnEqual():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator=''

def btnClear():
    global operator
    operator=''
    text_input.set('')


# G U I
window= Tk()
window.title("CALCULATOR")

text_input= StringVar()
text_display=Entry(window, font=("arial",20, "bold"), textvariable=text_input, bd=30, insertwidth=4, bg="powder blue",justify="right").grid(columnspan=4)
operator= ''

#buttons
bt0=Button(window, padx=16, pady=16, bd=10, fg='purple', font=("arial",20, "bold"), text='0',command= lambda:btnClick(0) ).grid(row=4 , column= 1)
bt1=Button(window, padx=16, pady=16, bd=10, fg='purple', font=("arial",20, "bold"), text='1',command= lambda:btnClick(1) ).grid(row=1 , column= 0)
bt2=Button(window, padx=16, pady=16, bd=10, fg='purple', font=("arial",20, "bold"), text='2',command= lambda:btnClick(2) ).grid(row=1 , column= 1)
bt3=Button(window, padx=16, pady=16, bd=10, fg='purple', font=("arial",20, "bold"), text='3',command= lambda:btnClick(3) ).grid(row=1 , column= 2)
bt4=Button(window, padx=16, pady=16, bd=10, fg='purple', font=("arial",20, "bold"), text='4',command= lambda:btnClick(4) ).grid(row=2 , column= 0)
bt5=Button(window, padx=16, pady=16, bd=10, fg='purple', font=("arial",20, "bold"), text='5',command= lambda:btnClick(5) ).grid(row=2 , column= 1)
bt6=Button(window, padx=16, pady=16, bd=10, fg='purple', font=("arial",20, "bold"), text='6',command= lambda:btnClick(6) ).grid(row=2 , column= 2)
bt7=Button(window, padx=16, pady=16, bd=10, fg='purple', font=("arial",20, "bold"), text='7',command= lambda:btnClick(7) ).grid(row=3 , column= 0)
bt8=Button(window, padx=16, pady=16, bd=10, fg='purple', font=("arial",20, "bold"), text='8',command= lambda:btnClick(8) ).grid(row=3 , column= 1)
bt9=Button(window, padx=16, pady=16, bd=10, fg='purple', font=("arial",20, "bold"), text='9',command= lambda:btnClick(9) ).grid(row=3 , column= 2)

btClear=Button(window, padx=10, pady=10, bd=10, fg='red', font=("arial",20, "bold"), text='C',command=btnClear ).grid(row=4 , column= 0)
btEnter=Button(window, padx=10, pady=10, bd=10, fg='green', font=("arial",20, "bold"), text='=',command=btnEqual ).grid(row=4 , column= 2)

addiction=Button(window, padx=16, pady=16, bd=10, fg='black', font=("arial",20, "bold"), text='+',command= lambda:btnClick('+') ).grid(row=1 , column= 3)
subtraction=Button(window, padx=16, pady=16, bd=10, fg='black', font=("arial",20, "bold"), text='-',command= lambda:btnClick('-') ).grid(row=2 , column= 3)
division=Button(window, padx=16, pady=16, bd=10, fg='black', font=("arial",20, "bold"), text='/',command= lambda:btnClick('/') ).grid(row=3 , column= 3)
multiplication=Button(window, padx=16, pady=16, bd=10, fg='black', font=("arial",20, "bold"), text='*',command= lambda:btnClick('*') ).grid(row=4 , column= 3)

credit=Label(window, text="by Arman A",font=("arial",10, "bold"), fg='black').grid(row=5, column=1)
window.mainloop()