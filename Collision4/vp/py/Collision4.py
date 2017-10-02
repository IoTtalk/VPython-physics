#  1.  畫面設定
scene1 = display(width=600, height=400, background=vector(0.5,0.6,0.5), y=0)
arrow1 = arrow(display=scene1, pos=vector(-1,0,0), axis=vector(2,0,0), shaftwidth=0.005)
arrow4 = arrow(display=scene1, pos=vector(0,0,0), axis=vector(0,0.3,0), shaftwidth=0.005)

gd1 = gdisplay(x=600, y=0, title='v vs t', xtitle='t', ytitle='v', ymax=1, xmax=2, background=vector(0.3,0.3,0.3))
vt1 = gcurve(gdisplay=gd1, color=vector(0.5, 0.5, 0.5))
vt2 = gcurve(gdisplay=gd1, color=color.orange)
vts= (vt1, vt2)

#  2.  物體設定
ironball = sphere(display=scene1, radius=0.05, pos=vector(-0.2,0,0), color=vector(0.5, 0.5, 0.5)) 
ironball.m, ironball.v = (pi*4/3*(0.05)**3)*7.9*1e3, 0

ping_pong = sphere(display=scene1, radius=0.02, pos=vector(0.1,0,0), color=color.orange)
ping_pong.m, ping_pong.v = 2.6*10e-3, 0
balls=(ironball, ping_pong)

#  3.  定義函數
def collide(spd):

	ironball.v = spd
	
	def resetScene():
		scene1.background = vector(0.5, 0.6, 0.5)
	
	def collision():
		rate(200, collision)
		
		v1f = ironball.v*(ironball.m-ping_pong.m)/(ironball.m+ping_pong.m) + ping_pong.v*2*ping_pong.m/(ironball.m+ping_pong.m)
		v2f = ironball.v*2*ironball.m/(ping_pong.m+ironball.m) + ping_pong.v*(ping_pong.m-ironball.m)/(ping_pong.m+ironball.m)
			
		ironball.pos.x += ironball.v*dt
		vt1.plot(pos=(t,ironball.v))
		
		ping_pong.pos.x += ping_pong.v*dt
		vt2.plot(pos=(t,ping_pong.v))
		
		if abs(ironball.pos.x-ping_pong.pos.x) < (ironball.radius+ping_pong.radius) and ironball.v > ping_pong.v:
			ironball.v = v1f
			ping_pong.v = v2f
        
		if(ping_pong.pos.x >= 1):
			scene1.background = vector(0,0,0)
			rate(4, resetScene)
			ironball.v = 0
			ironball.pos.x = -0.2
			ping_pong.v = 0
			ping_pong.pos.x = 0.1
		
		
	collision()

#  4.  物體運動
dt = 0.001
t = 0

def handler(data):
	rate(1, progress)
	if data != None:
		collide(data/10)
	
def progress():
	csmPull(df, handler)
	
df='Velocity'
profile = {
	'dm_name' : 'Collision4',
	'df_list' : [df]
}

csmRegister(profile)

rate(1, progress)
