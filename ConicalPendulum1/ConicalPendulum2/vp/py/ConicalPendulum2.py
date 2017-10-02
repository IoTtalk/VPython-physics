#from visual import *

# The initial angle in radians.
theta_e = pi/2.0
theta_s = pi/2.0
theta_m = pi/2.0
#console.log("123 ", theta)
# The initial angular velocity
omega_m = 0
omega_e = 0
omega_s = 0

# Set g and the length of the pendulum
###g = 9.80
ge = 9.8
gs = 273.42
gm = 1.568
L = 1.00

# These  four lines control the size of the window of
# the animation and the scale. The details of these lines
# are not important for our purposes.

scene = display(background = vector(0, 0, 0))
#scene.autoscale = 0
scene.height = 600
scene.width = 600
#scene.range = vector(2.0,2.0,2.0)
scene.center = vector(0, 0, 0)
scene.forward = vector(0, 0, 0)
#scene.background = vector(1, 0, 0)

#
# Now we build the pendulum which we will animate.
#

# The ceiling for the pendulum
ceiling = cylinder(pos = vector(0, 0, -0.5), axis = vector(0, 0, 1), radius = 0.02, color = color.cyan)

# The "frame" construct groups two or more objects into a single one.
# Here we group the cylinder and the sphere into a single object
# which is the pendulum.


string_e = cylinder(pos = vector(0, 0, 0), radius = 0.003, length = 1, color = color.white)
ball_e = sphere(pos = vector(1, 0 ,0), radius = 0.05, color = color.cyan)

string_s = cylinder(pos = vector(0, 0, 0), radius = 0.003, length = 1, color = color.white)
ball_s = sphere(pos = vector(1, 0 ,0), radius = 0.05, color = color.magenta)

string_m = cylinder(pos = vector(0, 0, 0), radius = 0.003, length = 1, color = color.white)
ball_m = sphere(pos = vector(1, 0 ,0), radius = 0.05, color = color.yellow)
# Rotate the pendulum about the z axis. Note that VPython measures
# angles with respect to the x (horizontal) axis. We are measuring
# angles with respect to the vertical (-y axis) so we subtract
# pi/2.0 radians from the angle.

string_e.rotate(axis = vector(0, 0, 1), angle = theta_e - pi/2.0)
ball_e.rotate(axis = vector(0, 0, 1), angle = theta_e - pi/2.0)

string_s.rotate(axis = vector(0, 0, 1), angle = theta_s - pi/2.0)
ball_s.rotate(axis = vector(0, 0, 1), angle = theta_s - pi/2.0)

string_m.rotate(axis = vector(0, 0, 1), angle = theta_m - pi/2.0)
ball_m.rotate(axis = vector(0, 0, 1), angle = theta_m - pi/2.0)


# The time
t = 0.

# Below we will want to store the old value of the time.
# Set it the "impossible" value of -1 initially.
t_old = -1.

# The time step
dt = 0.0005
#global theta
#def Rotate(speed):
#console.log("XDD")
def pendulum_rotate(spd):

    lucy()
    
    def lucy():
        if(spd==1) or (spd==2) or (spd==3):
            if (spd == 1):
                dt = (1/-spd)*0.000005
            elif(spd==2):
                ball_e.radius = 0.1
            else:
                ball_e.color = color.white
        elif(spd==4) or (spd==5) or (spd==6):
            if(spd == 4):
                dt = (1/-spd)*0.0005
            elif(spd == 5):
                ball_s.radius = 0.1
            else :
                ball_s.color = color.white
        elif(spd==7) or (spd==8) or (spd==9):
            if(spd == 7):
                dt = (1/-spd)*0.005
            elif(spd == 8):
                ball_m.radius = 0.1
            else :
                ball_m.color = color.white

        global t, dt
        global theta_e, theta_s, theta_m
        global omega_e, omega_s, omega_m
        #rate(500, lucy)
        alpha_e = -(ge/L) * sin(theta_e)
        alpha_s = -(gs/L) * sin(theta_s)
        alpha_m = -(gm/L) * sin(theta_m)
        # The new value of the angular velocity
        omega_e = omega_e + alpha_e * dt
        omega_s = omega_s + alpha_s * dt
        omega_m = omega_m + alpha_m * dt
        # The change in the angle of the pendulum
        d_theta_e = omega_e * dt
        d_theta_s = omega_s * dt
        d_theta_m = omega_m * dt

        # Rotate the pendulum about the z axis by the change in the angle
        string_e.rotate(axis = vector(0,0,1), angle = d_theta_e)
        ball_e.pos = vector(ball_e.pos.x*cos(d_theta_e) - ball_e.pos.y*sin(d_theta_e), 
                           ball_e.pos.y*cos(d_theta_e) + ball_e.pos.x*sin(d_theta_e),
                           0)

        string_s.rotate(axis = vector(0,0,1), angle = d_theta_s)
        ball_s.pos = vector(ball_s.pos.x*cos(d_theta_s) - ball_s.pos.y*sin(d_theta_s), 
                           ball_s.pos.y*cos(d_theta_s) + ball_s.pos.x*sin(d_theta_s),
                           0)

        string_m.rotate(axis = vector(0,0,1), angle = d_theta_m)
        ball_m.pos = vector(ball_m.pos.x*cos(d_theta_m) - ball_m.pos.y*sin(d_theta_m), 
                           ball_m.pos.y*cos(d_theta_m) + ball_m.pos.x*sin(d_theta_m),
                           0)
        
        # Update the value of the angle
        theta_e = theta_e + d_theta_e
        theta_s = theta_s + d_theta_s
        theta_m = theta_m + d_theta_m
        # Update the time
        t = t + dt
        ###console.log("3")

        rate(100, lucy)
    
    

def handler(data):
    rate(1, progress)
    if data!= None:
        pendulum_rotate(data)

def progress():
    #rate(1, handler(5))
    csmPull(df, handler)

rate(1, handler) 

df = 'Command'
profile = {
    'dm_name':'ConicalPendulum2',
    'df_list':[df]
}
csmRegister(profile)
