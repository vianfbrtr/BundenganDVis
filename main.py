import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import numpy as np
#import matplotlib          #IF U'RE USING ANACONDA, JUST KEEP THIS 2 LINES AS COMMENT
#matplotlib.use('QT5Agg')   #IF U'RE NOT, UNCOMMENT THIS
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.max_open_warning': 0})
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from gui_app import *
from about import *
from visualization import *
from all_dialog import *
from ket_arah import *

#----------- 

def main():
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()

    sys.exit(app.exec_())

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)



class mainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        #SETUP MENU UTAMA
        self.ui.beranda_button.setStyleSheet("border-left: 3px solid #303f9f; background-color: #ecf0f1;")
        self.ui.beranda_button.clicked.connect(self.changeTabHome)
        self.ui.bund1_button.clicked.connect(self.changeTabBund1)
        self.ui.bund2_button.clicked.connect(self.changeTabBund2)
        self.ui.compare_button.clicked.connect(self.changeTabCompare)
        self.ui.help_button.clicked.connect(self.changeTabHelp)
        self.ui.about_button.clicked.connect(self.changeTabAbout)
        

        self.defineCanvas1()
        self.defineCanvas2()
        self.defineCanvasCompare()

    def defineCanvas1(self):
    ####SET CANVAS BUNDENGAN 1#####
        '''KONTUR'''
        self.meshFigure11 = plt.figure()
        self.canvas11_mesh = FigureCanvas(self.meshFigure11)
        self.navigasi_mesh11 = NavigationToolbar(self.canvas11_mesh, self)
        self.ui.b1senar1_mesh_plotLayout.addWidget(self.canvas11_mesh)
        self.ui.b1senar1_mesh_plotLayout.addWidget(self.navigasi_mesh11)
        
        self.meshFigure12 = plt.figure()
        self.canvas12_mesh = FigureCanvas(self.meshFigure12)
        self.navigasi_mesh12 = NavigationToolbar(self.canvas12_mesh, self)
        self.ui.b1senar2_mesh_plotLayout.addWidget(self.canvas12_mesh)
        self.ui.b1senar2_mesh_plotLayout.addWidget(self.navigasi_mesh12)

        self.meshFigure13 = plt.figure()
        self.canvas13_mesh = FigureCanvas(self.meshFigure13)
        self.navigasi_mesh13 = NavigationToolbar(self.canvas13_mesh, self)
        self.ui.b1senar3_mesh_plotLayout.addWidget(self.canvas13_mesh)
        self.ui.b1senar3_mesh_plotLayout.addWidget(self.navigasi_mesh13)

        self.meshFigure14 = plt.figure()
        self.canvas14_mesh = FigureCanvas(self.meshFigure14)
        self.navigasi_mesh14 = NavigationToolbar(self.canvas14_mesh, self)
        self.ui.b1senar4_mesh_plotLayout.addWidget(self.canvas14_mesh)
        self.ui.b1senar4_mesh_plotLayout.addWidget(self.navigasi_mesh14)
        '''POLAR'''
        self.polarfigure11 = plt.figure()
        self.canvas11_polar = FigureCanvas(self.polarfigure11)
        self.navigasi_polar11 = NavigationToolbar(self.canvas11_polar, self)
        self.ui.b1senar1_layoutPolar.addWidget(self.canvas11_polar)
        self.ui.b1senar1_layoutPolar.addWidget(self.navigasi_polar11)

        self.polarfigure12 = plt.figure()
        self.canvas12_polar = FigureCanvas(self.polarfigure12)
        self.navigasi_polar12 = NavigationToolbar(self.canvas12_polar, self)
        self.ui.b1senar2_layout_polar.addWidget(self.canvas12_polar)
        self.ui.b1senar2_layout_polar.addWidget(self.navigasi_polar12)
        
        self.polarfigure13 = plt.figure()
        self.canvas13_polar = FigureCanvas(self.polarfigure13)
        self.navigasi_polar13 = NavigationToolbar(self.canvas13_polar, self)
        self.ui.b1senar3_layout_polar.addWidget(self.canvas13_polar)
        self.ui.b1senar3_layout_polar.addWidget(self.navigasi_polar13)

        self.polarfigure14 = plt.figure()
        self.canvas14_polar = FigureCanvas(self.polarfigure14)
        self.navigasi_polar14 = NavigationToolbar(self.canvas14_polar, self)
        self.ui.b1senar4_layout_polar.addWidget(self.canvas14_polar)
        self.ui.b1senar4_layout_polar.addWidget(self.navigasi_polar14)



        '''SET PLOT SEMUA SENAR BUNDENGAN1 FOR BETTER EXPERIENCE'''
        '''SENAR 1'''
        ax11 = self.meshFigure11.add_subplot(111)
        contour11 = grafik(1,1)
        contour11.kontur()
        plot_contour11 = ax11.contourf(contour11.frekuensi, contour11.arah, contour11.ttb, levels = contour11.interval_warna)
        self.meshFigure11.colorbar(plot_contour11).set_label(label = 'Tingkat Tekanan Bunyi (dB)', size = 12, labelpad = 15)
        ax11.set_xscale('log')
        ax11.set_xlabel('Frekuensi (Hz)', size = 12, labelpad = 15)
        ax11.set_ylabel('Arah bunyi', size = 12, labelpad = 15)
        self.canvas11_mesh.draw()

        self.tone11 = grafik(1,1)
        self.tone11.polar()
        self.axp11 = self.polarfigure11.add_subplot(projection = 'polar')
        self.axp11.plot(self.tone11.arah, self.tone11.ttb_tiap_arah[0])
        self.axp11.set_rmax(0)
        self.axp11.set_rticks(np.linspace(-54, -9, 6))
        self.ui.b1s1n1_cekbox.setChecked(True)
        
        '''SENAR 2'''
        ax12 = self.meshFigure12.add_subplot(111)
        contour12 = grafik(1,2)
        contour12.kontur()
        plot_contour12 = ax12.contourf(contour12.frekuensi, contour12.arah, contour12.ttb, levels = contour12.interval_warna)
        self.meshFigure12.colorbar(plot_contour12).set_label(label = 'Tingkat Tekanan Bunyi (dB)', size = 12, labelpad = 15)
        ax12.set_xscale('log')
        ax12.set_xlabel('Frekuensi (Hz)', size = 12, labelpad = 15)
        ax12.set_ylabel('Arah bunyi', size = 12, labelpad = 15)
        self.canvas12_mesh.draw()

        self.tone12 = grafik(1,2)
        self.tone12.polar()
        self.axp12 = self.polarfigure12.add_subplot(projection = 'polar')
        self.axp12.plot(self.tone12.arah, self.tone12.ttb_tiap_arah[0])
        self.axp12.set_rmax(0)
        self.axp12.set_rticks(np.linspace(-54, -9, 6))
        self.ui.b1s2n1_cekbox.setChecked(True)

        '''SENAR 3'''
        ax13 = self.meshFigure13.add_subplot(111)
        contour13 = grafik(1,3)
        contour13.kontur()
        plot_contour13 = ax13.contourf(contour13.frekuensi, contour13.arah, contour13.ttb, levels = contour13.interval_warna)
        self.meshFigure13.colorbar(plot_contour13).set_label(label = 'Tingkat Tekanan Bunyi (dB)', size = 12, labelpad = 15)
        ax13.set_xscale('log')
        ax13.set_xlabel('Frekuensi (Hz)', size = 12, labelpad = 15)
        ax13.set_ylabel('Arah bunyi', size = 12, labelpad = 15)
        self.canvas13_mesh.draw()

        self.tone13 = grafik(1,3)
        self.tone13.polar()
        self.axp13 = self.polarfigure13.add_subplot(projection = 'polar')
        self.axp13.plot(self.tone13.arah, self.tone13.ttb_tiap_arah[0])
        self.axp13.set_rmax(0)
        self.axp13.set_rticks(np.linspace(-54, -9, 6))
        self.ui.b1s3n1_cekbox.setChecked(True)

        '''SENAR 4'''
        ax14 = self.meshFigure14.add_subplot(111)
        contour14 = grafik(1,4)
        contour14.kontur()
        plot_contour14 = ax14.contourf(contour14.frekuensi, contour14.arah, contour14.ttb, levels = contour14.interval_warna)
        self.meshFigure14.colorbar(plot_contour14).set_label(label = 'Tingkat Tekanan Bunyi (dB)', size = 12, labelpad = 15)
        ax14.set_xscale('log')
        ax14.set_xlabel('Frekuensi (Hz)', size = 12, labelpad = 15)
        ax14.set_ylabel('Arah bunyi', size = 12, labelpad = 15)
        self.canvas14_mesh.draw()

        self.tone14 = grafik(1,4)
        self.tone14.polar()
        self.axp14 = self.polarfigure14.add_subplot(projection = 'polar')
        self.axp14.plot(self.tone14.arah, self.tone14.ttb_tiap_arah[0])
        self.axp14.set_rmax(0)
        self.axp14.set_rticks(np.linspace(-54, -9, 6))
        self.ui.b1s4n1_cekbox.setChecked(True)


    def defineCanvas2(self):
    ####SET CANVAS BUNDENGAN 2#####
        '''KONTUR'''
        self.meshFigure21 = plt.figure()
        self.canvas21_mesh = FigureCanvas(self.meshFigure21)
        self.navigasi_mesh21 = NavigationToolbar(self.canvas21_mesh, self)
        self.ui.b2senar1_mesh_plotLayout.addWidget(self.canvas21_mesh)
        self.ui.b2senar1_mesh_plotLayout.addWidget(self.navigasi_mesh21)
        self.meshFigure22 = plt.figure()
        self.canvas22_mesh = FigureCanvas(self.meshFigure22)
        self.navigasi_mesh22 = NavigationToolbar(self.canvas22_mesh, self)
        self.ui.b2senar2_mesh_plotLayout.addWidget(self.canvas22_mesh)
        self.ui.b2senar2_mesh_plotLayout.addWidget(self.navigasi_mesh22)
        self.meshFigure23 = plt.figure()
        self.canvas23_mesh = FigureCanvas(self.meshFigure23)
        self.navigasi_mesh23 = NavigationToolbar(self.canvas23_mesh, self)
        self.ui.b2senar3_mesh_plotLayout.addWidget(self.canvas23_mesh)
        self.ui.b2senar3_mesh_plotLayout.addWidget(self.navigasi_mesh23)
        self.meshFigure24 = plt.figure()
        self.canvas24_mesh = FigureCanvas(self.meshFigure24)
        self.navigasi_mesh24 = NavigationToolbar(self.canvas24_mesh, self)
        self.ui.b2senar4_mesh_plotLayout.addWidget(self.canvas24_mesh)
        self.ui.b2senar4_mesh_plotLayout.addWidget(self.navigasi_mesh24)
        self.meshFigure25 = plt.figure()
        self.canvas25_mesh = FigureCanvas(self.meshFigure25)
        self.navigasi_mesh25 = NavigationToolbar(self.canvas25_mesh, self)
        self.ui.b2senar5_mesh_plotLayout.addWidget(self.canvas25_mesh)
        self.ui.b2senar5_mesh_plotLayout.addWidget(self.navigasi_mesh25)
        self.meshFigure26 = plt.figure()
        self.canvas26_mesh = FigureCanvas(self.meshFigure26)
        self.navigasi_mesh26 = NavigationToolbar(self.canvas26_mesh, self)
        self.ui.b2senar6_mesh_plotLayout.addWidget(self.canvas26_mesh)
        self.ui.b2senar6_mesh_plotLayout.addWidget(self.navigasi_mesh26)
        self.meshFigure27 = plt.figure()
        self.canvas27_mesh = FigureCanvas(self.meshFigure27)
        self.navigasi_mesh27 = NavigationToolbar(self.canvas27_mesh, self)
        self.ui.b2senar7_mesh_plotLayout.addWidget(self.canvas27_mesh)
        self.ui.b2senar7_mesh_plotLayout.addWidget(self.navigasi_mesh27)
        self.meshFigure28 = plt.figure()
        self.canvas28_mesh = FigureCanvas(self.meshFigure28)
        self.navigasi_mesh28 = NavigationToolbar(self.canvas28_mesh, self)
        self.ui.b2senar8_mesh_plotLayout.addWidget(self.canvas28_mesh)
        self.ui.b2senar8_mesh_plotLayout.addWidget(self.navigasi_mesh28)

        '''POLAR'''
        self.polarfigure21 = plt.figure()
        self.canvas21_polar = FigureCanvas(self.polarfigure21)
        self.navigasi_polar21 = NavigationToolbar(self.canvas21_polar, self)
        self.ui.b2senar1_layoutPolar.addWidget(self.canvas21_polar)
        self.ui.b2senar1_layoutPolar.addWidget(self.navigasi_polar21)
        self.polarfigure22 = plt.figure()
        self.canvas22_polar = FigureCanvas(self.polarfigure22)
        self.navigasi_polar22 = NavigationToolbar(self.canvas22_polar, self)
        self.ui.b2senar2_layout_polar.addWidget(self.canvas22_polar)
        self.ui.b2senar2_layout_polar.addWidget(self.navigasi_polar22)
        self.polarfigure23 = plt.figure()
        self.canvas23_polar = FigureCanvas(self.polarfigure23)
        self.navigasi_polar23 = NavigationToolbar(self.canvas23_polar, self)
        self.ui.b2senar3_layout_polar.addWidget(self.canvas23_polar)
        self.ui.b2senar3_layout_polar.addWidget(self.navigasi_polar23)
        self.polarfigure24 = plt.figure()
        self.canvas24_polar = FigureCanvas(self.polarfigure24)
        self.navigasi_polar24 = NavigationToolbar(self.canvas24_polar, self)
        self.ui.b2senar4_layout_polar.addWidget(self.canvas24_polar)
        self.ui.b2senar4_layout_polar.addWidget(self.navigasi_polar24)
        self.polarfigure25 = plt.figure()
        self.canvas25_polar = FigureCanvas(self.polarfigure25)
        self.navigasi_polar25 = NavigationToolbar(self.canvas25_polar, self)
        self.ui.b2senar5_layoutPolar.addWidget(self.canvas25_polar)
        self.ui.b2senar5_layoutPolar.addWidget(self.navigasi_polar25)
        self.polarfigure26 = plt.figure()
        self.canvas26_polar = FigureCanvas(self.polarfigure26)
        self.navigasi_polar26 = NavigationToolbar(self.canvas26_polar, self)
        self.ui.b2senar6_layoutPolar.addWidget(self.canvas26_polar)
        self.ui.b2senar6_layoutPolar.addWidget(self.navigasi_polar26)
        self.polarfigure27 = plt.figure()
        self.canvas27_polar = FigureCanvas(self.polarfigure27)
        self.navigasi_polar27 = NavigationToolbar(self.canvas27_polar, self)
        self.ui.b2senar7_layoutPolar.addWidget(self.canvas27_polar)
        self.ui.b2senar7_layoutPolar.addWidget(self.navigasi_polar27)
        self.polarfigure28 = plt.figure()
        self.canvas28_polar = FigureCanvas(self.polarfigure28)
        self.navigasi_polar28 = NavigationToolbar(self.canvas28_polar, self)
        self.ui.b2senar8_layoutPolar.addWidget(self.canvas28_polar)
        self.ui.b2senar8_layoutPolar.addWidget(self.navigasi_polar28)

        '''SET PLOT SEMUA SENAR BUNDENGAN2'''
        '''SENAR 1'''
        ax21 = self.meshFigure21.add_subplot(111)
        contour21 = grafik(2,1)
        contour21.kontur()
        plot_contour21 = ax21.contourf(contour21.frekuensi, contour21.arah, contour21.ttb, levels = contour21.interval_warna)
        self.meshFigure21.colorbar(plot_contour21).set_label(label = 'Tingkat Tekanan Bunyi (dB)', size = 12, labelpad = 15)
        ax21.set_xscale('log')
        ax21.set_xlabel('Frekuensi (Hz)', size = 12, labelpad = 15)
        ax21.set_ylabel('Arah bunyi', size = 12, labelpad = 15)
        self.canvas21_mesh.draw()

        self.tone21 = grafik(2,1)
        self.tone21.polar()
        self.axp21 = self.polarfigure21.add_subplot(projection = 'polar')
        self.axp21.plot(self.tone21.arah, self.tone21.ttb_tiap_arah[0])
        self.axp21.set_rmax(0)
        self.axp21.set_rticks(np.linspace(-54, -9, 6))
        self.ui.b2s1n1_cekbox.setChecked(True)
        '''SENAR 2'''
        ax22 = self.meshFigure22.add_subplot(111)
        contour22 = grafik(2,2)
        contour22.kontur()
        plot_contour22 = ax22.contourf(contour22.frekuensi, contour22.arah, contour22.ttb, levels = contour22.interval_warna)
        self.meshFigure22.colorbar(plot_contour22).set_label(label = 'Tingkat Tekanan Bunyi (dB)', size = 12, labelpad = 15)
        ax22.set_xscale('log')
        ax22.set_xlabel('Frekuensi (Hz)', size = 12, labelpad = 15)
        ax22.set_ylabel('Arah bunyi', size = 12, labelpad = 15)
        self.canvas22_mesh.draw()

        self.tone22 = grafik(2,2)
        self.tone22.polar()
        self.axp22 = self.polarfigure22.add_subplot(projection = 'polar')
        self.axp22.plot(self.tone22.arah, self.tone22.ttb_tiap_arah[0])
        self.axp22.set_rmax(0)
        self.axp22.set_rticks(np.linspace(-54, -9, 6))
        self.ui.b2s2n1_cekbox.setChecked(True)
        '''SENAR 3'''
        ax23 = self.meshFigure23.add_subplot(111)
        contour23 = grafik(2,3)
        contour23.kontur()
        plot_contour23 = ax23.contourf(contour23.frekuensi, contour23.arah, contour23.ttb, levels = contour23.interval_warna)
        self.meshFigure23.colorbar(plot_contour23).set_label(label = 'Tingkat Tekanan Bunyi (dB)', size = 12, labelpad = 15)
        ax23.set_xscale('log')
        ax23.set_xlabel('Frekuensi (Hz)', size = 12, labelpad = 15)
        ax23.set_ylabel('Arah bunyi', size = 12, labelpad = 15)
        self.canvas23_mesh.draw()

        self.tone23 = grafik(2,3)
        self.tone23.polar()
        self.axp23 = self.polarfigure23.add_subplot(projection = 'polar')
        self.axp23.plot(self.tone23.arah, self.tone23.ttb_tiap_arah[0])
        self.axp23.set_rmax(0)
        self.axp23.set_rticks(np.linspace(-54, -9, 6))
        self.ui.b2s3n1_cekbox.setChecked(True)
        '''SENAR 4'''
        ax24 = self.meshFigure24.add_subplot(111)
        contour24 = grafik(2,4)
        contour24.kontur()
        plot_contour24 = ax24.contourf(contour24.frekuensi, contour24.arah, contour24.ttb, levels = contour24.interval_warna)
        self.meshFigure24.colorbar(plot_contour24).set_label(label = 'Tingkat Tekanan Bunyi (dB)', size = 12, labelpad = 15)
        ax24.set_xscale('log')
        ax24.set_xlabel('Frekuensi (Hz)', size = 12, labelpad = 15)
        ax24.set_ylabel('Arah bunyi', size = 12, labelpad = 15)
        self.canvas24_mesh.draw()

        self.tone24 = grafik(2,4)
        self.tone24.polar()
        self.axp24 = self.polarfigure24.add_subplot(projection = 'polar')
        self.axp24.plot(self.tone24.arah, self.tone24.ttb_tiap_arah[0])
        self.axp24.set_rmax(0)
        self.axp24.set_rticks(np.linspace(-54, -9, 6))
        self.ui.b2s4n1_cekbox.setChecked(True)
        '''SENAR 5'''
        ax25 = self.meshFigure25.add_subplot(111)
        contour25 = grafik(2,5)
        contour25.kontur()
        plot_contour25 = ax25.contourf(contour25.frekuensi, contour25.arah, contour25.ttb, levels = contour25.interval_warna)
        self.meshFigure25.colorbar(plot_contour25).set_label(label = 'Tingkat Tekanan Bunyi (dB)', size = 12, labelpad = 15)
        ax25.set_xscale('log')
        ax25.set_xlabel('Frekuensi (Hz)', size = 12, labelpad = 15)
        ax25.set_ylabel('Arah bunyi', size = 12, labelpad = 15)
        self.canvas25_mesh.draw()

        self.tone25 = grafik(2,5)
        self.tone25.polar()
        self.axp25 = self.polarfigure25.add_subplot(projection = 'polar')
        self.axp25.plot(self.tone25.arah, self.tone25.ttb_tiap_arah[0])
        self.axp25.set_rmax(0)
        self.axp25.set_rticks(np.linspace(-54, -9, 6))
        self.ui.b2s5n1_cekbox.setChecked(True)
        '''SENAR 6'''
        ax26 = self.meshFigure26.add_subplot(111)
        contour26 = grafik(2,6)
        contour26.kontur()
        plot_contour26 = ax26.contourf(contour26.frekuensi, contour26.arah, contour26.ttb, levels = contour26.interval_warna)
        self.meshFigure26.colorbar(plot_contour26).set_label(label = 'Tingkat Tekanan Bunyi (dB)', size = 12, labelpad = 15)
        ax26.set_xscale('log')
        ax26.set_xlabel('Frekuensi (Hz)', size = 12, labelpad = 15)
        ax26.set_ylabel('Arah bunyi', size = 12, labelpad = 15)
        self.canvas26_mesh.draw()

        self.tone26 = grafik(2,6)
        self.tone26.polar()
        self.axp26 = self.polarfigure26.add_subplot(projection = 'polar')
        self.axp26.plot(self.tone26.arah, self.tone26.ttb_tiap_arah[0])
        self.axp26.set_rmax(0)
        self.axp26.set_rticks(np.linspace(-54, -9, 6))
        self.ui.b2s6n1_cekbox.setChecked(True)
        '''SENAR 7'''
        ax27 = self.meshFigure27.add_subplot(111)
        contour27 = grafik(2,7)
        contour27.kontur()
        plot_contour27 = ax27.contourf(contour27.frekuensi, contour27.arah, contour27.ttb, levels = contour27.interval_warna)
        self.meshFigure27.colorbar(plot_contour27).set_label(label = 'Tingkat Tekanan Bunyi (dB)', size = 12, labelpad = 15)
        ax27.set_xscale('log')
        ax27.set_xlabel('Frekuensi (Hz)', size = 12, labelpad = 15)
        ax27.set_ylabel('Arah bunyi', size = 12, labelpad = 15)
        self.canvas27_mesh.draw()

        self.tone27 = grafik(2,7)
        self.tone27.polar()
        self.axp27 = self.polarfigure27.add_subplot(projection = 'polar')
        self.axp27.plot(self.tone27.arah, self.tone27.ttb_tiap_arah[0])
        self.axp27.set_rmax(0)
        self.axp27.set_rticks(np.linspace(-54, -9, 6))
        self.ui.b2s7n1_cekbox.setChecked(True)
        '''SENAR 8'''
        ax28 = self.meshFigure28.add_subplot(111)
        contour28 = grafik(2,8)
        contour28.kontur()
        plot_contour28 = ax28.contourf(contour28.frekuensi, contour28.arah, contour28.ttb, levels = contour28.interval_warna)
        self.meshFigure28.colorbar(plot_contour28).set_label(label = 'Tingkat Tekanan Bunyi (dB)', size = 12, labelpad = 15)
        ax28.set_xscale('log')
        ax28.set_xlabel('Frekuensi (Hz)', size = 12, labelpad = 15)
        ax28.set_ylabel('Arah bunyi', size = 12, labelpad = 15)
        self.canvas28_mesh.draw()

        self.tone28 = grafik(2,8)
        self.tone28.polar()
        self.axp28 = self.polarfigure28.add_subplot(projection = 'polar')
        self.axp28.plot(self.tone28.arah, self.tone28.ttb_tiap_arah[0])
        self.axp28.set_rmax(0)
        self.axp28.set_rticks(np.linspace(-54, -9, 6))
        self.ui.b2s8n1_cekbox.setChecked(True)

    def defineCanvasCompare(self):
        self.polarcompare1 = plt.figure()
        self.canvas1_compare = FigureCanvas(self.polarcompare1)
        self.navigasi_compare1 = NavigationToolbar(self.canvas1_compare, self)
        self.ui.layout_polar_compare1.addWidget(self.canvas1_compare)
        self.ui.layout_polar_compare1.addWidget(self.navigasi_compare1)
        self.axc1 = self.polarcompare1.add_subplot(projection = 'polar')
        self.canvas1_compare.draw()
        self.polarcompare2 = plt.figure()
        self.canvas2_compare = FigureCanvas(self.polarcompare2)
        self.navigasi_compare2 = NavigationToolbar(self.canvas2_compare, self)
        self.ui.layout_polar_compare2.addWidget(self.canvas2_compare)
        self.ui.layout_polar_compare2.addWidget(self.navigasi_compare2)
        self.axc2 = self.polarcompare2.add_subplot(projection = 'polar')
        self.canvas2_compare.draw()
        self.polarcompare12 = plt.figure()
        self.canvas12_compare = FigureCanvas(self.polarcompare12)
        self.navigasi_compare12 = NavigationToolbar(self.canvas12_compare, self)
        self.ui.layout_polar_compare12.addWidget(self.canvas12_compare)
        self.ui.layout_polar_compare12.addWidget(self.navigasi_compare12)
        self.axc12 = self.polarcompare12.add_subplot(projection = 'polar')
        self.canvas12_compare.draw()



