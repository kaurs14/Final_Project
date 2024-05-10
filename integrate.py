import numpy as np
import matplotlib.pyplot as plt

#Apply rk45 integrator"""
def rk4(p,v,delta_t,N_bodies,M):
    """Implement rk4 integrator"""

    k1p, k1v = Nbody_derivatives(p, v, N_bodies, M)
    k2p, k2v = Nbody_derivatives(p+k1p*0.5*delta_t, v+k1v*0.5*delta_t, N_bodies, M)
    k3p, k3v = Nbody_derivatives(p+k2p*0.5*delta_t, v+k2v*0.5*delta_t, N_bodies, M)
    k4p, k4v = Nbody_derivatives(p+k3p*delta_t, v+k3v*delta_t, N_bodies, M)
    return p+delta_t*(k1p+2*(k2p+k3p)+k4p)/6, v+delta_t*(k1v+2*(k2v+k3v)+k4v)/6

#Apply Euler integrator
def euler(p,v,delta_t,N_bodies,M):
    """Implement euler integrator"""
    dpdt, dvdt = Nbody_derivatives(p, v, N_bodies, M)
    p, v = p + dpdt*delta_t, v + dvdt*delta_t
    return p, v

#  Given Nbody_derivatives helps to calculate acceleration and velocity
def Nbody_derivatives(pos, vel, N_bodies,M):
    """Implement acceleration and velocity of two bodies"""
    dpdt = vel
    G = 1.0
    dvdt = np.zeros(vel.shape)
    r = np.linalg.norm( pos[1,:]-pos[0,:])
    rhat = (pos[1,:] - pos[0,:])/r
    dvdt[0,:]= G*M[1]/(r*r)*rhat
    dvdt[1,:]= -G*M[0]/(r*r)*rhat
    return dpdt, dvdt

def total_energy(pos,vel,N_bodies,M):
    """calculate total energy of the system"""
    G = 1.0
    r = np.linalg.norm( pos[1,:]-pos[0,:])
    total_KE = 0.5*M[0]*np.sum(vel[0]**2) + 0.5*M[1]*np.sum(vel[1]**2)
    total_PE = -G*M[0]*M[1]/r
    total_E = total_KE +total_PE
    return total_E

def total_angular_momentum(pos,vel,N_bodies,M):
    """calculate total angular momentum of the system"""
    r_vec = pos[1,:]-pos[0,:]
    v_vec = vel[1,:]-vel[0,:]
    total_L = M[1]*np.cross(v_vec,r_vec)
    return np.linalg.norm(total_L)
