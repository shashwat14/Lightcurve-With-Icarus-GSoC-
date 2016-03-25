# -*- coding: utf-8 -*-
"""
Coding Exercise for GSoC'16 under McGill Space Institute
"""
import numpy as np
import matplotlib.pyplot as plt
from astropy import units as u
from astropy.analytic_functions import blackbody_lambda


def calculateFlux(wavelength, T):
    
    """
    Parameters:
    wavelength: Wavelength in nanometre
    T: Temperature in Kelvin

    Returns:
    flux in units of(erg / (m2 nm s)
    """
    flux = blackbody_lambda(wavelength*u.nm,T*u.K)
    return flux.value*3.14*1e5
    
def ObservedFlux(wavelength,T):
    
    """
    Params: 
    Wavelenth in nanometre
    T = Temperature in Kelvin
    
    Returns:
    observedFlux
    
    """
    #Solar radius = 2.25461 * 1e-8 parsecs
    
    obsFlux = calculateFlux(wavelength,T) * ((2.25461 * 1e-8) / (10.))**2
    return obsFlux


def plotFlux(W,Flux,T):

    """
    Parameters:
    W: Wavelength in nanometre
    Flux: flux in units of (erg / m2 nm s)
    T: Temperature in Kelvin

    Plots graph of observed Flux verses Wavelength
    """
    plt.plot(W,Flux)
    plt.title('Blackbody Curve at ' + str(T) + " K")
    plt.ylabel('Flux (erg / (m2 nm s))',fontsize=11)
    plt.xlabel("Wavelength (nm)")
    plt.show()

def flux2Mag(T,var):
     
    """
    Params:
    T = Temperature in Kelvin
    var = "U", "V", "B", or "R"
    
    Returns:
    magnitude for corresponding U, V, B or R
    """
    
    #band = variable that stores reference information
    band = {"U" : (365.,66,3.98 * 1e-4),
     "V" : (551.,88,3.63 * 1e-4),
     "B" : (445.,94,6.95 * 1e-4),
     "R" : (658.,138,2.254 * 1e-4)}
    
    cwl = band[var][0]
    F0 = band[var][2]
    m = -2.5 * np.log10(ObservedFlux(cwl,T)/(F0))
    return m
    
     
T = 6000. #Temperature
W = np.arange(1.,1000.,1.)
Flux = calculateFlux(W,T)
plotFlux(W,Flux,T)
print flux2Mag(T,"U")
print flux2Mag(T,"B")
print flux2Mag(T,"V")
print flux2Mag(T,"R")
