import numpy as np
from setup import initial_conditions
import matplotlib.pyplot as plt
from output import plot_orbit_xyplane,time_evolution_xposition
from integrate import rk1

def Nbody_derivatives(pos, vel, N_bodies,M):
# given N bodies, implement the force equations as stated above.
    dpdt = vel
    G = 1.0
    dvdt = np.zeros(vel.shape)
    r = np.linalg.norm( pos[1,:]-pos[0,:])
    rhat = (pos[1,:] - pos[0,:])/r
    dvdt[0,:]= G*M[1]/(r*r)*rhat
    dvdt[1,:]= -G*M[0]/(r*r)*rhat
    return dpdt, dvdt

def run_Nbody(tend, tframe, dt, N_bodies,integrator):
    pos_vel,M = initial_conditions(N_bodies=2)
    p = pos_vel[:,0:3]
    v = pos_vel[:,3:6]
    t = 0
    tnext = tframe
    positions = []
    velocities = []
    times = []
    while t<tend :
        while t < tnext :
            # compute using rk2
            delta_t = min(tnext-t,dt)
            if integrator=="simple":
                dpdt, dvdt = Nbody_derivatives(p, v, N_bodies, M)
                p, v = rk1(p,v,delta_t,dpdt,dvdt)
            t += delta_t
        positions.append(p.copy())
        velocities.append(v.copy())
        times.append(tnext)
        tnext += tframe
    return positions, velocities, times

frames = 100
tframe = 0.25
dt = 0.0001
N_bodies = 2
positions, velocities, times = run_Nbody(frames*tframe, tframe, dt,N_bodies,integrator = "simple")

plot_orbit_xyplane(positions)
time_evolution_xposition(times,positions)
