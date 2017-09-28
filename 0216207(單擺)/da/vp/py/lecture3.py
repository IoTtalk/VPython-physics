
g=9.8               #���O�[�t�� 9.8 m/s^2
size = 0.05         #�y�b�| 0.05 m
L = 1.0             #�ӽu�� 1.0m
theta = 60 * pi / 180  #���\�_�l���� = 15 degrees
omega = 0           #�쨤�t�� = 0
init_theta = theta
w = -1;

scene = display(width=1200, height=1000,center = vector(0, -L/2, 0), background=vector(0.5,0.5,0))     #�]�w�e��
#ceiling = box(length=2, height=0.001, width=2, color=color.blue)    #�e�Ѫ��O
ball = sphere(radius = size,  color=color.white)                      #�e�y
string = cylinder(pos=vector(0,0,0), radius=0.003)                           #�e�ӽu�A�@�ݦb(0,0,0)
ball.pos = vector(L * sin(theta), -L*cos(theta), 0)
string.axis = ball.pos - string.pos
dt = 0.001
#scene.bind('mousedown', click_mousedown)
#scene.bind('mouseup', click_mouseup)
#scene.bind('mousemove', drag)

def swing(data):
    #ball = sphere(pos=vector(-24.5, 10.0, 0.0), radius=size, color=color.white)
    global theta
    global ball
    global L
    global dt
    global init_theta
    global w
    global omega
    global ev


    omega += sqrt(g/L)/(1+theta*theta/16)*dt*w
    theta = theta + (omega * dt)
    ball.pos = vector(L * sin(theta), -L*cos(theta), 0)
    string.axis = ball.pos - string.pos
    if w == 1:
        if theta > 0:
            w=-1*w
    elif w==-1:
        if theta < 0:
            w=-1*w
    rate(1000,swing)
rate(1000,swing)

'''def handler(data):
    rate(1,progress)
    global theta
    global omega
    global ball
    if data != None:
        #15
        if data ==1:
            theta = 15 * pi / 180
            omega = 0
            ball.radius = size*1
            ball.color = color.white
        #30
        elif data ==2:
            theta = 30 * pi / 180
            omega = 0
            ball.radius = size*1.5
            ball.color = color.green
        #45
        elif data ==3:
            theta = 45 * pi / 180
            omega = 0
            ball.radius = size*2
            ball.color = color.yellow
        #60
        elif data ==4:
            theta = 60 * pi / 180
            omega = 0
            ball.radius = size*2.5
            ball.color = color.red
        #75
        elif data ==5:
            theta = 75 * pi / 180
            omega = 0
            ball.radius = size*3
            ball.color = color.black
        #90
        elif data ==6:
            theta = 90 * pi / 180
            omega = 0
            ball.radius = size*3.5
            ball.color = color.orange
        #-15
        elif data ==7:
            theta = -15 * pi / 180
            omega = 0
            ball.radius = size*1
            ball.color = color.white
        #-30
        elif data ==8:
            theta = -30 * pi / 180
            omega = 0
            ball.radius = size*1.5
            ball.color = color.green
        #-45
        elif data ==9:
            theta = -45 * pi / 180
            omega = 0
            ball.radius = size*2
            ball.color = color.yellow
        #-60
        elif data ==10:
            theta = -60 * pi / 180
            omega = 0
            ball.radius = size*2.5
            ball.color = color.red
        #-75
        elif data ==0:
            theta = -75 * pi / 180
            omega = 0
            ball.radius = size*3
            ball.color = color.black
        #-90
        elif data ==11:
            theta = -90 * pi / 180
            omega = 0
            ball.radius = size*3.5
            ball.color = color.orange'''

def handler1(data_theta):
    rate(1,progress)
    global theta
    global omega
    global ball
    if data_theta != None:
        theta = (data_theta) * pi / 180
        omega = 0
        ball.radius = size*1
        ball.color = color.white
def progress():
    csmPull(df,handler1)
rate(1000,progress)
#df='control_val'
df='theta'
profile={
    'dm_name':'Simple_Pendulum',
    'df_list':[df]
}

csmRegister(profile)
