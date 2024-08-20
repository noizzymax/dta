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
    
    file_name = filedialog.askopenfilename(initialdir = "/", title = "Select a File", 
                                           filetypes = (("XOB files", "*.xob*"), ("all files", "*.*")))
    # file_name = "../bin/data/data.xob"
    label_cog.config(text = file_name)
    min_time, max_time = load_cog(file_name)
    scale_time = ttk.Scale(orient = HORIZONTAL, length = 200, from_ = min_time, to = max_time, value = min_time, variable = res_time)
    scale_time.pack()
    scale_time.place(x = 210, y = 130)
    

def choose_file_amort1():
    global label_am1
    
    file_name_st = filedialog.askopenfilename(initialdir = "/", title = "Select a File",
                                              filetypes = (("XOB files", "*.xob*"), ("all files", "*.*")))
    file_name_am = filedialog.askopenfilename(initialdir = "/", title = "Select a File",
                                              filetypes = (("XOB files", "*.xob*"), ("all files", "*.*")))
    label_am1.config(text = "Static point: " + file_name_st + "\nAmort point: " + file_name_am)
    load_amort(file_name_st, file_name_am, 1)


def choose_file_amort2():
    global label_am2

    file_name_st = filedialog.askopenfilename(initialdir = "/", title = "Select a File",
                                              filetypes = (("XOB files", "*.xob*"), ("all files", "*.*")))
    file_name_am = filedialog.askopenfilename(initialdir = "/", title = "Select a File",
                                              filetypes = (("XOB files", "*.xob*"), ("all files", "*.*")))
    label_am2.config(text = "Static point: " + file_name_st + "\nAmort point: " + file_name_am)
    load_amort(file_name_st, file_name_am, 2)


def choose_file_amort3():
    global label_am1

    file_name_st = filedialog.askopenfilename(initialdir = "/", title = "Select a File",
                                              filetypes = (("XOB files", "*.xob*"), ("all files", "*.*")))
    file_name_am = filedialog.askopenfilename(initialdir = "/", title = "Select a File",
                                              filetypes = (("XOB files", "*.xob*"), ("all files", "*.*")))
    label_am3.config(text = "Static point: " + file_name_st + "\nAmort point: " + file_name_am)
    load_amort(file_name_st, file_name_am, 3)


def choose_file_amort4():
    global label_am1

    file_name_st = filedialog.askopenfilename(initialdir = "/", title = "Select a File",
                                              filetypes = (("XOB files", "*.xob*"), ("all files", "*.*")))
    file_name_am = filedialog.askopenfilename(initialdir = "/", title = "Select a File",
                                              filetypes = (("XOB files", "*.xob*"), ("all files", "*.*")))
    label_am4.config(text = "Static point: " + file_name_st + "\nAmort point: " + file_name_am)
    load_amort(file_name_st, file_name_am, 4)


def save_time():
    global label_time, label_vy, label_vz, label_rx
    global res_time

    res_data = update_res_data(res_time)

    label_time.config(text = "Время касания: " + str(res_data[0]))
    label_vy.config(text = "Горизонтальная скорость: " + str(res_data[1]))
    label_vz.config(text = "Вертикальная скорость: " + str(res_data[2]))
    label_rx.config(text = "Угол наклона: " + str(res_data[3]))
    return 0


def set_vel_gui():
    global label_cog
    global label_time, label_vy, label_vz, label_rx
    global label_entry_time, entry_time, button_time
    global res_time

    res_time = DoubleVar(value = 0.0)

    label_time = ttk.Label(text = "Время касания: ")
    label_time.pack()
    label_time.place(x = 30, y = 10)
    label_vy = ttk.Label(text = "Горизонтальная скорость: ")
    label_vy.pack()
    label_vy.place(x = 30, y = 30)
    label_vz = ttk.Label(text = "Вертикальная скорость: ")
    label_vz.pack()
    label_vz.place(x = 30, y = 50)
    label_rx = ttk.Label(text = "Угол наклона: ")
    label_rx.pack()
    label_rx.place(x = 30, y = 70)

    label_entry_time = ttk.Label(text = "Время касания:")
    label_entry_time.pack()
    label_entry_time.place(x = 30, y = 130)
    entry_time = ttk.Entry(width = 10, textvariable = res_time)
    entry_time.pack()
    entry_time.place(x = 130, y = 130)
    button_time = ttk.Button(text = "Save time", command = save_time)
    button_time.pack()
    button_time.place(x = 420, y = 130)

    button_cog = ttk.Button(text = "Open file (center of gravity)", command = choose_file_cog)
    button_cog.pack()
    button_cog.place(x = 30, y = 190)

    label_cog = ttk.Label()
    label_cog.pack()
    label_cog.place(x = 200, y = 195)


