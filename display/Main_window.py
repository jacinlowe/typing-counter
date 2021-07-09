from tkinter import *
from tkinter import WORD
from timeit import default_timer as timer

import random
import json


window_size = '500x250'
font_type = 'times'
font_size = '20'
font = f"{font_type} {font_size}"

window = Tk()

window.geometry(window_size)

x = 0

sentences_list: list

with open("../utilites/sentences.json") as file:
    sentences_list = json.load(file)['sentences']


def game():
    global x
    global sentences_list
    wpm = 0
    if x == 0:
        window.destroy()
        x += 1


    def check_result(event=None):
        if entry.get() == sentences_list[word]:

            end = timer()
            print(round(end-start, 2))
        else:
            print("Wrong Input")

    def words_per_min():
        temp_list = words.split(' ')

        return f'{len(temp_list)}'

    def keypress(event):
        w = Label(windows, text='Keypress: '+event.char)
        w.place(x=200, y=200)
    # words = ['programming', 'coding', 'algorithim', 'systems', 'python', 'software']

    word = random.randint(0, (len(sentences_list)-1))

    start = timer()
    windows = Tk()
    windows.geometry(window_size)

    words = sentences_list[word]

    x2 = Label(windows, text=words, font=font, wraplength=400, justify=CENTER)
    x2.place(x=10, y=10)
    L_wpm = Label(windows, text="words per min: " + words_per_min(), font=font)
    L_wpm.place(x=10, y=130)

    L_stTyping = Label(windows, text="Start Typing:", font=font)
    L_stTyping.place(x=10, y=50)

    entry = Entry(windows)
    entry.place(x=200, y=55)

    b_done = Button(windows, text='Done', command=check_result, width=12, bg='grey')
    windows.bind('<Return>', check_result)
    b_done.place(x=150, y=100)



    b3 = Button(windows, text='Try Again', command=game, width=12, bg="grey")
    b3.place(x=250, y=100)
    windows.mainloop()



x1 = Label(window, text='Lets start Playing...', font=font)
x1.place(x=10, y=50)
b1 = Button(window, text='Go', command=game, width=12, bg='grey')
b1.place(x=50, y=100)


window.mainloop()
