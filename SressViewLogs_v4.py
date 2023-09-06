import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, CheckButtons
import matplotlib as mpl
plt.style.use('seaborn-darkgrid')

Overburden = 1 #psi/ft
PorePressure = 0.45 #psi/ft
Biot = 0.65

# 0 = Normal, 1 = Strike, 2 = Reverse
stress_regime = 0
if stress_regime == 0:
    gamma_h = 0.03
    gamma_H = 0.15
elif stress_regime == 1:
    gamma_h = 0.03
    gamma_H = 0.35
elif stress_regime == 2:
    gamma_h = 0.35
    gamma_H = 0.45

dflas = pd.read_csv("TestFile.csv")
# Clean df, remove depths with incomplete data
dflas_clean = dflas.dropna().copy()
print(list(dflas_clean.columns))
st_wave = False
if 'DTST' in list(dflas_clean.columns):
    st_wave = True
print(st_wave)   

def VerticalStress(Overburden):
    dflas_clean['Overburden'] = Overburden * dflas_clean['TDEP'] / 0.3048
    return dflas_clean['Overburden'].to_numpy()

dflas_clean['PorePressure'] = PorePressure * dflas_clean['TDEP'] / 0.3048
dflas_clean['Vp'] = 1 / dflas_clean['DTCO'] * 0.3048 * 1000000
dflas_clean['Vs'] = 1 / dflas_clean['DTSM'] * 0.3048 * 1000000

# Isotropic Properties

dflas_clean['Poisson'] =  (dflas_clean['Vp']**2 - 2*dflas_clean['Vs']**2) / (2*(dflas_clean['Vp']**2 - dflas_clean['Vs']**2))

dflas_clean['YoungModulus'] = 2*dflas_clean['DEN']*dflas_clean['Vs']**2*(1+dflas_clean['Poisson'])*100**3/1000*14.7/101325/1000000

# Isotropic Stress

def IsoStress(Overburden, PorePressure, Biot, gamma_h):
    dflas_clean['Overburden'] = Overburden * dflas_clean['TDEP'] / 0.3048
    dflas_clean['PorePressure'] = PorePressure * dflas_clean['TDEP'] / 0.3048
    dflas_clean['IsotropicStress'] = (dflas_clean['Poisson']/(1-dflas_clean['Poisson']))*(dflas_clean['Overburden']-Biot*dflas_clean['PorePressure'])+Biot*dflas_clean['PorePressure']+ gamma_h * dflas_clean['Overburden']

    return dflas_clean['IsotropicStress'].to_numpy() 

# Anisotropic Logs

# M-ANNIE (Stoneley) Stiffness Coefficient
# st_wave = False

if st_wave:
    def Stoneley(Overburden, PorePressure, Biot, gamma_h):
        K1 = 1.1
        K2 = 0.8
        mud_den = 1.53 #g/cc
        dt_f = 190 #us/ft

        dflas_clean['C33_St'] = (dflas_clean['DEN']*dflas_clean['Vp']**2)*(100**3/1000*14.7/101325)/1000000
        dflas_clean['C44_St'] = (dflas_clean['DEN']*dflas_clean['Vs']**2)*(100**3/1000*14.7/101325)/1000000
        dflas_clean['C66_St'] =(mud_den/(dflas_clean['DTST']**2-dt_f**2))*(0.3048**2*100**3/1000*(10**6)**2)*(14.7/101325)/1000000
        dflas_clean['C11_St'] = K1*(dflas_clean['C33_St']+2*(dflas_clean['C66_St']-dflas_clean['C44_St']))
        dflas_clean['C12_St'] = dflas_clean['C11_St']-2*dflas_clean['C66_St']
        dflas_clean['C13_St'] = K2*dflas_clean['C12_St']

        # M-ANNIE 2 Isotropic Properties

        dflas_clean['Ev_St'] = dflas_clean['C33_St']-(2*dflas_clean['C13_St']**2)/(dflas_clean['C11_St']+dflas_clean['C12_St'])

        dflas_clean['Eh_St'] = (dflas_clean['C11_St']-dflas_clean['C12_St'])*(dflas_clean['C11_St']*dflas_clean['C33_St']-2*dflas_clean['C13_St']**2+dflas_clean['C12_St']*dflas_clean['C33_St'])/(dflas_clean['C11_St']*dflas_clean['C33_St']-dflas_clean['C13_St']**2)

        dflas_clean['vv_St'] = dflas_clean['C13_St']/(dflas_clean['C11_St']+dflas_clean['C12_St'])
        dflas_clean['vh_St'] = (dflas_clean['C12_St']*dflas_clean['C33_St']-dflas_clean['C13_St']**2)/(dflas_clean['C11_St']*dflas_clean['C33_St']-dflas_clean['C13_St']**2)

        # M-ANNIE 2 Isotropic Stress

        dflas_clean['VTIStress_St'] = (dflas_clean['Eh_St']/dflas_clean['Ev_St'])*(dflas_clean['vv_St']/(1-dflas_clean['vh_St']))*(dflas_clean['Overburden']-Biot*dflas_clean['PorePressure'])+Biot*dflas_clean['PorePressure']+gamma_h*dflas_clean['Overburden']

        dflas_clean['VTIStress_St'] = dflas_clean['VTIStress_St'][(dflas_clean[['VTIStress_St']] > 0).all(axis=1)]

        return dflas_clean['VTIStress_St'].to_numpy()

    def Stoneley_MAX(Overburden, PorePressure, Biot, gamma_h, gamma_H):
        dflas_clean['St_MAX'] = Stoneley(Overburden, PorePressure, Biot, gamma_h) + gamma_H * VerticalStress(Overburden)
        return dflas_clean['St_MAX'].to_numpy()
    # Velocity Regression Stiffness Coefficient


