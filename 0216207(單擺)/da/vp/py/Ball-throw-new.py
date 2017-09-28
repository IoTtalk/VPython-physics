
g=9.8
size = 0.7
scene = display(title='Bouncing_Ball', width=800, height=800, background=(0.6,0.3,0.2), center=(0,7,0))
floor = box(length=24, height=0.5, width=4, color=color.green, pos= (-9,0,0))
box(length=8, height=0.5, width=4, color=color.red, pos= (7,0,0) )
box(length=8, height=0.5, width=4, color=color.green, pos= (15,0,0) )

scene.range=18
camera_x1=0.8
camera_x2=0.0
scene.forward=(camera_x1,camera_x2,-1)
scene.center=(-7,7,0)


def balljump(spd):
    ball = sphere(pos=(-24.5, 10.0, 0.0), radius=size, color=color.white)
    ball.velocity = vector(spd, -1.0, 0.0)

    dt = 0.003
    playFlag=0
	
	def resetScene:
		scene.background=(0.6,0.3,0.2)
    
    def jump():
		if ball.pos.x < 15:
			rate(1000,jump)
		else
			ball.visible = False
			gj_playFlag = 1
			
        if (ball.pos.x < 10 and ball.pos.x > 1.5) and ball.pos.y < 1 :
            scene.background = (0,0,0)
			rate(4,resetScene)
		
        previous_x = ball.pos.x
        ball.pos = ball.pos + ball.velocity * dt

        if ball.y < size and ball.velocity.y < 0:
            ball.velocity.y = - ball.velocity.y

        else:
            ball.velocity.y = ball.velocity.y - g * dt
	jump()

    

def handler(data):
	rate(1,progress)
	balljump(data)

def progress():
	rate(1,handler(5))
	
rate(1,progress)

