import tkinter as tk
#creating window
window=tk.Tk()

#creating canvas
canvas1 = tk.Canvas(window, width = 400, height = 300, bg="purple")
canvas1.pack()

#creating USERNAME label
a1=tk.Label(window, text="USERNAME: ", fg="black")
canvas1.create_window(50, 90, window=a1)

#creating PASSWORD label
a2=tk.Label(window, text="PASSWORD: ", fg="black")
canvas1.create_window(50, 120, window=a2)

#entry box for password
entry1 = tk.Entry (window) 
canvas1.create_window(150, 90, window=entry1)

#entry box for username
entry2 = tk.Entry (window) 
canvas1.create_window(150, 120, window=entry2)

# sex type
female=tk.Label(window, text="Sex Type: ", bg="purple", fg="yellow")
canvas1.create_window(300, 70, window=female)
radio= tk.IntVar()
R1=tk.Radiobutton(window, text="male",variable=radio,value=1,bg="purple",fg="black")
canvas1.create_window(300, 90, window=R1)
R2=tk.Radiobutton(window, text="female",variable=radio,value=2,bg="purple",fg="black")
canvas1.create_window(305, 110, window=R2)
               
#function that checks if username and password are correct or not
def gett():
    x1=entry1.get()
    x2=entry2.get()
    if x1=="arman" and x2=="1234":
         label1 = tk.Label(window, text= "WELCOME USER")
         canvas1.create_window(80, 50, window=label1)
    else:
        label1 = tk.Label(window, text= "WRONG COMBO", fg="red")
        canvas1.create_window(80, 50, window=label1)
        
def mrmiss():
    y1=radio.get()
    if y1== True:
         label1 = tk.Label(window, text= "Hello MR.")
         canvas1.create_window(80, 20, window=label1)
    else:
        label1 = tk.Label(window, text= "Hello Miss")
        canvas1.create_window(80, 20, window=label1)

def run():
    gett()
    mrmiss()
        
#button for submiting
button1 = tk.Button(text='submit',command=run, activebackground="green", activeforeground="black", font="50")
canvas1.create_window(45, 155, window=button1)

#button for exiting the program
button2 = tk.Button(text='QUIT',command=quit, activebackground="red")
canvas1.create_window(30, 270, window=button2)
window.mainloop()
