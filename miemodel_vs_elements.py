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
matrix = sys.argv[2]
vac = sys.argv[3]
vdc = sys.argv[4]

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



def load_data(path, ignore_nlines=56):
    with open(path, 'rt') as fd:
        rows = []
        for index, line in enumerate(fd):
            if index < ignore_nlines:
                continue

            columns = [float(x) for x in line.split()]
            values = columns[0::]
            rows.append(values)

        return zip(*rows)

x = load_data(os.path.join(sub_path, matrix))
#


#lista = [, , ]
#nombres = ['', '', '']

#for i, j in zip(lista, nombres)



matrix_elements.sort()
scattering_elements = dict()

pylab.figure(figsize=(10, 10), dpi=400)

pylab.rc('text', usetex=True)
pylab.rc("font", size = 9)

index2 = 0

for index, name in enumerate(matrix_elements):
    data = get_data(name)

    if name == 'F11' or name == 'F12' or name == 'F21' or name == 'F33' or name == 'F34' or name == 'F43' or name == 'F44':

        if name == 'F11':
            index2 = 1
            x[index2] = [item/x[index2][30] for item in x[index2]]
        elif name == 'F12':
            index2 = 2
            x[index2] = [-item for item in x[index2]]
        elif name == 'F21':
            index2 = 2
            x[index2] = [-item for item in x[index2]]
        elif name == 'F33':
            index2 = 3
        elif name == 'F34':
            index2 = 4
        elif name == 'F43':
            index2 = 4
            x[index2] = [-item for item in x[index2]]
        elif name == 'F44':
            index2 = 3

    scattering_elements[name] = data

    pylab.subplot(4, 4, index + 1)

    letter, number = split_name(name)

    if index == 0:
        pylab.yscale('log')
        pylab.text(30, 0.03, name, fontsize=12)
    elif name == 'F22':
        pylab.ylim(ymin = 0)
        pylab.ylim(ymax = 1.1)
        pylab.gca().yaxis.set_minor_locator(MultipleLocator(0.1))
        pylab.text(15, 0.7, name+r'$\rm /F_{11}$', fontsize=12)
        matplotlib.pyplot.axhline(1, 0, 180,  "-", color ='r', markersize = 4, label='Mie Model')
    else:
        pylab.ylim(ymin = -1)
        pylab.ylim(ymax = 1)
        pylab.gca().yaxis.set_minor_locator(MultipleLocator(0.1))

        if name == 'F12':
            pylab.text(15, -0.7, '-'+name+r'$\rm /F_{11}$', fontsize=12)
        else:
            pylab.text(15, -0.7, name+r'$\rm /F_{11}$', fontsize=12)

    if name == 'F12':

        pylab.errorbar(data['deg'], -data['data'], 
                       fmt='o', mfc='None', mec='black', 
                       markersize = 4, yerr=data['error'], 
                       ecolor='black', elinewidth=0.5,
                       capsize= 0, label=str(sample_name))

        if index2 != 0:
            pylab.plot(x[0], x[index2], "r-", markersize = 4, label='Mie Model')
            index2 = 0
    else:

        pylab.errorbar(data['deg'], data['data'], 
                       fmt='o', mfc='None', mec='black', 
                       markersize = 4, yerr=data['error'], 
                       ecolor='black', elinewidth=0.5,
                       capsize= 0, label=str(sample_name))

        if index2 != 0:
            if name == 'F43':
                pylab.plot(x[0], x[index2], "r-", markersize = 4, label='Mie Model')
            else:
                pylab.plot(x[0], x[index2], "r-", markersize = 4, label='Mie Model')
            index2 = 0



    pylab.xticks([0, 45, 90, 135, 180])
    pylab.gca().xaxis.set_minor_locator(MultipleLocator(15))  
    


pylab.tight_layout()
pylab.legend(loc='center left', bbox_to_anchor=(1, 0.5), title='Vdc='+str(vdc)+'  Vac='+str(vac))
pylab.savefig(sample_name, bbox_inches='tight', dpi=400)
pylab.show()









