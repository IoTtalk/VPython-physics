g = 9.8             			#重力加速度 9.8 m/s^2
L = 4.9             			#板長度
size = 0.1          			#球半徑 0.1m
#th = 30 * pi / 180  		#板斜度 30度
dt = 0.001

scene = display(width=900, height=900, background=vector(0.5,0.5,0))
scene.center = vector(0,(L-2*size)/2,0)					#設定視窗中心點
scene.forward = vector(-0.125, 0.1, -1)							#設定視窗視角方向
#board = box(length=L, height=0.001, width=1)				#畫斜板
#board.pos = vector(-L*cos(th)/2 - size*sin(th) , L*sin(th)/2-size*cos(th), 0)	#斜板的中心
#board.axis=vector(-L*cos(th), L*sin(th),0)					#斜板的方向	
floor = box(length=10, height=0.001, width=1)                #畫地板
floor.pos = vector(-L/2, -0.1, 0)
floor.axis=vector(-L,0,0)
#1
"""ball = sphere(radius = size, color = color.red)			#球
ball.pos = vector(-L*cos(th), L*sin(th), 0)        	 	#球初始位置 
ball.v = vector(0.0, 0.0, 0.0)"""              			#球初速            
#2


def setPos(data):

    th = data*pi / 180  		#板斜度
    board = box(length=L, height=0.001, width=1)				#畫斜板
    board.pos = vector(-L*cos(th)/2 - size*sin(th) , L*sin(th)/2-size*cos(th), 0)	#斜板的中心
    board.axis=vector(-L*cos(th), L*sin(th),0)					#斜板的方向	
    
    #1
    if th!=0:
        if data<=20:
            ball = sphere(radius = size, color = color.black)			#球
        elif data<=40:
            ball = sphere(radius = size, color = color.blue)
        elif data<=60:
            ball = sphere(radius = size, color = color.yellow)
        elif data<=80:
            ball = sphere(radius = size, color = color.orange)
        elif data==90:
            ball = sphere(radius = size, color = color.red)
        ball.pos = vector(-L*cos(th), L*sin(th), 0)        	 	#球初始位置 
        ball.v = vector(0.0, 0.0, 0.0)                      			#球初速            
    #2
    def resetScene():
        scene.background = vector(0.5, 0.5, 0)
        ball.pos = vector(-L*cos(th), L*sin(th), 0)        	 	#球初始位置 
        ball.v = vector(0.0, 0.0, 0.0)
    def fall():
        if ball.pos.x < 0.0:
            rate(1000,fall)
            a = vector(g * sin(th) * cos(th), - g * sin(th) * sin(th), 0)     #加速度
            ball.v = ball.v + a * dt
            ball.pos = ball.pos + ball.v * dt

        else :
            scene.background = vector(0,0,0)
            rate(4,resetScene)
            ball.visible = False
            board.visible = False
    fall()
#3

def handler(data):
    rate(1, progress)
    if data != None:
        setPos(data)

def progress():
    csmPull(df, handler)

df='Angle'
profile = {
    'dm_name':'Ball-Slide1',
    'df_list':[df]
	
}
csmRegister(profile)
rate(1, progress)
