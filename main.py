'''
红色为信号显示
蓝色为fft变换后信号显示


COM端口需要自行设置
arduino程序见

'''

import pyqtgraph as pg
from PyQt5.QtCore import QTimer
import serial
import threading
from scipy.fftpack import fft
import numpy as np



def update():
    x = np.linspace(0, 1, 100)
    data = list((abs(fft(all_data))/len(x)-20)[range(1, int(len(x)/2))])
    fft_.setData(data)
    all_data_copy = all_data
    max_ = np.max(all_data)
    min_ = np.min(all_data)
    cha = max_ - min_
    formated = all_data-max_+cha/2

    for i in range(len(formated)//2):
        if cha<0.5 :
            break
        elif -cha/5<formated[i]<cha/5 and formated[i]<formated[i+1]:
            all_data_copy =all_data_copy[i:]
            for j in range(i-1):
                all_data_copy = np.append(all_data_copy,np.array([0]))
            break
    all_data_copy = np.append(all_data_copy, np.array([0]))
    signal.setData(all_data_copy)



def ComRecvDeal():
    global fly,all_data
    try:
        t = serial.Serial('COM4', 38400)
        while (True):
            try:
                data = int(str(t.readline())[2:-5])/10
                all_data = np.append(all_data, data)
                all_data = all_data[1:]
            except:
                pass
    except:
        print("串口打开失败")


if __name__ == '__main__':
    threading.Thread(target=ComRecvDeal).start()
    all_data = np.array([0]*200)
    app = pg.mkQApp()
    win = pg.GraphicsWindow()
    win.setWindowTitle(u'波形显示')


    p = win.addPlot()
    #yuan = p.plot(pen='b', name='a')
    fft_ = p.plot(pen='b', name='a')
    signal = p.plot(pen='r', name='a')


    timer = QTimer()
    timer.timeout.connect(update)  # 定时刷新数据显示
    timer.start()
    app.exec_()