def VelReg(Overburden, PorePressure, Biot, gamma_h):
    dflas_clean['C33_VelReg'] = (dflas_clean['DEN']*dflas_clean['Vp']**2)*(100**3/1000*14.7/101325)/1000000
    dflas_clean['C44_VelReg'] = (dflas_clean['DEN']*dflas_clean['Vs']**2)*(100**3/1000*14.7/101325)/1000000
    dflas_clean['Vp90_VelReg'] = (0.8615*dflas_clean['Vp']/1000+1.3315)*1000
    dflas_clean['Vs90_VelReg'] = (0.8467*dflas_clean['Vs']/1000+0.8161)*1000
    dflas_clean['Vp45_VelReg'] = (0.9189*dflas_clean['Vp']/1000+0.6175)*1000
    dflas_clean['C11_VelReg'] = (dflas_clean['DEN']*dflas_clean['Vp90_VelReg']**2)*(100**3/1000*14.7/101325)/1000000
    dflas_clean['C66_VelReg'] = (dflas_clean['DEN']*dflas_clean['Vs90_VelReg']**2)*(100**3/1000*14.7/101325)/1000000
    dflas_clean['C13_VelReg'] = (np.sqrt(4*dflas_clean['DEN']**2*dflas_clean['Vp45_VelReg']**4*(100**6/1000**2)*(14.7**2/101325**2)/1000000**2-2*dflas_clean['DEN']*dflas_clean['Vp45_VelReg']**2*(100**3/1000)*(14.7/101325)/1000000*(dflas_clean['C11_VelReg']+dflas_clean['C33_VelReg']+2*dflas_clean['C44_VelReg'])+(dflas_clean['C11_VelReg']+dflas_clean['C44_VelReg'])*(dflas_clean['C33_VelReg']+dflas_clean['C44_VelReg']))-dflas_clean['C44_VelReg'])
    dflas_clean['C12_VelReg'] = dflas_clean['C11_VelReg']-2*dflas_clean['C66_VelReg']

    # Velocity Regression Isotropic Properties

    dflas_clean['Ev_VelReg'] = dflas_clean['C33_VelReg']-(2*dflas_clean['C13_VelReg']**2)/(dflas_clean['C11_VelReg']+dflas_clean['C12_VelReg'])

    dflas_clean['Eh_VelReg'] = (dflas_clean['C11_VelReg']-dflas_clean['C12_VelReg'])*(dflas_clean['C11_VelReg']*dflas_clean['C33_VelReg']-2*dflas_clean['C13_VelReg']**2+dflas_clean['C12_VelReg']*dflas_clean['C33_VelReg'])/(dflas_clean['C11_VelReg']*dflas_clean['C33_VelReg']-dflas_clean['C13_VelReg']**2)

    dflas_clean['vv_VelReg'] = dflas_clean['C13_VelReg']/(dflas_clean['C11_VelReg']+dflas_clean['C12_VelReg'])
    dflas_clean['vh_VelReg'] = (dflas_clean['C12_VelReg']*dflas_clean['C33_VelReg']-dflas_clean['C13_VelReg']**2)/(dflas_clean['C11_VelReg']*dflas_clean['C33_VelReg']-dflas_clean['C13_VelReg']**2)

    # Velocity Regression Isotropic Stress

    dflas_clean['VTIStress_VelReg'] = (dflas_clean['Eh_VelReg']/dflas_clean['Ev_VelReg'])*(dflas_clean['vv_VelReg']/(1-dflas_clean['vh_VelReg']))*(dflas_clean['Overburden']-Biot*dflas_clean['PorePressure'])+Biot*dflas_clean['PorePressure'] + gamma_h *dflas_clean['Overburden']

    dflas_clean['VTIStress_VelReg'] = dflas_clean['VTIStress_VelReg'][(dflas_clean[['VTIStress_VelReg']] > 0).all(axis=1)]
    
    return dflas_clean['VTIStress_VelReg'].to_numpy()   

