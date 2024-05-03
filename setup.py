import numpy as np

def initial_conditions(N_bodies):
    pos_and_vel = np.zeros([N_bodies,6])
    G= 1.0
    pos_and_vel[1,0] = 1.0
    pos_and_vel[1,4] = 1.0
    M = np.array([1.0, 3e-6])
    return pos_and_vel,M
