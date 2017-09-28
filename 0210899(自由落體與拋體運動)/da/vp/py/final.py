size = 0.25
height = 15.0

scene = display(width=800, height=800, center = vector(0, height/2, 0), background=vector(0.5, 0.5, 0))
floor = box(length=30, height=0.01, width=10, color=color.blue)

def ballfall(data):
    ball = sphere(radius = size, color = color.red)
    ball.pos = vector(0, height, 0)
    ball.velocity = vector(0,0,0)
    dt = 0.001
    g = data

    def fall():
        if ball.pos.y >= size:
            rate(1000, fall)
        else:
            ball.visible = False
        ball.pos = ball.pos + ball.velocity * dt
        ball.velocity.y += -g*dt
    
    fall()
	
def handler(data):
    rate(1, progress)
    ballfall(data)
	
def progress():
    csmPull(df, handler)	

df = 'gValue'
profile = {
    'dm_name' : 'Free-Fall',
    'df_list' : [df]
}	

csmRegister(profile)
	
rate(1, progress)	