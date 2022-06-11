import numpy as np
import matplotlib.pyplot as plt
from scipy import constants

CONSTANT_M = 2  # Car mass
CONSTANT_m = 1  # Pendulum mass
CONSTANT_l = 1  # Pendulum length

theta_set_width = 2/3*np.pi #rad (120º)

#Fuzzy sets (We will use Spanish acronyms)
NG=-2
NP=-1
Z=0
PP=1
PG=2



# Simulating the pendulum car model.
# Parameters:
#   t_max: maximum time (starts in 0)
#   delta_t: time increment in each iteration
#   theta_0: initial angle (degrees)
#   v_0: initial angular velocity (radians/s)
#   a_0: initial angular acceleration (radians/s2)


def simulate(t_max, delta_t, theta_0, v_0):  # a_0 REMOVED from function inputs
    # Step 0: Initial conditions
    theta =maptheta((theta_0 * np.pi) / 180)
    v = v_0
    # a = a_0 REMOVED. It results from the matematical model
    a = calculate_acceleration(theta, v, 0)  # ADDED

    # Simulate
    y = []
    x = np.arange(0, t_max, delta_t)
    y.append(theta)  # ADDED

    for _ in x:  # REORDERED so every variable depends on previous step
        theta = maptheta(theta + v * delta_t + a * np.power(delta_t, 2) / 2)
        v = v + a * delta_t
        a = calculate_acceleration(theta, v, 0)
        y.append(theta)
    x = np.append(x, t_max)  # ADDED

    _, ax = plt.subplots()
    ax.plot(x, y)

    ax.set(xlabel='time (s)', ylabel='theta (rad)',
           title='Delta t = ' + str(delta_t) + " s")
    ax.grid()

    plt.show()


# Compute current acceleration given the current angle and angular velocity, and the force applied

def calculate_acceleration(theta, v, f):
    numerator = constants.g * np.sin(theta) + np.cos(theta) * (
        (-f - CONSTANT_m * CONSTANT_l * np.power(v, 2) * np.sin(theta)) / (CONSTANT_M + CONSTANT_m))
    denominator = CONSTANT_l * \
        (4/3 - (CONSTANT_m * np.power(np.cos(theta), 2) / (CONSTANT_M + CONSTANT_m)))
    return numerator / denominator

def maptheta(theta):
    if theta > np.pi:  # Thanks Copilot
        theta = theta-2*np.pi
    elif theta < -np.pi:
        theta = theta+2*np.pi
    return theta

def mu_T(theta, FS):
  #For NP and PP sum or rest 60º*pi/180 from theta
  #For NG,PG build a shoulder function
  if FS==Z:
    if theta>theta_set_width/2 or theta<-theta_set_width/2:
      return 0
    elif theta>0:
      return 1-theta/(theta_set_width/2)
    elif theta<0:
      return 1+theta/(theta_set_width/2)
    else:
      print("Unexpected theta value")
#For velocity and Force use different ***_set_width and input variable name



simulate(10, 0.0001, 45, 0)  # Removed acceleration from function inputs
