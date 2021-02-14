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
    def __init__(self,data='',data_ventre='',data_dos='',data_normal='',data_retourner='',Accelerometer='',Gyroscope=''):
        self.data = data
        self.data_ventre = data_ventre
        self.data_dos = data_dos
        self.data_normal = data_normal
        self.data_retourner = data_retourner
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
        
    def capteur_droite_ou_gauche(self):
        
        #calcul r pour tel sur le ventre
        
        f_ventre = open(self.data_ventre, "r")
        r_ventre = csv.reader(f_ventre, delimiter=",")
        lignes_ventre = list(r_ventre)
        f_ventre.seek(0)                           # retour au début du fichier
        f_ventre.close()
        
        col_1_ventre = np.array(lignes_ventre)[1:,0] #temps
        col_2_ventre = np.array(lignes_ventre)[1:,1] #omega
        col_3_ventre = np.array(lignes_ventre)[1:,2] #acceleration
        
        temps_ventre = col_1_ventre.astype(np.float)
        omega_ventre = col_2_ventre.astype(np.float)
        accel_ventre = col_3_ventre.astype(np.float)
        
        coef_ventre = (accel_ventre[50]-accel_ventre[15])/(omega_ventre[50]**2-omega_ventre[15]**2)*100
        print('Sur le ventre r est :',coef_ventre)
        #calcul r pour tel sur le dos
        
        f_dos = open(self.data_dos, "r")
        r_dos = csv.reader(f_dos, delimiter=",")
        lignes_dos = list(r_dos)
        f_dos.seek(0)                           # retour au début du fichier
        f_dos.close()
        
        col_1_dos = np.array(lignes_dos)[1:,0] #temps
        col_2_dos = np.array(lignes_dos)[1:,1] #omega
        col_3_dos = np.array(lignes_dos)[1:,2] #acceleration
        
        temps_dos = col_1_dos.astype(np.float)
        omega_dos = col_2_dos.astype(np.float)
        accel_dos = col_3_dos.astype(np.float)
        
        coef_dos = (accel_dos[50]-accel_dos[15])/(omega_dos[50]**2-omega_dos[15]**2)*100
        print('Sur le dos r est :',coef_dos)
        #droite ou gauche ?
        if coef_dos>coef_ventre :
            print('Le capteur est à gauche !')
        else:
            print('Le capteur est à droite !')
        
    def capteur(self):
            
        #calcul r pour tel sur le ventre
        f_ventre = open(self.data_ventre, "r")
        r_ventre = csv.reader(f_ventre, delimiter=",")
        lignes_ventre = list(r_ventre)
        f_ventre.seek(0)                           # retour au début du fichier
        f_ventre.close()
        
        col_1_ventre = np.array(lignes_ventre)[1:,0] #temps
        col_2_ventre = np.array(lignes_ventre)[1:,1] #omega
        col_3_ventre = np.array(lignes_ventre)[1:,2] #acceleration
        
        temps_ventre = col_1_ventre.astype(np.float)
        omega_ventre = col_2_ventre.astype(np.float)
        accel_ventre = col_3_ventre.astype(np.float)
        
        coef_ventre = (accel_ventre[50]-accel_ventre[15])/(omega_ventre[50]**2-omega_ventre[15]**2)*100
        print('Sur le ventre r est :',coef_ventre)
        
        #calcul r pour tel sur le dos
        f_dos = open(self.data_dos, "r")
        r_dos = csv.reader(f_dos, delimiter=",")
        lignes_dos = list(r_dos)
        f_dos.seek(0)                           # retour au début du fichier
        f_dos.close()
        
        col_1_dos = np.array(lignes_dos)[1:,0] #temps
        col_2_dos = np.array(lignes_dos)[1:,1] #omega
        col_3_dos = np.array(lignes_dos)[1:,2] #acceleration
        
        temps_dos = col_1_dos.astype(np.float)
        omega_dos = col_2_dos.astype(np.float)
        accel_dos = col_3_dos.astype(np.float)
        
        coef_dos = (accel_dos[50]-accel_dos[15])/(omega_dos[50]**2-omega_dos[15]**2)*100
        print('Sur le dos r est :',coef_dos)
        
        #calcul r pour tel a l'endroit
        f_normal = open(self.data_normal, "r")
        r_normal = csv.reader(f_normal, delimiter=",")
        lignes_normal = list(r_normal)
        f_normal.seek(0)                           # retour au début du fichier
        f_normal.close()
        
        col_1_normal = np.array(lignes_normal)[1:,0] #temps
        col_2_normal = np.array(lignes_normal)[1:,1] #omega
        col_3_normal = np.array(lignes_normal)[1:,2] #acceleration
        
        temps_normal = col_1_normal.astype(np.float)
        omega_normal = col_2_normal.astype(np.float)
        accel_normal = col_3_normal.astype(np.float)
        
        coef_normal = (accel_normal[50]-accel_normal[15])/(omega_normal[50]**2-omega_normal[15]**2)*100
        print("A l'endroit r est :",coef_normal)
        
        #calcul r pour tel a l'envers
        f_ret = open(self.data_retourner, "r")
        r_ret = csv.reader(f_ret, delimiter=",")
        lignes_ret = list(r_ret)
        f_ret.seek(0)                           # retour au début du fichier
        f_ret.close()
        
        col_1_ret = np.array(lignes_ret)[1:,0] #temps
        col_2_ret = np.array(lignes_ret)[1:,1] #omega
        col_3_ret = np.array(lignes_ret)[1:,2] #acceleration
        
        temps_ret = col_1_ret.astype(np.float)
        omega_ret = col_2_ret.astype(np.float)
        accel_ret = col_3_ret.astype(np.float)
        
        coef_ret = (accel_ret[50]-accel_ret[15])/(omega_ret[50]**2-omega_ret[15]**2)*100
        print("A l'envers r est :",coef_ret)
        
        gd = 0
        hb = 0
        
        #emplacement ?
        
        if coef_dos>coef_ventre :
            gd = 0 # a gauche
        else:
            gd = 1 # a droite
        if coef_normal>coef_ret :
            hb = 0 # en haut
        else : 
            hb = 1 #en bas
            
        if gd == 0 and hb == 0:
            print('Le capteur est en haut à gauche !!')
        elif gd == 0 and hb == 1:
            print('Le capteur est en bas à gauche !!')
        elif gd == 1 and hb == 0:
            print('Le capteur est en haut à droite !!')
        elif gd == 1 and hb == 1:
            print('Le capteur est en bas à droite !!')
        else :
            None
        
        
                
data = Centripete(data='Data.csv',data_ventre='Data_ventre.csv',data_dos='Data_dos.csv',data_normal='Data_normal.csv',data_retourner='data_retourner.csv',Accelerometer='Accelerometer.csv',Gyroscope='Gyroscope.csv')
#data.plot_phyphox()
#data.plot_nous()
#data.capteur_droite_ou_gauche()
data.capteur()