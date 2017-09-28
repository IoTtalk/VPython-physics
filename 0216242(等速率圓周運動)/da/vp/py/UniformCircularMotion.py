scene = display(width=1000, height=1000, background=vector(0.5,0.6,0.5))
table = cylinder(pos=vector(0,-0.03,0), axis=vector(0,-0.01,0), radius=0.7)
center = cylinder(pos=vector(0, -0.03, 0), axis = vector(0, 0.03, 0), radius = 0.007)

a_arrow = arrow(shaftwidth = 0.01,color = color.red)
v_arrow = arrow(shaftwidth = 0.01,color = color.yellow)
a_label = label(text='a',height=15,opacity=0,box=False)
v_label = label(text='v',height=15,opacity=0,box=False)

ball = sphere(pos=vector(-0.5,0,0), radius=0.03, color=color.blue)
r = sqrt(ball.pos.x*ball.pos.x + ball.pos.y*ball.pos.y + ball.pos.z*ball.pos.z)
ball.v = vector(0, 0, 0.5)
period = 2*pi*r/ sqrt(ball.v.x**2+ball.v.y**2+ball.v.z**2)
dt = 0.001
w = 2*pi/period
w1 = w
def change(time):
    global w1
    global ball
    ball.pos=vector(-0.5,0,0)
    ball.v = vector(0, 0, 0.5)
    w1 = w *sqrt(time)

def Basic():
    global ball
    ball.pos=vector(-0.5,0,0)
    ball.v = vector(0, 0, 0.5)
    def run():
        global ball
        global w1
        ball.a = vector(-(ball.pos.x)*w1*w1*cos(w1*dt),0,-(ball.pos.z)*w1*w1*cos(w1*dt))
        ball.v.x +=ball.a.x*dt
        ball.v.y +=ball.a.y*dt
        ball.v.z +=ball.a.z*dt
        ball.pos.x += ball.v.x*dt
        ball.pos.y += ball.v.y*dt
        ball.pos.z += ball.v.z*dt
        a_arrow.pos=ball.pos
        a_arrow.axis=vector(ball.a.x/3,ball.a.y/3,ball.a.z/3)
        v_arrow.pos=ball.pos
        v_arrow.axis=vector(ball.v.x/3,ball.v.y/3,ball.v.z/3)
        a_label.pos.x=a_arrow.pos.x+a_arrow.axis.x*1.2
        a_label.pos.y=a_arrow.pos.y+a_arrow.axis.y*1.2
        a_label.pos.z=a_arrow.pos.z+a_arrow.axis.z*1.2
        v_label.pos.x=v_arrow.pos.x+v_arrow.axis.x*1.2
        v_label.pos.y=v_arrow.pos.y+v_arrow.axis.y*1.2
        v_label.pos.z=v_arrow.pos.z+v_arrow.axis.z*1.2
        
        rate(1000,run)
    new1=0
    run()
    
'''
def Hourglass():
    ball1 = sphere(pos=vector(-0.5,0,0), radius=0.03, color=color.blue)
    ball2 = sphere(pos=vector(-0.5,0.06,0), radius=0.03, color=color.blue)
    ball3 = sphere(pos=vector(-0.5,0.12,0), radius=0.03, color=color.blue)
    ball4 = sphere(pos=vector(-0.5,0.18,0), radius=0.03, color=color.blue)
    ball5 = sphere(pos=vector(-0.5,0.24,0), radius=0.03, color=color.blue)
    ball6 = sphere(pos=vector(-0.5,0.30,0), radius=0.03, color=color.blue)
    ball1.v = vector(0, 0, 0.5)
    ball2.v = vector(0, 0, 0.5)
    ball3.v = vector(0, 0, 0.5)
    ball4.v = vector(0, 0, 0.5)
    ball5.v = vector(0, 0, 0.5)
    ball6.v = vector(0, 0, 0.5)
    r = 0.5
    period = 2*pi
    w = 20*pi/period
    dt = 0.001 
    #omega=omega*w
    def run():
        ball1.a = vector(-(ball1.pos.x)*w*w*cos(w*dt),0,-(ball1.pos.z)*w*w*cos(w*dt))
        ball1.v.x +=ball1.a.x*dt
        ball1.v.y +=ball1.a.y*dt
        ball1.v.z +=ball1.a.z*dt
        ball1.pos.x += ball1.v.x*dt
        ball1.pos.y += ball1.v.y*dt
        ball1.pos.z += ball1.v.z*dt

        ball2.a = vector(-(ball2.pos.x)*w*w*cos(w*dt),0,-(ball2.pos.z)*w*w*cos(w*dt))
        ball2.v.x +=ball2.a.x*dt
        ball2.v.y +=ball2.a.y*dt
        ball2.v.z +=ball2.a.z*dt
        ball2.pos.x += ball2.v.x*dt
        ball2.pos.y += ball2.v.y*dt
        ball2.pos.z += ball2.v.z*dt

        ball3.a = vector(-(ball3.pos.x)*w*w*cos(w*dt),0,-(ball3.pos.z)*w*w*cos(w*dt))
        ball3.v.x +=ball3.a.x*dt
        ball3.v.y +=ball3.a.y*dt
        ball3.v.z +=ball3.a.z*dt
        ball3.pos.x += ball3.v.x*dt
        ball3.pos.y += ball3.v.y*dt
        ball3.pos.z += ball3.v.z*dt
        
        ball4.a = vector(-(ball1.pos.x)*w*w*cos(w*dt),0,-(ball1.pos.z)*w*w*cos(w*dt))
        ball4.v.x +=ball4.a.x*dt
        ball4.v.y +=ball4.a.y*dt
        ball4.v.z +=ball4.a.z*dt
        ball4.pos.x += ball4.v.x*dt
        ball4.pos.y += ball4.v.y*dt
        ball4.pos.z += ball4.v.z*dt

        ball5.a = vector(-(ball1.pos.x)*w*w*cos(w*dt),0,-(ball1.pos.z)*w*w*cos(w*dt))
        ball5.v.x +=ball5.a.x*dt
        ball5.v.y +=ball5.a.y*dt
        ball5.v.z +=ball5.a.z*dt
        ball5.pos.x += ball5.v.x*dt
        ball5.pos.y += ball5.v.y*dt
        ball5.pos.z += ball5.v.z*dt

        ball6.a = vector(-(ball1.pos.x)*w*w*cos(w*dt),0,-(ball1.pos.z)*w*w*cos(w*dt))
        ball6.v.x +=ball6.a.x*dt
        ball6.v.y +=ball6.a.y*dt
        ball6.v.z +=ball6.a.z*dt
        ball6.pos.x += ball6.v.x*dt
        ball6.pos.y += ball6.v.y*dt
        ball6.pos.z += ball6.v.z*dt
        rate(1000,run)    
    run()
'''
def handler(data):
    rate(1,progress)
    if data!=None:
        change(data)
 
def progress():
    csmPull(df, handler)


df = 'Omega'
profile = {
    'dm_name':'UniformCircularMotion',
    'df_list':[df]
}

csmRegister(profile)
rate(1,Basic)
rate(1,progress)