def VelReg_MAX(Overburden, PorePressure, Biot, gamma_h, gamma_H):
    dflas_clean['VelReg_MAX'] = VelReg(Overburden, PorePressure, Biot, gamma_h) + gamma_H * VerticalStress(Overburden)
    return dflas_clean['VelReg_MAX'].to_numpy()

# Remove zeros from DataFrame
dflas_clean = dflas_clean[(dflas_clean > 0).all(axis=1)]

dflas_clean.to_excel("CleanLogs.xlsx")


figure = plt.figure(num = "StressView")
axis1 = figure.add_subplot(1,2,1)
[vstress] = axis1.plot(VerticalStress(Overburden), dflas_clean['TDEP'], label = r'$\sigma_v$', color = 'black', linewidth = 1)
[IsotropicStress] = axis1.plot(IsoStress(Overburden, PorePressure, Biot, gamma_h), dflas_clean['TDEP'], label = r'$\sigma^{iso}$', color = 'tab:red', linewidth = 0.5)
if st_wave:
    [St_h] = axis1.plot(Stoneley(Overburden, PorePressure, Biot, gamma_h), dflas_clean['TDEP'], label = r'$\sigma^{St}_h$', color = 'tab:green', linewidth = 0.75)
    [St_H] = axis1.plot(Stoneley_MAX(Overburden, PorePressure, Biot, gamma_h, gamma_H), dflas_clean['TDEP'], label = r'$\sigma_H^{St}$', linewidth = 1, color = 'tab:purple', alpha = 0.9)
[Vr_h] = axis1.plot(VelReg(Overburden, PorePressure, Biot, gamma_h), dflas_clean['TDEP'], label = r'$\sigma^{Vr}_h$', color = 'tab:blue', linewidth = 0.75)
[Vr_H] = axis1.plot(VelReg_MAX(Overburden, PorePressure, Biot, gamma_h, gamma_H), dflas_clean['TDEP'], label = r'$\sigma_H^{Vr}$', linewidth = 1, color = 'tab:orange', alpha = 0.75)

depth_cal = [4000]
stress_cal = [9000]
axis1.scatter(stress_cal, depth_cal, s = 30, color = 'tab:brown')

axes1 = figure.gca() 

axes1.invert_yaxis()
axes1.xaxis.tick_top()

axes1.tick_params(axis='both', which='major', labelsize=15)
# plt.grid(True)

axes1.get_xaxis().set_minor_locator(mpl.ticker.AutoMinorLocator())
axes1.get_yaxis().set_minor_locator(mpl.ticker.AutoMinorLocator())
axes1.grid(b=True, which='major', color='w', linewidth=2.0)
axes1.grid(b=True, which='minor', color='w', linewidth=0.5)

