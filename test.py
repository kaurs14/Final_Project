from integrate import rk4, euler
from setup import initial_conditions
import matplotlib.pyplot as plt
#define time reversal function for the integrator
def test_time_reversal(integrator):
    """Implement test_time_reversal function"""
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
        if integrator == "rk4":
            p, v = rk4(p,v,dt,N_bodies,M)
        elif integrator == "euler":
            p, v = euler(p,v,dt,N_bodies,M)
        positions.append(p.copy())
        velocities.append(v.copy())
        times.append(t)
        t += dt
    rev_positions = []
    rev_velocities = []
    while revt >= t0:
        if integrator == "rk4":
            p, v = rk4(p,v,-dt,N_bodies,M)
        elif integrator == "euler":
            p, v = euler(p,v,-dt,N_bodies,M)
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
    plt.savefig("time_reversal_check_{}.jpeg".format(integrator))
    plt.show()
test_time_reversal(integrator ='rk4')
test_time_reversal(integrator = 'euler')
# Other two tests I did whether total energy and total anular momentum of the system conserved.
# Both Plots are in the final_project folder.
