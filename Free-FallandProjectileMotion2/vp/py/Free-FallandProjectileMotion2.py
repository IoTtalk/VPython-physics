
g=9.8 #重力加速度 9.8 m/s^2
size = 1 #球半徑 0.25 m
height = 15.0 #球初始高度 15 m

scene = display(width=800, height=800, background=vector(0.5,0.5,0.0), center=vector(0,height/2,0))
floor = box(length=80, height=2, width=10, color=color.green)
basketwall = box(length = 2,height = 52,width = 10,pos=vector(40,25,0) )
basgoal = box(length=2,height=10, width= 10,pos=vector(40,43,0),color=color.red)

spd = 30
angle = 45;
posit = 0;


laba =label(pos=vector(0,40,0), text='angle =  '+angle+' 度')
labp =label(pos=vector(0,35,0), text='position = '+posit)
labv =label(pos=vector(0,30,0), text='speed = '+spd)


def ballpos(x):
	global posit
	if(x==1):
		posit -= 5
	elif(x==3):
		posit += 5
	else:
		posit = 0
	labp.text = 'pos = '+ posit



def ballangle(x):
	global angle
	if(x==4):
		angle-=5
	elif(x==6):
		angle+=5
	else:
		angle = 45
	laba.text = 'angle = '+angle+' 度' 


def ballv(x):
	global spd
	if(x==7):
		spd=spd-5
	elif(x==9):
		spd=spd+5
	else:
		spd = 30
	labv.text='speed = ' +spd
def ballthrow():
	ball = sphere(pos=vector(-40+posit,size, 0.0), radius=size, color=color.blue)
	ball.v = vector(spd*cos(angle*pi/180),spd*sin(angle*pi/180),0.0)
	floor.color = color.green
	scene.color = color.yellow
	dt = 0.001

	
	def down():
		if ball.pos.y <= 48 and ball.pos.y>=38 and ball.pos.x >= 39 and ball.pos.x<=41:
			ball.color = color.red
			scene.color = color.black
			floor.color = color.white
		elif ball.pos.x > 41 or ball.pos.y < 0:
			ball.visible = False
		else :
			rate(1000,down)
			ball.pos = ball.pos +ball.v*dt
			ball.v.y = ball.v.y - g*dt
	down()

def handler(data):
	rate(1,progress)
	if data == 1 or data == 2 or data == 3:
		ballpos(data)
	elif data == 4 or data == 5 or data == 6:
		ballangle(data)
	elif data == 7 or data == 8 or data == 9:
		ballv(data)
	elif data == 0:
		ballthrow()
		
	
    
def progress():
    csmPull('Command',handler)


profile = {
		'dm_name':'Free-FallandProjectileMotion2',
		'df_list':['Command']
}
csmRegister(profile)	
rate(1,progress)


