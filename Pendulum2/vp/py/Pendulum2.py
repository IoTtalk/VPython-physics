from visual import *
g=9.8               
size = 0.05         
L = 1.0             
omega = 0           


scene = display(width=1200, height=1000,center = vector(0, -L/2, 0), background=vector(0.8,0.8,0.8))
myscene = display.get_selected()
myscene.lights [0].color = color.gray(0.2)
myscene.ambient = color.gray(0.8)
ceiling = box(length=2, height=0.001, width=2, color=color.blue,visible = True)
ball0 = sphere(radius = size*8,  color=color.yellow,visible = False,pos=vector(0,0.1,0))  
ball = sphere(radius = size*5,  color=color.black,visible = False,pos=vector(0,0,0.5))   
ball1 = sphere(radius = size,  color=color.red)
ball1_2 = sphere(radius = size,  color=color.red, visible = False) 
ball2 = sphere(radius = size,  color=color.blue , visible = False)                 
string1 = cylinder(pos=vector(0,0,0), radius=0.003)
string1_2 = cylinder(pos=vector(0,0,0), radius=0.003, visible = False)                                     
string2 = cylinder(pos=vector(0,0,0), radius=0.003 , visible = False)                                     
vol1 = label(pos=vector(-0.5,0,1), text='START!!',background=vector(0.2,0.2,0.2),height = 20 )
vol2 = label(pos=vector(0.5,0,1), text='START!!',background=vector(0.2,0.2,0.2),height = 20 ,visible = False)

ball3 = sphere(radius = size*0.01,  color=color.yellow,visible = False)
string3 = cylinder(pos=vector(0,0,0),color=color.yellow, radius=0.06,visible = False)
ball3_1 = sphere(radius = size*0.01,  color=color.yellow,visible = False)
string3_1 = cylinder(pos=vector(0,0,0),color=color.yellow, radius=0.06,visible = False)
ball3_2 = sphere(radius = size*0.01,  color=color.yellow,visible = False)
string3_2 = cylinder(pos=vector(0,0,0),color=color.yellow, radius=0.06,visible = False)
ball3_3 = sphere(radius = size*0.01,  color=color.yellow,visible = False)
string3_3 = cylinder(pos=vector(0,0,0),color=color.yellow, radius=0.06,visible = False)
ball3_4 = sphere(radius = size*0.01,  color=color.yellow,visible = False)
string3_4 = cylinder(pos=vector(0,0,0),color=color.yellow, radius=0.06,visible = False)
ball3_5 = sphere(radius = size*0.01,  color=color.yellow,visible = False)
string3_5 = cylinder(pos=vector(0,0,0),color=color.yellow, radius=0.06,visible = False)
ball31 = sphere(radius = size*0.01,  color=color.yellow,visible = False)
string31 = cylinder(pos=vector(0,0,0),color=color.yellow, radius=0.06,visible = False)
ball3_11 = sphere(radius = size*0.01,  color=color.yellow,visible = False)
string3_11 = cylinder(pos=vector(0,0,0),color=color.yellow, radius=0.06,visible = False)
ball3_21 = sphere(radius = size*0.01,  color=color.yellow,visible = False)
string3_21 = cylinder(pos=vector(0,0,0),color=color.yellow, radius=0.06,visible = False)
ball3_31 = sphere(radius = size*0.01,  color=color.yellow,visible = False)
string3_31 = cylinder(pos=vector(0,0,0),color=color.yellow, radius=0.06,visible = False)
ball3_41 = sphere(radius = size*0.01,  color=color.yellow,visible = False)
string3_41 = cylinder(pos=vector(0,0,0),color=color.yellow, radius=0.06,visible = False)
ball3_51 = sphere(radius = size*0.01,  color=color.yellow,visible = False)
string3_51 = cylinder(pos=vector(0,0,0),color=color.yellow, radius=0.06,visible = False)

vol3 = label(pos=vector(-0.5,0,-1), text='START!!',background=vector(0.2,0.2,0.2),height = 20 ,visible = False)

v1 = 0.001  
a1 = 0
theta1 = 0
v2 = 0.002  
a2 = 0
theta2 = 90 * 3.14 / 180
dt = 0.0001
flag = 0
v3 = 0.00001
theta3 = 0
x = 0

