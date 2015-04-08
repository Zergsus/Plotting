# encoding: UTF-8

import sys
import os.path
import glob
import numpy as np
import matplotlib
from matplotlib.ticker import MultipleLocator
import pylab

# Take data files from folder specified by user

folder = sys.argv[1]
vac = sys.argv[2]
vdc = sys.argv[3]

sub_path = '/home/jesus/Doctorado/reducciones_lab/'

path = os.path.join(sub_path, folder, "*.F*")

file_list = glob.glob(path)

# Take sample name from file name

sample_name = os.path.splitext(os.path.basename(file_list[0]))[0]

# Make a list with files ending with F11, F12, ...

matrix_elements = []

for item in file_list:
    extension = os.path.splitext(item)[1][1:]
    matrix_elements.append(extension)

# Define function that gets data from files

def get_data(n):
    return np.genfromtxt(os.path.join(sub_path, folder, sample_name + '.') + str(n), 
                         delimiter='\t', 
                         dtype=None , 
                         usecols=(0, 1, 2), 
                         names='deg, data, error')
    #return deg, data = np.loadtxt(os.path.join(sub_path, folder, sample_name + '.') + str(n), 
                                  #delimiter='\t', usecols=(0, 1), unpack=True)
def split_name(name):
    return name[0], name[1:]


def load_data(path, ignore_nlines=6):
    with open(path, 'rt') as fd:
        rows = []
        for index, line in enumerate(fd):
            if index < ignore_nlines:
                continue

            columns = [float(x) for x in line.split()]
            values = [columns[0]] + columns[1::2]
            rows.append(values)

        return zip(*rows)


#


#lista = [, , ]
#nombres = ['', '', '']

#for i, j in zip(lista, nombres)



matrix_elements.sort()
scattering_elements = dict()

pylab.figure(figsize=(10, 10), dpi=400)

pylab.rc('text', usetex=True)
pylab.rc("font", size = 9)


for index, name in enumerate(matrix_elements):
    data = get_data(name)

    if name == 'F11' or name == 'F12' or name == 'F22' or name == 'F33' or name == 'F34' or name == 'F44':

        if name == 'F11':
            index2 = 1
        elif name == 'F12':
            index2= 2
        elif name == 'F22':
            index2= 3
        elif name == 'F33':
            index2= 4
        elif name == 'F34':
            index2= 5
        elif name == 'F44':
            index2= 6


    scattering_elements[name] = data

    pylab.subplot(4, 4, index + 1)

    letter, number = split_name(name)


    if index == 0:
        pylab.yscale('log')
        pylab.text(30, 0.03, name, fontsize=12)
    elif index2 == 3:
        pylab.ylim(ymin = 0)
        pylab.ylim(ymax = 1.1)
        pylab.gca().yaxis.set_minor_locator(MultipleLocator(0.1))
        index2 = 0
    else:
        pylab.ylim(ymin = -1)
        pylab.ylim(ymax = 1)
        pylab.gca().yaxis.set_minor_locator(MultipleLocator(0.1))


    if name == 'F12':

        pylab.errorbar(data['deg'], -data['data'], 
                       fmt='o', mfc='None', mec='black', 
                       markersize = 4, yerr=data['error'], 
                       ecolor='black', elinewidth=0.5,
                       capsize= 0, label=str(sample_name))
    else:

        pylab.errorbar(data['deg'], data['data'], 
                       fmt='o', mfc='None', mec='black', 
                       markersize = 4, yerr=data['error'], 
                       ecolor='black', elinewidth=0.5,
                       capsize= 0, label=str(sample_name))

    xmin,xmax = pylab.xlim()
    ymin,ymax = pylab.ylim()

    if name == 'F11':
        pylab.text(0.4*xmax, 0.2*ymax, r'$F_{{{0}}}$'.format(str(number)), fontsize=12)
    elif name == 'F12':
        pylab.text(0.4*xmax, 0.75*ymax, '-'+r'$F_{{{0}}}$'.format(str(number))+r'$\rm /\textit{$F$}_{11}$', fontsize=12)
    else:
        pylab.text(0.4*xmax, 0.75*ymax, r'$F_{{{0}}}$'.format(str(number))+r'$\rm /\textit{$F$}_{11}$', fontsize=12)



    pylab.xticks([0, 45, 90, 135, 180])
    pylab.gca().xaxis.set_minor_locator(MultipleLocator(15))  
    


pylab.tight_layout()
pylab.legend(loc='center left', bbox_to_anchor=(1, 0.5), title='Vdc='+str(vdc)+'  Vac='+str(vac))
pylab.savefig(sample_name, bbox_inches='tight', dpi=400)
pylab.show()









