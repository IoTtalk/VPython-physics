from visual import *
size = 0.1          #²y¥b®| 0.1 m

scene = display(width=800, height=800,  background=vector(0.5,0.5,0),center=vector(0,0,0))             	#µe­±³]©w
scene.center = vector(0,0,0)
#scene.range=1
camera_x1=0.8
camera_x2=0.0
#scene.forward=vector(camera_x1,camera_x2,-1)



b1 = sphere(radius = size,  color=color.yellow)         				
#b2 = sphere(radius = size,  color=color.green)          				
#b3 = sphere(radius = size,  color=color.red)          				
b1.pos = vector( 0.6 , 0.1, 0)                        	
#b2.pos = vector( 0 , 0 , 0 )   
#b3.pos = vector(-0.2,-0.3,0)                         	
b1.velocity = vector(-0.2, 0, 0)                              	
#b2.velocity = vector(0 , 0, 0)   
#b3.velocity = vector(0.2,0.1,0)
'''
b3 = sphere(radius = size,  color=color.red)          				
b3.velocity = vector(0.2,0.1,0)
b3.pos = vector(-0.2,-0.3,0)
'''
b2 = "no"
b3 = "no"
b4 = "no"
b5 = "no"

def distance(a,b):
	if a != "no" and b != "no":
		dis_x = abs(a.pos.x-b.pos.x)
		dis_y = abs(a.pos.y-b.pos.y)
		dis_z = abs(a.pos.z-b.pos.z)
		return (dis_x**2 + dis_y**2 + dis_z**2)**0.5

