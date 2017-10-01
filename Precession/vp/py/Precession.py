###parameter

g = 9.8
M, R, w = 0.5, 0.10, 0.05
I = 0.5 * M * R ** 2
l,r = 0.12, 0.005
theta = 70 * pi/180.0
Omega = 10*2*pi*vector(cos(theta),sin(theta),0)
lr = 0.045
dt=0.01

###background
scene = display(width = 1000,height = 1000,range = 0.6,background = vector(0.5,0.5,0))
base = cone(pos=vector(0,-0.2,0),axis=vector(0,0.2,0),color=color.blue,radius=0.1,texture=textures.earth)

shaft = cylinder(pos=vector(0,0,0),axis=vector(0,l*sin(theta),l*cos(theta)),radius=r,length=l,texture=textures.wood)
disk = cylinder(pos=vector(0,(lr-w/2)*sin(theta),(lr-w/2)*cos(theta)),axis=vector(w*cos(theta),w*sin(theta),0),radius=R,texture=textures.wood)
pointer = arrow(pos=vector(0,0,0), axis=vector(0,0.05,0), shaftwidth=0.0001)

disk_len = disk.length
alpha = 0.0
label1 = label( pos=vec(0,0.2,0), text='M= '+M )
label3 = label( pos=vec(0,0.3,0), text='speed= '+mag(Omega) )
label4 = label( pos=vec(0,0.35,0), text= 'procession= Mgr/Iw')
label2 = label( pos=vec(0,0.25,0), text='procession= ' )

def main():
    global disk_len,alpha,Omega,procession,shaft,disk,M
    procession = M * g * lr / I / mag(Omega)
    label2.text='procession= '+procession
    delta_angle = mag(Omega) * dt
    
    if alpha >= 2*pi:
        alpha=0
    else:
        alpha += procession*dt*10
    Omega_temp = vector(l*cos(theta)*sin(alpha),l*sin(theta),l*cos(theta)*cos(alpha))
    Omega.axis = mag(Omega)*hat(Omega_temp)
    shaft.axis = l*hat(Omega_temp)
    shaft.rotate(angle = delta_angle, axis = hat(Omega_temp))
    disk.pos = (lr-w/2)*hat(Omega_temp)
    disk.axis = w*hat(Omega_temp)
    disk.rotate(angle = delta_angle, axis = hat(Omega_temp))
def handler(data):
    rate(50,progress)
    global Omega,theta,M,R,I,w
    label3.text='speed= '+mag(Omega)
    main()

    if data!=None:
        if data!=0:
            Omega= data*2*pi*vector(cos(theta),sin(theta),0)
        else:
            if M<10:
                M+=0.5
                I = 0.5 * M * R ** 2
                w+=0.01
            else:
                M=0.5
                I = 0.5 * M * R ** 2
                w=0.05
            label1.text='M= '+M


def progress():
    csmPull('Speed',handler)


profile = {
    'dm_name':'Precession',
    'df_list':['Speed']
    }

csmRegister(profile)

rate(50,progress)
