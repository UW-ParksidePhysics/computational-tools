from vpython import *

from generate_freefall_data import initial_position

# Set simulation parameters
initial_angle = pi/6
initial_speed = 10
initial_velocity = initial_speed * vector(cos(initial_angle), sin(initial_angle), 0)
gravitational_acceleration = vector(0, -10, 0)
time_step = 0.005
initial_position = vector(-2, 0, 0)

# Create a 3D scene
scene = canvas(title="VPython in Jupyter Notebook",
               width=600, height=400,
               center=vector(0,0,0), background=color.white)

# Add objects to the scene
ball = sphere(pos=vector(0,0,0), radius=0.5, color=color.red)
floor = box(pos=vector(0,-0.5,0), size=vector(4,0.1,4), color=color.blue)

ball.velocity = initial_velocity
ball.pos = initial_position

# Animation loop
while True:
    rate(50)  # Controls the frame rate (50 updates per second)
    ball.velocity += gravitational_acceleration * time_step
    ball.pos += ball.velocity * time_step  # Move the ball
    if ball.pos.y < 0:  # Reset when it goes too far
        break
