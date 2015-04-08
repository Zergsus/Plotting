# encoding: UTF-8

import sys
import os.path
import glob
import numpy as np
import matplotlib
from matplotlib.ticker import MultipleLocator
import pylab

# Take data files from folder specified by user

element = sys.argv[1]
folders = sys.argv[2:]

for folder in folders:
	path = os.path.join(folder, "*.F*")

file_list = glob.glob(path)

# Take sample name from file name

sample_name = os.path.splitext(os.path.basename(file_list[0]))[0]

# Make a list with files ending with F11, F12, ...

matrix_elements = []

for item in file_list:
    extension = os.path.splitext(item)[1][1:]
    matrix_elements.append(extension)

# Define function that gets data from files


def get_data(n,folder):
    return np.genfromtxt(os.path.join(folder, sample_name + '.') + str(n), 
                         delimiter='\t', 
                         dtype=None , 
                         usecols=(0, 1, 2), 
                         names='deg, data, error')
    #return deg, data = np.loadtxt(os.path.join(sub_path, folder, sample_name + '.') + str(n), 
                                  #delimiter='\t', usecols=(0, 1), unpack=True)
def split_name(name):
    return name[0], name[1:]

#Plot function

def plot_element(name,folder,symbol,label):

	data = get_data(element,folder)

	if element == 'F12':

		pylab.errorbar(data['deg'], -data['data'], 
		               fmt='o', mfc='None', mec=symbol, 
		               markersize = 4, yerr=data['error'], 
		               ecolor=symbol, elinewidth=0.5,
		               capsize= 0, label=label)

		pylab.plot((0,180), (0,0), '--', color='k', linewidth=0.5)
	else:

		pylab.errorbar(data['deg'], data['data'], 
		               fmt='o', mfc='None', mec=symbol, 
		               markersize = 4, yerr=data['error'], 
		               ecolor=symbol, elinewidth=0.5,
		               capsize= 0, label=label)


	xmin,xmax = pylab.xlim()
	ymin,ymax = pylab.ylim()

	if element == 'F11':
		pylab.yscale('log')
	elif element == 'F22':
		pylab.ylim(ymin = 0)
		pylab.ylim(ymax = 1.1)
		pylab.gca().yaxis.set_minor_locator(MultipleLocator(0.1))
	else:
		pylab.ylim(ymin = 1.8*ymin)
		pylab.ylim(ymax = 1.8*ymax)
		pylab.gca().yaxis.set_minor_locator(MultipleLocator(0.1))


	pylab.xticks([0, 45, 90, 135, 180])
	pylab.gca().xaxis.set_minor_locator(MultipleLocator(15))

	return xmax,ymax  

##############################################

pylab.figure(figsize=(3, 3), dpi=400)

pylab.rc('text', usetex=True)
pylab.rc("font", size = 9)

symbol=['blue','green']
label=['488nm','520nm']

for number,(folder) in enumerate(folders):
	xmax,ymax=plot_element(element,folder,symbol[number],label[number])

letter, number = split_name(element)

pylab.xlabel( " Scattering angle (degrees) " , fontsize =9)

if element == 'F11':
	pylab.text(0.4*xmax, 0.2*ymax, r'$F_{{{0}}}$'.format(str(number)), fontsize=12)
elif element == 'F12':
	pylab.text(0.4*xmax, 0.75*ymax, '-'+r'$F_{{{0}}}$'.format(str(number))+r'$\rm /\textit{$F$}_{11}$', fontsize=12)
else:
	pylab.text(0.4*xmax, 0.75*ymax, r'$F_{{{0}}}$'.format(str(number))+r'$\rm /\textit{$F$}_{11}$', fontsize=12)
    

pylab.tight_layout()
pylab.legend(numpoints=1,frameon=False,prop={'size':6})
pylab.savefig(element + sample_name + '.eps', bbox_inches='tight', dpi=400)


