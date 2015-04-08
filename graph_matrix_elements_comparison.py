# encoding: UTF-8

import sys
import os.path
import glob
import numpy as np
import matplotlib
from matplotlib.ticker import MultipleLocator
import pylab

# Take data files from folder specified by user

folders = sys.argv[1:]

path=[]

for item in folders:
    path.append(os.path.join(item, "*.F*"))



files_list = []

for item in path:
    files_list.append(glob.glob(item))


# Take sample name from file name

sample_name = []

for sample in files_list:
    first_element = os.path.basename(sample[0])
    name = os.path.splitext(first_element)[0]
    sample_name.append(name)



# Make a list with files ending with F11, F12, ...

prematrix_elements = []

for sample in files_list:
    sample_extensions = []
    for element in sample:
        ext = os.path.splitext(element)[1][1:]
        sample_extensions.append(ext)
    prematrix_elements.append(sample_extensions)

matrix_elements = prematrix_elements[0]

for minilist in prematrix_elements:
    for element in minilist:
        if element not in matrix_elements:
            matrix_elements.append(element)

matrix_elements.sort()


# Define function that gets data from files

def get_data(n,sample,folder):
    return np.genfromtxt(os.path.join(folder, sample ) + '.' + str(n), 
                         delimiter='\t', 
                         dtype=None , 
                         usecols=(0, 1, 2), 
                         names='deg, data, error')


def split_name(name):
    return name[0], name[1:]


#==============Plotting functions====================

def plot_element_position(data,name,symbol,label):

    position_elements = ['F11','F12','F13','F14','F21','F22','F23','F24',
                       'F31','F32','F33','F34','F41','F42','F43','F44']

    indices = np.arange(len(position_elements))

    element_index = dict(zip(position_elements,indices))


    index = element_index[str(name)]


  


    pylab.subplot(4, 4, index+1)
                

    if name == 'F12':

		pylab.errorbar(data['deg'], -data['data'], 
		               fmt='o', mfc='None', mec=symbol, 
		               markersize = 4, yerr=data['error'], 
		               ecolor=symbol, elinewidth=0.5,
		               capsize= 0, label=label)

    else:

		pylab.errorbar(data['deg'], data['data'], 
		               fmt='o', mfc='None', mec=symbol, 
		               markersize = 4, yerr=data['error'], 
		               ecolor=symbol, elinewidth=0.5,
		               capsize= 0, label=label)

    xmin,xmax = pylab.xlim()
    ymin,ymax = pylab.ylim()

    if ymax > y_max_absolute[str(name)]:
        y_max_absolute[str(name)] = ymax


    if name=='F11':
        pylab.yscale('log')
    elif name=='F22':
        pylab.ylim(ymin = 0)
        pylab.ylim(ymax = 1.1)
        pylab.gca().yaxis.set_minor_locator(MultipleLocator(0.1))
        pylab.plot((0,180), (1,1), '--', color='k', linewidth=0.5)
    elif name == 'F12':
        pylab.ylim(ymin = -0.1)
        pylab.ylim(ymax = 0.3)
        pylab.gca().yaxis.set_minor_locator(MultipleLocator(0.1))
        pylab.plot((0,180), (0,0), '--', color='k', linewidth=0.5)
    elif name == 'F21':
        pylab.ylim(ymin = -0.3)
        pylab.ylim(ymax = 0.1)
        pylab.gca().yaxis.set_minor_locator(MultipleLocator(0.1))
        pylab.plot((0,180), (0,0), '--', color='k', linewidth=0.5) 
    elif name == 'F34':
        pylab.ylim(ymin = -0.1)
        pylab.ylim(ymax = 0.5)
        pylab.gca().yaxis.set_minor_locator(MultipleLocator(0.1))
        pylab.plot((0,180), (0,0), '--', color='k', linewidth=0.5)
    elif name == 'F43':
        pylab.ylim(ymin = -0.5)
        pylab.ylim(ymax = 0.1)
        pylab.gca().yaxis.set_minor_locator(MultipleLocator(0.1))
        pylab.plot((0,180), (0,0), '--', color='k', linewidth=0.5)
    else:
        pylab.ylim(ymin =-1)
        pylab.ylim(ymax = 1)
        pylab.gca().yaxis.set_minor_locator(MultipleLocator(0.1))

    


    pylab.xticks([0, 45, 90, 135, 180])
    pylab.gca().xaxis.set_minor_locator(MultipleLocator(15))



######################## MAIN ##################################

pylab.figure(figsize=(10, 10), dpi=400)

pylab.rc('text', usetex=True)
pylab.rc("font", size = 9)


symbols = ['b','g']
labels = ['488nm','520nm']


position_elements = ['F11','F12','F13','F14','F21','F22','F23','F24',
                     'F31','F32','F33','F34','F41','F42','F43','F44']

full_of_ones = [-1] * len(position_elements)

y_max_absolute = dict(zip(position_elements,full_of_ones))





combo_folders = zip(folders,sample_name,prematrix_elements)


for index, (folder,sample,elements) in enumerate(combo_folders):

    for element in elements: 
        data = get_data(element,sample,folder)

        plot_element_position(data, element, symbols[index], labels[index])



        letter, number = split_name(element)

        if index == 0:

            ymin,ymax = pylab.ylim()

            if element == 'F11':
                pylab.text(0.4*180, 0.2*ymax, r'$F_{{{0}}}$'.format(str(number)), fontsize=12)
            elif element == 'F12' or element == 'F21':
                pylab.text(0.4*180, 0.65*ymax, r'-$F_{{{0}}}$'.format(str(number))+r'$\rm /\textit{$F$}_{11}$', fontsize=12)
            elif element == 'F34' or element == 'F43':
                pylab.text(0.4*180, 0.6*ymax, r'$F_{{{0}}}$'.format(str(number))+r'$\rm /\textit{$F$}_{11}$', fontsize=12)
            else:
                pylab.text(0.4*180, 0.75*ymax, r'$F_{{{0}}}$'.format(str(number))+r'$\rm /\textit{$F$}_{11}$', fontsize=12)


pylab.tight_layout()
pylab.legend(loc='center left', bbox_to_anchor=(1, 0.5), numpoints=1)
pylab.savefig(sample_name[0], bbox_inches='tight', dpi=400) 










