L = 4.9             			#�O����
size = 0.1          			#�y�b�| 0.1m
th = 30 * pi / 180  		#�O�׫� 30��
dt = 0.001

scene = display(width=900, height=900, background=vector(0.5,0.5,0), center=vector(0,(L-2*size)*sin(th)/2,0))

scene.forward = vector(-2, 0, -1)							#�]�w����������V
board = box(length=L, height=0.001, width=1)				#�e�תO
board.pos = vector(-L*cos(th)/2 - size*sin(th) , L*sin(th)/2-size*cos(th), 0)	#�תO������
board.axis=vector(-L*cos(th), L*sin(th),0)					#�תO����V	

def slope(spd):
	ball = sphere(pos=vector(-L*cos(th), L*sin(th), 0), radius = size, color = color.red)		#�y
	ball.velocity = vector(0.0, 0.0, 0.0)                      		#�y��t 

	g = 9.8 * spd
	gj_playFlag=1

	def roll():
		if ball.pos.y < 0:
			ball.visible = False
			gj_playFlag=1
			
		if ball.pos.x < 4.9:
			rate(1000, roll)
		
		a = vector(g * sin(th) * cos(th), - g * sin (th) * sin(th), 0)          #�[�t��
		ball.velocity = ball.velocity + a * dt                                            
		ball.pos = ball.pos + ball.velocity * dt                                       
	roll()


def handler(data):
	rate(1, progress)
	if data != None:
		slope(data)
	
df = 'Constant'
profile = {
	'dm_name': 'Ball-Slide2',
	'df_list': [df]
}
csmRegister(profile)

def progress():
	#rate(1, handler(5))
	csmPull(df,handler)

rate(1, progress)

