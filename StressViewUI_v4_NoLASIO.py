import sys
import numpy as np
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QCheckBox
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, CheckButtons
import matplotlib as mpl
import re
plt.style.use('seaborn-darkgrid')

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        width = 420
        height = 420
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(width, height)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setToolTip("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 381, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.verticalLayoutWidget.setFont(font)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_browse_button = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_browse_button.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_browse_button.setSpacing(0)
        self.verticalLayout_browse_button.setObjectName("verticalLayout_browse_button")
        self.browse_las_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browse_las_button.sizePolicy().hasHeightForWidth())
        self.browse_las_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.browse_las_button.setFont(font)
        self.browse_las_button.setObjectName("browse_las_button")
        self.verticalLayout_browse_button.addWidget(self.browse_las_button)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 260, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.verticalLayoutWidget_2.setFont(font)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_calpoints = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_calpoints.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_calpoints.setObjectName("verticalLayout_calpoints")
        self.cal_points_checkbox = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.cal_points_checkbox.setFont(font)
        self.cal_points_checkbox.setObjectName("cal_points_checkbox")
        self.verticalLayout_calpoints.addWidget(self.cal_points_checkbox)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(280, 260, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.verticalLayoutWidget_3.setFont(font)
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_calpointsfloats = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_calpointsfloats.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_calpointsfloats.setObjectName("verticalLayout_calpointsfloats")
        self.cal_points_floats = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.cal_points_floats.setFont(font)
        self.cal_points_floats.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cal_points_floats.setText("")
        self.cal_points_floats.setAlignment(QtCore.Qt.AlignCenter)
        self.cal_points_floats.setObjectName("cal_points_floats")
        self.verticalLayout_calpointsfloats.addWidget(self.cal_points_floats)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(20, 70, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.verticalLayoutWidget_4.setFont(font)
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_NF = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_NF.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_NF.setObjectName("verticalLayout_NF")
        self.NFault_checkbox = QtWidgets.QCheckBox(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.NFault_checkbox.setFont(font)
        self.NFault_checkbox.setObjectName("NFault_checkbox")
        self.verticalLayout_NF.addWidget(self.NFault_checkbox)
        self.verticalLayoutWidget_10 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_10.setGeometry(QtCore.QRect(20, 300, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.verticalLayoutWidget_10.setFont(font)
        self.verticalLayoutWidget_10.setObjectName("verticalLayoutWidget_10")
        self.verticalLayout_plot_button = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_plot_button.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_plot_button.setObjectName("verticalLayout_plot_button")
        self.visualize_button = QtWidgets.QPushButton(self.verticalLayoutWidget_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.visualize_button.sizePolicy().hasHeightForWidth())
        self.visualize_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.visualize_button.setFont(font)
        self.visualize_button.setObjectName("visualize_button")
        self.verticalLayout_plot_button.addWidget(self.visualize_button)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(20, 110, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.verticalLayoutWidget_6.setFont(font)
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_VS = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_VS.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_VS.setObjectName("verticalLayout_VS")
        self.VS_label = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.VS_label.setObjectName("VS_label")
        self.verticalLayout_VS.addWidget(self.VS_label)
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(20, 230, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.verticalLayoutWidget_7.setFont(font)
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_gammaH = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_gammaH.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_gammaH.setObjectName("verticalLayout_gammaH")
        self.gammaH_label = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        self.gammaH_label.setObjectName("gammaH_label")
        self.verticalLayout_gammaH.addWidget(self.gammaH_label)
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(20, 170, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.verticalLayoutWidget_8.setFont(font)
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayout_Biot = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_Biot.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_Biot.setObjectName("verticalLayout_Biot")
        self.Biot_label = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.Biot_label.setObjectName("Biot_label")
        self.verticalLayout_Biot.addWidget(self.Biot_label)
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(20, 200, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.verticalLayoutWidget_9.setFont(font)
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.verticalLayout_gammah = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_gammah.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_gammah.setObjectName("verticalLayout_gammah")
        self.gammah_label = QtWidgets.QLabel(self.verticalLayoutWidget_9)
        self.gammah_label.setObjectName("gammah_label")
        self.verticalLayout_gammah.addWidget(self.gammah_label)
        self.verticalLayoutWidget_11 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_11.setGeometry(QtCore.QRect(20, 140, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.verticalLayoutWidget_11.setFont(font)
        self.verticalLayoutWidget_11.setObjectName("verticalLayoutWidget_11")
        self.verticalLayout_PP = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_11)
        self.verticalLayout_PP.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_PP.setObjectName("verticalLayout_PP")
        self.PP_label = QtWidgets.QLabel(self.verticalLayoutWidget_11)
        self.PP_label.setObjectName("PP_label")
        self.verticalLayout_PP.addWidget(self.PP_label)
        self.verticalLayoutWidget_12 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_12.setGeometry(QtCore.QRect(280, 110, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.verticalLayoutWidget_12.setFont(font)
        self.verticalLayoutWidget_12.setObjectName("verticalLayoutWidget_12")
        self.verticalLayout_VSfloats = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_12)
        self.verticalLayout_VSfloats.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_VSfloats.setObjectName("verticalLayout_VSfloats")
        self.VS_floats = QtWidgets.QLineEdit(self.verticalLayoutWidget_12)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.VS_floats.setFont(font)
        self.VS_floats.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.VS_floats.setText("")
        self.VS_floats.setAlignment(QtCore.Qt.AlignCenter)
        self.VS_floats.setObjectName("VS_floats")
        self.verticalLayout_VSfloats.addWidget(self.VS_floats)
        self.verticalLayoutWidget_13 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_13.setGeometry(QtCore.QRect(280, 140, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.verticalLayoutWidget_13.setFont(font)
        self.verticalLayoutWidget_13.setObjectName("verticalLayoutWidget_13")
        self.verticalLayout_PPfloats = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_13)
        self.verticalLayout_PPfloats.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_PPfloats.setObjectName("verticalLayout_PPfloats")
        self.PP_floats = QtWidgets.QLineEdit(self.verticalLayoutWidget_13)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.PP_floats.setFont(font)
        self.PP_floats.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PP_floats.setText("")
        self.PP_floats.setAlignment(QtCore.Qt.AlignCenter)
        self.PP_floats.setObjectName("PP_floats")
        self.verticalLayout_PPfloats.addWidget(self.PP_floats)
        self.verticalLayoutWidget_14 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_14.setGeometry(QtCore.QRect(280, 170, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.verticalLayoutWidget_14.setFont(font)
        self.verticalLayoutWidget_14.setObjectName("verticalLayoutWidget_14")
        self.verticalLayout_Biotfloats = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_14)
        self.verticalLayout_Biotfloats.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_Biotfloats.setObjectName("verticalLayout_Biotfloats")
        self.Biot_floats = QtWidgets.QLineEdit(self.verticalLayoutWidget_14)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.Biot_floats.setFont(font)
        self.Biot_floats.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Biot_floats.setText("")
        self.Biot_floats.setAlignment(QtCore.Qt.AlignCenter)
        self.Biot_floats.setObjectName("Biot_floats")
        self.verticalLayout_Biotfloats.addWidget(self.Biot_floats)
        self.verticalLayoutWidget_15 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_15.setGeometry(QtCore.QRect(280, 200, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.verticalLayoutWidget_15.setFont(font)
        self.verticalLayoutWidget_15.setObjectName("verticalLayoutWidget_15")
        self.verticalLayout_gammahfloats = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_15)
        self.verticalLayout_gammahfloats.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_gammahfloats.setObjectName("verticalLayout_gammahfloats")
        self.gammah_floats = QtWidgets.QLineEdit(self.verticalLayoutWidget_15)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.gammah_floats.setFont(font)
        self.gammah_floats.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gammah_floats.setText("")
        self.gammah_floats.setAlignment(QtCore.Qt.AlignCenter)
        self.gammah_floats.setObjectName("gammah_floats")
        self.verticalLayout_gammahfloats.addWidget(self.gammah_floats)
        self.verticalLayoutWidget_16 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_16.setGeometry(QtCore.QRect(280, 230, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.verticalLayoutWidget_16.setFont(font)
        self.verticalLayoutWidget_16.setObjectName("verticalLayoutWidget_16")
        self.verticalLayout_gammaHfloats = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_16)
        self.verticalLayout_gammaHfloats.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_gammaHfloats.setObjectName("verticalLayout_gammaHfloats")
        self.gammaH_floats = QtWidgets.QLineEdit(self.verticalLayoutWidget_16)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.gammaH_floats.setFont(font)
        self.gammaH_floats.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gammaH_floats.setText("")
        self.gammaH_floats.setAlignment(QtCore.Qt.AlignCenter)
        self.gammaH_floats.setObjectName("gammaH_floats")
        self.verticalLayout_gammaHfloats.addWidget(self.gammaH_floats)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(280, 70, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.verticalLayoutWidget_5.setFont(font)
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_RF = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_RF.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_RF.setObjectName("verticalLayout_RF")
        self.RFault_checkbox = QtWidgets.QCheckBox(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.RFault_checkbox.setFont(font)
        self.RFault_checkbox.setObjectName("RFault_checkbox")
        self.verticalLayout_RF.addWidget(self.RFault_checkbox)
        self.verticalLayoutWidget_17 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_17.setGeometry(QtCore.QRect(150, 70, 124, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.verticalLayoutWidget_17.setFont(font)
        self.verticalLayoutWidget_17.setObjectName("verticalLayoutWidget_17")
        self.verticalLayout_SSF = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_17)
        self.verticalLayout_SSF.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_SSF.setObjectName("verticalLayout_SSF")
        self.SSFault_checkbox = QtWidgets.QCheckBox(self.verticalLayoutWidget_17)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.SSFault_checkbox.setFont(font)
        self.SSFault_checkbox.setObjectName("SSFault_checkbox")
        self.verticalLayout_SSF.addWidget(self.SSFault_checkbox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 420, 21))
        self.menubar.setObjectName("menubar")
        self.how_to_use = QtWidgets.QMenu(self.menubar)
        self.how_to_use.setObjectName("how_to_use")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.UserGuide = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.UserGuide.setFont(font)
        self.UserGuide.setProperty("Pressed", True)
        self.UserGuide.setObjectName("UserGuide")
        self.About = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.About.setFont(font)
        self.About.setObjectName("About")
        self.how_to_use.addAction(self.UserGuide)
        self.how_to_use.addAction(self.About)
        self.menubar.addAction(self.how_to_use.menuAction())

        self.retranslateUi(MainWindow)
        self.About.triggered.connect(self.About_pop_up)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.VS_floats.setText("1.0")
        self.PP_floats.setText("0.45")
        self.Biot_floats.setText("0.65")

        def open_Las_file(self):
            global dflas_clean
            filename, _ = QtWidgets.QFileDialog.getOpenFileName(filter = "*.csv")
            # las = lasio.read(filename)
            dflas_clean = pd.read_csv(filename)
            # Show data 
            # print(las.curves)
            # Make LAS file into DataFrame
            # dflas = las.df().reset_index()

            # Clean df, remove depths with incomplete data
            # dflas_clean = dflas.dropna().copy()
        
        self.browse_las_button.clicked.connect(open_Las_file)

        def NFCheck():
            if self.NFault_checkbox.isChecked() == True:
                self.gammah_floats.setText("0.03")
                self.gammaH_floats.setText("0.15")
            if self.NFault_checkbox.isChecked() == False:
                self.gammah_floats.setText("")
                self.gammaH_floats.setText("")
        def SSFCheck():
            if self.SSFault_checkbox.isChecked() == True:
                self.gammah_floats.setText("0.03")
                self.gammaH_floats.setText("0.35")
            if self.SSFault_checkbox.isChecked() == False:
                self.gammah_floats.setText("")
                self.gammaH_floats.setText("")
        def RFCheck():
            if self.RFault_checkbox.isChecked() == True:
                print('HELLO')
                self.gammah_floats.setText("0.35")
                self.gammaH_floats.setText("0.45")
            if self.RFault_checkbox.isChecked() == False:
                self.gammah_floats.setText("")
                self.gammaH_floats.setText("")

        self.NFault_checkbox.stateChanged.connect(NFCheck)
        self.SSFault_checkbox.stateChanged.connect(SSFCheck)
        self.RFault_checkbox.stateChanged.connect(RFCheck)

        def plotting():
            Overburden = float((self.VS_floats.text()))
            PorePressure = float((self.PP_floats.text()))
            Biot = float((self.Biot_floats.text()))
            gamma_h = float((self.gammah_floats.text()))
            gamma_H = float((self.gammaH_floats.text()))

            # print(Overburden, PorePressure, Biot, gamma_h, gamma_H)

            # dflas_clean['Overburden'] = Overburden * dflas_clean['TDEP'] / 0.3048
            # dflas_clean['PorePressure'] = PorePressure * dflas_clean['TDEP'] / 0.3048
            dflas_clean['Vp'] = 1 / dflas_clean['DTCO'] * 0.3048 * 1000000
            dflas_clean['Vs'] = 1 / dflas_clean['DTSM'] * 0.3048 * 1000000

            # Isotropic Properties

            dflas_clean['Poisson'] =  (dflas_clean['Vp']**2 - 2*dflas_clean['Vs']**2) / (2*(dflas_clean['Vp']**2 - dflas_clean['Vs']**2))

            dflas_clean['YoungModulus'] = 2*dflas_clean['DEN']*dflas_clean['Vs']**2*(1+dflas_clean['Poisson'])*100**3/1000*14.7/101325/1000000
            
            # Vertical Stress

            def VerticalStress(Overburden):
                dflas_clean['Overburden'] = Overburden * dflas_clean['TDEP'] / 0.3048
                return dflas_clean['Overburden'].to_numpy()
         
            # Isotropic Stress

            def IsoStress(Overburden, PorePressure, Biot, gamma_h):
                dflas_clean['Overburden'] = Overburden * dflas_clean['TDEP'] / 0.3048
                dflas_clean['PorePressure'] = PorePressure * dflas_clean['TDEP'] / 0.3048
                dflas_clean['IsotropicStress'] = (dflas_clean['Poisson']/(1-dflas_clean['Poisson']))*(dflas_clean['Overburden']-Biot*dflas_clean['PorePressure'])+Biot*dflas_clean['PorePressure']+ gamma_h * dflas_clean['Overburden']
                
                return dflas_clean['IsotropicStress'].to_numpy() 
            
            VerticalStress(Overburden)
            IsoStress(Overburden, PorePressure, Biot, gamma_h)

            # Anisotropic Logs: Stoneley 
            if 'DTST' in list(dflas_clean.columns):

                def Stoneley(Overburden, PorePressure, Biot, gamma_h):
                    K1 = 1.1
                    K2 = 0.8
                    mud_den = 1.53 #g/cc
                    dt_f = 190 #us/ft

                    # Stiffness Coefficient
                    dflas_clean['C33_St'] = (dflas_clean['DEN']*dflas_clean['Vp']**2)*(100**3/1000*14.7/101325)/1000000
                    dflas_clean['C44_St'] = (dflas_clean['DEN']*dflas_clean['Vs']**2)*(100**3/1000*14.7/101325)/1000000
                    dflas_clean['C66_St'] =(mud_den/(dflas_clean['DTST']**2-dt_f**2))*(0.3048**2*100**3/1000*(10**6)**2)*(14.7/101325)/1000000
                    dflas_clean['C11_St'] = K1*(dflas_clean['C33_St']+2*(dflas_clean['C66_St']-dflas_clean['C44_St']))
                    dflas_clean['C12_St'] = dflas_clean['C11_St']-2*dflas_clean['C66_St']
                    dflas_clean['C13_St'] = K2*dflas_clean['C12_St']

                    # Isotropic Properties

                    dflas_clean['Ev_St'] = dflas_clean['C33_St']-(2*dflas_clean['C13_St']**2)/(dflas_clean['C11_St']+dflas_clean['C12_St'])

                    dflas_clean['Eh_St'] = (dflas_clean['C11_St']-dflas_clean['C12_St'])*(dflas_clean['C11_St']*dflas_clean['C33_St']-2*dflas_clean['C13_St']**2+dflas_clean['C12_St']*dflas_clean['C33_St'])/(dflas_clean['C11_St']*dflas_clean['C33_St']-dflas_clean['C13_St']**2)

                    dflas_clean['vv_St'] = dflas_clean['C13_St']/(dflas_clean['C11_St']+dflas_clean['C12_St'])
                    dflas_clean['vh_St'] = (dflas_clean['C12_St']*dflas_clean['C33_St']-dflas_clean['C13_St']**2)/(dflas_clean['C11_St']*dflas_clean['C33_St']-dflas_clean['C13_St']**2)

                    # Minimum Isotropic Stress

                    dflas_clean['VTIStress_St'] = (dflas_clean['Eh_St']/dflas_clean['Ev_St'])*(dflas_clean['vv_St']/(1-dflas_clean['vh_St']))*(dflas_clean['Overburden']-Biot*dflas_clean['PorePressure'])+Biot*dflas_clean['PorePressure']+gamma_h*dflas_clean['Overburden']

                    dflas_clean['VTIStress_St'] = dflas_clean['VTIStress_St'][(dflas_clean[['VTIStress_St']] > 0).all(axis=1)]

                    return dflas_clean['VTIStress_St'].to_numpy()

                # Maximum Isotropic Stress

                def Stoneley_MAX(Overburden, PorePressure, Biot, gamma_h, gamma_H):
                    dflas_clean['St_MAX'] = Stoneley(Overburden, PorePressure, Biot, gamma_h) + gamma_H * VerticalStress(Overburden)
                    return dflas_clean['St_MAX'].to_numpy()

            # Stoneley(Overburden, PorePressure, Biot, gamma_h)
            # Stoneley_MAX(Overburden, PorePressure, Biot, gamma_h, gamma_H)

            # Anisotropic Logs: Velocity Regression 
            def VelReg(Overburden, PorePressure, Biot, gamma_h):

                # Stiffness Coefficient
                dflas_clean['C33_VelReg'] = (dflas_clean['DEN']*dflas_clean['Vp']**2)*(100**3/1000*14.7/101325)/1000000
                dflas_clean['C44_VelReg'] = (dflas_clean['DEN']*dflas_clean['Vs']**2)*(100**3/1000*14.7/101325)/1000000
                dflas_clean['Vp90_VelReg'] = (0.8615*dflas_clean['Vp']/1000+1.3315)*1000
                dflas_clean['Vs90_VelReg'] = (0.8467*dflas_clean['Vs']/1000+0.8161)*1000
                dflas_clean['Vp45_VelReg'] = (0.9189*dflas_clean['Vp']/1000+0.6175)*1000
                dflas_clean['C11_VelReg'] = (dflas_clean['DEN']*dflas_clean['Vp90_VelReg']**2)*(100**3/1000*14.7/101325)/1000000
                dflas_clean['C66_VelReg'] = (dflas_clean['DEN']*dflas_clean['Vs90_VelReg']**2)*(100**3/1000*14.7/101325)/1000000
                dflas_clean['C13_VelReg'] = (np.sqrt(4*dflas_clean['DEN']**2*dflas_clean['Vp45_VelReg']**4*(100**6/1000**2)*(14.7**2/101325**2)/1000000**2-2*dflas_clean['DEN']*dflas_clean['Vp45_VelReg']**2*(100**3/1000)*(14.7/101325)/1000000*(dflas_clean['C11_VelReg']+dflas_clean['C33_VelReg']+2*dflas_clean['C44_VelReg'])+(dflas_clean['C11_VelReg']+dflas_clean['C44_VelReg'])*(dflas_clean['C33_VelReg']+dflas_clean['C44_VelReg']))-dflas_clean['C44_VelReg'])
                dflas_clean['C12_VelReg'] = dflas_clean['C11_VelReg']-2*dflas_clean['C66_VelReg']

                #  Isotropic Properties

                dflas_clean['Ev_VelReg'] = dflas_clean['C33_VelReg']-(2*dflas_clean['C13_VelReg']**2)/(dflas_clean['C11_VelReg']+dflas_clean['C12_VelReg'])

                dflas_clean['Eh_VelReg'] = (dflas_clean['C11_VelReg']-dflas_clean['C12_VelReg'])*(dflas_clean['C11_VelReg']*dflas_clean['C33_VelReg']-2*dflas_clean['C13_VelReg']**2+dflas_clean['C12_VelReg']*dflas_clean['C33_VelReg'])/(dflas_clean['C11_VelReg']*dflas_clean['C33_VelReg']-dflas_clean['C13_VelReg']**2)

                dflas_clean['vv_VelReg'] = dflas_clean['C13_VelReg']/(dflas_clean['C11_VelReg']+dflas_clean['C12_VelReg'])
                dflas_clean['vh_VelReg'] = (dflas_clean['C12_VelReg']*dflas_clean['C33_VelReg']-dflas_clean['C13_VelReg']**2)/(dflas_clean['C11_VelReg']*dflas_clean['C33_VelReg']-dflas_clean['C13_VelReg']**2)

                # Minimum Isotropic Stress

                dflas_clean['VTIStress_VelReg'] = (dflas_clean['Eh_VelReg']/dflas_clean['Ev_VelReg'])*(dflas_clean['vv_VelReg']/(1-dflas_clean['vh_VelReg']))*(dflas_clean['Overburden']-Biot*dflas_clean['PorePressure'])+Biot*dflas_clean['PorePressure'] + gamma_h *dflas_clean['Overburden']

                return dflas_clean['VTIStress_VelReg'].to_numpy()   
            
            # Maximum Isotropic Stress
            def VelReg_MAX(Overburden, PorePressure, Biot, gamma_h, gamma_H):
                dflas_clean['VelReg_MAX'] = VelReg(Overburden, PorePressure, Biot, gamma_h) + gamma_H * VerticalStress(Overburden)
                return dflas_clean['VelReg_MAX'].to_numpy()
            
            # Remove zeros from DataFrame
            # dflas_clean = dflas_clean[(dflas_clean > 0).all(axis=1)]

            # print(dflas_clean)
            # VelReg(Overburden, PorePressure, Biot, gamma_h)
            # VelReg_MAX(Overburden, PorePressure, Biot, gamma_h, gamma_H)

            figure = plt.figure(num = "StressView")
            axis1 = figure.add_subplot(1,2,1)

            [vstress] = axis1.plot(VerticalStress(Overburden), dflas_clean['TDEP'], label = r'$\sigma_v$', color = 'black', linewidth = 1)
            [IsotropicStress] = axis1.plot(IsoStress(Overburden, PorePressure, Biot, gamma_h), dflas_clean['TDEP'], label = r'$\sigma^{iso}$', color = 'tab:red', linewidth = 0.5)

            [Vr_h] = axis1.plot(VelReg(Overburden, PorePressure, Biot, gamma_h), dflas_clean['TDEP'], label = r'$\sigma^{Vr}_h$', color = 'tab:blue', linewidth = 0.75)
            [Vr_H] = axis1.plot(VelReg_MAX(Overburden, PorePressure, Biot, gamma_h, gamma_H), dflas_clean['TDEP'], label = r'$\sigma_H^{Vr}$', linewidth = 1, color = 'tab:orange', alpha = 0.75)

            if 'DTST' in list(dflas_clean.columns):
                [St_h] = axis1.plot(Stoneley(Overburden, PorePressure, Biot, gamma_h), dflas_clean['TDEP'], label = r'$\sigma^{St}_h$', color = 'tab:green', linewidth = 0.75)
                [St_H] = axis1.plot(Stoneley_MAX(Overburden, PorePressure, Biot, gamma_h, gamma_H), dflas_clean['TDEP'], label = r'$\sigma_H^{St}$', linewidth = 1, color = 'tab:purple', alpha = 0.9)

            if self.cal_points_checkbox.isChecked() == True and self.cal_points_floats.text():
                depths = re.findall(r'\(\s*\+?(-?\d+)\s*\,', self.cal_points_floats.text())
                stresses = re.findall(r'\,\s*\+?(-?\d+)\s*\)', self.cal_points_floats.text())
                depths = list(map(int, depths))               
                stresses = list(map(int, stresses))
                axis1.scatter(stresses, depths, s = 30, color = 'tab:brown', label = 'Calibration Points')

            axes = figure.gca() 

            axes.invert_yaxis()
            axes.xaxis.tick_top()

            axes.tick_params(axis='both', which='major', labelsize=15)

            axes.get_xaxis().set_minor_locator(mpl.ticker.AutoMinorLocator())
            axes.get_yaxis().set_minor_locator(mpl.ticker.AutoMinorLocator())
            axes.grid(b=True, which='major', color='w', linewidth=2.0)
            axes.grid(b=True, which='minor', color='w', linewidth=0.5)
            axes.get_xaxis().set_major_formatter(mpl.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
            axes.get_yaxis().set_major_formatter(mpl.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
            plt.ylabel('TVD (m)', size = 20)
            plt.title('Minimum Stress (psi)', size = 20)

            # plt.legend(prop={'size': 15}, loc = 'best')

            # Location and dimensions of sliders
            OB_slider_ax  = figure.add_axes([0.58, 0.85, 0.35, 0.03])
            OB_slider = Slider(OB_slider_ax, 'Overburden (psi/ft)', 0.1, 1.1, valinit=Overburden)

            PP_slider_ax  = figure.add_axes([0.58, 0.75, 0.35, 0.03])
            PP_slider = Slider(PP_slider_ax, 'Pore Pressure (psi/ft)', 0.1, 1.1, valinit=PorePressure)

            Biot_slider_ax  = figure.add_axes([0.58, 0.65, 0.35, 0.03])
            Biot_slider = Slider(Biot_slider_ax, 'Biot Coefficient', 0.4, 0.9, valinit=Biot)

            gh_slider_ax  = figure.add_axes([0.58, 0.55, 0.35, 0.03])
            gh_slider = Slider(gh_slider_ax, r'$\gamma_h$', 0, 1, valinit=gamma_h)

            gH_slider_ax  = figure.add_axes([0.58, 0.45, 0.35, 0.03])
            gH_slider = Slider(gH_slider_ax, r'$\gamma_H$', 0, 1, valinit=gamma_H)

            # Updating plot with sliders
            def sliders_on_changed(val):
                vstress.set_xdata(VerticalStress(OB_slider.val))
                IsotropicStress.set_xdata(IsoStress(OB_slider.val, PP_slider.val, Biot_slider.val, gh_slider.val))
                if 'DTST' in list(dflas_clean.columns):
                    St_h.set_xdata(Stoneley(OB_slider.val, PP_slider.val, Biot_slider.val, gh_slider.val))
                    St_H.set_xdata(Stoneley_MAX(OB_slider.val, PP_slider.val, Biot_slider.val, gh_slider.val, gH_slider.val))
                Vr_h.set_xdata(VelReg(OB_slider.val, PP_slider.val, Biot_slider.val, gh_slider.val))
                Vr_H.set_xdata(VelReg_MAX(OB_slider.val, PP_slider.val, Biot_slider.val, gh_slider.val, gH_slider.val))
                figure.canvas.draw_idle()
                figure.canvas.flush_events()

            OB_slider.on_changed(sliders_on_changed)
            PP_slider.on_changed(sliders_on_changed)
            Biot_slider.on_changed(sliders_on_changed)
            gh_slider.on_changed(sliders_on_changed)
            gH_slider.on_changed(sliders_on_changed)

            OB_slider.label.set_fontsize(13)
            PP_slider.label.set_fontsize(13)
            Biot_slider.label.set_fontsize(13)
            gh_slider.label.set_fontsize(13)
            gH_slider.label.set_fontsize(13)

            # Reset button
            reset_button_ax = figure.add_axes([0.60, 0.35, 0.1, 0.04])
            reset_button = Button(reset_button_ax, 'Reset logs', color='#c7cdd1', hovercolor='#0874bb')
            def reset_button_on_clicked(mouse_event):
                OB_slider.reset()
                PP_slider.reset()
                Biot_slider.reset()
                gh_slider.reset()
                gH_slider.reset()
            reset_button.on_clicked(reset_button_on_clicked)
            reset_button.label.set_fontsize(15)
            
            # Save button
            save_button_ax = figure.add_axes([0.80, 0.35, 0.1, 0.04])
            save_button = Button(save_button_ax, 'Save as CSV', color='#c7cdd1', hovercolor='#0874bb')
            def save_button_on_clicked(mouse_event):
                dflas_clean.to_excel("CleanLogs.xlsx")
            save_button.on_clicked(save_button_on_clicked)
            save_button.label.set_fontsize(15)

            if 'DTST' in list(dflas_clean.columns):
                labels = [r'$\sigma_v$', r'$\sigma^{iso}$', r'$\sigma^{St}_h$', r'$\sigma^{St}_H$', r'$\sigma^{Vr}_h$', r'$\sigma^{Vr}_H$']
                lines = [vstress, IsotropicStress, St_h, St_H, Vr_h, Vr_H]
                colors = ["black", "tab:red", "tab:green", "tab:purple", "tab:blue", "tab:orange"]
            else:
                labels = [r'$\sigma_v$', r'$\sigma^{iso}$', r'$\sigma^{Vr}_h$', r'$\sigma^{Vr}_H$']
                lines = [vstress, IsotropicStress, Vr_h, Vr_H]
                colors = ["black", "tab:red", "tab:blue", "tab:orange"]

            # Line toggles
            def toggle(label):
                index = labels.index(label)
                lines[index].set_visible(not lines[index].get_visible())
                figure.canvas.draw()

            activated = [True] * len(lines)

            check_button_ax = figure.add_axes([0.02, 0.63, 0.15, 0.25], facecolor = (0,0.3,0.75,0.0))
            check_button = CheckButtons(check_button_ax, labels, activated)
            check_button.on_clicked(toggle)
            [check_button.labels[i].set_fontsize(16) for i in range(0,len(check_button.labels))]
            
            # Customize line toggles
            for r in check_button.rectangles:
                r.set_facecolor("white") 
                # r.set_edgecolor("k")
                # r.set_alpha(0.2) 
            for i, c in enumerate(colors):
                check_button.labels[i].set_color(c)
                check_button.labels[i].set_alpha(0.7)
            for j in range(0,len(check_button.lines)):
                for k in range(0,len(check_button.lines[0])):
                    check_button.lines[j][k].set_color(colors[j])
            
            # Normal Fault label
            Normal_button_ax = figure.add_axes([0.58, 0.21, 0.35, 0.03])
            Normal_button = Button(Normal_button_ax, r'Normal Fault: $\sigma_v > \sigma_H > \sigma_h$', color='#c7cdd1', hovercolor='#c7cdd1')
            Normal_button.label.set_fontsize(15)

            # Strike Fault label
            strike_button_ax = figure.add_axes([0.58, 0.16, 0.35, 0.03])
            strike_button = Button(strike_button_ax, r'Strike-Slipe Fault: $\sigma_H > \sigma_v > \sigma_h$', color='#c7cdd1', hovercolor='#c7cdd1')
            strike_button.label.set_fontsize(15)

            # Reverse Fault label
            reverse_button_ax = figure.add_axes([0.58, 0.11, 0.35, 0.03])
            reverse_button = Button(reverse_button_ax, r'Reverse Fault: $\sigma_H > \sigma_h > \sigma_v$ ', color='#c7cdd1', hovercolor='#c7cdd1')
            reverse_button.label.set_fontsize(15)

            plt.show()
            dflas_clean.to_excel("CleanLogs.xlsx")

        self.visualize_button.clicked.connect(plotting)

    def About_pop_up(self):
                message = QMessageBox()
                message.setWindowTitle('Information')
                message.setText('Dany Hachem, PhD in Petroleum Geosystems Engineering, University of Texas at Austin, USA \n \nSau-Wai Wong, Principal Consultant and CEO, Rybka Rock')
                message.setStandardButtons(QMessageBox.Yes)
                buttonY = message.button(QMessageBox.Yes)
                buttonY.setText('Dismiss')
                x = message.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "StressView"))
        self.browse_las_button.setText(_translate("MainWindow", "Browse CSV files"))
        self.cal_points_checkbox.setText(_translate("MainWindow", "Add calibration points"))
        self.cal_points_floats.setToolTip(_translate("MainWindow", "Must be in the format (Depth, Stress)"))
        self.NFault_checkbox.setText(_translate("MainWindow", "Normal Fault"))
        self.visualize_button.setText(_translate("MainWindow", "Plot Stresses"))
        self.VS_label.setText(_translate("MainWindow", "Initial Vertical Stress gradient (psi/ft)"))
        self.Biot_label.setText(_translate("MainWindow", "Biot Coefficient"))
        self.gammah_label.setText(_translate("MainWindow", u'\u03B3<sub>h</sub>'))
        self.gammaH_label.setText(_translate("MainWindow",  u'\u03B3<sub>H</sub>'))
        self.PP_label.setText(_translate("MainWindow", "Initial Pore Pressure gradient (psi/ft)"))
        self.VS_floats.setToolTip(_translate("MainWindow", ""))
        self.PP_floats.setToolTip(_translate("MainWindow", ""))
        self.Biot_floats.setToolTip(_translate("MainWindow", ""))
        self.gammah_floats.setToolTip(_translate("MainWindow", ""))
        self.gammaH_floats.setToolTip(_translate("MainWindow", ""))
        self.RFault_checkbox.setText(_translate("MainWindow", "Reverse Fault"))
        self.SSFault_checkbox.setText(_translate("MainWindow", "Strike-Slip Fault"))
        self.how_to_use.setTitle(_translate("MainWindow", "File"))
        self.UserGuide.setText(_translate("MainWindow", "User Guide"))
        self.About.setText(_translate("MainWindow", "About"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
