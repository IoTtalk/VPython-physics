
g = 10           #重力加速度 9.8 m/s^2
size = 0.5       #球半徑 0.05 m
r = 0.5             #彈簧原長 0.5m
k = 10              #彈簧力常數 10 N/m
m = 0.2             #球質量 0.2 kg
big = 0
small = 0
redflag = 0
blueflag = 0
greenflag = 0

scene = display(width=800, height=800, center=vector(0, -r*0.6, 0), background=vector(1,1,0))  #設定畫面
ceiling = box(length=3, height=0.005, width=3, color=color.black)                    #畫天花板
"""ball = sphere(radius = size,  color=color.red)                              #畫球
spring = helix(radius=0.02, thickness =0.01)                                #畫彈簧,不動端在(0,0,0)

ball.pos0 = vector(0, -r, 0) 					#球的初位置，即彈簧運動端的初位置
ball.pos = vector(0, -r , 0)        					#球在時間＝０時的位置
ball.v = vector(0, 0, 0)            					#球初速
"""
dt = 0.001  

def ans(data):
	if data == 1:
		redball = sphere(radius = size,  color=vector(1,0,0))                              #畫球
		redspring = helix(radius=0.02, thickness =0.01)                                #畫彈簧,不動端在(0,0,0)
		redspring.pos = vector(-1,0,0);
		
		redball.pos0 = vector(-1, -r, 0) 					#球的初位置，即彈簧運動端的初位置
		redball.pos = vector(-1, -r , 0)        					#球在時間＝０時的位置
		redball.v = vector(0, 0, 0)      
	elif data == 2:
		blueball = sphere(radius = size,  color=vector(0,0,1))                            
		bluespring = helix(radius=0.02, thickness =0.01) 
		bluespring.pos = vector(0,0,0);

		blueball.pos0 = vector(0, -r, 0) 					
		blueball.pos = vector(0, -r , 0)        					
		blueball.v = vector(0, 0, 0)      
	elif data == 3:
		greenball = sphere(radius = size,  color=vector(0,1,0))                            
		greenspring = helix(radius=0.02, thickness =0.01) 
		greenspring.pos = vector(1,0,0);

		greenball.pos0 = vector(1, -r, 0) 					
		greenball.pos = vector(1, -r , 0)        					
		greenball.v = vector(0, 0, 0)   
	elif data == 4:
		global big
		big = big + 0.0001
	elif data == 5:
		global big
		big = 0
		global small
		small = 0	
	elif data == 6:
		global big
		big = 0
		global small
		small = small + 0.0001
	elif data == 7:	
		global redflag
		if redflag ==0:
			redflag = 1
		else:
			redflag = 0
	elif data == 8:	
		global blueflag
		if blueflag ==0:
			blueflag = 1
		else:
			blueflag = 0
	elif data == 9:	
		global greenflag
		if greenflag ==0:
			greenflag = 1
		else:
			greenflag = 0					
	elif data == 0:
		global g
		g = 0;
	
	elif data == 10:
		global g
		g = g + 5
	elif data == 11:
		global g
		g = g - 5

	def join():
		rate(1000,join)
		if data == 1:
			redball.radius = redball.radius + big
			if redball.radius>0.05:
				redball.radius = redball.radius - small
			
			redspring.axis = redball.pos - redspring.pos 		#彈簧的全長＝彈簧不動端的位置向量到球現在的位置向量
			redball.color.y = redball.color.y + 0.0005
			redball.color.z = redball.color.z + 0.0005
			if redball.color.y > 1:
				redball.color.y = 0
				redball.color.z = 0

										
			global redflag					
			if redflag == 1:
				redball.v.y = 0
			else:
				redball.a = vector(0, - g - k * (redball.pos.y - redball.pos0.y )/m , 0)	#球的加速度的y分量 = - g - k*(彈簧伸長量)/m	
				redball.v = redball.v + redball.a*dt
			redball.pos = redball.pos +redball.v*dt
		
		if data == 2:
			blueball.radius = blueball.radius + big
			if blueball.radius>0.05:
				blueball.radius = blueball.radius - small
			bluespring.axis = blueball.pos - bluespring.pos 		
			blueball.color.x = blueball.color.x - 0.0005
			if blueball.color.x < 0:
				blueball.color.x = 1
								
			global blueflag					
			if blueflag == 1:
				blueball.v.y = 0
			else:
				blueball.a = vector(0, - g - k * (blueball.pos.y - blueball.pos0.y )/m , 0)
				blueball.v =  blueball.v + blueball.a*dt
			blueball.pos = blueball.pos +blueball.v*dt
		
		if data == 3:
			greenball.radius = greenball.radius + big
			if greenball.radius>0.05:
				greenball.radius = greenball.radius - small
			greenspring.axis = greenball.pos - greenspring.pos 		
			greenball.color.x = greenball.color.x - 0.0005
			if greenball.color.x < 0:
				greenball.color.x = 1
								
			global greenflag					
			if greenflag == 1:
				greenball.v.y = 0
			else:
				greenball.a = vector(0, - g - k * (greenball.pos.y - greenball.pos0.y )/m , 0)
				greenball.v =  greenball.v + greenball.a*dt
			greenball.pos = greenball.pos +greenball.v*dt
	join()
	
def handler(data):
	rate(1, progress)
	if data != None:
		ans(data)
    
def progress():
    csmPull(df,handler)

df = 'Command'
profile = {
    'dm_name': 'Spring-SHM2',
    'df_list': [df]
}
csmRegister(profile)

rate(1, progress)
