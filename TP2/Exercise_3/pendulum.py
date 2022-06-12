import numpy as np
import matplotlib.pyplot as plt
from scipy import constants

CONSTANT_M = 2  # Car mass
CONSTANT_m = 1  # Pendulum mass
CONSTANT_l = 1  # Pendulum length

theta_set_width = 1/3*np.pi  # rad (60º)
w_set_width = 1  # Correct value(rad/s)
Force_set_width = 200  # (N?)(-10 a 10 segun paper?-50 a 50 o 100 suena mejor)
# +-80º If reaches this point, velocity is made zero.
theta_limit = np.pi/2-10/180*np.pi

# Fuzzy sets (We will use Spanish acronyms)
NG = -2
NP = -1
Z = 0
PP = 1
PG = 2


# Simulating the pendulum car model.
# Parameters:
#   t_max: maximum time (starts in 0)
#   delta_t: time increment in each iteration
#   theta_0: initial angle (degrees)
#   v_0: initial angular velocity (radians/s)
#   a_0: initial angular acceleration (radians/s2)


def simulate(t_max, delta_t, theta_0, w_0):  # a_0 REMOVED from function inputs

    # Step 0: Initial conditions
    # theta_0 must be between +-80º. Make error control for input theta?
    theta = maptheta((theta_0 * np.pi) / 180)
    w = w_0
    # a = a_0 REMOVED. It results from the matematical model
    a = calculate_acceleration(theta, w, 0)  # ADDED

    # Simulate
    y = []
    x = np.arange(0, t_max, delta_t)
    y.append(theta)  # ADDED

    for _ in x:  # REORDERED so every variable depends on previous step
        theta = maptheta(theta + w * delta_t + a * np.power(delta_t, 2) / 2)
        if(theta == theta_limit or theta == -theta_limit):
            w = 0
        else:
            w += a * delta_t

        a = calculate_acceleration(theta, w, control_Force(theta, w))
        y.append(theta)
    x = np.append(x, t_max)  # ADDED

    _, ax = plt.subplots()
    ax.plot(x, y)

    ax.set(xlabel='time (s)', ylabel='theta (rad)',
           title='Delta t = ' + str(delta_t) + " s")
    ax.grid()

    plt.show()


# Compute current acceleration given the current angle and angular velocity, and the force applied

def calculate_acceleration(theta, w, f):
    numerator = constants.g * np.sin(theta) + np.cos(theta) * (
        (-f - CONSTANT_m * CONSTANT_l * np.power(w, 2) * np.sin(theta)) / (CONSTANT_M + CONSTANT_m))
    denominator = CONSTANT_l * \
        (4/3 - (CONSTANT_m * np.power(np.cos(theta), 2) / (CONSTANT_M + CONSTANT_m)))
    return numerator / denominator


def maptheta(theta):
    if theta > theta_limit:
        theta = theta_limit
    elif theta < -theta_limit:
        theta = -theta_limit
    return theta


def mu(value, FS, half_set_width):  # Considering 5 fuzzy sets.
    # half_set_width--> variable set width/2
    # value--> variable's value
    if FS == NP:
        value += half_set_width*np.pi/(180)
    elif FS == PP:
        value -= half_set_width*np.pi/(180)

    if FS == Z or FS == NP or FS == PP:
        if value > half_set_width or value < -half_set_width:
            return 0
        elif value >= 0:
            return 1-value/(half_set_width)
        elif value < 0:
            return 1+value/(half_set_width)
        else:
            print("Unexpected variable value")
    # For NG,PG build a shoulder function
    elif FS == PG:
        if value > 2*half_set_width:
            return 1
        elif value < half_set_width:
            return 0
        else:
            return (value-half_set_width)/(half_set_width)
    elif FS == NG:  # Following is copilot's code untouched
        if value < -2*half_set_width:
            return 1
        elif value > -half_set_width:
            return 0
        else:
            return (value+half_set_width)/(half_set_width)


def control_Force(theta, w):
    F_PG = max(
        min(mu(theta, NG, theta_set_width), mu(w, NG, w_set_width)),
        min(mu(theta, NG, theta_set_width), mu(w, NP, w_set_width)),
        min(mu(theta, NG, theta_set_width), mu(w, Z, w_set_width)),
        min(mu(theta, NP, theta_set_width), mu(w, NG, w_set_width)),
        min(mu(theta, NP, theta_set_width), mu(w, NP, w_set_width)),
        min(mu(theta, Z, theta_set_width), mu(w, NG, w_set_width))
    )
    F_PP = max(
        min(mu(theta, NG, theta_set_width), mu(w, PP, w_set_width)),
        min(mu(theta, NP, theta_set_width), mu(w, Z, w_set_width)),
        min(mu(theta, Z, theta_set_width), mu(w, NP, w_set_width)),
        min(mu(theta, PP, theta_set_width), mu(w, NG, w_set_width)),
    )
    # Commented because its center is zero, then it doesn't add weight to the calculation
    # F_Z=max(
    #  min(mu(theta,NG,theta_set_width),mu(w,PG,w_set_width)),
    #  min(mu(theta,NP,theta_set_width),mu(w,PP,w_set_width)),
    #  min(mu(theta,Z ,theta_set_width),mu(w,Z ,w_set_width)),
    #  min(mu(theta,PP,theta_set_width),mu(w,NP,w_set_width)),
    #  min(mu(theta,PG,theta_set_width),mu(w,NG,w_set_width)),
    # )
    F_NP = max(
        min(mu(theta, NP, theta_set_width), mu(w, PG, w_set_width)),
        min(mu(theta, Z, theta_set_width), mu(w, PP, w_set_width)),
        min(mu(theta, PP, theta_set_width), mu(w, Z, w_set_width)),
        min(mu(theta, PG, theta_set_width), mu(w, NP, w_set_width))
    )
    # Z,PG//PP,PG//PP,PP//PG,PG//PG,PP//PG,Z:
    F_NG = max(
        min(mu(theta, Z, theta_set_width), mu(w, PG, w_set_width)),
        min(mu(theta, PP, theta_set_width), mu(w, PG, w_set_width)),
        min(mu(theta, PP, theta_set_width), mu(w, PP, w_set_width)),
        min(mu(theta, PG, theta_set_width), mu(w, PG, w_set_width)),
        min(mu(theta, PG, theta_set_width), mu(w, PP, w_set_width)),
        min(mu(theta, PG, theta_set_width), mu(w, Z, w_set_width)),
    )

    F = Force_set_width*(F_PG+F_PP/2-F_NP/2-F_NG)
    print(F_PG,F_NG,F_PP,F_NP)
    return F


simulate(10, 0.0001, 45, 0)  # Removed acceleration from function inputs
