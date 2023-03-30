# Importing Tkinter module
from tkinter import *
from tkinter.ttk import *

# Creating master Tkinter window
master = Tk()

# Creating object of photoimage class
# Image should be in the same folder
# in which script is saved
p1 = PhotoImage(file = 'privacy.png')

# Setting icon of master window
master.iconphoto(False, p1)

# Creating button# Buttons
# enc_button = Button(my_frame, text="Encrypt", font=("Helvetica", 18), command=encrypt)
# enc_button.grid(row=0, column=0)
#
# dec_button = Button(my_frame, text="Decrypt", font=("Helvetica", 18), command=decrypt)
# dec_button.grid(row=0, column=1, padx=20)
#
# clear_button = Button(my_frame, text="Terminate", font=("Helvetica", 18), command=clear)
# clear_button.grid(row=0, column=2)
#
# # Label
# enc_label = Label(root, text="Encrypt/Decrypt Text...", font=("Helvetica", 14))
# enc_label.pack()


# Label
enc_label = Label(master, text="Encrypt/Decrypt Text...", font=("Helvetica", 14))
enc_label.pack()

# Text Input Field
my_text = Text(master, width=58, height=12)
my_text.pack(pady=10)

password_label = Label(master, text="Enter Your Password in the box below", font=("Helvetica", 14))
password_label.pack()

my_entry = Entry(master, font=("helvetica", 18), width=35, show="*")
my_entry.pack(pady=10)


# Infinite loop can be terminated by
# keyboard or mouse interrupt
# or by any predefined function (destroy())
mainloop()

