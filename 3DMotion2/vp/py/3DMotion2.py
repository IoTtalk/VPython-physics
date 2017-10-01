#from visual import *
#from visual.graph import *

#  1. 變數設定
size = 0.2                # 球的半徑 0.2 m
g = vector(0,-9.8,0)     # 重力加速度

#  2. 畫面設定 
scene = display(width = 960, height = 600, center = vector(15,0,0), background=(0.5,0.6,0.5))
#gd1 = gdisplay(x = 800, y = 0, title = 't v.s. y', xtitle = 't (s)', ytitle='y (m)', ymax = 10, xmax = 10)
#ty = gcurve(gdisplay = gd1, color = color.yellow)
c1 = curve(color = color.yellow)
c2 = curve(color = color.red)
floor = box(pos=vector(15,-0.05,0), length = 70, height = 1, width=70)

#  3. 初始條件
def balljump(scl):
    global c1, c2, t, dt, ball
    #ball = sphere(radius = size, color = color.blue, make_trail= True)
    #ball.pos = vector(0, size, 0) 
    #ball.v = vector(5, 10, 0)
    c1.visible = False
    c2.visible = False
    c1 = curve(color = color.yellow)
    c2 = curve(color = color.red)
    dt = 0.05
    t = 0
    
    #  4. 物體運動部分
    #while t<5:
    #    rate(1000)
    #    ty.plot( pos = (t, ball.pos.y) )
    #    t += dt
    #    if ball.pos.y <= size:
    #        ball.v.y = abs(ball.v.y)
    #    
    #    ball.pos += ball.v*dt
    #    ball.v += g*dt
    def resetScene():
        scene.background = vector(0.5, 0.6, 0.5)
    def jump():
        global c1, c2, dt, t, ball
        
        if t < 100:
            rate(500, jump)

        #x = 4*sin(2*t+3.1415/16)*2.71828**(-t*0.02)+2*sin(6*t+3*3.1415/2)*2.71828**(-t*0.0315)
        #y = sin(1.002*t+13*3.1415/16)*2.71828*(-t*0.02)+sin(3*t+3.1415)*2.71828**(-t*0.02)
        x = (2+cos(16*t))*cos(t)
        y = (2+cos(16*t))*sin(t)
        z = sin(16*t)
        #c1.append(pos = [vector(3*cos(t)+10, t*0.4, 3*sin(t))], radius = 0.01*scl)
        #c2.append(pos = [vector(x*scl*0.1+15,t*0.2,y*scl*0.1)], radius = cos(t)*sin(t)*0.3)
        c1.append(pos = [vector(2*x,t*0.5+0.5,2*y)], radius = 0.01*scl)
        c2.append(pos = [vector(x*scl*0.1+20,t*scl*0.03+0.5,y*scl*0.1)], radius = 0.1)

        t = t + dt
            

        '''
        if ball.pos.y <= size:
            ball.v.y = abs(ball.v.y)
    
        ball.pos = ball.pos + ball.v*dt
        ball.v = ball.v + g*dt
        '''
    jump()

def handler(data):
    rate(1, progress)
    if data != None:
        balljump(data)

def progress():
    csmPull(df, handler)
    #rate(1, handler)

df = 'Scale'
profile = {
    'dm_name':'3DMotion2',
    'df_list':[df]
}

csmRegister(profile)
rate(1, progress)

