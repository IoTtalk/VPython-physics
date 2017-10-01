#from visual import *

#  1. 畫面設定
scene = display(title='Bouncing_Ball',width=1000, height=1000, background=vector(0.5,0.6,0.5))
table = cylinder(pos=vector(0,-0.03,0), axis=vector(0,-0.01,0), radius=0.7)
center = cylinder(pos=vector(0, -0.03, 0), axis = vector(0, 0.03, 0), radius = 0.007)

target1 = cylinder(pos=vector(5, 0, -0.1), axis = vector(0.03, 0, 0), radius = 1, color = color.black)
target1 = cylinder(pos=vector(5, 0, -0.1), axis = vector(0.032, 0, 0), radius = 0.8, color = color.white)
target1 = cylinder(pos=vector(5, 0, -0.1), axis = vector(0.034, 0, 0), radius = 0.6, color = color.black)
target1 = cylinder(pos=vector(5, 0, -0.1), axis = vector(0.036, 0, 0), radius = 0.4, color = color.white)
target1 = cylinder(pos=vector(5, 0, -0.1), axis = vector(0.038, 0, 0), radius = 0.2, color = color.red)

#ball = sphere(pos=vector(-0.5,0,0), radius=0.03, color=color.blue)
#a_arrow = arrow(shaftwidth = 0.01, color = color.red)
#v_arrow = arrow(shaftwidth = 0.01, color = color.yellow)
#a_label = label(text='a', height=15, opacity = 0, box= False)
#v_label = label(text='v', height=15, opacity = 0, box= False)
score = label(pos=vector(5, 1.5, -0.1),text='score', xoffset=20,yoffset=12, space=target1.radius,height=10, border=6,font='sans')
##1

#  2. 設定參數、初始值
#ball.v = vector(0, 0, 0.5)
input =1
test  =1

text_score=''
#dt = 0.001
#ball.a = vector(0,0,0.1)
def runs():
	
	ball = sphere(pos=vector(0.9,0,0), radius=0.05, color=color.blue)
	a_arrow = arrow(shaftwidth = 0.01, color = color.red)
	
	#a_label = label(text='a', height=15, opacity = 0, box= False)
	
	r = 0.9
	ball.v = vector(0, 0, 0.9)
	ball.a = vector(0,0,0.1)
	playFlag=1
	dt = 0.001
	#def throw():
	#	rate(1000*input,throw)
	def run():
		print 'run'		
		global input
		global test
		global text_score
		if ball.pos.x >5.2 or ball.pos.z > 5.2 or ball.pos.x <-5.2 or ball.pos.z <-5.2:
			ball.visible = False
			a_arrow.visible = False
			global score
			score.text = text_score
			
			
			
			
		else :
			rate(1000*test,run)
			vv=ball.v.x*ball.v.x +ball.v.y*ball.v.y+ball.v.z*ball.v.z
			if input == 10  :
				ball.a=vector(0,0,0)
				
			else :
				ball.a = - (vv / r) * (ball.pos/r)
				a_arrow.pos = ball.pos
				a_arrow.axis =  ball.a
				if ball.a.x < 0.1 and ball.a.x > -0.1 and ball.v.x >0 :
					ball.color = color.red
				else :
					ball.color = color.blue
			
			if ball.pos.z < 0.1 and ball.pos.x > 0:
				text_score = str( round(100/(0.1-ball.pos.z),3))
			elif ball.pos.x < 0:
				text_score = 'Wrong direction'
			else :
				text_score = str( round(-100/(0.1-ball.pos.z),3))
			#ball.a = - (vv / r) * (ball.pos/r)
			ball.v = ball.v + ball.a*dt
			ball.pos = ball.pos + ball.v*dt
			
			#a_arrow.pos = ball.pos
			#a_arrow.axis =  ball.a 
			#a_label.pos = a_arrow.pos + a_arrow.axis*1.2
			
			
	run()

    

def handler(data):
	#ballfall(data)
	rate(1, progress)
	if data != None:
		global input
		global test
		input = data
		if input <10:
			test =input
		if input == 11:
			runs()
		
def progress():
    csmPull(df,handler)



df = 'Frequency'
profile = {
    'dm_name': 'UniformCircularMotion2',
    'df_list': [df]
}
csmRegister(profile)

rate(1, progress)
a=runs()