######## EVERY MENU CONFIGURATION ######

    def changeTabHome(self):
        self.ui.beranda_button.setStyleSheet("border-left: 3px solid #303f9f; background-color: #ecf0f1;")
        self.ui.bund1_button.setStyleSheet("")
        self.ui.bund2_button.setStyleSheet("")
        self.ui.compare_button.setStyleSheet("")
        self.ui.help_button.setStyleSheet("")
        self.ui.pages_widget.setCurrentWidget(self.ui.beranda_page)

#### BUNDENGAN 1 PAGES #####
    def changeTabBund1(self):
        self.ui.beranda_button.setStyleSheet("")
        self.ui.bund1_button.setStyleSheet("border-left: 3px solid #303f9f; background-color: #ecf0f1;")
        self.ui.bund2_button.setStyleSheet("")
        self.ui.compare_button.setStyleSheet("")
        self.ui.help_button.setStyleSheet("")
        self.ui.pages_widget.setCurrentWidget(self.ui.bund1_page)
        self.ui.stackedWidget_bund1.setCurrentWidget(self.ui.choice_bund1)

        
        

        ###DEFINE BUTTON FUNCTION####
        self.ui.b1s1_button.clicked.connect(self.b1s1Show)
        self.ui.b1s2_button.clicked.connect(self.b1s2Show)
        self.ui.b1s3_button.clicked.connect(self.b1s3Show)
        self.ui.b1s4_button.clicked.connect(self.b1s4Show)

    def backbund1(self):
        self.ui.stackedWidget_bund1.setCurrentWidget(self.ui.choice_bund1)
        
    '''SENAR 1'''
    def b1s1Show(self):
        self.ui.back_button_b1s1.clicked.connect(self.backbund1)
        self.ui.stackedWidget_bund1.setCurrentWidget(self.ui.b1senar1)
        self.ui.b1senar1_tabWidget.setCurrentWidget(self.ui.b1senar1_measure)
        self.ui.b1s1_applyBtn.clicked.connect(self.compare_b1s1)
        self.ui.b1s1_peakBtn.clicked.connect(self.open_peakb1s1)
    
    def open_peakb1s1(self):
        self.dialogNada_b1s1 = QDialog()
        self.ui_peakb1s1 = Ui_dial_nada_b1s1()
        self.ui_peakb1s1.setupUi(self.dialogNada_b1s1)
        self.dialogNada_b1s1.show()

    def compare_b1s1(self):
        self.polarfigure11.clear()
        self.axp11 = self.polarfigure11.add_subplot(projection = 'polar')
        if self.ui.b1s1n1_cekbox.isChecked() == True:
            self.axp11.plot(self.tone11.arah, self.tone11.ttb_tiap_arah[0], label = 'Nada 1')
        if self.ui.b1s1n2_cekbox.isChecked() == True:
            self.axp11.plot(self.tone11.arah, self.tone11.ttb_tiap_arah[1], label = 'Nada 2')
        if self.ui.b1s1n3_cekbox.isChecked() == True:
            self.axp11.plot(self.tone11.arah, self.tone11.ttb_tiap_arah[2], label = 'Nada 3')
        if self.ui.b1s1n4_cekbox.isChecked() == True:
            self.axp11.plot(self.tone11.arah, self.tone11.ttb_tiap_arah[3], label = 'Nada 4')
        if self.ui.b1s1n1_cekbox.isChecked() == False and self.ui.b1s1n2_cekbox.isChecked() == False and self.ui.b1s1n3_cekbox.isChecked() == False and self.ui.b1s1n4_cekbox.isChecked() == False:
            pass
        
        self.axp11.set_rmax(0)
        self.axp11.set_rticks(np.linspace(-54, -9, 6))
        self.axp11.legend(bbox_to_anchor=(1, 0.5))
        self.canvas11_polar.draw()

    '''SENAR 2'''
    def b1s2Show(self):
        self.ui.back_button_b1s2.clicked.connect(self.backbund1)
        self.ui.stackedWidget_bund1.setCurrentWidget(self.ui.b1senar2)
        self.ui.b1senar2_tabWidget.setCurrentWidget(self.ui.b1senar2_measure)
        self.ui.b1s2_applyBtn.clicked.connect(self.compare_b1s2)
        self.ui.b1s2_peakBtn.clicked.connect(self.open_peakb1s2)

    def open_peakb1s2(self):
        self.dialogNada_b1s2 = QDialog()
        self.ui_peakb1s2 = Ui_dial_nada_b1s2()
        self.ui_peakb1s2.setupUi(self.dialogNada_b1s2)
        self.dialogNada_b1s2.show()

    def compare_b1s2(self):
        self.polarfigure12.clear()
        self.axp12 = self.polarfigure12.add_subplot(projection = 'polar')
        if self.ui.b1s2n1_cekbox.isChecked() == True:
            self.axp12.plot(self.tone12.arah, self.tone12.ttb_tiap_arah[0], label = 'Nada 1')
        if self.ui.b1s2n2_cekbox.isChecked() == True:
            self.axp12.plot(self.tone12.arah, self.tone12.ttb_tiap_arah[1], label = 'Nada 2')
        if self.ui.b1s2n1_cekbox.isChecked() == False and self.ui.b1s2n2_cekbox.isChecked() == False:
            pass

        self.axp12.set_rmax(0)
        self.axp12.set_rticks(np.linspace(-54, -9, 6))
        self.axp12.legend(bbox_to_anchor=(1, 0.5))
        self.canvas12_polar.draw()
    '''SENAR 3'''
    def b1s3Show(self):
        self.ui.back_button_b1s3.clicked.connect(self.backbund1)
        self.ui.stackedWidget_bund1.setCurrentWidget(self.ui.b1senar3)
        self.ui.b1senar3_tabWidget.setCurrentWidget(self.ui.b1senar3_measure)
        self.ui.b1s3_applyBtn.clicked.connect(self.compare_b1s3)
        self.ui.b1s3_peakBtn.clicked.connect(self.open_peakb1s3)
    
    def open_peakb1s3(self):
        self.dialogNada_b1s3 = QDialog()
        self.ui_peakb1s3 = Ui_dial_nada_b1s3()
        self.ui_peakb1s3.setupUi(self.dialogNada_b1s3)
        self.dialogNada_b1s3.show()

    def compare_b1s3(self):
        self.polarfigure13.clear()
        self.axp13 = self.polarfigure13.add_subplot(projection = 'polar')
        if self.ui.b1s3n1_cekbox.isChecked() == True:
            self.axp13.plot(self.tone13.arah, self.tone13.ttb_tiap_arah[0], label = 'Nada 1')
        if self.ui.b1s3n2_cekbox.isChecked() == True:
            self.axp13.plot(self.tone13.arah, self.tone13.ttb_tiap_arah[1], label = 'Nada 2')
        if self.ui.b1s3n1_cekbox.isChecked() == False and self.ui.b1s3n2_cekbox.isChecked() == False:
            pass

        self.axp13.set_rmax(0)
        self.axp13.set_rticks(np.linspace(-54, -9, 6))
        self.axp13.legend(bbox_to_anchor=(1, 0.5))
        self.canvas13_polar.draw()
    '''SENAR 4'''
    def b1s4Show(self):
        self.ui.back_button_b1s4.clicked.connect(self.backbund1)
        self.ui.stackedWidget_bund1.setCurrentWidget(self.ui.b1senar4)
        self.ui.b1senar4_tabWidget.setCurrentWidget(self.ui.b1senar4_measure)
        self.ui.b1s4_applyBtn.clicked.connect(self.compare_b1s4)
        self.ui.b1s4_peakBtn.clicked.connect(self.open_peakb1s4)
    
    def open_peakb1s4(self):
        self.dialogNada_b1s4 = QDialog()
        self.ui_peakb1s4 = Ui_dial_nada_b1s4()
        self.ui_peakb1s4.setupUi(self.dialogNada_b1s4)
        self.dialogNada_b1s4.show()

    def compare_b1s4(self):
        self.polarfigure14.clear()
        self.axp14 = self.polarfigure14.add_subplot(projection = 'polar')
        if self.ui.b1s4n1_cekbox.isChecked() == True:
            self.axp14.plot(self.tone14.arah, self.tone14.ttb_tiap_arah[0], label = 'Nada 1')
        if self.ui.b1s4n2_cekbox.isChecked() == True:
            self.axp14.plot(self.tone14.arah, self.tone14.ttb_tiap_arah[1], label = 'Nada 2')
        if self.ui.b1s4n1_cekbox.isChecked() == False and self.ui.b1s4n2_cekbox.isChecked() == False:
            pass

        self.axp14.set_rmax(0)
        self.axp14.set_rticks(np.linspace(-54, -9, 6))
        self.axp14.legend(bbox_to_anchor=(1, 0.5))
        self.canvas14_polar.draw()


