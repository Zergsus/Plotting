import numpy as np
import matplotlib
from matplotlib.ticker import MultipleLocator
import pylab
import os.path

#--------READING FROM FILES----------

path = '/home/jesus/Doctorado/reducciones_lab/'

folder = 'reduccion_2_141017' + '/'

def get_data(n):
    return np.genfromtxt(os.path.join(path, folder, 'WhiteClay.F') + str(n), delimiter='\t', dtype=None , usecols=(0, 1), names='deg, data')


f11 = get_data(11)

print f11

#F12
f12 = np.genfromtxt(path + folder + '/WhiteClay.F12', delimiter='\t', dtype=None , usecols=(0, 1), names='deg, data')

#F13
f13 = np.genfromtxt(path + folder + '/WhiteClay.F13', delimiter='\t', dtype=None , usecols=(0, 1), names='deg, data')

#F14
f14 = np.genfromtxt(path + folder + '/WhiteClay.F14', delimiter='\t', dtype=None , usecols=(0, 1), names='deg, data')

#F21
f21 = np.genfromtxt(path + folder + '/WhiteClay.F21', delimiter='\t', dtype=None , usecols=(0, 1), names='deg, data')

#F22
f22 = np.genfromtxt(path + folder + '/WhiteClay.F22', delimiter='\t', dtype=None , usecols=(0, 1), names='deg, data')

#F24
f24 = np.genfromtxt(path + folder + '/WhiteClay.F24', delimiter='\t', dtype=None , usecols=(0, 1), names='deg, data')

#F31
f31 = np.genfromtxt(path + folder + '/WhiteClay.F31', delimiter='\t', dtype=None , usecols=(0, 1), names='deg, data')

#F32
f32 = np.genfromtxt(path + folder + '/WhiteClay.F32', delimiter='\t', dtype=None , usecols=(0, 1), names='deg, data')

#F33
f33 = np.genfromtxt(path + folder + '/WhiteClay.F33', delimiter='\t', dtype=None , usecols=(0, 1), names='deg, data')

#F34
f34 = np.genfromtxt(path + folder + '/WhiteClay.F34', delimiter='\t', dtype=None , usecols=(0, 1), names='deg, data')

#F41
f41 = np.genfromtxt(path + folder + '/WhiteClay.F41', delimiter='\t', dtype=None , usecols=(0, 1), names='deg, data')

#F43
f43 = np.genfromtxt(path + folder + '/WhiteClay.F43', delimiter='\t', dtype=None , usecols=(0, 1), names='deg, data')

#F44
f44 = np.genfromtxt(path + folder + '/WhiteClay.F44', delimiter='\t', dtype=None , usecols=(0, 1), names='deg, data')


#--------------------------

pylab.figure(figsize=(10, 10), dpi=100)
pylab.rc("font", size = 9)


pylab.subplot(4, 4, 1)
pylab.plot(f11['deg'], f11['data'], "ro", mfc='None', mec='black', markersize = 4)
pylab.yscale('log')
pylab.xticks([0, 45, 90, 135, 180])
pylab.gca().xaxis.set_minor_locator(MultipleLocator(15))
pylab.text(30, 0.03, "$F_{11}$", fontsize=12)

pylab.subplot(4, 4, 2)
pylab.plot(f12['deg'], -f12['data'], "ro", mfc='None', mec='black', markersize = 4)
pylab.ylim(ymin = -1)
pylab.ylim(ymax = 1)
pylab.xticks([0, 45, 90, 135, 180])
pylab.gca().xaxis.set_minor_locator(MultipleLocator(15))
pylab.gca().yaxis.set_minor_locator(MultipleLocator(0.1))
pylab.text(15, -0.7, "$-F_{12}/F_{11}$", fontsize=12)

pylab.subplot(4, 4, 3)
pylab.plot(f13['deg'], f13['data'], "ro", mfc='None', mec='black', markersize = 4)
pylab.ylim(ymin = -1)
pylab.ylim(ymax = 1)
pylab.xticks([0, 45, 90, 135, 180])
pylab.gca().xaxis.set_minor_locator(MultipleLocator(15))
pylab.gca().yaxis.set_minor_locator(MultipleLocator(0.1))
pylab.text(30, -0.7, "$F_{13}/F_{11}$", fontsize=12)

pylab.subplot(4, 4, 4)
pylab.plot(f14['deg'], f14['data'], "ro", mfc='None', mec='black', markersize = 4)
pylab.ylim(ymin = -1)
pylab.ylim(ymax = 1)
pylab.xticks([0, 45, 90, 135, 180])
pylab.gca().xaxis.set_minor_locator(MultipleLocator(15))
pylab.gca().yaxis.set_minor_locator(MultipleLocator(0.1))
pylab.text(30, -0.7, "$F_{14}/F_{11}$", fontsize=12)

pylab.subplot(4, 4, 5)
pylab.plot(f21['deg'], f21['data'], "ro", mfc='None', mec='black', markersize = 4)
pylab.ylim(ymin = -1)
pylab.ylim(ymax = 1)
pylab.xticks([0, 45, 90, 135, 180])
pylab.gca().xaxis.set_minor_locator(MultipleLocator(15))
pylab.gca().yaxis.set_minor_locator(MultipleLocator(0.1))
pylab.text(30, -0.7, "$F_{21}/F_{11}$", fontsize=12)

