from visual import *

g = 9.8
r = 0.5
n = 0
p = -1.6

scene = display(width = 800, height = 800, center = vector(0, -0.2, 0), background = vector(0.3,0.75,0))
ceiling = box(length = 3, height = 0.05, width = 0.8, color = color.red)

dt = 0.001



def Hookeball(w):
	global p
	ball = sphere(color = color.blue)
	spring = helix(radius = 0.02, thickness = 0.01)
	ball.pos = vector(p, -r, 0)
	spring.pos = vector(p, 0 ,0)
	ball.v = vector(0, 0, 0)
	spring.axis = ball.pos - spring.pos
	size = 0.06
	if w == 1:
		ball.m = 0.2
		ball.k = 50
	if w == 2:
		ball.m = 0.8
		ball.k = 50
	if w == 3:
		ball.m = 1.4
		ball.k = 50
	if w == 4:
		size = 0.03
		ball.m = 0.8
		ball.k = 50
	if w == 5:
		size = 0.05
		ball.m = 0.8
		ball.k = 50
	if w == 6:
		size = 0.07
		ball.m = 0.8
		ball.k = 50
	if w == 7:
		ball.m = 0.8
		ball.k = 20	
	if w == 8:
		ball.m = 0.8
		ball.k = 50
	if w == 9:
		ball.m = 0.8
		ball.k = 80
	ball.radius = size	
	
	label_m = label(pos = vector(p, 0.4, 0), text = 'M = ' + ball.m)
	label_size = label(pos = vector(p, 0.3, 0), text = 'Size = ' + size)
	label_k = label(pos = vector(p, 0.2, 0), text = 'K = ' + ball.k)
	p = p + 0.4
	def exe():
		rate(500, exe)
		spring.axis = ball.pos - spring.pos
		spring_force = -ball.k * (mag(spring.axis) - r) * spring.axis / mag(spring.axis)
		ball.a = vector(0, -g, 0) + spring_force / ball.m
		ball.v = ball.v + ball.a*dt
		ball.pos =  ball.pos + ball.v*dt
	exe()

def handler(data):
	rate(1, progress)
	if data != None:
		Hookeball( data )
def progress():
	csmPull( 'Speed', handler )

df = 'Speed'
profile = {
	'dm_name' : 'HookesLaw1',
	'df_list' : [df]
}

csmRegister( profile )

rate( 1, progress )