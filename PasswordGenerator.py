from tkinter import *
from random import * 
from pyclip import *

def gp():
	try:
		length = int(ent_length.get())
		if length < 6 or length > 12:
			lab_msg.configure(text="password length should be between 6 and 12 characters")
		else:
			text = "abcdefghijklmnopqrstuvwxyz"

			if uc.get() == 1:
				text = text + text.upper()

			if di.get() == 1:
				text = text + "1234567890"

			if sp.get() == 1:
				text = text + "!@#$%^&*():><"

			text = list(text)
			pw = ""
			for i in range(1, length+1, 1):
				pw = pw + choice(text)
			lab_msg.configure(text=pw)
			copy(pw)
	except ValueError:
		lab_msg.configure(text="please enter integers only")

root = Tk()
root.title("Password Generator App")
root.geometry("800x600+300+50")
f = ("Arial", 30, "bold")

lab_header = Label(root, text="Password Generator", font=f)
lab_length = Label(root, text="Enter Password length: ", font=f)
ent_length = Entry(root, font = f)

uc = IntVar()
cb_uc = Checkbutton(root, text="Uppercase", font=f, variable=uc)
di = IntVar()
cb_di = Checkbutton(root, text="Digits", font=f, variable=di)
sp = IntVar()
cb_sp = Checkbutton(root, text="Special characters", font=f, variable=sp)
btn_generate = Button(root, text="Generate Password", font=f, command=gp)
lab_msg = Label(root, text="", font=f)

lab_header.pack(pady=5)
lab_length.pack(pady=5)
ent_length.pack(pady=5)
cb_uc.pack(pady=5)
cb_di.pack(pady=5)
cb_sp.pack(pady=5)
btn_generate.pack(pady=5)
lab_msg.pack(pady=5)

root.mainloop()

