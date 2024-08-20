import matplotlib.pyplot as plt

def load_amort( file_name_st, file_name_am, am_num ):
    if file_name_st == "" or file_name_am == "":
        return
    
    st_file_str = open(file_name_st).read()
    am_file_str = open(file_name_am).read()
    
    st_file_str = st_file_str.replace(',', '')
    st_file_str = st_file_str.split('\n')
    am_file_str = am_file_str.replace(',', '')
    am_file_str = am_file_str.split('\n')
    
    am_time, am_pt = [], []
    st_time, st_pt = [], []
    
    for s in st_file_str:
        s = s.split()
        if len(s) < 8:
            continue
        st_time.append(float(s[1]))
        st_pt.append([float(s[2]), float(s[3]), float(s[4])])

    for s in am_file_str:
        s = s.split()
        if len(s) < 8:
            continue
        am_time.append(float(s[1]))
        am_pt.append([float(s[2]), float(s[3]), float(s[4])])

    if am_time[0] > st_time[0]:
        t = 1
        while st_time[t] != am_time[0]:
            t += 1
        st_time = st_time[t:]
        st_pt = st_pt[t:]
    elif am_time[0] < st_time[0]:
        t = 1
        while am_time[t] != st_time[0]:
            t += 1
        am_time = am_time[t:]
        am_pt = am_pt[t:]
    
    time, delt = [], []
    am_ind, st_ind = 0, 0
    
    etal = ((am_pt[0][0] - st_pt[0][0]) ** 2 + (am_pt[0][1] - st_pt[0][1]) ** 2 + (am_pt[0][2] - st_pt[0][2]) ** 2) ** 0.5
    
    while am_ind != (len(am_time) - 1) and st_ind != (len(st_time) - 1):
        if am_time[am_ind] == st_time[st_ind]:
            time.append(am_time[am_ind])
            d = ((am_pt[am_ind][0] - st_pt[st_ind][0]) ** 2 + (am_pt[am_ind][1] - st_pt[st_ind][1]) ** 2 + (am_pt[am_ind][2] - st_pt[st_ind][2]) ** 2) ** 0.5
            delt.append(d - etal)
            am_ind += 1
            st_ind += 1
        elif am_time[am_ind] < st_time[st_ind]:
            delt.append(None)
            time.append(am_time[am_ind])
            am_ind += 1
        elif am_time[am_ind] > st_time[st_ind]:
            delt.append(None)
            time.append(st_time[st_ind])
            st_ind += 1

    plt.figure(3)
    plt.plot(time, delt, label = "am" + str(am_num))
    plt.legend()
    plt.xlabel("time")
    plt.ylabel("amorts")
    # plt.xlim(time[0], time[len(time) - 1])
    # plt.xticks(np.arange(time[0], time[len(time) - 1], 0.1))
    
    plt.show()
    return 0