def set_amorts_gui():
    global label_am1, label_am2, label_am3, label_am4
    
    button_am1 = ttk.Button(text = "Open file (amort 1)", command = choose_file_amort1 )
    button_am1.pack()
    button_am1.place(x = 30, y = 230)
    label_am1 = ttk.Label(text = "Static point: \nAmort point: ")
    label_am1.pack()
    label_am1.place(x = 150, y = 235)

    button_am2 = ttk.Button(text = "Open file (amort 2)", command = choose_file_amort2)
    button_am2.pack()
    button_am2.place(x = 30, y = 270)
    label_am2 = ttk.Label(text = "Static point: \nAmort point: ")
    label_am2.pack()
    label_am2.place(x = 150, y = 275)

    button_am3 = ttk.Button(text = "Open file (amort 3)", command = choose_file_amort3)
    button_am3.pack()
    button_am3.place(x = 30, y = 310)
    label_am3 = ttk.Label(text = "Static point: \nAmort point: ")
    label_am3.pack()
    label_am3.place(x = 150, y = 315)
    
    button_am4 = ttk.Button(text = "Open file (amort 4)", command = choose_file_amort4)
    button_am4.pack()
    button_am4.place(x = 30, y = 350)
    label_am4 = ttk.Label(text = "Static point: \nAmort point: ")
    label_am4.pack()
    label_am4.place(x = 150, y = 355)
    

def main():
    win = Tk()
    win.geometry("650x1000+900+0")
    
    set_vel_gui()
    set_amorts_gui()
    
    plt.ion()
    
    win.mainloop()


main()