pylab.subplot(4, 4, 6)
pylab.plot(f22['deg'], f22['data'], "ro", mfc='None', mec='black', markersize = 4)
pylab.ylim(ymin = -1)
pylab.ylim(ymax = 1)
pylab.xticks([0, 45, 90, 135, 180])
pylab.gca().xaxis.set_minor_locator(MultipleLocator(15))
pylab.gca().yaxis.set_minor_locator(MultipleLocator(0.1))
pylab.text(30, -0.7, "$F_{22}/F_{11}$", fontsize=12)

pylab.subplot(4, 4, 8)
pylab.plot(f24['deg'], f24['data'], "ro", mfc='None', mec='black', markersize = 4)
pylab.ylim(ymin = -1)
pylab.ylim(ymax = 1)
pylab.xticks([0, 45, 90, 135, 180])
pylab.gca().xaxis.set_minor_locator(MultipleLocator(15))
pylab.gca().yaxis.set_minor_locator(MultipleLocator(0.1))
pylab.text(30, -0.7, "$F_{24}/F_{11}$", fontsize=12)

pylab.subplot(4, 4, 9)
pylab.plot(f31['deg'], f31['data'], "ro", mfc='None', mec='black', markersize = 4)
pylab.ylim(ymin = -1)
pylab.ylim(ymax = 1)
pylab.xticks([0, 45, 90, 135, 180])
pylab.gca().xaxis.set_minor_locator(MultipleLocator(15))
pylab.gca().yaxis.set_minor_locator(MultipleLocator(0.1))
pylab.text(30, -0.7, "$F_{31}/F_{11}$", fontsize=12)

pylab.subplot(4, 4, 10)
pylab.plot(f32['deg'], f32['data'], "ro", mfc='None', mec='black', markersize = 4)
pylab.ylim(ymin = -1)
pylab.ylim(ymax = 1)
pylab.xticks([0, 45, 90, 135, 180])
pylab.gca().xaxis.set_minor_locator(MultipleLocator(15))
pylab.gca().yaxis.set_minor_locator(MultipleLocator(0.1))
pylab.text(30, -0.7, "$F_{32}/F_{11}$", fontsize=12)

pylab.subplot(4, 4, 11)
pylab.plot(f33['deg'], f33['data'], "ro", mfc='None', mec='black', markersize = 4)
pylab.ylim(ymin = -1)
pylab.ylim(ymax = 1)
pylab.xticks([0, 45, 90, 135, 180])
pylab.gca().xaxis.set_minor_locator(MultipleLocator(15))
pylab.gca().yaxis.set_minor_locator(MultipleLocator(0.1))
pylab.text(30, -0.7, "$F_{33}/F_{11}$", fontsize=12)

pylab.subplot(4, 4, 12)
pylab.plot(f34['deg'], f34['data'], "ro", mfc='None', mec='black', markersize = 4)
pylab.ylim(ymin = -1)
pylab.ylim(ymax = 1)
pylab.xticks([0, 45, 90, 135, 180])
pylab.gca().xaxis.set_minor_locator(MultipleLocator(15))
pylab.gca().yaxis.set_minor_locator(MultipleLocator(0.1))
pylab.text(30, -0.7, "$F_{34}/F_{11}$", fontsize=12)

pylab.subplot(4, 4, 13)
pylab.plot(f41['deg'], f41['data'], "ro", mfc='None', mec='black', markersize = 4)
pylab.ylim(ymin = -1)
pylab.ylim(ymax = 1)
pylab.xticks([0, 45, 90, 135, 180])
pylab.gca().xaxis.set_minor_locator(MultipleLocator(15))
pylab.gca().yaxis.set_minor_locator(MultipleLocator(0.1))
pylab.text(30, -0.7, "$F_{41}/F_{11}$", fontsize=12)

pylab.subplot(4, 4, 15)
pylab.plot(f43['deg'], f43['data'], "ro", mfc='None', mec='black', markersize = 4)
pylab.ylim(ymin = -1)
pylab.ylim(ymax = 1)
pylab.xticks([0, 45, 90, 135, 180])
pylab.gca().xaxis.set_minor_locator(MultipleLocator(15))
pylab.gca().yaxis.set_minor_locator(MultipleLocator(0.1))
pylab.text(30, -0.7, "$F_{43}/F_{11}$", fontsize=12)

pylab.subplot(4, 4, 16)
pylab.plot(f44['deg'], f44['data'], "ro", mfc='None', mec='black', markersize = 4)
pylab.ylim(ymin = -1)
pylab.ylim(ymax = 1)
pylab.xticks([0, 45, 90, 135, 180])
pylab.gca().xaxis.set_minor_locator(MultipleLocator(15))
pylab.gca().yaxis.set_minor_locator(MultipleLocator(0.1))
pylab.text(30, -0.7, "$F_{44}/F_{11}$", fontsize=12)

pylab.tight_layout()
pylab.show()




