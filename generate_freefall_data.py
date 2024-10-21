import numpy as np
from astropy.constants import g0


number_of_times = 10
standard_gravity = g0.value
initial_velocity = 0
initial_position = 10

freefall_time = (initial_velocity + np.sqrt(initial_velocity**2+2*standard_gravity*initial_position))/standard_gravity
times = np.linspace(0, freefall_time, number_of_times)

velocities = initial_velocity - standard_gravity * times
positions = initial_position + initial_velocity * times - 0.5 * standard_gravity * times**2

for time, position in zip(times, positions):
    print(time, position)

np.savetxt('freefall_times_positions.txt', np.column_stack((times, positions)), fmt='%7.4f')
