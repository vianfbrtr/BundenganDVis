import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



def polarplot():
    #SENAR 1
    b1s1 = pd.read_excel('Data/Bundengan 1.xlsx', sheet_name='Senar 1')
    b1s1 = b1s1.set_index('Frequency (Hz)')
    b1s1 = b1s1.head()

    frekuensi = b1s1.index

    b1senar1 = {}
    for i in frekuensi:
        b1senar1[i] = b1s1.loc[i].to_numpy()

    theta = np.array([i * np.pi/6 for i in range(13)])
    
    for frek in b1senar1:
        r = b1senar1[frek]
        axs = plt.subplot(projection='polar')
        plt.title('Direktivitas Bunyi Senar 1 Bundengan Pak Munir')
        axs.plot(theta, r, label = frek)
        axs.set_rmax(0)
        axs.set_rticks([-60, -45, -30, -15])
        axs.legend(loc = 4, bbox_to_anchor=(0., -0.1, 1., -0.1), title = 'Frekuensi (Hz)')
        
    plt.show()


def grafikKontur():
    #Senar1
    b1s1 = pd.read_excel('Data/Bundengan 1.xlsx', sheet_name = 'Senar 4').set_index('Frequency (Hz)').head(256).transpose()
    arah = b1s1.index.to_numpy()
    frekuensi = b1s1.columns.to_numpy()
    ttb = b1s1.to_numpy()
    levels = np.linspace(-60, 0, 21)

    plt.figure(num='Bundengan Pak Munir, Senar 4')
    plt.contourf(frekuensi, arah, ttb, levels = levels)
    plt.colorbar()
    plt.xscale('log')

    #plt.xlabel('Frekuensi (Hz)', size = 12, labelpad = 15)
    #plt.ylabel('Arah bunyi', size = 12, labelpad = 15)

    plt.show()

grafikKontur()

