import numpy as np
from setup import initial_conditions
import matplotlib.pyplot as plt
from output import plot_orbit_xyplane,time_evolution_xposition, plot_orbit_xzplane,time_evolution_yposition
from integrate import euler, rk4



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
            if integrator=="euler":
                p, v = euler(p,v,delta_t,N_bodies,M)
            elif integrator== "rk4":
                p, v = rk4(p,v,delta_t,N_bodies,M)
            else:
                print("please specify either rk4 or euler only")
                exit()
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
positions, velocities, times = run_Nbody(frames*tframe, tframe, dt,N_bodies,integrator = "rk4")

plot_orbit_xyplane(positions)
time_evolution_xposition(times,positions)
plot_orbit_xzplane(positions)
time_evolution_yposition(times,positions)