def single():
    global theta1,v1,a1,theta2,v2,a2,dt,v3,theta3,x
    rate(1000,single)
    
    a1 = a1 - v1*dt*100    
    v1 = v1 + a1*dt
    theta1 = theta1 + v1 
    ball1.pos = vector(L * sin(theta1)*0.7, -L*cos(theta1)*0.7, 0)
    string1.axis = ball1.pos - string1.pos
    ball1_2.pos = vector(L * -sin(theta1)*0.7, -L*cos(theta1)*0.7, 0)
    string1_2.axis = ball1_2.pos - string1_2.pos
    v2 = v2 + a2*dt
    theta2 = theta2 + v2
    ball2.pos = vector(L * sin(theta2) * 1.2, -L*cos(theta2)*1.2, 0)
    string2.axis = ball2.pos - string2.pos
    vol1.text='v =  ' + str(int(10000*v1)) + '\n a = ' + str(int(1000*a1)) + '\n theta = ' + str(abs(int(theta1*180/3.14 % 360)))
    vol2.text='v =  ' + str(int(10000*v2)) + '\n a = ' + str(int(1000*a2)) + '\n theta = ' + str(abs(int(theta2*180/3.14 % 360)))
    
    
    temp0 = theta3*180/3.14 % 360
    if((temp0 <=60 and temp0 >= 0)or(temp0 >= 120 and temp0 <= 180)or(temp0 >= 240 and temp0 <= 300)):
        string3.color = vector(0,0,0) 
        string3_1.color = color.yellow 
        string3_2.color = vector(0,0,0) 
        string3_3.color = color.yellow
        string3_4.color = vector(0,0,0) 
        string3_5.color = color.yellow
    else:
        string3.color = color.yellow
        string3_1.color = vector(0,0,0)
        string3_2.color = color.yellow
        string3_3.color = vector(0,0,0)
        string3_4.color = color.yellow
        string3_5.color = vector(0,0,0)
        
    temp1 = (theta3+30)*180/3.14 % 360
    if((temp1 <=60 and temp1 >= 0)or(temp1 >= 120 and temp1 <= 180)or(temp1 >= 240 and temp1 <= 300)):
        string31.color = vector(0,0,0) 
        string3_11.color = color.yellow 
        string3_21.color = vector(0,0,0) 
        string3_31.color = color.yellow
        string3_41.color = vector(0,0,0) 
        string3_51.color = color.yellow 
    else:
        string31.color = color.yellow
        string3_11.color = vector(0,0,0)
        string3_21.color = color.yellow
        string3_31.color = vector(0,0,0)
        string3_41.color = color.yellow
        string3_51.color = vector(0,0,0)
    theta3 = theta3 + v3
    ball3.pos = vector(L * sin(theta3) * 1.2, -L*cos(theta3)*1.2, 0)
    string3.axis = ball3.pos - string3.pos
    ball3_1.pos = vector(L * sin(theta3+ 60 * 3.14 / 180) * 1.2, -L*cos(theta3+60 * 3.14 / 180)*1.2, 0)
    string3_1.axis = ball3_1.pos - string3_1.pos
    ball3_2.pos = vector(L * sin(theta3+ 120 * 3.14 / 180) * 1.2, -L*cos(theta3+120 * 3.14 / 180)*1.2, 0)
    string3_2.axis = ball3_2.pos - string3_2.pos
    ball3_3.pos = vector(L * sin(theta3+ 180 * 3.14 / 180) * 1.2, -L*cos(theta3+180 * 3.14 / 180)*1.2, 0)
    string3_3.axis = ball3_3.pos - string3_3.pos
    ball3_4.pos = vector(L * sin(theta3+ 240 * 3.14 / 180) * 1.2, -L*cos(theta3+240 * 3.14 / 180)*1.2, 0)
    string3_4.axis = ball3_4.pos - string3_4.pos
    ball3_5.pos = vector(L * sin(theta3+ 300 * 3.14 / 180) * 1.2, -L*cos(theta3+300 * 3.14 / 180)*1.2, 0)
    string3_5.axis = ball3_5.pos - string3_5.pos
    ball31.pos = vector(L * sin(theta3+ 30 * 3.14 / 180) * 1.2, -L*cos(theta3+ 30 * 3.14 / 180)*1.2, 0)
    string31.axis = ball31.pos - string31.pos
    ball3_11.pos = vector(L * sin(theta3+ 90 * 3.14 / 180) * 1.2, -L*cos(theta3+90  * 3.14 / 180)*1.2, 0)
    string3_11.axis = ball3_11.pos - string3_11.pos
    ball3_21.pos = vector(L * sin(theta3+ 150 * 3.14 / 180) * 1.2, -L*cos(theta3+150 * 3.14 / 180)*1.2, 0)
    string3_21.axis = ball3_21.pos - string3_21.pos
    ball3_31.pos = vector(L * sin(theta3+ 210 * 3.14 / 180) * 1.2, -L*cos(theta3+210 * 3.14 / 180)*1.2, 0)
    string3_31.axis = ball3_31.pos - string3_31.pos
    ball3_41.pos = vector(L * sin(theta3+ 270 * 3.14 / 180) * 1.2, -L*cos(theta3+270 * 3.14 / 180)*1.2, 0)
    string3_41.axis = ball3_41.pos - string3_41.pos
    ball3_51.pos = vector(L * sin(theta3+ 330 * 3.14 / 180) * 1.2, -L*cos(theta3+330 * 3.14 / 180)*1.2, 0)
    string3_51.axis = ball3_51.pos - string3_51.pos
    
    vol3.text='v =  ' + str(int(10000*v3)) + '\n theta = ' + str(abs(int(theta3*180/3.14 % 360)))

    
