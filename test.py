from integrate import rk4
from setup import initial_conditions
import matplotlib.pyplot as plt
def test_time_reversal():
    t0 = 0
    dt = 0.1
    t1 = 100
    N_bodies = 2
    pos_vel,M = initial_conditions(N_bodies)
    p = pos_vel[:,0:3]
    v = pos_vel[:,3:6]
    t = t0
    revt = t1
    positions = []
    velocities = []
    times = []
    revtimes = []
    while t <= t1:
        p, v = rk4(p,v,dt,N_bodies,M)
        positions.append(p.copy())
        velocities.append(v.copy())
        times.append(t)
        t += dt
    rev_positions = []
    rev_velocities = []
    while revt >= t0:
        p, v = rk4(p,v,-dt,N_bodies,M)
        rev_positions.append(p.copy())
        rev_velocities.append(v.copy())
        revtimes.append(revt)
        revt -= dt
    fig, ax = plt.subplots(1, 1)

    for ind,pos in enumerate(positions):
        if ind == 0:
            ax.scatter(pos[0,0], pos[0,1], color='cyan', marker='o', label = "Sun")
            ax.scatter(pos[1,0], pos[1,1], color='red', marker='o', label = "Earth")
        else:
            ax.scatter(pos[0,0], pos[0,1], color='cyan', marker='o')
            ax.scatter(pos[1,0], pos[1,1], color='red', marker='o')
    for ind,pos in enumerate(rev_positions):
        if ind == 0:
            ax.scatter(pos[0,0], pos[0,1], color='cyan', marker='o', label = "Sun")
            ax.scatter(pos[1,0], pos[1,1], color='orange', marker='x', label = "Earth_reverse")
        else:
            ax.scatter(pos[0,0], pos[0,1], color='cyan', marker='o')
            ax.scatter(pos[1,0], pos[1,1], color='orange', marker='x')
    plt.legend(loc = 'upper right')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title("Orbital Plane from the Top")
    plt.savefig("time_reversal_check.jpeg")
    plt.show()
test_time_reversal()
