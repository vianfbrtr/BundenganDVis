import numpy as np
import pandas as pd
from scipy.signal import find_peaks


class grafik:
    def __init__(self, nomor_bundengan, nomor_senar):
        #CALL THE EXCEL FILE DATA
        self.nomor_bundengan = nomor_bundengan
        self.nomor_senar = nomor_senar
        self.data_bund = pd.read_excel(f'data/Bundengan {nomor_bundengan}.xlsx', sheet_name=f'Senar {nomor_senar}')
        self.data_bund = self.data_bund.set_index('Frequency (Hz)').head(256)

    def kontur(self):
        #MAKE VARIABLE FOR KONTUR PLOT
        self.data_bund = self.data_bund.transpose()

        self.arah = self.data_bund.index.to_numpy()
        self.frekuensi = self.data_bund.columns.to_numpy()
        self.ttb = self.data_bund.to_numpy()

        self.interval_warna = np.linspace(-60, 0, 21)

    def polar(self):
        ###REMOVE FREQUENCY WITH A LOT OF NOISE#####
        self.data_bund = self.data_bund.tail(253)

        ###PEAK DETECTION####
        self.frekuensi = self.data_bund.index.to_numpy()
        self.ttb_nol = self.data_bund['0º'].to_numpy()
        
        if self.nomor_bundengan == 1:
            puncak, _ = find_peaks(self.ttb_nol, prominence=10)
        else:
            puncak, _ = find_peaks(self.ttb_nol, prominence=20)

        self.frekuensi_alami = self.frekuensi[puncak]
        self.ttb_alami = self.ttb_nol[puncak]
        
        self.ttb_tiap_arah = {}
        for i, v in enumerate(self.frekuensi_alami):
            self.ttb_tiap_arah[i] = self.data_bund.loc[v].to_numpy()

        self.arah = np.array([i * np.pi/6 for i in range(13)])


    