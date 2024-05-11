#Import Libraries
import numpy as np
import matplotlib.pyplot as plt


#  Plot bound orbit with two bodies on the xy plane
def plot_orbit_xyplane(positions):
    """Plot bound orbit on the xy plane"""
    fig, ax = plt.subplots(1, 1)

    for ind,pos in enumerate(positions):
        if ind == 0:
            ax.scatter(pos[0,0], pos[0,1], color='green', marker='o', label = "Sun")
            ax.scatter(pos[1,0], pos[1,1], color='red', marker='o', label = "Earth")
        else:
            ax.scatter(pos[0,0], pos[0,1], color='green', marker='o')
            ax.scatter(pos[1,0], pos[1,1], color='red', marker='o')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title("Orbital Plane from the Top")
    plt.savefig("bound_orbit_xy.jpeg")
    plt.show()

#Plot evolution of time VS position in the x direction
def time_evolution_xposition(times,positions):
    """Plot evolution of time VS position in the x direction"""
    fig, ax = plt.subplots(1, 1)
    for ind,pos in enumerate(positions):
        if ind == 0:
           ax.scatter(times[ind], pos[0,0], color='green', marker='o', label = "Sun")
           ax.scatter(times[ind], pos[1,0], color='red', marker='o', label = "Earth")
        else:
           ax.scatter(times[ind], pos[0,0], color='green', marker='o')
           ax.scatter(times[ind], pos[1,0], color='red', marker='o')
    plt.legend()
    plt.xlabel('t')
    plt.ylabel('x')
    plt.title("X_Position VS Time")
    plt.savefig("time_evolution_xposition.jpeg")
    plt.show()

#  Plot bound orbit with two bodies on the xz plane
def plot_orbit_xzplane(positions):
    """Plot orbit on the xz plane"""
    fig, ax = plt.subplots(1, 1)

    for ind,pos in enumerate(positions):
        if ind == 0:
            ax.scatter(pos[0,0], pos[0,2], color='green', marker='o', label = "Sun")
            ax.scatter(pos[1,0], pos[1,2], color='red', marker='o', label = "Earth")
        else:
            ax.scatter(pos[0,0], pos[0,2], color='green', marker='o')
            ax.scatter(pos[1,0], pos[1,2], color='red', marker='o')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('z')
    plt.title("In the Orbital Plane")
    plt.savefig("bound_orbit_xz.jpeg")
    plt.show()

#Plot evolution of time VS position in the y direction
def time_evolution_yposition(times,positions):
    """Plot evolution of time VS position in the y direction"""
    fig, ax = plt.subplots(1, 1)
    for ind,pos in enumerate(positions):
        if ind == 0:
           ax.scatter(times[ind], pos[0,1], color='green', marker='o', label = "Sun")
           ax.scatter(times[ind], pos[1,1], color='red', marker='o', label = "Earth")
        else:
           ax.scatter(times[ind], pos[0,1], color='green', marker='o')
           ax.scatter(times[ind], pos[1,1], color='red', marker='o')
    plt.legend()
    plt.xlabel('t')
    plt.ylabel('y')
    plt.title("Y_Position VS Time")
    plt.savefig("time_evolution_yposition.jpeg")
    plt.show()

# Define new function to plot total energy of the system with time evolution
def plot_energy_time(times,total_E):
    """Plot total energy Vs time of the system"""
    plt.figure()
    plt.plot(times,total_E)
    plt.xlabel('Times')
    plt.ylabel('Total Energy')
    plt.title("Times VS Total Energy")
    plt.savefig("time_vs_total energy.jpeg")
    plt.show()

# Define new function to plot total angular momentum of the system with time evolution
def plot_total_angular_momentum_time(times,total_L):
    """Plot total angular momentum Vs time of the system"""
    plt.figure()
    plt.plot(times,total_L)
    plt.xlabel('Times')
    plt.ylabel('Total Angular Momentum')
    plt.title("Times VS Total Angular Momentum")
    plt.savefig("time_vs_total angular momentum.jpeg")
    plt.show()