def collision(data):
	global b2,b3,b4,b5
	dt = 0.001  
	
	if data == 0:
		b1.velocity = vector(-0.3,0.2,0)
		if b2 != "no":
			b2.velocity = vector(0,0,0)
		if b3 != "no":
			b3.velocity = vector(0.2,0.1,0)
		if b4 != "no":
			b4.velocity = vector(0,0,0)
	elif data == 1:#elif data > 4 and data < 5: #up and down (1)		
		b1.velocity = b1.velocity * (-1)
		y1 = b1.velocity.y
		b1.velocity=vector(0,y1,0)

		if b2 != "no":
			b2.velocity = b2.velocity * (-1)
			y2 = b2.velocity.y
			b2.velocity=vector(0,y2,0)
		if b3 != "no":
			b3.velocity = b3.velocity * (-1)
			y3 = b3.velocity.y
			b3.velocity=vector(0,y3,0)
		if b4 != "no":			
			b4.velocity = b4.velocity * (-1)
			y4 = b4.velocity.y
			b4.velocity=vector(0,y4,0)
		
	elif data==2:#data > 9 and data < 10: #right and left (2)
		
		b1.velocity = b1.velocity * (-1)
		x1 = b1.velocity.x
		b1.velocity=vector(x1,0,0)

		if b2 != "no":
			b2.velocity = b2.velocity * (-1)
			x2 = b2.velocity.x
			b2.velocity=vector(x2,0,0)
		if b3 != "no":			
			b3.velocity = b3.velocity * (-1)
			x3 = b3.velocity.x
			b3.velocity=vector(x3,0,0)
		if b4 != "no":			
			b4.velocity = b4.velocity * (-1)
			x4 = b4.velocity.x
			b4.velocity=vector(x4,0,0)
		
	elif data==3:#data > 13 and data < 14:
		if b2 == "no":
			b2 = sphere(radius = size,  color=color.green)          				
			b2.pos = vector( 0 , 0 , 0 )   
			b2.velocity = vector(0 , 0, 0)   
		elif b3 == "no":
			b3 = sphere(radius = size,  color=color.red)          				
			b3.velocity = vector(0.2,0.1,0)
			b3.pos = vector(0.5,0.5,0)
		elif b4 == "no":
			b4 = sphere(radius = size,  color=color.black)          				
			b4.velocity = vector(0.3,0.1,0)
			b4.pos = vector(-0.5,-0.5,0)
	elif data==4:#data > 18 and data < 19:
		if b4 != "no":
			b4.color = vector(0.5,0.5,0)
			b4.visible = False
			del b4
			b4 = "no"
		elif b3 != "no":
			b3.color = vector(0.5,0.5,0)
			b3.visible = False
			del b3	
			b3 = "no"
		elif b2 != "no":
			b2.color = vector(0.5,0.5,0)
			b2.visible = False
			del b2	
			b2 = "no"
	elif data==5:#data > 31 and data < 32:
		if b2 != "no" and b3 =="no":
			b2.pos = b1.pos - vector(0.08,0.08,0)
			b2.velocity = b1.velocity
		elif b3 != "no" and b4=="no":
			b2.pos = b1.pos - vector(0.1,0.1,0)
			b2.velocity = b1.velocity
			b3.pos = b1.pos + vector(0.1,0.1,0)
			b3.velocity = b1.velocity
			#b3.pos = b4.pos - vector(0.08,0.08,0)
			#b3.velocity = b4.velocity
		elif b4 != "no":
			b2.pos = b1.pos - vector(0.1,0.1,0)
			b2.velocity = b1.velocity
			b3.pos = b1.pos + vector(0.1,0.1,0)
			b3.velocity = b1.velocity
			b4.pos = b2.pos - vector(0.1,0.1,0)
			b4.velocity = b1.velocity
	else:
		b1.velocity = b1.velocity * (data / 7.5)
		if b2 != "no":
			b2.velocity = b2.velocity * (data / 7.5)	
		if b3 != "no":
			b3.velocity = b3.velocity * (data / 7.5)
		if b4 != "no":
			b4.velocity = b4.velocity * (data / 7.5)	
	def jump():                           	#²y2ªì³t
		rate(500,jump)	
		if distance(b1,b2) <= 2*size:			
			v1prime = b1.velocity - ((b1.pos-b2.pos)  * dot (b1.velocity-b2.velocity, b1.pos-b2.pos)) / distance(b1,b2)**2
			v2prime = b2.velocity - ((b2.pos-b1.pos)  * dot (b2.velocity-b1.velocity, b2.pos-b1.pos)) / distance(b1,b2)**2
			b1.velocity, b2.velocity = v1prime, v2prime
		if distance(b3,b2) <= 2*size:			
			v3prime = b3.velocity - ((b3.pos-b2.pos)  * dot (b3.velocity-b2.velocity, b3.pos-b2.pos)) / distance(b3,b2)**2
			v2prime = b2.velocity - ((b2.pos-b3.pos)  * dot (b2.velocity-b3.velocity, b2.pos-b3.pos)) / distance(b3,b2)**2
			b3.velocity, b2.velocity = v3prime, v2prime
		if distance(b1,b3) <= 2*size:			
			v1prime = b1.velocity - ((b1.pos-b3.pos)  * dot (b1.velocity-b3.velocity, b1.pos-b3.pos)) / distance(b1,b3)**2
			v3prime = b3.velocity - ((b3.pos-b1.pos)  * dot (b3.velocity-b1.velocity, b3.pos-b1.pos)) / distance(b1,b3)**2
			b1.velocity, b3.velocity = v1prime, v3prime
		if distance(b1,b4) <= 2*size:
			v1prime = b1.velocity - ((b1.pos-b4.pos)  * dot (b1.velocity-b4.velocity, b1.pos-b4.pos)) / distance(b1,b4)**2
			v4prime = b4.velocity - ((b4.pos-b1.pos)  * dot (b4.velocity-b1.velocity, b4.pos-b1.pos)) / distance(b1,b4)**2
			b1.velocity, b4.velocity = v1prime, v4prime
		if distance(b2,b4) <= 2*size:
			v2prime = b2.velocity - ((b2.pos-b4.pos)  * dot (b2.velocity-b4.velocity, b2.pos-b4.pos)) / distance(b2,b4)**2
			v4prime = b4.velocity - ((b4.pos-b2.pos)  * dot (b4.velocity-b2.velocity, b4.pos-b2.pos)) / distance(b2,b4)**2
			b2.velocity, b4.velocity = v2prime, v4prime
		if distance(b3,b4) <= 2*size:
			v3prime = b3.velocity - ((b3.pos-b4.pos)  * dot (b3.velocity-b4.velocity, b3.pos-b4.pos)) / distance(b3,b4)**2
			v4prime = b4.velocity - ((b4.pos-b3.pos)  * dot (b4.velocity-b3.velocity, b4.pos-b3.pos)) / distance(b3,b4)**2
			b3.velocity, b4.velocity = v3prime, v4prime	
		b1.pos =  b1.pos + b1.velocity * dt 
		if b2 != "no":
			b2.pos =  b2.pos + b2.velocity * dt
		if b3 != "no":
			b3.pos =  b3.pos + b3.velocity * dt
		if b4 != "no":
			b4.pos =  b4.pos + b4.velocity * dt


		if b1.pos.x < -0.63 or b1.pos.x > 0.63:
			b1.velocity.x = -b1.velocity.x	
		if b1.pos.y < -0.63 or b1.pos.y > 0.63:
			b1.velocity.y = -b1.velocity.y	
		if b2 != "no":
			if b2.pos.x < -0.63 or b2.pos.x > 0.63:
				b2.velocity.x = -b2.velocity.x	
			if b2.pos.y < -0.63 or b2.pos.y > 0.63:
				b2.velocity.y = -b2.velocity.y	
		if b3 != "no":
			if b3.pos.x < -0.63 or b3.pos.x > 0.63:
				b3.velocity.x = -b3.velocity.x	
			if b3.pos.y < -0.63 or b3.pos.y > 0.63:
				b3.velocity.y = -b3.velocity.y	
		if b4 != "no":
			if b4.pos.x < -0.63 or b4.pos.x > 0.63:
				b4.velocity.x = -b4.velocity.x	
			if b4.pos.y < -0.63 or b4.pos.y > 0.63:
				b4.velocity.y = -b4.velocity.y	
		

		
		
	jump()


def handler(data):
	global flag2,b3
	rate(1,progress)
	if data != None:
		collision(data)

def progress():
	#rate(1,handler(5))
	csmPull(df,handler)

rate(1,progress) #每秒執行一次progress



#-----registration
df = 'Command'
profile = {
	'dm_name':'Collision1',
	'df_list':[df]
}

csmRegister(profile)
'''
0 :0
1: 4.54545454
2: 9.09090909
3: 13.63636363
4: 18.18181818
5: 22.72727272
6: 27.272727
7: 31.818181
8: 36.363636
9: 40.909090
*: 45.45454 5
#: 50
'''
