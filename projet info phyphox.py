# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 21:43:24 2021

@author: Myrann
"""

#Orienté objet

import csv
import matplotlib.pyplot as plt
import numpy as np

class Centripete():
    def __init__(self,data='',Accelerometer='',Gyroscope=''):
        self.data = data
        self.Accelerometer = Accelerometer
        self.Gyroscope = Gyroscope
    def plot_phyphox(self):
        f = open(self.data, "r")
        r = csv.reader(f, delimiter=",")
        lignes = list(r)
        f.seek(0)                           # retour au début du fichier
        f.close()
        
        col_1 = np.array(lignes)[1:,0] #temps
        col_2 = np.array(lignes)[1:,1] #omega
        col_3 = np.array(lignes)[1:,2] #acceleration
        
        temps = col_1.astype(np.float)
        omega = col_2.astype(np.float)
        accel = col_3.astype(np.float)
        
        coef = (accel[50]-accel[15])/(omega[50]**2-omega[15]**2)
        print('Le rayson calculer par phyphox est :',coef*100,'cm')
        
        plt.figure(0)
        plt.scatter(omega,accel)
        plt.title(f'Acceleration en fct de w, r={coef*100} cm')
        plt.xlabel('w en rad/s')
        plt.ylabel('a en m/s²')
        #plt.savefig('Donnee centripete a en fct de w, r=6,55cm')
        
        plt.figure(1)
        plt.scatter(omega**2,accel)
        plt.title(f'Acceleration en fct de w², r={coef*100} cm')
        plt.xlabel('w en rad/s')
        #plt.savefig('1er donnee centripete a en fct de w², r=6,55cm')
        
        
    def plot_nous(self):
        #acceleration
        f = open(self.Accelerometer, "r")
        r = csv.reader(f, delimiter=",")
        lignes = list(r)
        f.seek(0)                           # retour au début du fichier
        f.close()
        
        
        col_0 = np.array(lignes)[1:,0] #t   les valeurs de l'acceleration ici
        col_1 = np.array(lignes)[1:,1] #x
        col_2 = np.array(lignes)[1:,2] #y
        col_3 = np.array(lignes)[1:,3] #z
        
        t = col_0.astype(np.float)     #on converti en beau tableau
        ax = col_1.astype(np.float)
        ay = col_2.astype(np.float)
        az = col_3.astype(np.float)
        normea = np.sqrt(ax**2+ay**2)  #on calcul la norme, pas accel sur z
        
        #gyroscope
        f1 = open(self.Gyroscope, "r")
        r1 = csv.reader(f1, delimiter=",")
        lignes1 = list(r1)
        f1.seek(0)                           # retour au début du fichier
        f1.close()
        
        col_00 = np.array(lignes1)[1:,0]
        col_11 = np.array(lignes1)[1:,1] #x
        col_22 = np.array(lignes1)[1:,2] #y
        col_33 = np.array(lignes1)[1:,3] #z
        
        t1 = col_00.astype(np.float)
        wx = col_11.astype(np.float)
        wy = col_22.astype(np.float)
        wz = col_33.astype(np.float)
        normew = np.sqrt(wx**2+wy**2+wz**2)
        
        diff = np.abs(len(col_11)-len(col_1)) #calcul diff de taille de valeurs entre accel et gyro
        
        col_1 = np.array(lignes)[1+diff:,1] #x
        col_2 = np.array(lignes)[1+diff:,2] #y
        
        ax = col_1.astype(np.float)
        ay = col_2.astype(np.float)
        normea = np.sqrt(ax**2+ay**2)
        
        coef = (normea[1000]-normea[500])/(normew[1000]**2-normew[500]**2)
        print('Le rayson calculer par nous est :',coef*100,'cm')
        
        
        plt.figure(2)
        plt.title(f'Acceleration en fct de w, r={coef*100} cm')
        plt.scatter(normew,normea)
        plt.xlabel('w en rad/s')
        plt.ylabel('a en m/s²')
        
        #plt.savefig('donnee w, sans g, tel sur le ventre, r=2,75cm')
        
        plt.figure(3)
        plt.title(f'Acceleration en fonction de w², r={coef*100} cm')
        plt.scatter(normew**2,normea)
        plt.xlabel('w² en rad²/s²')
        plt.ylabel('a en m/s²')
        
        #plt.savefig('donnee w² sans g, tel sur le ventre, r=2,75cm')
                
data = Centripete('Data.csv','Accelerometer.csv','Gyroscope.csv')
data.plot_phyphox()
data.plot_nous()