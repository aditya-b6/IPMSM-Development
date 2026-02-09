import numpy as np
import matplotlib.pyplot as plt
from scipy import fsolve

Tb=1
Wb=1
V=1
p = 4 #pole pairs

#base values
T=Tb
W=Wb
Ld=0
L = (3*p*V**2)/(2*Wb**2*T**2)
Lq = L
i = (2*T*Wb)/(3*p*V)
id=i
iq=i
Ym = L*i


gamma_b = 30*(np.pi/180)

def MTPA(x,y):
    lambda_m = x
    Z = y
    gamma_b = np.arcsin((lambda_m - np.sqrt(lambda_m**2 + 8 * Ld**2 * (1 - Z)**2 * i**2)) / (4 * Ld * (1 - Z) * i))
    Ld = (lambda_m*i*np.cos(gamma_b)-Tb)/((1-Z)*i**2*(np.sin(2*gamma_b)/2))
    i = np.sqrt[((V**2/Wb**2)-lambda_m**2+(2*lambda_m*Ld*i*np.sin(gamma_b))/(((np.sin(gamma_b))**2+(Z**2*(np.cos(gamma_b))**2)))*Ld**2)]

    return(Ld,i)



    

