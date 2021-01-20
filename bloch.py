# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 20:49:38 2021

@author: Adrien
"""

import matplotlib as mpl
from pylab import *
from qutip import *
from matplotlib import cm
import imageio

def animate_bloch(states, duration=0.2, save_all=False):

    b = Bloch()
    b.vector_color = ['r']
    b.view = [-40,30]
    images=[]
    try:
        length = len(states)
    except:
        length = 1
        states = [states]
    ## normalize colors to the length of data ##
    nrm = mpl.colors.Normalize(0,length)
    colors = cm.cool(nrm(range(length))) # options: cool, summer, winter, autumn etc.

    ## customize sphere properties ##
    b.point_color = list(colors) # options: 'r', 'g', 'b' etc.
    b.point_marker = ['o']
    b.point_size = [30]
    
    for i in range(length):
        b.clear()
        b.add_states(states[i])
        b.add_states(states[:(i+1)],'point')
        if save_all:
            b.save(dirc='tmp') #saving images to tmp directory
            filename="tmp/bloch_%01d.png" % i
        else:
            filename='temp_file.png'
            b.save(filename)
        images.append(imageio.imread(filename))
    imageio.mimsave('bloch_anim.gif', images, duration=duration)

states = []


thetas1 = linspace(0,pi,25)

for theta in thetas1:
    ##states.append((cos(theta/2)*basis(2,0) + (1+0j)*sin(theta/2)*basis(2,1)).unit()) #90ygauche
    states.append((cos(theta/2)*basis(2,0) - (0+1j)*sin(theta/2)*basis(2,1)).unit()) #90xdoroite
    ##states.append((cos(theta/2)*basis(2,0) + (0+0j)*sin(theta/2)*basis(2,1)).unit())

animate_bloch(states, duration=0.1, save_all=False)