axes1.get_xaxis().set_major_formatter(mpl.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
axes1.get_yaxis().set_major_formatter(mpl.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
plt.ylabel('TVD (m)', size = 20)
plt.title('Minimum Stress (psi)', size = 20)


# plt.legend (prop={'size': 15}, loc = 'best')

# Location and dimensions of sliders
OB_slider_ax  = figure.add_axes([0.58, 0.85, 0.35, 0.03])
OB_slider = Slider(OB_slider_ax, 'Overburden (psi/ft)', 0.1, 1.1, valinit=Overburden, valstep = 0.01)

PP_slider_ax  = figure.add_axes([0.58, 0.75, 0.35, 0.03])
PP_slider = Slider(PP_slider_ax, 'Pore Pressure (psi/ft)', 0.1, 1.1, valinit=PorePressure, valstep = 0.01)

Biot_slider_ax  = figure.add_axes([0.58, 0.65, 0.35, 0.03])
Biot_slider = Slider(Biot_slider_ax, 'Biot Coefficient', 0.2, 0.9, valinit=Biot, valstep = 0.01)

gh_slider_ax  = figure.add_axes([0.58, 0.55, 0.35, 0.03])
gh_slider = Slider(gh_slider_ax, r'$\gamma_h$', 0, 1, valinit=gamma_h, valstep = 0.01)

gH_slider_ax  = figure.add_axes([0.58, 0.45, 0.35, 0.03])
gH_slider = Slider(gH_slider_ax, r'$\gamma_H$', 0, 1, valinit=gamma_H, valstep = 0.01)

# Updating plot with sliders
def sliders_on_changed(val):
    vstress.set_xdata(VerticalStress(OB_slider.val))
    IsotropicStress.set_xdata(IsoStress(OB_slider.val, PP_slider.val, Biot_slider.val, gh_slider.val))
    if st_wave:
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

# Reset button
reset_button_ax = figure.add_axes([0.60, 0.35, 0.1, 0.04])
reset_button = Button(reset_button_ax, 'Reset', color='#c7cdd1', hovercolor='#0874bb')
reset_button.label.set_fontsize(12)

def reset_button_on_clicked(mouse_event):
    OB_slider.reset()
    PP_slider.reset()
    Biot_slider.reset()
    gh_slider.reset()
    gH_slider.reset()
    print("YAY")
reset_button.on_clicked(reset_button_on_clicked)


# Save Button
save_button_ax = figure.add_axes([0.80, 0.35, 0.1, 0.04])
save_button = Button(save_button_ax, 'Save as CSV', color='#c7cdd1', hovercolor='#0874bb')
def save_button_on_clicked(mouse_event):
    dflas_clean.to_excel("CleanLogs.xlsx")
save_button.on_clicked(save_button_on_clicked)
save_button.label.set_fontsize(12)


if st_wave:
    lines = [vstress, IsotropicStress, St_h, St_H, Vr_h, Vr_H]
    labels = [r'$\sigma_v$', r'$\sigma^{iso}$', r'$\sigma^{St}_h$', r'$\sigma^{St}_H$', r'$\sigma^{Vr}_h$', r'$\sigma^{Vr}_H$']
    colors = ["black", "tab:red", "tab:green", "tab:purple", "tab:blue", "tab:orange"]

else:
    lines = [vstress, IsotropicStress, Vr_h, Vr_H]
    labels = [r'$\sigma_v$', r'$\sigma^{iso}$', r'$\sigma^{Vr}_h$', r'$\sigma^{Vr}_H$']
    colors = ["black", "tab:red", "tab:blue", "tab:orange"]

def toggle(label):
    index = labels.index(label)
    lines[index].set_visible(not lines[index].get_visible())
    figure.canvas.draw()

activated = [True] * len(lines)

check_button_ax = figure.add_axes([0.02, 0.63, 0.15, 0.25], facecolor = (0,0.3,0.75,0.0))
check_button = CheckButtons(check_button_ax, labels, activated)
check_button.on_clicked(toggle)

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


[check_button.labels[i].set_fontsize(13) for i in range(0,len(check_button.labels))]

# Normal Fault label
Normal_button_ax = figure.add_axes([0.58, 0.21, 0.35, 0.03])
Normal_button = Button(Normal_button_ax, r'Normal Fault: $\sigma_v > \sigma_H > \sigma_h$', color='#c7cdd1', hovercolor='#c7cdd1')
Normal_button.label.set_fontsize(12)

# Strike Fault label
strike_button_ax = figure.add_axes([0.58, 0.16, 0.35, 0.03])
strike_button = Button(strike_button_ax, r'Strike-Slipe Fault: $\sigma_H > \sigma_v > \sigma_h$', color='#c7cdd1', hovercolor='#c7cdd1')
strike_button.label.set_fontsize(12)

# Reverse Fault label
reverse_button_ax = figure.add_axes([0.58, 0.11, 0.35, 0.03])
reverse_button = Button(reverse_button_ax, r'Reverse Fault: $\sigma_H > \sigma_h > \sigma_v$ ', color='#c7cdd1', hovercolor='#c7cdd1')
reverse_button.label.set_fontsize(12)

plt.show()

