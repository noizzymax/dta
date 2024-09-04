from tkinter import *
from tkinter import filedialog
from tkinter import ttk

from velocity import *
from amorts import *

label_cog = []
label_time, label_vy, label_vz, label_rx = [], [], [], []
label_entry_time, entry_time, scale_time, button_time = [], [], [], []

res_time = []

label_am1, label_am2, label_am3, label_am4 = [], [], [], []


def choose_file_cog():
    global label_cog, scale_time

    file_name = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                           filetypes=(("XOB files", "*.xob*"), ("all files", "*.*")))
    # file_name = "../bin/data/data.xob"
    label_cog.config(text=file_name)
    min_time, max_time = load_cog(file_name)
    scale_time = ttk.Scale(orient=HORIZONTAL, length=200, from_=min_time, to=max_time, value=min_time,
                           variable=res_time)
    scale_time.pack()
    scale_time.place(x=210, y=130)


def choose_file_amort1():
    global label_am1

    file_name_st = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                              filetypes=(("XOB files", "*.xob*"), ("all files", "*.*")))
    file_name_am = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                              filetypes=(("XOB files", "*.xob*"), ("all files", "*.*")))
    label_am1.config(text="Static point: " + file_name_st + "\nAmort point: " + file_name_am)
    load_amort(file_name_st, file_name_am, 1)


def choose_file_amort2():
    global label_am2

    file_name_st = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                              filetypes=(("XOB files", "*.xob*"), ("all files", "*.*")))
    file_name_am = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                              filetypes=(("XOB files", "*.xob*"), ("all files", "*.*")))
    label_am2.config(text="Static point: " + file_name_st + "\nAmort point: " + file_name_am)
    load_amort(file_name_st, file_name_am, 2)


def choose_file_amort3():
    global label_am1

    file_name_st = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                              filetypes=(("XOB files", "*.xob*"), ("all files", "*.*")))
    file_name_am = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                              filetypes=(("XOB files", "*.xob*"), ("all files", "*.*")))
    label_am3.config(text="Static point: " + file_name_st + "\nAmort point: " + file_name_am)
    load_amort(file_name_st, file_name_am, 3)


def choose_file_amort4():
    global label_am1

    file_name_st = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                              filetypes=(("XOB files", "*.xob*"), ("all files", "*.*")))
    file_name_am = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                              filetypes=(("XOB files", "*.xob*"), ("all files", "*.*")))
    label_am4.config(text="Static point: " + file_name_st + "\nAmort point: " + file_name_am)
    load_amort(file_name_st, file_name_am, 4)


def save_time():
    global label_time, label_vy, label_vz, label_rx
    global res_time

    res_data = update_res_data(res_time)

    label_time.config(text="Время касания: " + str(res_data[0]))
    label_vy.config(text="Горизонтальная скорость: " + str(res_data[1]))
    label_vz.config(text="Вертикальная скорость: " + str(res_data[2]))
    label_rx.config(text="Угол наклона: " + str(res_data[3]))
    return 0


def set_vel_gui():
    global label_cog
    global label_time, label_vy, label_vz, label_rx
    global label_entry_time, entry_time, button_time
    global res_time
    global entry_time

    res_time = DoubleVar(value=0.0)

    label_time = ttk.Label(text="Время касания: ")
    label_time.pack()
    label_time.place(x=30, y=10)
    label_vy = ttk.Label(text="Горизонтальная скорость: ")
    label_vy.pack()
    label_vy.place(x=30, y=30)
    label_vz = ttk.Label(text="Вертикальная скорость: ")
    label_vz.pack()
    label_vz.place(x=30, y=50)
    label_rx = ttk.Label(text="Угол наклона: ")
    label_rx.pack()
    label_rx.place(x=30, y=70)

    label_entry_time = ttk.Label(text="Время касания:")
    label_entry_time.pack()
    label_entry_time.place(x=30, y=130)
    entry_time = ttk.Entry(width=10, textvariable=res_time)
    entry_time.pack()
    entry_time.place(x=130, y=130)
    button_time = ttk.Button(text="Save time", command=save_time)
    button_time.pack()
    button_time.place(x=420, y=130)

    button_cog = ttk.Button(text="Open file (center of gravity)", command=choose_file_cog)
    button_cog.pack()
    button_cog.place(x=30, y=190)

    label_cog = ttk.Label()
    label_cog.pack()
    label_cog.place(x=200, y=195)


def set_amorts_gui():
    global label_am1, label_am2, label_am3, label_am4

    button_am1 = ttk.Button(text="Open file (amort 1)", command=choose_file_amort1)
    button_am1.pack()
    button_am1.place(x=30, y=230)
    label_am1 = ttk.Label(text="Static point: \nAmort point: ")
    label_am1.pack()
    label_am1.place(x=150, y=235)

    button_am2 = ttk.Button(text="Open file (amort 2)", command=choose_file_amort2)
    button_am2.pack()
    button_am2.place(x=30, y=270)
    label_am2 = ttk.Label(text="Static point: \nAmort point: ")
    label_am2.pack()
    label_am2.place(x=150, y=275)

    button_am3 = ttk.Button(text="Open file (amort 3)", command=choose_file_amort3)
    button_am3.pack()
    button_am3.place(x=30, y=310)
    label_am3 = ttk.Label(text="Static point: \nAmort point: ")
    label_am3.pack()
    label_am3.place(x=150, y=315)

    button_am4 = ttk.Button(text="Open file (amort 4)", command=choose_file_amort4)
    button_am4.pack()
    button_am4.place(x=30, y=350)
    label_am4 = ttk.Label(text="Static point: \nAmort point: ")
    label_am4.pack()
    label_am4.place(x=150, y=355)


def onclick(event):
    global ix, iy, res_time, entry_time
    ix, iy = event.xdata, event.ydata
    print(f'x = {ix}, y = {iy}')
    res_time = DoubleVar(value=ix)
    text = str(ix)
    entry_time.delete(0, END)
    entry_time.insert(0, text)

cid = plt.connect('button_press_event', onclick)


def main():
    win = Tk()
    win.geometry("650x1000+900+0")

    set_vel_gui()
    set_amorts_gui()

    plt.ion()

    win.mainloop()


main()