'''
import sys
import matplotlib.pyplot as plt
from pynput import keyboard

# move OYZ

time_coord = 0
vel_time, rotx, vy, vz = [], [], [], []
gr_vel, gr_rot, vel_timeline, rot_timeline = [], [], [], []
am_time, am = [[], [], [], []], [[], [], [], []]
res_data = [0, 0, 0, 0]


def on_click(event):
    global time_coord

    print(event.xdata)
    print('Do you want to save this time as start time? (y/n)')
    time_coord = event.xdata


def on_press(key):
    global vel_time, vy, vz, rotx
    global gr_vel, gr_rot, vel_timeline, rot_timeline
    global res_data

    if key == keyboard.Key.esc:
        return False  # stop listener
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    if k == 'y' or k == 'н':
        res_time_ind = get_time_ind()
        res_data.clear()

        res_data.append(vel_time[res_time_ind])
        res_data.append(vy[res_time_ind])
        res_data.append(vz[res_time_ind])
        res_data.append(rotx[res_time_ind])
        print(res_data)

        vel_timeline.remove()
        vel_timeline = gr_vel.axvline(x=vel_time[res_time_ind], color='grey', label='start time line', linestyle='--')

        rot_timeline.remove()
        rot_timeline = gr_rot.axvline(x=vel_time[res_time_ind], color='grey', label='start time line', linestyle='--')


def on_close(event):
    global res_data

    f = open("res.txt", 'w')
    f.write("Касание: " + str(res_data[0]) + '\n')
    f.write("Угол наклона: " + str(res_data[1]) + '\n')
    f.write("Скорость (горизонтальная): " + str(res_data[2]) + '\n')
    f.write("Скорость (вертикальная): " + str(res_data[3]) + '\n')
    f.close()
    print("Close")


def load_vel(file_name):
    global vel_time
    global rotx, vy, vz

    file = open(file_name, 'r')
    text = file.read().split('\n')[2:]

    flag = 0
    coords = []

    for s in text:
        if s == "":
            continue
        s = s.split()
        vel_time.append(float(s[1]))
        rotx.append(float(s[5]))
        coords.append([float(s[3]), float(s[4])])
        if flag == 1:
            cl = len(coords) - 1
            vy.append((coords[cl][0] - coords[cl - 1][0]) / (vel_time[cl] - vel_time[cl - 1]) / 1000)
            vz.append((coords[cl][1] - coords[cl - 1][1]) / (vel_time[cl] - vel_time[cl - 1]) / 1000)
        flag = 1
    vy.append(0)
    vz.append(0)


def get_end_ind():
    global vy, vz

    flag, end_vy = 0, -1
    for i in range(len(vy)):
        if abs(vy[i]) <= 0.01:
            flag += 1
        else:
            flag = 0
        if flag == 1:
            end_vy = i
        if flag > 50:
            break

    flag, end_vz = 0, -1
    for i in range(len(vz)):
        if abs(vz[i]) <= 0.01:
            flag += 1
        else:
            flag = 0
        if flag == 1:
            end_vz = i
        if flag > 50:
            break

    return max(end_vy, end_vz)


def get_time_ind():
    global time_coord, vel_time

    mi = 10 ** 6
    res_time_ind = 0
    for i in range(len(vel_time)):
        if abs(vel_time[i] - time_coord) < mi:
            mi = abs(vel_time[i] - time_coord)
            res_time_ind = i
    return res_time_ind


def load_amort(pt_fn, am_fn):
    time_pt, time_am, pt, am = [], [], [], []
    res_time, delt = [], []

    pt_text = open(pt_fn).read().split('\n')
    for s in pt_text:
        if s == "":
            continue
        s = s.split()
        time_pt.append(float(s[1]))
        pt.append([float(s[2]), float(s[3]), float(s[4])])

    for am_fn_one in am_fn:
        if am_fn_one == "":
            continue
        am_text = open(am_fn_one).read().split('\n')

        for s in am_text:
            if s == "":
                continue
            s = s.split()
            time_am.append(float(s[1]))
            am.append([float(s[2]), float(s[3]), float(s[4])])

    start_ind = 0
    if time_am[0] > time_pt[0]:
        for t in range(len(time_pt)):
            if time_pt[t] == time_am[0]:
                start_ind = t
                break
        time_pt = time_pt[start_ind:]
        pt = pt[start_ind:]
    elif time_am[0] < time_pt[0]:
        for t in range(len(time_am)):
            if time_am[t] == time_pt[0]:
                start_ind = t
                break
        time_am = time_am[start_ind:]
        am = am[start_ind:]

    etal = ((am[0][0] - pt[0][0]) ** 2 + (am[0][1] - pt[0][1]) ** 2 + (am[0][2] - pt[0][2]) ** 2) ** 0.5

    t_am, t_pt = 0, 0
    while t_pt != (len(time_pt) - 1) and t_am != (len(time_am) - 1):
        if time_pt[t_pt] == time_am[t_am]:
            res_time.append(time_pt[t_pt])
            delt.append(((am[t_am][0] - pt[t_pt][0]) ** 2 + (am[t_am][1] - pt[t_pt][1]) ** 2 + (
                        am[t_am][2] - pt[t_pt][2]) ** 2) ** 0.5 - etal)
            t_pt += 1
            t_am += 1
        elif time_pt[t_pt] < time_am[t_am]:
            res_time.append(time_pt[t_pt])
            delt.append(None)
            t_pt += 1
        elif time_pt[t_pt] > time_am[t_am]:
            res_time.append(time_am[t_am])
            delt.append(None)
            t_am += 1

    return res_time, delt


def load_amorts(file_name_ar):
    global am_time, am

    file_name_ar = file_name_ar.split('\n')
    i = 0
    for file_name in file_name_ar:
        if file_name == "":
            continue
        file_name = file_name.split()
        am_time[i], am[i] = load_amort(file_name[0], file_name[1:])
        i += 1


def main():
    global vel_time, rotx, vy, vz
    global gr_vel, gr_rot, vel_timeline, rot_timeline
    global am_time, am

    print("File with links: ")
    file = open("link.txt")
    # file = open(input().split()[0])

    load_vel(file.readline().split('\n')[0])
    load_amorts(file.read())

    plt.ion()

    end_ind = get_end_ind()
    gr_vel = plt.subplot(2, 2, 1)
    gr_vel.plot(vel_time, vy, label="vy")
    gr_vel.plot(vel_time, vz, label="vz")
    vel_timeline = gr_vel.axvline(x=time_coord, color='grey', label='start time line', linestyle='--')
    gr_vel.set_xlabel("time")
    gr_vel.set_ylabel("velocity")
    gr_vel.legend()
    gr_vel.set_xlim(vel_time[0], vel_time[end_ind])

    gr_rot = plt.subplot(2, 2, 3)
    gr_rot.plot(vel_time, rotx, label="rotx")
    rot_timeline = gr_rot.axvline(x=time_coord, color='grey', label='start time line', linestyle='--')
    gr_rot.set_xlabel("time")
    gr_rot.set_ylabel("rotation")
    gr_rot.legend()
    gr_rot.set_xlim(vel_time[0], vel_time[end_ind])

    gr_am = plt.subplot(1, 2, 2)
    for i in range(len(am)):
        if am[i] == []:
            continue
        gr_am.plot(am_time[i], am[i], label=("am" + str(i + 1)))
    gr_am.set_xlabel("time")
    gr_am.set_ylabel("amorts")
    gr_am.legend()
    gr_am.set_xlim(am_time[0][0], vel_time[end_ind])

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    plt.connect('close_event', on_close)
    plt.connect('button_press_event', on_click)
    plt.show(block=True)


main()

'''

