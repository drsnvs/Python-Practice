
import tkinter

print(dir(tkinter))

window = tkinter.Tk()


# set size of window
window.geometry("500x500")

# not change size of window
# window.resizable(width=False,height=True)

window.title("Darshan's Window")


# need write
label1 = tkinter.Label(window,text="Enter Your Full Name: ")
label1.place(x=0,y=0)

# take input from user
txtbox = tkinter.Entry(window)
txtbox.place(x=130,y=0)

# show to the user
l1 = tkinter.Label(window,text="Answer")
l1.place(x=50,y=50)

l2 = tkinter.Label(window,text="Answer")
l2.place(x=100,y=50)

l3 = tkinter.Label(window,text="Answer")
l3.place(x=150,y=50)

# button
# btn = tkinter.Button(window,text="Enter")
# btn.place(x=0,y=20)

def btn_cmd():
    btn_cmd_txt = txtbox.get()
    splt = btn_cmd_txt.split()
    if btn_cmd_txt:
        if str().join(splt).isalpha():
            l1['text'] = splt[0]
            l2['text'] = splt[1]
            l3['text'] = splt[2]

            print('clicked')
        else:
            print("Enter Valid")



btn1 = tkinter.Button(window,text="Enter",command=btn_cmd)
btn1.place(x=0,y=20)



# Run the window
window.mainloop()