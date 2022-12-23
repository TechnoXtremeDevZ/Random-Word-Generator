# -*- coding: utf-8 -*-
from tkinter import *
import random

root=Tk()
root.title("Random Word Generator")
root.geometry("500x500")

label_random_word = Label(root)

def randomWord():
    alpha_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    
    random_no1 = random.randint(1, 26)
    random_no2 = random.randint(1, 26)
    random_no3 = random.randint(1, 26)
    random_no4 = random.randint(1, 26)
    random_no5 = random.randint(1, 26)

    random_alpha1 = alpha_list[random_no1]
    random_alpha2 = alpha_list[random_no2]
    random_alpha3 = alpha_list[random_no3]
    random_alpha4 = alpha_list[random_no4]
    random_alpha5 = alpha_list[random_no5]
    
    label_random_word["text"] = random_alpha1 + random_alpha2 + random_alpha3 + random_alpha4 + random_alpha5
    
btn = Button(root, text="Generate Random Numbers", command=randomWord, bg="medium aquamarine", fg="white")
btn.place(relx=0.5, rely=0.4, anchor=CENTER)

label_random_word.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()