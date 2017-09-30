L = 4.9             			#板長度
size = 0.1          			#球半徑 0.1m
th = 30 * pi / 180  		#板斜度 30度
dt = 0.001

scene = display(width=900, height=900, background=vector(0.5,0.5,0), center=vector(0,(L-2*size)*sin(th)/2,0))

scene.forward = vector(-2, 0, -1)							#設定視窗視角方向
board = box(length=L, height=0.001, width=1)				#畫斜板
board.pos = vector(-L*cos(th)/2 - size*sin(th) , L*sin(th)/2-size*cos(th), 0)	#斜板的中心
board.axis=vector(-L*cos(th), L*sin(th),0)					#斜板的方向	

def slope(spd):
	ball = sphere(pos=vector(-L*cos(th), L*sin(th), 0), radius = size, color = color.red)		#球
	ball.velocity = vector(0.0, 0.0, 0.0)                      		#球初速 

	g = 9.8 * spd
	gj_playFlag=1

	def roll():
		if ball.pos.y < 0:
			ball.visible = False
			gj_playFlag=1
			
		if ball.pos.x < 4.9:
			rate(1000, roll)
		
		a = vector(g * sin(th) * cos(th), - g * sin (th) * sin(th), 0)          #加速度
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

