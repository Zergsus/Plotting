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
                         usecols=(0, 1), 
                         names='deg, data')

def split_name(name):
    return name[0], name[1:]



# 


matrix_elements.sort()
scattering_elements = dict()

pylab.figure(figsize=(10, 10), dpi=400)

pylab.rc('text', usetex=True)
pylab.rc("font", size = 9)

for index, name in enumerate(matrix_elements):
    data = get_data(name)
    scattering_elements[name] = data

    pylab.subplot(4, 4, index + 1)

    letter, number = split_name(name)

    if index == 0:
        pylab.yscale('log')
        pylab.text(30, 0.03, name, fontsize=12)
    else:
        pylab.ylim(ymin = -1)
        pylab.ylim(ymax = 1)
        pylab.gca().yaxis.set_minor_locator(MultipleLocator(0.1))
        if index == 1:
            pylab.text(15, -0.7, '-'+name+'/F11', fontsize=12)
        else:
            pylab.text(15, -0.7, name+'/F11', fontsize=12)

    if index == 1:
        pylab.plot(data['deg'], -data['data'], "o", mfc='None', mec='black', markersize = 4)
    else:
        pylab.plot(data['deg'], data['data'], "o", mfc='None', mec='black', markersize = 4)


    pylab.xticks([0, 45, 90, 135, 180])
    pylab.gca().xaxis.set_minor_locator(MultipleLocator(15))  
    


pylab.tight_layout()
pylab.savefig(sample_name, bbox_inches='tight', dpi=400)
pylab.show()