#BUNDENGAN 2 SETUP
    def changeTabBund2(self):
        self.ui.beranda_button.setStyleSheet("")
        self.ui.bund1_button.setStyleSheet("")
        self.ui.bund2_button.setStyleSheet("border-left: 3px solid #303f9f; background-color: #ecf0f1;")
        self.ui.compare_button.setStyleSheet("")
        self.ui.help_button.setStyleSheet("")
        self.ui.pages_widget.setCurrentWidget(self.ui.bund2_page)
        
        #####DEFINE BUTTON STRING#####
        self.ui.b2s1_button.clicked.connect(self.b2s1Show)
        self.ui.b2s2_button.clicked.connect(self.b2s2Show)
        self.ui.b2s3_button.clicked.connect(self.b2s3Show)
        self.ui.b2s4_button.clicked.connect(self.b2s4Show)
        self.ui.b2s5_button.clicked.connect(self.b2s5Show)
        self.ui.b2s6_button.clicked.connect(self.b2s6Show)
        self.ui.b2s7_button.clicked.connect(self.b2s7Show)
        self.ui.b2s8_button.clicked.connect(self.b2s8Show)

    def backbund2(self):
        self.ui.stackedWidget_bund2.setCurrentWidget(self.ui.choice_bund2)
    
    '''SENAR 1'''
    def b2s1Show(self):
        self.ui.back_button_b2s1.clicked.connect(self.backbund2)
        self.ui.stackedWidget_bund2.setCurrentWidget(self.ui.b2senar1)
        self.ui.b2senar1_tabWidget.setCurrentWidget(self.ui.b2senar1_measure)
        self.ui.b2s1_applyBtn.clicked.connect(self.compare_b2s1)
        self.ui.b2s1_peakBtn.clicked.connect(self.open_peakb2s1)
    def open_peakb2s1(self):
        self.dialogNada_b2s1 = QDialog()
        self.ui_peakb2s1 = Ui_dial_nada_b2s1()
        self.ui_peakb2s1.setupUi(self.dialogNada_b2s1)
        self.dialogNada_b2s1.show()
    def compare_b2s1(self):
        self.polarfigure21.clear()
        self.axp21 = self.polarfigure21.add_subplot(projection = 'polar')
        if self.ui.b2s1n1_cekbox.isChecked() == True:
            self.axp21.plot(self.tone21.arah, self.tone21.ttb_tiap_arah[0], label = 'Nada 1')
        if self.ui.b2s1n2_cekbox.isChecked() == True:
            self.axp21.plot(self.tone21.arah, self.tone21.ttb_tiap_arah[1], label = 'Nada 2')
        if self.ui.b2s1n1_cekbox.isChecked() == False and self.ui.b2s1n2_cekbox.isChecked() == False:
            pass
        
        self.axp21.set_rmax(0)
        self.axp21.set_rticks(np.linspace(-54, -9, 6))
        self.axp21.legend(bbox_to_anchor=(1, 0.5))
        self.canvas21_polar.draw()

    def b2s2Show(self):
        self.ui.back_button_b2s2.clicked.connect(self.backbund2)
        self.ui.stackedWidget_bund2.setCurrentWidget(self.ui.b2senar2)
        self.ui.b2senar2_tabWidget.setCurrentWidget(self.ui.b2senar2_measure)
        self.ui.b2s2_applyBtn.clicked.connect(self.compare_b2s2)
        self.ui.b2s2_peakBtn.clicked.connect(self.open_peakb2s2)
    def open_peakb2s2(self):
        self.dialogNada_b2s2 = QDialog()
        self.ui_peakb2s2 = Ui_dial_nada_b2s2()
        self.ui_peakb2s2.setupUi(self.dialogNada_b2s2)
        self.dialogNada_b2s2.show()
    def compare_b2s2(self):
        self.polarfigure22.clear()
        self.axp22 = self.polarfigure22.add_subplot(projection = 'polar')
        if self.ui.b2s2n1_cekbox.isChecked() == True:
            self.axp22.plot(self.tone22.arah, self.tone22.ttb_tiap_arah[0], label = 'Nada 1')
        if self.ui.b2s2n2_cekbox.isChecked() == True:
            self.axp22.plot(self.tone22.arah, self.tone22.ttb_tiap_arah[1], label = 'Nada 2')
        if self.ui.b2s2n1_cekbox.isChecked() == False and self.ui.b2s2n2_cekbox.isChecked() == False:
            pass
        
        self.axp22.set_rmax(0)
        self.axp22.set_rticks(np.linspace(-54, -9, 6))
        self.axp22.legend(bbox_to_anchor=(1, 0.5))
        self.canvas22_polar.draw()

    def b2s3Show(self):
        self.ui.back_button_b2s3.clicked.connect(self.backbund2)
        self.ui.stackedWidget_bund2.setCurrentWidget(self.ui.b2senar3)
        self.ui.b2senar3_tabWidget.setCurrentWidget(self.ui.b2senar3_measure)
        self.ui.b2s3_applyBtn.clicked.connect(self.compare_b2s3)
        self.ui.b2s3_peakBtn.clicked.connect(self.open_peakb2s3)
    def open_peakb2s3(self):
        self.dialogNada_b2s3 = QDialog()
        self.ui_peakb2s3 = Ui_dial_nada_b2s3()
        self.ui_peakb2s3.setupUi(self.dialogNada_b2s3)
        self.dialogNada_b2s3.show()
    def compare_b2s3(self):
        self.polarfigure23.clear()
        self.axp23 = self.polarfigure23.add_subplot(projection = 'polar')
        if self.ui.b2s3n1_cekbox.isChecked() == True:
            self.axp23.plot(self.tone23.arah, self.tone23.ttb_tiap_arah[0], label = 'Nada 1')
        if self.ui.b2s3n2_cekbox.isChecked() == True:
            self.axp23.plot(self.tone23.arah, self.tone23.ttb_tiap_arah[1], label = 'Nada 2')
        if self.ui.b2s3n3_cekbox.isChecked() == True:
            self.axp23.plot(self.tone23.arah, self.tone23.ttb_tiap_arah[2], label = 'Nada 3')
        if self.ui.b2s3n4_cekbox.isChecked() == True:
            self.axp23.plot(self.tone23.arah, self.tone23.ttb_tiap_arah[3], label = 'Nada 4')
        if self.ui.b2s3n1_cekbox.isChecked() == False and self.ui.b2s3n2_cekbox.isChecked() == False and self.ui.b2s3n3_cekbox.isChecked() == False and self.ui.b2s3n4_cekbox.isChecked() == False:
            pass
        
        self.axp23.set_rmax(0)
        self.axp23.set_rticks(np.linspace(-54, -9, 6))
        self.axp23.legend(bbox_to_anchor=(1, 0.5))
        self.canvas23_polar.draw()

    def b2s4Show(self):
        self.ui.back_button_b2s4.clicked.connect(self.backbund2)
        self.ui.stackedWidget_bund2.setCurrentWidget(self.ui.b2senar4)
        self.ui.b2senar4_tabWidget.setCurrentWidget(self.ui.b2senar4_measure)
        self.ui.b2s4_applyBtn.clicked.connect(self.compare_b2s4)
        self.ui.b2s4_peakBtn.clicked.connect(self.open_peakb2s4)
    def open_peakb2s4(self):
        self.dialogNada_b2s4 = QDialog()
        self.ui_peakb2s4 = Ui_dial_nada_b2s4()
        self.ui_peakb2s4.setupUi(self.dialogNada_b2s4)
        self.dialogNada_b2s4.show()
    def compare_b2s4(self):
        self.polarfigure24.clear()
        self.axp24 = self.polarfigure24.add_subplot(projection = 'polar')
        if self.ui.b2s4n1_cekbox.isChecked() == True:
            self.axp24.plot(self.tone24.arah, self.tone24.ttb_tiap_arah[0], label = 'Nada 1')
        if self.ui.b2s4n2_cekbox.isChecked() == True:
            self.axp24.plot(self.tone24.arah, self.tone24.ttb_tiap_arah[1], label = 'Nada 2')
        if self.ui.b2s4n3_cekbox.isChecked() == True:
            self.axp24.plot(self.tone24.arah, self.tone24.ttb_tiap_arah[2], label = 'Nada 3')
        if self.ui.b2s4n1_cekbox.isChecked() == False and self.ui.b2s4n2_cekbox.isChecked() == False and self.ui.b2s4n3_cekbox.isChecked() == False:
            pass
        
        self.axp24.set_rmax(0)
        self.axp24.set_rticks(np.linspace(-54, -9, 6))
        self.axp24.legend(bbox_to_anchor=(1, 0.5))
        self.canvas24_polar.draw()

    def b2s5Show(self):
        self.ui.back_button_b2s5.clicked.connect(self.backbund2)
        self.ui.stackedWidget_bund2.setCurrentWidget(self.ui.b2senar5)
        self.ui.b2senar5_tabWidget.setCurrentWidget(self.ui.b2senar5_measure)
        self.ui.b2s5_applyBtn.clicked.connect(self.compare_b2s5)
        self.ui.b2s5_peakBtn.clicked.connect(self.open_peakb2s5)
    def open_peakb2s5(self):
        self.dialogNada_b2s5 = QDialog()
        self.ui_peakb2s5 = Ui_dial_nada_b2s5()
        self.ui_peakb2s5.setupUi(self.dialogNada_b2s5)
        self.dialogNada_b2s5.show()
    def compare_b2s5(self):
        self.polarfigure25.clear()
        self.axp25 = self.polarfigure25.add_subplot(projection = 'polar')
        if self.ui.b2s5n1_cekbox.isChecked() == True:
            self.axp25.plot(self.tone25.arah, self.tone25.ttb_tiap_arah[0], label = 'Nada 1')
        if self.ui.b2s5n2_cekbox.isChecked() == True:
            self.axp25.plot(self.tone25.arah, self.tone25.ttb_tiap_arah[1], label = 'Nada 2')
        if self.ui.b2s5n1_cekbox.isChecked() == False and self.ui.b2s5n2_cekbox.isChecked() == False:
            pass
        
        self.axp25.set_rmax(0)
        self.axp25.set_rticks(np.linspace(-54, -9, 6))
        self.axp25.legend(bbox_to_anchor=(1, 0.5))
        self.canvas25_polar.draw()

    def b2s6Show(self):
        self.ui.back_button_b2s6.clicked.connect(self.backbund2)
        self.ui.stackedWidget_bund2.setCurrentWidget(self.ui.b2senar6)
        self.ui.b2senar6_tabWidget.setCurrentWidget(self.ui.b2senar6_measure)
        self.ui.b2s6_applyBtn.clicked.connect(self.compare_b2s6)
        self.ui.b2s6_peakBtn.clicked.connect(self.open_peakb2s6)
    def open_peakb2s6(self):
        self.dialogNada_b2s6 = QDialog()
        self.ui_peakb2s6 = Ui_dial_nada_b2s6()
        self.ui_peakb2s6.setupUi(self.dialogNada_b2s6)
        self.dialogNada_b2s6.show()
    def compare_b2s6(self):
        self.polarfigure26.clear()
        self.axp26 = self.polarfigure26.add_subplot(projection = 'polar')
        if self.ui.b2s6n1_cekbox.isChecked() == True:
            self.axp26.plot(self.tone26.arah, self.tone26.ttb_tiap_arah[0], label = 'Nada 1')
        if self.ui.b2s6n2_cekbox.isChecked() == True:
            self.axp26.plot(self.tone26.arah, self.tone26.ttb_tiap_arah[1], label = 'Nada 2')
        if self.ui.b2s6n3_cekbox.isChecked() == True:
            self.axp26.plot(self.tone26.arah, self.tone26.ttb_tiap_arah[2], label = 'Nada 3')
        if self.ui.b2s6n4_cekbox.isChecked() == True:
            self.axp26.plot(self.tone26.arah, self.tone26.ttb_tiap_arah[3], label = 'Nada 4')
        if self.ui.b2s6n1_cekbox.isChecked() == False and self.ui.b2s6n2_cekbox.isChecked() == False and self.ui.b2s6n3_cekbox.isChecked() == False and self.ui.b2s6n4_cekbox.isChecked() == False:
            pass
        
        self.axp26.set_rmax(0)
        self.axp26.set_rticks(np.linspace(-54, -9, 6))
        self.axp26.legend(bbox_to_anchor=(1, 0.5))
        self.canvas26_polar.draw()

    def b2s7Show(self):
        self.ui.back_button_b2s7.clicked.connect(self.backbund2)
        self.ui.stackedWidget_bund2.setCurrentWidget(self.ui.b2senar7)
        self.ui.b2senar7_tabWidget.setCurrentWidget(self.ui.b2senar7_measure)
        self.ui.b2s7_applyBtn.clicked.connect(self.compare_b2s7)
        self.ui.b2s7_peakBtn.clicked.connect(self.open_peakb2s7)
    def open_peakb2s7(self):
        self.dialogNada_b2s7 = QDialog()
        self.ui_peakb2s7 = Ui_dial_nada_b2s7()
        self.ui_peakb2s7.setupUi(self.dialogNada_b2s7)
        self.dialogNada_b2s7.show()
    def compare_b2s7(self):
        self.polarfigure27.clear()
        self.axp27 = self.polarfigure27.add_subplot(projection = 'polar')
        if self.ui.b2s7n1_cekbox.isChecked() == True:
            self.axp27.plot(self.tone27.arah, self.tone27.ttb_tiap_arah[0], label = 'Nada 1')
        if self.ui.b2s7n2_cekbox.isChecked() == True:
            self.axp27.plot(self.tone27.arah, self.tone27.ttb_tiap_arah[1], label = 'Nada 2')
        if self.ui.b2s7n1_cekbox.isChecked() == False and self.ui.b2s7n2_cekbox.isChecked() == False:
            pass
        
        self.axp27.set_rmax(0)
        self.axp27.set_rticks(np.linspace(-54, -9, 6))
        self.axp27.legend(bbox_to_anchor=(1, 0.5))
        self.canvas27_polar.draw()

    def b2s8Show(self):
        self.ui.back_button_b2s8.clicked.connect(self.backbund2)
        self.ui.stackedWidget_bund2.setCurrentWidget(self.ui.b2senar8)
        self.ui.b2senar8_tabWidget.setCurrentWidget(self.ui.b2senar8_measure)
        self.ui.b2s8_applyBtn.clicked.connect(self.compare_b2s8)
        self.ui.b2s8_peakBtn.clicked.connect(self.open_peakb2s8)
    def open_peakb2s8(self):
        self.dialogNada_b2s8 = QDialog()
        self.ui_peakb2s8 = Ui_dial_nada_b2s8()
        self.ui_peakb2s8.setupUi(self.dialogNada_b2s8)
        self.dialogNada_b2s8.show()
    def compare_b2s8(self):
        self.polarfigure28.clear()
        self.axp28 = self.polarfigure28.add_subplot(projection = 'polar')
        if self.ui.b2s8n1_cekbox.isChecked() == True:
            self.axp28.plot(self.tone28.arah, self.tone28.ttb_tiap_arah[0], label = 'Nada 1')
        if self.ui.b2s8n2_cekbox.isChecked() == True:
            self.axp28.plot(self.tone28.arah, self.tone28.ttb_tiap_arah[1], label = 'Nada 2')
        if self.ui.b2s8n1_cekbox.isChecked() == False and self.ui.b2s8n2_cekbox.isChecked() == False:
            pass
        
        self.axp28.set_rmax(0)
        self.axp28.set_rticks(np.linspace(-54, -9, 6))
        self.axp28.legend(bbox_to_anchor=(1, 0.5))
        self.canvas28_polar.draw()
        
        

    



    '''COMPARE PAGE SETUP'''
    def changeTabCompare(self):
        self.ui.beranda_button.setStyleSheet("")
        self.ui.bund1_button.setStyleSheet("")
        self.ui.bund2_button.setStyleSheet("")
        self.ui.compare_button.setStyleSheet("border-left: 3px solid #303f9f; background-color: #ecf0f1;")
        self.ui.help_button.setStyleSheet("")
        self.ui.pages_widget.setCurrentWidget(self.ui.compare_page)

        self.ui.clear_compare1_btn.clicked.connect(self.clearCompare1)
        self.ui.ket_arahb1.clicked.connect(self.openAngleClue)
        self.ui.compareb1s1.clicked.connect(self.dial_b1s1)
        self.ui.compareb1s2.clicked.connect(self.dial_b1s2)
        self.ui.compareb1s3.clicked.connect(self.dial_b1s3)
        self.ui.compareb1s4.clicked.connect(self.dial_b1s4)

        self.ui.clear_compare2_btn.clicked.connect(self.clearCompare2)
        self.ui.ket_arahb2.clicked.connect(self.openAngleClue)
        self.ui.compareb2s1.clicked.connect(self.dial_b2s1)
        self.ui.compareb2s2.clicked.connect(self.dial_b2s2)
        self.ui.compareb2s3.clicked.connect(self.dial_b2s3)
        self.ui.compareb2s4.clicked.connect(self.dial_b2s4)
        self.ui.compareb2s5.clicked.connect(self.dial_b2s5)
        self.ui.compareb2s6.clicked.connect(self.dial_b2s6)
        self.ui.compareb2s7.clicked.connect(self.dial_b2s7)
        self.ui.compareb2s8.clicked.connect(self.dial_b2s8)

        self.ui.clear_compare12.clicked.connect(self.clearCompare12)
        self.ui.ket_arahb12.clicked.connect(self.openAngleClue)
        self.ui.b1compare_btn.clicked.connect(self.dial_allb1)
        self.ui.b2compare_btn.clicked.connect(self.dial_allb2)

    def openAngleClue(self):
        self.dialMethodAngle = QDialog()
        self.dialogAngle = Ui_ket_arah_polar()
        self.dialogAngle.setupUi(self.dialMethodAngle)
        self.dialMethodAngle.show()


    '''COMPARE PAGE BUND 1'''
    def clearCompare1(self):
        self.polarcompare1.clear()
        self.axc1 = self.polarcompare1.add_subplot(projection = 'polar')
        self.canvas1_compare.draw()

    
    def dial_b1s1(self):
        self.dialMethod_b1s1 = QDialog()
        self.dialogb1s1 = Ui_dialog_compareb1s1()
        self.dialogb1s1.setupUi(self.dialMethod_b1s1)
        self.dialMethod_b1s1.show()

        self.dialogb1s1.cancel_btn.clicked.connect(lambda: self.dialMethod_b1s1.close())
        self.dialogb1s1.apply_btn.clicked.connect(self.getValue_b1s1)

    def getValue_b1s1(self):
        if self.dialogb1s1.n1_cekbox.isChecked() == True:
            self.axc1.plot(self.tone11.arah, self.tone11.ttb_tiap_arah[0], label = 'Nada 1 Senar 1')
        if self.dialogb1s1.n2_cekbox.isChecked() == True:
            self.axc1.plot(self.tone11.arah, self.tone11.ttb_tiap_arah[1], label = 'Nada 2 Senar 1')
        if self.dialogb1s1.n3_cekbox.isChecked() == True:
            self.axc1.plot(self.tone11.arah, self.tone11.ttb_tiap_arah[2], label = 'Nada 3 Senar 1')
        if self.dialogb1s1.n4_cekbox.isChecked() == True:
            self.axc1.plot(self.tone11.arah, self.tone11.ttb_tiap_arah[3], label = 'Nada 4 Senar 1')
            

        self.axc1.set_rmax(0)
        self.axc1.set_rticks(np.linspace(-54, -9, 6))
        self.axc1.legend(bbox_to_anchor=(1, 0.5))
        self.canvas1_compare.draw()

        self.dialMethod_b1s1.close()

    def dial_b1s2(self):
        self.dialMethod_b1s2 = QDialog()
        self.dialogb1s2 = Ui_dialog_compareb1s2()
        self.dialogb1s2.setupUi(self.dialMethod_b1s2)
        self.dialMethod_b1s2.show()

        self.dialogb1s2.cancel_btn.clicked.connect(lambda: self.dialMethod_b1s2.close())
        self.dialogb1s2.apply_btn.clicked.connect(self.getValue_b1s2)

    def getValue_b1s2(self):
        if self.dialogb1s2.n1_cekbox.isChecked() == True:
            self.axc1.plot(self.tone12.arah, self.tone12.ttb_tiap_arah[0], label = 'Nada 1 Senar 2')
        if self.dialogb1s2.n2_cekbox.isChecked() == True:
            self.axc1.plot(self.tone12.arah, self.tone12.ttb_tiap_arah[1], label = 'Nada 2 Senar 2')
        
        self.axc1.set_rmax(0)
        self.axc1.set_rticks(np.linspace(-54, -9, 6))
        self.axc1.legend(bbox_to_anchor=(1, 0.5))
        self.canvas1_compare.draw()

        self.dialMethod_b1s2.close()

    def dial_b1s3(self):
        self.dialMethod_b1s3 = QDialog()
        self.dialogb1s3 = Ui_dialog_compareb1s3()
        self.dialogb1s3.setupUi(self.dialMethod_b1s3)
        self.dialMethod_b1s3.show()

        self.dialogb1s3.cancel_btn.clicked.connect(lambda: self.dialMethod_b1s3.close())
        self.dialogb1s3.apply_btn.clicked.connect(self.getValue_b1s3)

    def getValue_b1s3(self):
        if self.dialogb1s3.n1_cekbox.isChecked() == True:
            self.axc1.plot(self.tone13.arah, self.tone13.ttb_tiap_arah[0], label = 'Nada 1 Senar 3')
        if self.dialogb1s3.n2_cekbox.isChecked() == True:
            self.axc1.plot(self.tone13.arah, self.tone13.ttb_tiap_arah[1], label = 'Nada 2 Senar 3')

        self.axc1.set_rmax(0)
        self.axc1.set_rticks(np.linspace(-54, -9, 6))
        self.axc1.legend(bbox_to_anchor=(1, 0.5))
        self.canvas1_compare.draw()

        self.dialMethod_b1s3.close()

    def dial_b1s4(self):
        self.dialMethod_b1s4 = QDialog()
        self.dialogb1s4 = Ui_dialog_compareb1s4()
        self.dialogb1s4.setupUi(self.dialMethod_b1s4)
        self.dialMethod_b1s4.show()

        self.dialogb1s4.cancel_btn.clicked.connect(lambda: self.dialMethod_b1s4.close())
        self.dialogb1s4.apply_btn.clicked.connect(self.getValue_b1s4)

    def getValue_b1s4(self):
        if self.dialogb1s4.n1_cekbox.isChecked() == True:
            self.axc1.plot(self.tone14.arah, self.tone14.ttb_tiap_arah[0], label = 'Nada 1 Senar 4')
        if self.dialogb1s4.n2_cekbox.isChecked() == True:
            self.axc1.plot(self.tone14.arah, self.tone14.ttb_tiap_arah[1], label = 'Nada 2 Senar 4')

        self.axc1.set_rmax(0)
        self.axc1.set_rticks(np.linspace(-54, -9, 6))
        self.axc1.legend(bbox_to_anchor=(1, 0.5))
        self.canvas1_compare.draw()

        self.dialMethod_b1s4.close()

    '''COMPARE PAGE BUND 2'''
    def clearCompare2(self):
        self.polarcompare2.clear()
        self.axc2 = self.polarcompare2.add_subplot(projection = 'polar')
        self.canvas2_compare.draw()

    def dial_b2s1(self):
        self.dialMethod_b2s1 = QDialog()
        self.dialogb2s1 = Ui_dialog_compareb2s1()
        self.dialogb2s1.setupUi(self.dialMethod_b2s1)
        self.dialMethod_b2s1.show()

        self.dialogb2s1.cancel_btn.clicked.connect(lambda: self.dialMethod_b2s1.close())
        self.dialogb2s1.apply_btn.clicked.connect(self.getValue_b2s1)
    def getValue_b2s1(self):
        if self.dialogb2s1.n1_cekbox.isChecked() == True:
            self.axc2.plot(self.tone21.arah, self.tone21.ttb_tiap_arah[0], label = 'Nada 1 Senar 1')
        if self.dialogb2s1.n2_cekbox.isChecked() == True:
            self.axc2.plot(self.tone21.arah, self.tone21.ttb_tiap_arah[1], label = 'Nada 2 Senar 1') 

        self.axc2.set_rmax(0)
        self.axc2.set_rticks(np.linspace(-54, -9, 6))
        self.axc2.legend(bbox_to_anchor=(1, 0.5))
        self.canvas2_compare.draw()

        self.dialMethod_b2s1.close()

    def dial_b2s2(self):
        self.dialMethod_b2s2 = QDialog()
        self.dialogb2s2 = Ui_dialog_compareb2s2()
        self.dialogb2s2.setupUi(self.dialMethod_b2s2)
        self.dialMethod_b2s2.show()

        self.dialogb2s2.cancel_btn.clicked.connect(lambda: self.dialMethod_b2s2.close())
        self.dialogb2s2.apply_btn.clicked.connect(self.getValue_b2s2)
    def getValue_b2s2(self):
        if self.dialogb2s2.n1_cekbox.isChecked() == True:
            self.axc2.plot(self.tone22.arah, self.tone22.ttb_tiap_arah[0], label = 'Nada 1 Senar 2')
        if self.dialogb2s2.n2_cekbox.isChecked() == True:
            self.axc2.plot(self.tone22.arah, self.tone22.ttb_tiap_arah[1], label = 'Nada 2 Senar 2') 

        self.axc2.set_rmax(0)
        self.axc2.set_rticks(np.linspace(-54, -9, 6))
        self.axc2.legend(bbox_to_anchor=(1, 0.5))
        self.canvas2_compare.draw()

        self.dialMethod_b2s2.close()

    def dial_b2s3(self):
        self.dialMethod_b2s3 = QDialog()
        self.dialogb2s3 = Ui_dialog_compareb2s3()
        self.dialogb2s3.setupUi(self.dialMethod_b2s3)
        self.dialMethod_b2s3.show()

        self.dialogb2s3.cancel_btn.clicked.connect(lambda: self.dialMethod_b2s3.close())
        self.dialogb2s3.apply_btn.clicked.connect(self.getValue_b2s3)
    def getValue_b2s3(self):
        if self.dialogb2s3.n1_cekbox.isChecked() == True:
            self.axc2.plot(self.tone23.arah, self.tone23.ttb_tiap_arah[0], label = 'Nada 1 Senar 3')
        if self.dialogb2s3.n2_cekbox.isChecked() == True:
            self.axc2.plot(self.tone23.arah, self.tone23.ttb_tiap_arah[1], label = 'Nada 2 Senar 3') 
        if self.dialogb2s3.n3_cekbox.isChecked() == True:
            self.axc2.plot(self.tone23.arah, self.tone23.ttb_tiap_arah[2], label = 'Nada 3 Senar 3') 
        if self.dialogb2s3.n4_cekbox.isChecked() == True:
            self.axc2.plot(self.tone23.arah, self.tone23.ttb_tiap_arah[3], label = 'Nada 4 Senar 3') 

        self.axc2.set_rmax(0)
        self.axc2.set_rticks(np.linspace(-54, -9, 6))
        self.axc2.legend(bbox_to_anchor=(1, 0.5))
        self.canvas2_compare.draw()

        self.dialMethod_b2s3.close()

    def dial_b2s4(self):
        self.dialMethod_b2s4 = QDialog()
        self.dialogb2s4 = Ui_dialog_compareb2s4()
        self.dialogb2s4.setupUi(self.dialMethod_b2s4)
        self.dialMethod_b2s4.show()

        self.dialogb2s4.cancel_btn.clicked.connect(lambda: self.dialMethod_b2s4.close())
        self.dialogb2s4.apply_btn.clicked.connect(self.getValue_b2s4)
    def getValue_b2s4(self):
        if self.dialogb2s4.n1_cekbox.isChecked() == True:
            self.axc2.plot(self.tone24.arah, self.tone24.ttb_tiap_arah[0], label = 'Nada 1 Senar 4')
        if self.dialogb2s4.n2_cekbox.isChecked() == True:
            self.axc2.plot(self.tone24.arah, self.tone24.ttb_tiap_arah[1], label = 'Nada 2 Senar 4') 
        if self.dialogb2s4.n3_cekbox.isChecked() == True:
            self.axc2.plot(self.tone24.arah, self.tone24.ttb_tiap_arah[2], label = 'Nada 3 Senar 4')

        self.axc2.set_rmax(0)
        self.axc2.set_rticks(np.linspace(-54, -9, 6))
        self.axc2.legend(bbox_to_anchor=(1, 0.5))
        self.canvas2_compare.draw()

        self.dialMethod_b2s4.close()
        
    def dial_b2s5(self):
        self.dialMethod_b2s5 = QDialog()
        self.dialogb2s5 = Ui_dialog_compareb2s5()
        self.dialogb2s5.setupUi(self.dialMethod_b2s5)
        self.dialMethod_b2s5.show()

        self.dialogb2s5.cancel_btn.clicked.connect(lambda: self.dialMethod_b2s5.close())
        self.dialogb2s5.apply_btn.clicked.connect(self.getValue_b2s5)
    def getValue_b2s5(self):
        if self.dialogb2s5.n1_cekbox.isChecked() == True:
            self.axc2.plot(self.tone25.arah, self.tone25.ttb_tiap_arah[0], label = 'Nada 1 Senar 5')
        if self.dialogb2s5.n2_cekbox.isChecked() == True:
            self.axc2.plot(self.tone25.arah, self.tone25.ttb_tiap_arah[1], label = 'Nada 2 Senar 5') 
        
        self.axc2.set_rmax(0)
        self.axc2.set_rticks(np.linspace(-54, -9, 6))
        self.axc2.legend(bbox_to_anchor=(1, 0.5))
        self.canvas2_compare.draw()

        self.dialMethod_b2s5.close()

    def dial_b2s6(self):
        self.dialMethod_b2s6 = QDialog()
        self.dialogb2s6 = Ui_dialog_compareb2s6()
        self.dialogb2s6.setupUi(self.dialMethod_b2s6)
        self.dialMethod_b2s6.show()

        self.dialogb2s6.cancel_btn.clicked.connect(lambda: self.dialMethod_b2s6.close())
        self.dialogb2s6.apply_btn.clicked.connect(self.getValue_b2s6)
    def getValue_b2s6(self):
        if self.dialogb2s6.n1_cekbox.isChecked() == True:
            self.axc2.plot(self.tone26.arah, self.tone26.ttb_tiap_arah[0], label = 'Nada 1 Senar 6')
        if self.dialogb2s6.n2_cekbox.isChecked() == True:
            self.axc2.plot(self.tone26.arah, self.tone26.ttb_tiap_arah[1], label = 'Nada 2 Senar 6') 
        if self.dialogb2s6.n3_cekbox.isChecked() == True:
            self.axc2.plot(self.tone26.arah, self.tone26.ttb_tiap_arah[2], label = 'Nada 3 Senar 6') 
        if self.dialogb2s6.n4_cekbox.isChecked() == True:
            self.axc2.plot(self.tone26.arah, self.tone26.ttb_tiap_arah[3], label = 'Nada 4 Senar 6') 
        
        self.axc2.set_rmax(0)
        self.axc2.set_rticks(np.linspace(-54, -9, 6))
        self.axc2.legend(bbox_to_anchor=(1, 0.5))
        self.canvas2_compare.draw()

        self.dialMethod_b2s6.close()

    def dial_b2s7(self):
        self.dialMethod_b2s7 = QDialog()
        self.dialogb2s7 = Ui_dialog_compareb2s7()
        self.dialogb2s7.setupUi(self.dialMethod_b2s7)
        self.dialMethod_b2s7.show()

        self.dialogb2s7.cancel_btn.clicked.connect(lambda: self.dialMethod_b2s7.close())
        self.dialogb2s7.apply_btn.clicked.connect(self.getValue_b2s7)
    def getValue_b2s7(self):
        if self.dialogb2s7.n1_cekbox.isChecked() == True:
            self.axc2.plot(self.tone27.arah, self.tone27.ttb_tiap_arah[0], label = 'Nada 1 Senar 7')
        if self.dialogb2s7.n2_cekbox.isChecked() == True:
            self.axc2.plot(self.tone27.arah, self.tone27.ttb_tiap_arah[1], label = 'Nada 2 Senar 7') 
        
        self.axc2.set_rmax(0)
        self.axc2.set_rticks(np.linspace(-54, -9, 6))
        self.axc2.legend(bbox_to_anchor=(1, 0.5))
        self.canvas2_compare.draw()

        self.dialMethod_b2s7.close()

    def dial_b2s8(self):
        self.dialMethod_b2s8 = QDialog()
        self.dialogb2s8 = Ui_dialog_compareb2s8()
        self.dialogb2s8.setupUi(self.dialMethod_b2s8)
        self.dialMethod_b2s8.show()

        self.dialogb2s8.cancel_btn.clicked.connect(lambda: self.dialMethod_b2s8.close())
        self.dialogb2s8.apply_btn.clicked.connect(self.getValue_b2s8)
    def getValue_b2s8(self):
        if self.dialogb2s8.n1_cekbox.isChecked() == True:
            self.axc2.plot(self.tone28.arah, self.tone28.ttb_tiap_arah[0], label = 'Nada 1 Senar 8')
        if self.dialogb2s8.n2_cekbox.isChecked() == True:
            self.axc2.plot(self.tone28.arah, self.tone28.ttb_tiap_arah[1], label = 'Nada 2 Senar 8') 
        
        self.axc2.set_rmax(0)
        self.axc2.set_rticks(np.linspace(-54, -9, 6))
        self.axc2.legend(bbox_to_anchor=(1, 0.5))
        self.canvas2_compare.draw()

        self.dialMethod_b2s8.close()

    '''COMPARE TWO BUNDENGAN'''
    def clearCompare12(self):
        self.polarcompare12.clear()
        self.axc12 = self.polarcompare12.add_subplot(projection = 'polar')
        self.canvas12_compare.draw()

    def dial_allb1(self):
        self.dialMethod_b1 = QDialog()
        self.dialogb1 = Ui_all_compare_b1()
        self.dialogb1.setupUi(self.dialMethod_b1)
        self.dialMethod_b1.show()

        self.dialogb1.s1_btn.clicked.connect(self.pickTone11)
        self.dialogb1.s2_btn.clicked.connect(self.pickTone12)
        self.dialogb1.s3_btn.clicked.connect(self.pickTone13)
        self.dialogb1.s4_btn.clicked.connect(self.pickTone14)

    def pickTone11(self):
        self.dialogb1.stackedWidget.setCurrentWidget(self.dialogb1.s1page)
        
        self.dialogb1.s1_btn.setStyleSheet("background-color: #303f9f; border-color: #303f9f ; color: #ffffff;")
        self.dialogb1.s2_btn.setStyleSheet("")
        self.dialogb1.s3_btn.setStyleSheet("")
        self.dialogb1.s4_btn.setStyleSheet("")

        self.dialogb1.s1apply_btn.clicked.connect(self.setTone11)

    def setTone11(self):
        if self.dialogb1.s1n1_cekbox.isChecked() == True:
            self.axc12.plot(self.tone11.arah, self.tone11.ttb_tiap_arah[0], label = 'Nada 1 Senar 1\nPak Munir')
        if self.dialogb1.s1n2_cekbox.isChecked() == True:
            self.axc12.plot(self.tone11.arah, self.tone11.ttb_tiap_arah[1], label = 'Nada 2 Senar 1\nPak Munir')
        if self.dialogb1.s1n3_cekbox.isChecked() == True:
            self.axc12.plot(self.tone11.arah, self.tone11.ttb_tiap_arah[2], label = 'Nada 3 Senar 1\nPak Munir')
        if self.dialogb1.s1n4_cekbox.isChecked() == True:
            self.axc12.plot(self.tone11.arah, self.tone11.ttb_tiap_arah[3], label = 'Nada 4 Senar 1\nPak Munir')

        self.axc12.set_rmax(0)
        self.axc12.set_rticks(np.linspace(-54, -9, 6))
        self.axc12.legend(bbox_to_anchor=(1, 0.5))
        self.canvas12_compare.draw()
        self.dialMethod_b1.close()        

    def pickTone12(self):
        self.dialogb1.stackedWidget.setCurrentWidget(self.dialogb1.s2page)
        
        self.dialogb1.s1_btn.setStyleSheet("")
        self.dialogb1.s2_btn.setStyleSheet("background-color: #303f9f; border: 0px; color: #ffffff;")
        self.dialogb1.s3_btn.setStyleSheet("")
        self.dialogb1.s4_btn.setStyleSheet("")

        self.dialogb1.s2apply_btn.clicked.connect(self.setTone12)

    def setTone12(self):
        if self.dialogb1.s2n1_cekbox.isChecked() == True:
            self.axc12.plot(self.tone12.arah, self.tone12.ttb_tiap_arah[0], label = 'Nada 1 Senar 2\nPak Munir')
        if self.dialogb1.s2n2_cekbox.isChecked() == True:
            self.axc12.plot(self.tone12.arah, self.tone12.ttb_tiap_arah[1], label = 'Nada 2 Senar 2\nPak Munir')
        
        self.axc12.set_rmax(0)
        self.axc12.set_rticks(np.linspace(-54, -9, 6))
        self.axc12.legend(bbox_to_anchor=(1, 0.5))
        self.canvas12_compare.draw()
        self.dialMethod_b1.close()

    def pickTone13(self):
        self.dialogb1.stackedWidget.setCurrentWidget(self.dialogb1.s3page)
        
        self.dialogb1.s1_btn.setStyleSheet("")
        self.dialogb1.s2_btn.setStyleSheet("")
        self.dialogb1.s3_btn.setStyleSheet("background-color: #303f9f; border-color: #303f9f ; color: #ffffff;")
        self.dialogb1.s4_btn.setStyleSheet("")

        self.dialogb1.s3apply_btn.clicked.connect(self.setTone13)

    def setTone13(self):
        if self.dialogb1.s3n1_cekbox.isChecked() == True:
            self.axc12.plot(self.tone13.arah, self.tone13.ttb_tiap_arah[0], label = 'Nada 1 Senar 3\nPak Munir')
        if self.dialogb1.s3n2_cekbox.isChecked() == True:
            self.axc12.plot(self.tone13.arah, self.tone13.ttb_tiap_arah[1], label = 'Nada 2 Senar 3\nPak Munir')

        self.axc12.set_rmax(0)
        self.axc12.set_rticks(np.linspace(-54, -9, 6))
        self.axc12.legend(bbox_to_anchor=(1, 0.5))
        self.canvas12_compare.draw()
        self.dialMethod_b1.close()

    def pickTone14(self):
        self.dialogb1.stackedWidget.setCurrentWidget(self.dialogb1.s4page)
        
        self.dialogb1.s1_btn.setStyleSheet("")
        self.dialogb1.s2_btn.setStyleSheet("")
        self.dialogb1.s3_btn.setStyleSheet("")
        self.dialogb1.s4_btn.setStyleSheet("background-color: #303f9f; border-color: #303f9f ; color: #ffffff;")

        self.dialogb1.s4apply_btn.clicked.connect(self.setTone14)

    def setTone14(self):
        if self.dialogb1.s4n1_cekbox.isChecked() == True:
            self.axc12.plot(self.tone14.arah, self.tone14.ttb_tiap_arah[0], label = 'Nada 1 Senar 4\nPak Munir')
        if self.dialogb1.s4n2_cekbox.isChecked() == True:
            self.axc12.plot(self.tone14.arah, self.tone14.ttb_tiap_arah[1], label = 'Nada 2 Senar 4\nPak Munir')

        self.axc12.set_rmax(0)
        self.axc12.set_rticks(np.linspace(-54, -9, 6))
        self.axc12.legend(bbox_to_anchor=(1, 0.5))
        self.canvas12_compare.draw()
        self.dialMethod_b1.close()

    def dial_allb2(self):
        self.dialMethod_b2 = QDialog()
        self.dialogb2 = Ui_all_compare_b2()
        self.dialogb2.setupUi(self.dialMethod_b2)
        self.dialMethod_b2.show()

        self.dialogb2.s1_btn.clicked.connect(self.pickTone21)
        self.dialogb2.s2_btn.clicked.connect(self.pickTone22)
        self.dialogb2.s3_btn.clicked.connect(self.pickTone23)
        self.dialogb2.s4_btn.clicked.connect(self.pickTone24)
        self.dialogb2.s5_btn.clicked.connect(self.pickTone25)
        self.dialogb2.s6_btn.clicked.connect(self.pickTone26)
        self.dialogb2.s7_btn.clicked.connect(self.pickTone27)
        self.dialogb2.s8_btn.clicked.connect(self.pickTone28)

    def pickTone21(self):
        self.dialogb2.stackedWidget.setCurrentWidget(self.dialogb2.s1page)
        
        self.dialogb2.s1_btn.setStyleSheet("background-color: #303f9f; color: #ffffff;")
        self.dialogb2.s2_btn.setStyleSheet("")
        self.dialogb2.s3_btn.setStyleSheet("")
        self.dialogb2.s4_btn.setStyleSheet("")
        self.dialogb2.s5_btn.setStyleSheet("")
        self.dialogb2.s6_btn.setStyleSheet("")
        self.dialogb2.s7_btn.setStyleSheet("")
        self.dialogb2.s8_btn.setStyleSheet("")

        self.dialogb2.s1apply_btn.clicked.connect(self.setTone21)

    def setTone21(self):
        if self.dialogb2.s1n1_cekbox.isChecked() == True:
            self.axc12.plot(self.tone21.arah, self.tone21.ttb_tiap_arah[0], label = 'Nada 1 Senar 1\nMas Sa\'id')
        if self.dialogb2.s1n2_cekbox.isChecked() == True:
            self.axc12.plot(self.tone21.arah, self.tone21.ttb_tiap_arah[1], label = 'Nada 2 Senar 1\nMas Sa\'id')

        self.axc12.set_rmax(0)
        self.axc12.set_rticks(np.linspace(-54, -9, 6))
        self.axc12.legend(bbox_to_anchor=(1, 0.5))
        self.canvas12_compare.draw()
        self.dialMethod_b2.close()
    def pickTone22(self):
        self.dialogb2.stackedWidget.setCurrentWidget(self.dialogb2.s2page)
        
        self.dialogb2.s1_btn.setStyleSheet("")
        self.dialogb2.s2_btn.setStyleSheet("background-color: #303f9f; color: #ffffff;")
        self.dialogb2.s3_btn.setStyleSheet("")
        self.dialogb2.s4_btn.setStyleSheet("")
        self.dialogb2.s5_btn.setStyleSheet("")
        self.dialogb2.s6_btn.setStyleSheet("")
        self.dialogb2.s7_btn.setStyleSheet("")
        self.dialogb2.s8_btn.setStyleSheet("")

        self.dialogb2.s2apply_btn.clicked.connect(self.setTone22)

    def setTone22(self):
        if self.dialogb2.s2n1_cekbox.isChecked() == True:
            self.axc12.plot(self.tone22.arah, self.tone22.ttb_tiap_arah[0], label = 'Nada 1 Senar 2\nMas Sa\'id')
        if self.dialogb2.s2n2_cekbox.isChecked() == True:
            self.axc12.plot(self.tone22.arah, self.tone22.ttb_tiap_arah[1], label = 'Nada 2 Senar 2\nMas Sa\'id')

        self.axc12.set_rmax(0)
        self.axc12.set_rticks(np.linspace(-54, -9, 6))
        self.axc12.legend(bbox_to_anchor=(1, 0.5))
        self.canvas12_compare.draw()
        self.dialMethod_b2.close()

    def pickTone23(self):
        self.dialogb2.stackedWidget.setCurrentWidget(self.dialogb2.s3page)
        
        self.dialogb2.s1_btn.setStyleSheet("")
        self.dialogb2.s2_btn.setStyleSheet("")
        self.dialogb2.s3_btn.setStyleSheet("background-color: #303f9f; color: #ffffff;")
        self.dialogb2.s4_btn.setStyleSheet("")
        self.dialogb2.s5_btn.setStyleSheet("")
        self.dialogb2.s6_btn.setStyleSheet("")
        self.dialogb2.s7_btn.setStyleSheet("")
        self.dialogb2.s8_btn.setStyleSheet("")

        self.dialogb2.s3apply_btn.clicked.connect(self.setTone23)

    def setTone23(self):
        if self.dialogb2.s3n1_cekbox.isChecked() == True:
            self.axc12.plot(self.tone23.arah, self.tone23.ttb_tiap_arah[0], label = 'Nada 1 Senar 3\nMas Sa\'id')
        if self.dialogb2.s3n2_cekbox.isChecked() == True:
            self.axc12.plot(self.tone23.arah, self.tone23.ttb_tiap_arah[1], label = 'Nada 2 Senar 3\nMas Sa\'id')
        if self.dialogb2.s3n3_cekbox.isChecked() == True:
            self.axc12.plot(self.tone23.arah, self.tone23.ttb_tiap_arah[2], label = 'Nada 3 Senar 3\nMas Sa\'id')
        if self.dialogb2.s3n4_cekbox.isChecked() == True:
            self.axc12.plot(self.tone23.arah, self.tone23.ttb_tiap_arah[3], label = 'Nada 4 Senar 3\nMas Sa\'id')

        self.axc12.set_rmax(0)
        self.axc12.set_rticks(np.linspace(-54, -9, 6))
        self.axc12.legend(bbox_to_anchor=(1, 0.5))
        self.canvas12_compare.draw()
        self.dialMethod_b2.close()

    def pickTone24(self):
        self.dialogb2.stackedWidget.setCurrentWidget(self.dialogb2.s4page)
        
        self.dialogb2.s1_btn.setStyleSheet("")
        self.dialogb2.s2_btn.setStyleSheet("")
        self.dialogb2.s3_btn.setStyleSheet("")
        self.dialogb2.s4_btn.setStyleSheet("background-color: #303f9f; color: #ffffff;")
        self.dialogb2.s5_btn.setStyleSheet("")
        self.dialogb2.s6_btn.setStyleSheet("")
        self.dialogb2.s7_btn.setStyleSheet("")
        self.dialogb2.s8_btn.setStyleSheet("")

        self.dialogb2.s4apply_btn.clicked.connect(self.setTone24)

    def setTone24(self):
        if self.dialogb2.s4n1_cekbox.isChecked() == True:
            self.axc12.plot(self.tone24.arah, self.tone24.ttb_tiap_arah[0], label = 'Nada 1 Senar 4\nMas Sa\'id')
        if self.dialogb2.s4n2_cekbox.isChecked() == True:
            self.axc12.plot(self.tone24.arah, self.tone24.ttb_tiap_arah[1], label = 'Nada 2 Senar 4\nMas Sa\'id')
        if self.dialogb2.s4n3_cekbox.isChecked() == True:
            self.axc12.plot(self.tone24.arah, self.tone24.ttb_tiap_arah[2], label = 'Nada 3 Senar 4\nMas Sa\'id')

        self.axc12.set_rmax(0)
        self.axc12.set_rticks(np.linspace(-54, -9, 6))
        self.axc12.legend(bbox_to_anchor=(1, 0.5))
        self.canvas12_compare.draw()
        self.dialMethod_b2.close()

    def pickTone25(self):
        self.dialogb2.stackedWidget.setCurrentWidget(self.dialogb2.s5page)
        
        self.dialogb2.s1_btn.setStyleSheet("")
        self.dialogb2.s2_btn.setStyleSheet("")
        self.dialogb2.s3_btn.setStyleSheet("")
        self.dialogb2.s4_btn.setStyleSheet("")
        self.dialogb2.s5_btn.setStyleSheet("background-color: #303f9f; color: #ffffff;")
        self.dialogb2.s6_btn.setStyleSheet("")
        self.dialogb2.s7_btn.setStyleSheet("")
        self.dialogb2.s8_btn.setStyleSheet("")

        self.dialogb2.s5apply_btn.clicked.connect(self.setTone25)

    def setTone25(self):
        if self.dialogb2.s5n1_cekbox.isChecked() == True:
            self.axc12.plot(self.tone25.arah, self.tone25.ttb_tiap_arah[0], label = 'Nada 1 Senar 5\nMas Sa\'id')
        if self.dialogb2.s5n2_cekbox.isChecked() == True:
            self.axc12.plot(self.tone25.arah, self.tone25.ttb_tiap_arah[1], label = 'Nada 2 Senar 5\nMas Sa\'id')

        self.axc12.set_rmax(0)
        self.axc12.set_rticks(np.linspace(-54, -9, 6))
        self.axc12.legend(bbox_to_anchor=(1, 0.5))
        self.canvas12_compare.draw()
        self.dialMethod_b2.close()

    def pickTone26(self):
        self.dialogb2.stackedWidget.setCurrentWidget(self.dialogb2.s6page)
        
        self.dialogb2.s1_btn.setStyleSheet("")
        self.dialogb2.s2_btn.setStyleSheet("")
        self.dialogb2.s3_btn.setStyleSheet("")
        self.dialogb2.s4_btn.setStyleSheet("")
        self.dialogb2.s5_btn.setStyleSheet("")
        self.dialogb2.s6_btn.setStyleSheet("background-color: #303f9f; color: #ffffff;")
        self.dialogb2.s7_btn.setStyleSheet("")
        self.dialogb2.s8_btn.setStyleSheet("")

        self.dialogb2.s6apply_btn.clicked.connect(self.setTone26)

    def setTone26(self):
        if self.dialogb2.s6n1_cekbox.isChecked() == True:
            self.axc12.plot(self.tone26.arah, self.tone26.ttb_tiap_arah[0], label = 'Nada 1 Senar 6\nMas Sa\'id')
        if self.dialogb2.s6n2_cekbox.isChecked() == True:
            self.axc12.plot(self.tone26.arah, self.tone26.ttb_tiap_arah[1], label = 'Nada 2 Senar 6\nMas Sa\'id')
        if self.dialogb2.s6n3_cekbox.isChecked() == True:
            self.axc12.plot(self.tone26.arah, self.tone26.ttb_tiap_arah[2], label = 'Nada 3 Senar 6\nMas Sa\'id')
        if self.dialogb2.s6n4_cekbox.isChecked() == True:
            self.axc12.plot(self.tone26.arah, self.tone26.ttb_tiap_arah[3], label = 'Nada 4 Senar 6\nMas Sa\'id')

        self.axc12.set_rmax(0)
        self.axc12.set_rticks(np.linspace(-54, -9, 6))
        self.axc12.legend(bbox_to_anchor=(1, 0.5))
        self.canvas12_compare.draw()
        self.dialMethod_b2.close()

    def pickTone27(self):
        self.dialogb2.stackedWidget.setCurrentWidget(self.dialogb2.s7page)
        
        self.dialogb2.s1_btn.setStyleSheet("")
        self.dialogb2.s2_btn.setStyleSheet("")
        self.dialogb2.s3_btn.setStyleSheet("")
        self.dialogb2.s4_btn.setStyleSheet("")
        self.dialogb2.s5_btn.setStyleSheet("")
        self.dialogb2.s6_btn.setStyleSheet("")
        self.dialogb2.s7_btn.setStyleSheet("background-color: #303f9f; color: #ffffff;")
        self.dialogb2.s8_btn.setStyleSheet("")

        self.dialogb2.s7apply_btn.clicked.connect(self.setTone27)

    def setTone27(self):
        if self.dialogb2.s7n1_cekbox.isChecked() == True:
            self.axc12.plot(self.tone27.arah, self.tone27.ttb_tiap_arah[0], label = 'Nada 1 Senar 7\nMas Sa\'id')
        if self.dialogb2.s7n2_cekbox.isChecked() == True:
            self.axc12.plot(self.tone27.arah, self.tone27.ttb_tiap_arah[1], label = 'Nada 2 Senar 7\nMas Sa\'id')
        
        self.axc12.set_rmax(0)
        self.axc12.set_rticks(np.linspace(-54, -9, 6))
        self.axc12.legend(bbox_to_anchor=(1, 0.5))
        self.canvas12_compare.draw()
        self.dialMethod_b2.close()
        
    def pickTone28(self):
        self.dialogb2.stackedWidget.setCurrentWidget(self.dialogb2.s8page)
        
        self.dialogb2.s1_btn.setStyleSheet("")
        self.dialogb2.s2_btn.setStyleSheet("")
        self.dialogb2.s3_btn.setStyleSheet("")
        self.dialogb2.s4_btn.setStyleSheet("")
        self.dialogb2.s5_btn.setStyleSheet("")
        self.dialogb2.s6_btn.setStyleSheet("")
        self.dialogb2.s7_btn.setStyleSheet("")
        self.dialogb2.s8_btn.setStyleSheet("background-color: #303f9f; color: #ffffff;")

        self.dialogb2.s8apply_btn.clicked.connect(self.setTone28)

    def setTone28(self):
        if self.dialogb2.s8n1_cekbox.isChecked() == True:
            self.axc12.plot(self.tone28.arah, self.tone28.ttb_tiap_arah[0], label = 'Nada 1 Senar 8\nMas Sa\'id')
        if self.dialogb2.s8n2_cekbox.isChecked() == True:
            self.axc12.plot(self.tone28.arah, self.tone28.ttb_tiap_arah[1], label = 'Nada 2 Senar 8\nMas Sa\'id')
        
        self.axc12.set_rmax(0)
        self.axc12.set_rticks(np.linspace(-54, -9, 6))
        self.axc12.legend(bbox_to_anchor=(1, 0.5))
        self.canvas12_compare.draw()
        self.dialMethod_b2.close()


    def changeTabHelp(self):
        self.ui.beranda_button.setStyleSheet("")
        self.ui.bund1_button.setStyleSheet("")
        self.ui.bund2_button.setStyleSheet("")
        self.ui.compare_button.setStyleSheet("")
        self.ui.help_button.setStyleSheet("border-left: 3px solid #303f9f; background-color: #ecf0f1;")
        self.ui.pages_widget.setCurrentWidget(self.ui.bund2_page)

        self.ui.pages_widget.setCurrentWidget(self.ui.help_page)

        self.help_kontur = QMovie('images/help_kontur_animate.gif')
        self.ui.gif_helpkontur.setMovie(self.help_kontur)
        self.help_kontur.start()

        self.help_nada = QMovie('images/help_nada_animate.gif')
        self.ui.gif_help_nada.setMovie(self.help_nada)
        self.help_nada.start()

    

    def changeTabAbout(self):
        self.dialMethodAbout = QDialog()
        self.dialogAbout = Ui_about_dialog()
        self.dialogAbout.setupUi(self.dialMethodAbout)
        self.dialMethodAbout.show()



if __name__ == '__main__':
    main()