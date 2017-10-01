#from visual import *

g = 9.8         # g = 9.8 m/s^2
size = 0.5     # ball radius = 0.25 m
height = 25.0   # ball center initial height = 15 m

# open a window
scene = display(width=800, height=800, center=vector(0,height/2, 0), background=vector(0.5, 0.5, 0.5))
# the floor
floor = box(length=30, height=0.01, width=10, color=color.blue)

h = Math.random()*6 + 6
r = Math.random()*1.5 + 1
s = Math.random()*3 + 3
pillar = box(pos=vector(10, h/2, 0), length=0.2, height=h, width=0.2, color=color.white, visible=False)
board = box(pos=vector(9.9, h, 0), length=0.2, height=s, width=s, color=color.white, visible=False)
basket = ring(pos=vector(9.8-r, h, 0), axis=vector(0,1,0), radius=r, thickness=0.1, color=color.red, visible=False)
value = label(pos=vector(-10, 0, 0), text=' Angle: ?\nSpeed: ?', height=20, border=10)

def Basketball():
    pillar.visible = True
    board.visible = True
    basket.visible = True
    
    h = Math.random()*6 + 6
    r = Math.random()*1.5 + 1
    s = Math.random()*3 + 3
    pillar.pos = vector(10, h/2, 0)
    pillar.height = h
    board.pos = pos=vector(9.9, h, 0)
    board.height = s
    board.width = s
    basket.pos = vector(9.8-r, h, 0)
    basket.radius = r

def FreeFall(angle):

    #ball.pos = vector(0, spd, 0)     # ball center initial position
    ball = sphere(pos=vector(-10, 0, 0), radius=size, color=color.white, texture=textures.earth)
    v = int(Math.random()*15) + 10
    ball.v = vector(0, 0, 0)
    ball.v.y = v * sin(pi/180*angle*10)          # ball initial velocity
    ball.v.x = v * cos(pi/180*angle*10)          # ball initial velocity
    value.text = ' Angle: '+ str(angle*10) + '\nSpeed: ' + str(v)
    dt = 0.001                  # time step
    ball.life = 0
    text = label(pos=vector(0, 20, 0), text='Excellent!!', height=50, border=10, visible = False)
    text.life = 0
    
    def Fall():
        rate(2000, Fall)
        if (ball.pos.y <= size and ball.v.y == 0) or ball.pos.x > 15 or ball.pos.x < -15 or ball.pos.y < -1 or ball.life > 4:
            ball.visible = False
            del ball
        elif ball.pos.y <= size and ball.v.y < 0:
            ball.v.y = -ball.v.y
            ball.life = ball.life + 1
        elif basket.visible and abs(ball.pos.x - board.pos.x) <= size and abs(ball.pos.y - board.pos.y) <= s/2:
            ball.v.x = -ball.v.x
            ball.life = ball.life + 1
        elif basket.visible and not text.visible and abs(ball.pos.y - basket.pos.y) <= size and abs(ball.pos.x - basket.pos.x) <= r-size:
            text.text='Excellent!!'
            text.visible = True
        elif basket.visible and not text.visible and abs(ball.pos.y - basket.pos.y) <= size and abs(ball.pos.x - basket.pos.x) <= r+size:
            text.text = 'Nice!'
            text.visible = True
        if text.visible:
            text.life = text.life + 0.001
            if text.life > 1:
                text.visible = False
                text.life = 0
        ball.pos = ball.pos + ball.v * dt
        ball.v.y = ball.v.y - g * dt
    Fall()

def handler(data):
    rate(1, progress)
    if data != None: # GettingFreeFall(data)control(data)
        if data == 0:
            Basketball()
        else:
            FreeFall(data)

def progress():
    #rate(1, handler(5))
    csmPull(df, handler)    #pull data

df = 'Height'
profile = {
    'dm_name': 'ProjectileMotion1',
    'df_list': [df]
}

csmRegister(profile)    #register

rate(1, progress)
