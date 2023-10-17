import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.integrate import ode

S_R = 40 # [cm^2]
g = 981 # [cm/s]
S_S30 = 0 # [cm/s] ! to compute in the lab !

t_0 = 0 # [s]
t_f = 250 # [s]
t_span = (t_0,t_f)
y_0 = np.array([])
 
def model_ODE_non_Linear(t,y,u,v):
    # y : flow rate (q_p) [mL/s]
    # v : disturbance noise
    return u/S_R - (v+S_S30)*np.sqrt(2*g*y)

sol = solve_ivp(model_ODE_non_Linear,t_span,y_0)

# ------------------------------------------------------------------------------------
# PLOTS
# ------------------------------------------------------------------------------------

fig = plt.figure()
fig = plt.plot(sol.t,sol.y)
fig = plt.xlabel("Time [s]")
fig = fig.ylabel("Water level in water tank [m]")