def speed(data):
    global v1,a1,v2,a2,theta1,v3
    data = int(data)
    
    if(data == 0):
        v1 = 0.001  
        a1 = 0
        theta1 = 0
        v2 = 0.002  
        a2 = 0
        vol1.visible = True
        ball1.visible = True
        vol2.visible = False
        ball2.visible = False
        string2.visible = False
        ball1_2.visible = False
        string1_2.visible = False
        ball0.visible = False
        ball.visible = False
        ball3.visible = False
        string3.visible = False
        ball3_1.visible = False
        string3_1.visible = False
        ball3_2.visible = False
        string3_2.visible = False
        ball3_3.visible = False
        string3_3.visible = False
        ball3_3.visible = False
        string3_3.visible = False
        ball3_4.visible = False
        string3_4.visible = False
        ball3_5.visible = False
        string3_5.visible = False
        ball31.visible = False
        string31.visible = False
        ball3_11.visible = False
        string3_11.visible = False
        ball3_21.visible = False
        string3_21.visible = False
        ball3_31.visible = False
        string3_31.visible = False
        ball3_31.visible = False
        string3_31.visible = False
        ball3_41.visible = False
        string3_41.visible = False
        ball3_51.visible = False
        string3_51.visible = False
        ceiling.visible =True
    elif(data == 1):
        v1 += 0.001
    elif(data == 2):
        v1 -= 0.001  
    elif(data == 3):
        ball2.visible = True
        string2.visible = True
        vol2.visible = True
    elif(data == 4):
        v2 *= 2
    elif(data == 5):
        v2 /= 2
    elif(data == 6):
        a2 += 0.005
    elif(data == 7):
        a2 -= 0.005
    elif(data == 8):
        ball1_2.visible = True
        string1_2.visible = True
    elif(data == 9):
        vol1.visible = False
        ball1.visible = False
        vol2.visible = False
        ball2.visible = False
        string2.visible = False
        ball1_2.visible = False
        string1_2.visible = False
        ball0.visible = True
        ball.visible = True
        ball3.visible = True
        string3.visible = True
        ball3_1.visible = True
        string3_1.visible = True
        ball3_2.visible = True
        string3_2.visible = True
        ball3_3.visible = True
        string3_3.visible = True
        ball3_3.visible = True
        string3_3.visible = True
        ball3_4.visible = True
        string3_4.visible = True
        ball3_5.visible = True
        string3_5.visible = True
        ball31.visible = True
        string31.visible = True
        ball3_11.visible = True
        string3_11.visible = True
        ball3_21.visible = True
        string3_21.visible = True
        ball3_31.visible = True
        string3_31.visible = True
        ball3_31.visible = True
        string3_31.visible = True
        ball3_41.visible = True
        string3_41.visible = True
        ball3_51.visible = True
        string3_51.visible = True
        ceiling.visible = False
    elif(data == 10):
        v3 = v3*2
    elif(data == 11):
        v3 = v3 /2

def handler(data):
    global v1,a1,theta1,v2,a2,flag
    rate(1,progress)
    if data != None:
        speed(data)
        if(flag == 0):
            v1 = 0.001  
            a1 = 0
            theta1 = 0
            v2 = 0.002  
            a2 = 0
            vol1.visible = True
            ball1.visible = True
            vol2.visible = False
            ball2.visible = False
            string2.visible = False
            ball1_2.visible = False
            string1_2.visible = False
            ball0.visible = False
            ball.visible = False
            ball3.visible = False
            string3.visible = False
            ball3_1.visible = False
            string3_1.visible = False
            ball3_2.visible = False
            string3_2.visible = False
            ball3_3.visible = False
            string3_3.visible = False
            ball3_3.visible = False
            string3_3.visible = False
            ball3_4.visible = False
            string3_4.visible = False
            ball3_5.visible = False
            string3_5.visible = False
            ball31.visible = False
            string31.visible = False
            ball3_11.visible = False
            string3_11.visible = False
            ball3_21.visible = False
            string3_21.visible = False
            ball3_31.visible = False
            string3_31.visible = False
            ball3_31.visible = False
            string3_31.visible = False
            ball3_41.visible = False
            string3_41.visible = False
            ball3_51.visible = False
            string3_51.visible = False
            ceiling.visible =True
            flag = 1
def progress():
    csmPull(df,handler)

rate(1,single)

df='Command'
profile={
    'dm_name':'Pendulum2',
    'df_list':[df]
}
csmRegister(profile)
rate(1,progress)





