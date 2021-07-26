# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 02:31:56 2020

@author: arkad
"""
import nrrd
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage.filters import convolve

plik = 'RegLib_C01_1.nrrd'

obraz, naglowek = nrrd.read(plik)

#print (naglowek)
print(obraz.shape)

filtr1 = np.array([[ 0, -1/4, 0],
                  [-1/4, 2, -1/4],
                  [ 0, -1/4, 0]])

filtr2 = np.array([[ -2, -1, 0], #https://ksopyla.com/python/operacja-splotu-przetwarzanie-obrazow/
                  [-1, 1, 1],  #filtr z powyższej strony służący do wydobycia wgłebi w obrazie w odcieniach szarosci
                  [ 0, 1, 2]])

def filtruj_obraz(obraz,filtr):
    """
    Parameters
    ----------
    obraz : image
        obraz do analizy
    filtr : mask
        maska konwolucyjna

    Returns
    -------
    None.

    """
    rys, osie = plt.subplots(ncols=5, nrows=2, constrained_layout=True) #wykres jest dzielony na 5 kolumn po 2 wiersze
    i=0
    for os in osie.flatten():    
        przekroj = obraz[i+1, 30:230] #obraz jest obcinany w celu powiększenia obrazu na wykresie
        wyostrzony = convolve(przekroj, filtr)
        print(wyostrzony.shape)
        os.imshow(wyostrzony, cmap=plt.cm.gray)
        os.set_xticks([])
        os.set_yticks([])
        i += obraz.shape[0] // len(osie.flatten())
    
    plt.show()

filtruj_obraz(obraz,filtr1)
filtruj_obraz(obraz,filtr2)
