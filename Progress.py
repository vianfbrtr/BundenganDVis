import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def bundengan1():
    #SENAR 1
    b1s1 = pd.read_excel('Data/Bundengan 1.xlsx', sheet_name='Senar 1')
    b1s1 = b1s1.set_index('Frequency (Hz)')
    b1s1 = b1s1.head()

    frekuensi = b1s1.index

    b1senar1 = {}
    for i in frekuensi:
        b1senar1[i] = b1s1.loc[i].to_numpy()

    theta = np.array([i * np.pi/6 for i in range(13)])

    
    for key in b1senar1:
        r = b1senar1[key]
        axs = plt.subplot(projection='polar')
        plt.title('Direktivitas Bunyi Senar 1 Bundengan Pak Munir')
        axs.plot(theta, r)
        axs.set_rmax(-40)
        axs.set_rticks([-60, -55, -50, -45])
        
    plt.show()

bundengan1()

