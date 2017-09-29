g = 9.8             			#���O�[�t�� 9.8 m/s^2
L = 4.9             			#�O����
size = 0.1          			#�y�b�| 0.1m
#th = 30 * pi / 180  		#�O�׫� 30��
dt = 0.001

scene = display(width=900, height=900, background=vector(0.5,0.5,0))
scene.center = vector(0,(L-2*size)/2,0)					#�]�w���������I
scene.forward = vector(-0.125, 0.1, -1)							#�]�w����������V
#board = box(length=L, height=0.001, width=1)				#�e�תO
#board.pos = vector(-L*cos(th)/2 - size*sin(th) , L*sin(th)/2-size*cos(th), 0)	#�תO������
#board.axis=vector(-L*cos(th), L*sin(th),0)					#�תO����V	
floor = box(length=10, height=0.001, width=1)                #�e�a�O
floor.pos = vector(-L/2, -0.1, 0)
floor.axis=vector(-L,0,0)
#1
"""ball = sphere(radius = size, color = color.red)			#�y
ball.pos = vector(-L*cos(th), L*sin(th), 0)        	 	#�y��l��m 
ball.v = vector(0.0, 0.0, 0.0)"""              			#�y��t            
#2


def setPos(data):

    th = data*pi / 180  		#�O�׫�
    board = box(length=L, height=0.001, width=1)				#�e�תO
    board.pos = vector(-L*cos(th)/2 - size*sin(th) , L*sin(th)/2-size*cos(th), 0)	#�תO������
    board.axis=vector(-L*cos(th), L*sin(th),0)					#�תO����V	
    
    #1
    if th!=0:
        if data<=20:
            ball = sphere(radius = size, color = color.black)			#�y
        elif data<=40:
            ball = sphere(radius = size, color = color.blue)
        elif data<=60:
            ball = sphere(radius = size, color = color.yellow)
        elif data<=80:
            ball = sphere(radius = size, color = color.orange)
        elif data==90:
            ball = sphere(radius = size, color = color.red)
        ball.pos = vector(-L*cos(th), L*sin(th), 0)        	 	#�y��l��m 
        ball.v = vector(0.0, 0.0, 0.0)                      			#�y��t            
    #2
    def resetScene():
        scene.background = vector(0.5, 0.5, 0)
        ball.pos = vector(-L*cos(th), L*sin(th), 0)        	 	#�y��l��m 
        ball.v = vector(0.0, 0.0, 0.0)
    def fall():
        if ball.pos.x < 0.0:
            rate(1000,fall)
            a = vector(g * sin(th) * cos(th), - g * sin(th) * sin(th), 0)     #�[�t��
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
