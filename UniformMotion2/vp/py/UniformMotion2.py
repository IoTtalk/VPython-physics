####################################程式開始###################################
from visual import *
#------------------------------------------------------------------------------
#  1. 參數設定
#------------------------------------------------------------------------------
#v = 0.03	   #木塊速度 = 0.03 m/s
dt = 0.0001	  #畫面更新的時間間隔，單位為s
t = 0		   #模擬所經過的時間 ，單位為s，初始值為0


#background

scene = display(title='1', width=800, height=800, x=0, y=0, center=vector(0,0.06,0), background = vector(0.5,0.6,0.5))
floor = box(pos=vector(0,-(0.005)/2,0), length=0.3, height=0.005, width=0.1)
line = box(pos=vector(0.15,0.1,0), length=0.00001, height=0.2, width=0.1, color = color.black)
cube = box(pos= vector(-0.15, 0.02/2, 0), length=0.02, height=0.02, width=0.02)


v = [vector(-0.5,0,0),vector(1,0,0)]


#cube movement

def move(v):
	
	cube.velocity = vector(v,0.0,0.0)

	def move2():

		rate(500,move2)
		
		console.log(v)
		if(cube.pos.x < 0.15 ):   
			cube.pos.x = cube.pos.x + cube.velocity.x * dt
		else if (v == 0):
			cube.velocity = vector(0.0,0.0,0.0);
		else:
			cube.pos.x = - 0.15
	

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

	'dm_name' : 'UniformMotion2',
	'df_list' : [df]

}
csmRegister(profile)
