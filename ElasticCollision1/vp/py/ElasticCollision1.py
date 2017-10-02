#  1.  畫面設定
scene1 = display(width=600, height=400, background=vector(0.5,0.6,0.5), y=0)
arrow1 = arrow(display=scene1, pos=vector(-1,0,0), axis=vector(2,0,0), shaftwidth=0.005)
arrow4 = arrow(display=scene1, pos=vector(0,0,0), axis=vector(0,0.3,0), shaftwidth=0.005)

gd1 = gdisplay(x=600, y=0, title='v vs t', xtitle='t', ytitle='v', ymax=1, xmax=2, background=vector(0.3,0.3,0.3))
vt1 = gcurve(gdisplay=gd1, color=vector(0.5, 0.5, 0.5))
vt2 = gcurve(gdisplay=gd1, color=color.orange)
#vts= (vt1, vt2)
dt = 0.001
#  2.  物體設定
ironball = sphere(display=scene1, radius=0.05, pos=vector(-0.2,0,0), color=vector(0.5, 0.5, 0.5)) 
ironball.m = (pi*4/3*(0.05)**3)*7.9*1e3
ironball.v = 0.25
ping_pong = sphere(display=scene1, radius=0.02, pos=vector(0.1,0,0), color=color.red)
ping_pong.m = 2.6*10e-3
ping_pong.v = 0
#balls=(ironball, ping_pong)

#  3.  定義函數
def collide(v1,v2,m1,m2):
	v1f = v1*(m1-m2)/(m1+m2) + v2*2*m2/(m1+m2)
	v2f = v1*2*m1/(m2+m1) + v2*(m2-m1)/(m2+m1)
	return v1f, v2f
	
#  4.  物體運動

def ballbump(p):
	if p < 23 and p > 22:
		p = 0
	else:
		p = p-22.5
	ping_pong.visible = True
	ironball.visible = True
	#ping_pong.pos.x = 0.1+p*0.01
	ping_pong.pos.x = 0.1
	ironball.pos.x = -0.2
	ironball.v = 0.25
	ping_pong.v = 0+p*0.01
	gj_playFlag=1
	def tmp():		
		if ping_pong.pos.x > 1:
			"""
			ironball.v = 0.25
			ironball.m = (pi*4/3*(0.05)**3)*7.9*1e3
			ping_pong.v = 0
			ping_pong.m = 2.6*10e-3		
			ping_pong.pos.x = 0.1+p*0.01
			ironball.pos.x = -0.2
			"""
			ping_pong.visible = False
			ironball.visible = False
			gj_playFlag=1
		else:
			rate(200,tmp)
		ironball.pos.x = ironball.v*dt + ironball.pos.x
		#vt1.plot(pos=vector(t,ironball.v))
		ping_pong.pos.x = ping_pong.v*dt + ping_pong.pos.x
		#vt2.plot(pos=vector(t,ping_pong.v))
		if abs(ironball.pos.x-ping_pong.pos.x) < (ironball.radius+ping_pong.radius) and ironball.v > ping_pong.v:
			ironball.v, ping_pong.v = collide(ironball.v,ping_pong.v,ironball.m,ping_pong.m)
		
	tmp()
	

	
def handler(data):
	rate(1,progress)
	if data != None:
		ballbump(data)
	
def progress():
	csmPull(df,handler)
	#rate(1,handler(5))
df = 'Speed'
profile = {
	'dm_name': 'ElasticCollision1',
	'df_list': [df]
}
csmRegister(profile)
rate(1,progress)