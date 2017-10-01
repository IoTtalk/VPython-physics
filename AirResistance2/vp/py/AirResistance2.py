
g = 9.8
size = 0.25

scene = display(title='bouncing projectile',center = vector(0,5,0),width = 1200 ,height = 800, background = vector(0.5,0.5,0))
floor = box(length = 100,height = 0.01 , weight = 4 , color = color.blue)
ball = sphere(radius = size , color = color.red ,make_trail = false)
##ruler1 = ruler.ruler(vector(-15,0,1),vector(1,0,0),unit = 2.0 , length = 30.0 ,thickness = 0.2)
##ruler2 = ruler.ruler(vector(-15,0,1),vector(0,1,0),unit = 1.0 , length = 10.0 ,thickness = 0.2)


ball.visible = False;
def fall(spd):

    ball.velocity = vector(spd,0.0,0.0)
    ball.pos = vector(-50.0,10.0,0.0)
    ball.visible = True;

    drag_coef = 0.42
    drag_power = 1.0
    dt = 0.002
    def drop():
        d = drag_coef * (ball.velocity^drag_power)
        if ball.pos.x < 50.0:
            rate(1000,drop)
        if ball.velocity.y < 0 :
            ball.velocity.y += (d * dt * 3.6)
        else:
            ball.velocity.y -= (d * dt * 3.6)
        if ball.velocity.x > 0:
            ball.velocity.x -= (d * dt * 0.47)
        ball.pos = ball.pos + ball.velocity * dt

        if ball.pos.y < size and ball.velocity.y < 0:
            ball.velocity.y = - ball.velocity.y
        else:
            ball.velocity.y = ball.velocity.y - (g * dt)


    drop()


def handler(data):
    rate(1, progress)
    if data != None:
        fall(data)

def progress():
    csmPull(df, handler)

df='Command'

profile = {
     'dm_name':'AirResistance2',
     'df_list':[df]
}
csmRegister(profile)

rate(1,progress)


