####################################程式開始###################################
from visual import *
#------------------------------------------------------------------------------
#  1. 參數設定
#------------------------------------------------------------------------------
#v = 0.03	   #木塊速度 = 0.03 m/s
dt = 0.0001	  #畫面更新的時間間隔，單位為s
t = 0		   #模擬所經過的時間 ，單位為s，初始值為0

#------------------------------------------------------------------------------
#  2. 畫面設定
#------------------------------------------------------------------------------
scene = display(width=800, height=800, x=0, y=0, center=vector(0,0.06,0), background=vector(0.5,0.6,0.5))
floor = box(pos=vector(0,-(0.005)/2,0), length=0.3, height=0.005, width=0.1)
line = box(pos=vector(0.15,0.1,0), length=0.00001, height=0.2, width=0.1, color = color.red)
cube = box(pos= vector(-0.15, 0.05/2, 0), length=0.02, height=0.02, width=0.02)


v = [vector(-0.5,0,0),vector(1,0,0)]
balls = []
balls[0] = sphere(pos=vector(-0.15, 0.16, 0), radius=0.01, color=color.green)
balls[1] = sphere(pos=vector(-0.15, 0.10, 0), radius=0.01, color=color.blue)



#------------------------------------------------------------------------------
#  3. 物體運動部分
#------------------------------------------------------------------------------
def move(v):
	
	cube.velocity = vector(v,0.0,0.0)

	def move2():

		playFlag = 0
		rate(500,move2)
	
		console.log(v)
		if(cube.pos.x < 0.15 ):   
			cube.pos.x = cube.pos.x + cube.velocity.x * dt
			if balls[1].pos.x < 0.04 and cube.velocity.x != 0:

				balls[0].pos.x = balls[0].pos.x + 0.16 * dt
				balls[1].pos.x = balls[1].pos.x + 0.3 * dt
			else if cube.velocity.x != 0:
				balls[0].pos.x = balls[0].pos.x + 0.16 * dt
				balls[1].pos.x = balls[1].pos.x + 0.05 * dt
			
		else:
			cube.pos.x = - 0.15


		if balls[0].pos.x >= 0.15 or balls[1].pos.x >= 0.15 :
			if balls[0].pos.x > balls[1].pos.x :
				balls[0].visible = False
				if balls[1].pos.x >= 0.15 :
					balls[1].visible = False

			else :
				balls[1].visible = False
				if balls[0].pos.x >= 0.15 :
					balls[0].visible = False	

	move2()


def handler(data):  
	rate(10,progress)
	if data != None:	
		move(data)


def progress():
	csmPull(df,handler)
   
rate(10,progress)
df= '1D-Velocity'
profile = {

	'dm_name' : 'UniformMotion',
	'df_list' : [df]

}
csmRegister(profile)
