#from visual import *

#  1. 參數設定
a = -9.8                 	#加速度值，在x、z方向為0，在y方向為g=-9.8 m/s^2
#vy = 0.0                  	#球的y方向初速
size = 0.5                  #球的半徑
h = 10.0                   	#球的初始高度
t = 0             		    #模擬所經過的時間 ，單位為s，初始值為0


#  2. 畫面設定
scene = display(title='One-dimensional Uniform Accelerated Motion', width=800, height=800
                    , forward=vector(0.8, -0.3, -1), center=vector(0, h/2, 0) , range=35
                    , background=vector(127/255, 178/255, 211/255))
floor = box(pos=vector(0, 0, 0), length=50, height=0.005, width=5, color=vector(0.8, 0.8, 0.8))
Label = label( pos=vec(-20, 0, 0), text='Height :   \nInitial Velocity :   \nG :', height=20 )


#  3. 描述物體的運動
def balldrop(x):
    x = x + 1
    ball_color = vector(1, x/11, x/11) 
    ball_pos = vector(x*40/12-20, x*2, 0)
    ball_size = 0.5
    ball_velocity = vector(0, x*1.5, 0)
    a = -(9.8 * (x*(3-1/3))/12 + 1/3)

    ball = sphere(pos=ball_pos, radius=ball_size, color=ball_color)
    ball.velocity = ball_velocity

    Label.text = 'Height : ' + (x*2) + '\nInitial Velocity : ' + ball_velocity.y + '\nG : ' + "{:8.2f}".format(a)
    dt = 0.001

    def drop():
        rate(2500, drop)
        ball.pos = ball.pos + ball.velocity * dt

        if ball.pos.y <= size:
            ball.velocity.y = abs(ball.velocity.y)
        else:
            ball.velocity.y = ball.velocity.y + a * dt
        
    drop()

def handler(data):
    #balldrop(data)
    rate(1, progress)
    if data != None:
        balldrop(data)
    
def progress():
    csmPull(df,handler)

df = 'Height'
profile = {
    'dm_name': 'UniformAcceleratedMotion1',
    'df_list': [df]
}
csmRegister(profile)

rate(1, progress)
