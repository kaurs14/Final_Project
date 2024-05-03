import numpy as np
import matplotlib.pyplot as plt


def plot_orbit_xyplane(positions):
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
    plt.savefig("bound_orbit_xy.jpeg")
    plt.show()

def time_evolution_xposition(times,positions):
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
    plt.savefig("time_evolution_xposition.jpeg")
    plt.show()
