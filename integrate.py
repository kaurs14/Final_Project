import numpy as np
import matplotlib.pyplot as plt

#Integrate euler method and RK4
def rk4(derivatives, t, dt, y):
    k1 = derivatives(t, y)
    k2 = derivatives(t, y+k1*0.5*dt)
    k3 = derivatives(t, y+k2*0.5*dt)
    k4 = derivatives(t, y+k3*dt)

    return y+dt*(k1+2*(k2+k3)+k4)/6

def rk1(p,v,delta_t,dpdt,dvdt):
    p, v = p + dpdt*delta_t, v + dvdt*delta_t
    return p, v
