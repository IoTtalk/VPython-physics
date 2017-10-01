G=6.673E-11
mass = {'Mercury':0.055*5.97E24 , 'Venus': 0.815*5.97E24,'earth': 5.97E24, 'mars':6.42E23, 'Jupiter': 317.9*5.97E24, 'Saturn':95.2*5.97E24, 'Uranus':14.52*5.97E24, 'Neptune':17.06*5.97E24}    # ?Hdictionary ?s?n?a?y?B?o?P???e?q
d_at_perihelion = {'Mercury': 0.58E11, 'Venus': 1.075E11, 'earth': 1.495E11, 'mars':2.279E11, 'Jupiter': 7.779E11, 'Saturn':1.421E12, 'Uranus': 2.872E12, 'Neptune':4.503E12}      # ?n?eAI??A?a?y??Vo?P?i??????ZA?o
v_at_perihelion = {'Mercury': 4.789E4, 'Venus': 3.503E4, 'earth': 2.9783E4, 'mars':2.4077E4, 'Jupiter': 1.307E4, 'Saturn':9.69E3, 'Uranus': 6.81E3, 'Neptune':5.43E3}      # ?b?n?eAI??A?a?y??Vo?P??????t???

scene = display(width=1000, height=1000, background=vector(0,0,0))
sun = sphere(pos=vector(0,0,0), radius = 2.1E10, color = color.orange, texture="http://i.imgur.com/aX5wp3G.jpg?2")
scene.lights = [local_light(pos=vector(0,0,0), color=color.white)]


#class planet_c(sphere):

    #console.log(999)
def a(object):
    m_sun = 1.99E30
    #console.log("sdfdsf")
    return -norm(object.pos) * G * m_sun / mag2(object.pos) 

earth = sphere(pos = vector(d_at_perihelion['earth'],0,0),radius = 9.5E9,
                texture=textures.earth, make_trail = True, retain = 365 *24)
earth.rotate(angle = pi/2, axis=vector(1, 0, 0))
earth.m = mass['earth']
earth.v = vector(0, v_at_perihelion['earth'], 0)

mars = sphere(pos = vector(d_at_perihelion['mars'],0,0), radius = 4.9E9,
                texture=textures.wood_old, make_trail = True, retain = 700 * 24)
mars.m = mass['mars']
mars.v = vector(0, v_at_perihelion['mars'], 0)

Mercury = sphere(pos = vector(d_at_perihelion['Mercury'],0,0), radius = 3.63E9,
                texture=textures.metal, make_trail = True, retain = 116 * 24)
Mercury.m = mass['Mercury']
Mercury.v = vector(0, v_at_perihelion['Mercury'], 0)

Venus = sphere(pos = vector(d_at_perihelion['Venus'],0,0), radius = 9.025E9,
                texture=textures.wood, make_trail = True, retain = 225 * 24)
Venus.m = mass['Venus']
Venus.v = vector(0, v_at_perihelion['Venus'], 0)

Jupiter = sphere(pos = vector(d_at_perihelion['Jupiter'],0,0), radius = 1.5E10,
                texture="http://i.imgur.com/5FbL240.jpg", make_trail = True, retain = 399 * 24)
Jupiter.m = mass['Jupiter']
Jupiter.v = vector(0, v_at_perihelion['Jupiter'], 0)

Saturn = sphere(pos = vector(d_at_perihelion['Saturn'],0,0), radius = 1.3E10,
                texture=textures.stucco, make_trail = True, retain = 378 * 24)
Saturn.m = mass['Saturn']
Saturn.v = vector(0, v_at_perihelion['Saturn'], 0)

Uranus = sphere(pos = vector(d_at_perihelion['Uranus'],0,0), radius = 1.1E10,
                texture=textures.rock, make_trail = True, retain = 370 * 24)
Uranus.m = mass['Uranus']
Uranus.v = vector(0, v_at_perihelion['Uranus'], 0)

Neptune = sphere(pos = vector(d_at_perihelion['Neptune'],0,0), radius = 1.0E10,
                texture=textures.granite, make_trail = True, retain = 367 * 24)
Neptune.m = mass['Neptune']
Neptune.v = vector(0, v_at_perihelion['Neptune'], 0)

planets = [Mercury, Venus, earth, mars, Jupiter, Saturn, Uranus, Neptune]

camera_x1=0.0
camera_x2=0.0
camera_x3=-1.0
#   4. ?B????A

def run(x): 
    global camera_x1,camera_x2,camera_x3,planets
    console.log("run"+str(x))
    dt= 60*60
    x = int(x)
    if x == 1:
        camera_x1 = camera_x1 + 0.4
    elif x == 2:
        camera_x1 = camera_x1 - 0.4
    elif x == 3:
        camera_x2 = camera_x2 + 0.4
    elif x == 4:
        camera_x2 = camera_x2 - 0.4
    elif x == 5:
        camera_x3 = camera_x3 + 0.4
    elif x == 6:
        camera_x3 = camera_x3 - 0.4
    elif x == 7:
        scene.range = scene.range*0.5
    elif x == 8:
        scene.range = scene.range/0.5
    elif x == 0:
        camera_x1=0.0
        camera_x2=0.0
        camera_x3=-1.0
    scene.forward=vector(camera_x1,camera_x2,camera_x3)
    def loop():
        rate(6*24,loop)
        #console.log(earth.v)
        for planet in planets:
            planet.v = planet.v + a(planet)* dt
            planet.pos = planet.pos + planet.v * dt
    loop()
            
def handler(data):
    rate(1,progress)
    if data!= None:
       console.log("handler"+str(data))
       run(data)

def progress():
    csmPull(df,handler)

df='Command'
profile = {
     'dm_name':'PlanetRevolution2',
	 'df_list':[df]
	 
}

csmRegister(profile)

rate(1,progress)


