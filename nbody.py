#Import Libraries
import numpy as np
from setup import initial_conditions
import matplotlib.pyplot as plt
from output import plot_orbit_xyplane,time_evolution_xposition, plot_orbit_xzplane,time_evolution_yposition
from integrate import euler, rk4,total_energy,total_angular_momentum
from output import plot_energy_time
from output import plot_total_angular_momentum_time

# Define n_body function to use rk45 and euler integrator for two body problem
def run_Nbody(tend, tframe, dt, N_bodies,integrator):
    """ Implement initial conditions of the n_body"""
    pos_vel,M = initial_conditions(N_bodies=2)
    p = pos_vel[:,0:3]
    v = pos_vel[:,3:6]
    t = 0
    tnext = tframe
    positions = []
    velocities = []
    times = []
    energy =[]
    momentum = []
    while t<tend :
        while t < tnext :
            delta_t = min(tnext-t,dt)
            if integrator=="euler":
                p, v = euler(p,v,delta_t,N_bodies,M)
            elif integrator== "rk4":
                p, v = rk4(p,v,delta_t,N_bodies,M)
            else:
                print("please specify either rk4 or euler only")
                exit()
            t += delta_t
            total_E = total_energy(p,v,N_bodies,M)
            total_L = total_angular_momentum(p,v,N_bodies,M)
        positions.append(p.copy())
        velocities.append(v.copy())
        times.append(tnext)
        energy.append(total_E)
        momentum.append(total_L)

        tnext += tframe
    return positions, velocities, times,energy,momentum

# Define variables to run plots
frames = 100
tframe = 0.25
dt = 0.0001
N_bodies = 2
positions, velocities, times,energy,momentum = run_Nbody(frames*tframe, tframe, dt,N_bodies,integrator = "rk4")

#Excute functions to run plots
plot_orbit_xyplane(positions)
time_evolution_xposition(times,positions)
plot_orbit_xzplane(positions)
time_evolution_yposition(times,positions)
plot_energy_time(times,energy)
plot_total_angular_momentum_time(times,momentum)
