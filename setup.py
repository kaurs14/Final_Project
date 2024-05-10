#Import Libraries
import numpy as np

# Define initial conditions for 2 bodies (Sun and Earth)
def initial_conditions(N_bodies):
    """Implement initial conditions of two bodies"""
    pos_and_vel = np.zeros([N_bodies,6])
    G= 1.0
    pos_and_vel[1,0] = 1.0
    pos_and_vel[1,4] = 1.0
    M = np.array([1.0, 3e-6])
    return pos_and_vel,M
