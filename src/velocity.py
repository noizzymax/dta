import matplotlib.pyplot as plt
import numpy as np

time, vy, vz, rx = [], [0], [0], []
vel_axvline, rot_axvline = [], []


def load_cog(file_name):
    global time, vy, vz, rx
    global vel_axvline, rot_axvline

    if file_name == "":
        return 0, 0
    file_str = open(file_name).read()
    file_str = file_str.replace(',', '')
    file_str = file_str.split('\n')

    time, vy, vz, rx = [], [0], [0], []
    prev_cy, prev_cz = 0, 0

    for s in file_str:
        s = s.split()
        if len(s) != 8:
            continue
        time.append(float(s[1]))
        rx.append(float(s[5]))
        cy, cz = float(s[3]), float(s[4])
        if len(time) != 1:
            vy.append((cy - prev_cy) / (time[len(time) - 1] - time[len(time) - 2]) / 1000)
            vz.append((cz - prev_cz) / (time[len(time) - 1] - time[len(time) - 2]) / 1000)
        prev_cy, prev_cz = cy, cz

    plt.figure(1)
    plt.clf()
    plt.plot(time, vy, label="Скорость Vy", linewidth=0.5)
    plt.plot(time, vz, label="Скорость Vz", linewidth=0.5)
    plt.legend()
    plt.xlabel("Время, с")
    plt.ylabel("Скорость, м/с")
    plt.xlim(time[0], time[len(time) - 1])
    vel_axvline = plt.axvline(x=time[0], color='grey', label='Момент касания', linestyle='--')
    plt.xticks(np.arange(time[0], time[len(time) - 1], 0.1))

    plt.figure(2)
    plt.clf()
    plt.plot(time, rx, label="RX", linewidth=0.5)
    plt.legend()
    plt.xlabel("Время, с")
    plt.ylabel("Тангаж, \N{DEGREE SIGN}")
    plt.xlim(time[0], time[len(time) - 1])
    rot_axvline = plt.axvline(x=time[0], color='grey', label='Момент касания', linestyle='--')
    plt.xticks(np.arange(time[0], time[len(time) - 1], 0.1))

    plt.show()

    return time[0], time[len(time) - 1]


def update_res_data(input_time):
    global vel_axvline, rot_axvline

    # time, vy, vz, rx
    rdi = 0
    delta = 10 ** 10
    # input_time = input_time.get()

    for i in range(len(time)):
        if abs(time[i] - input_time) < delta:
            delta = abs(time[i] - input_time)
            rdi = i

    vel_axvline.remove()
    plt.figure(1)
    vel_axvline = plt.axvline(x=time[rdi], color='grey', label='start time line', linestyle='--', linewidth=0.5)
    # plt.xlim(max(time[0], time[rdi] - 0.3), min(time[len(time) - 1], time[rdi] + 0.3))
    a = plt.xlim()
    plt.draw()
    rot_axvline.remove()
    plt.figure(2)
    rot_axvline = plt.axvline(x=time[rdi], color='grey', label='start time line', linestyle='--', linewidth=0.5)
    plt.xlim(a)

    plt.draw()

    return [time[rdi], vy[rdi], vz[rdi], rx[rdi]]
