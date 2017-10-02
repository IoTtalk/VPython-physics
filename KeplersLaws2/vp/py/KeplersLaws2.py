#Kepler's Laws.py

# plots the orbit of a planet in an eccentric orbit to illustrate
# the sweeping out of equal areas in equal times, with sun at focus
# The eccentricity of the orbit is random and determined by the initial velocity
# program uses normalised units (G =1)

# program by Peter Borcherds, University of Birmingham, England


def MonthStep(time, offset = 20, whole = 1): # mark the end of each "month"
    global ccolor   # have to make it global, since label uses it before it is updated
    if whole :
        Ltext = str(int(time *2 + dt))  #end of 'month', printing twice time gives about 12 'months' in 'year'
    else:
        Ltext =  duration + str(time * 2) +' "months"\n Initial speed: ' + str(round(speed, 3))
        ccolor = color.white
    label(pos=planet.pos, text = Ltext, color= ccolor,
          xoffset = offset * planet.pos.x, yoffset = offset * planet.pos.y)
    ccolor = (0.5*(1+random()),random(),random())   #randomise colour of radial vector
    return ccolor

scene = display(title = "Kepler's law of equal areas", width=1000, height=1000, range=3.2)
duration = 'Period: '
sun = sphere(color = color.yellow, radius = 0.1)    # motion of sun is ignored (or centre of mass coordinates)
scale = 1.0
poss = vector(0,scale,0)  
s = 0
#planet = sphere(pos = poss, color = color.cyan, radius = 0.04)

def move(data1):
	
	def movemove():
		
		          # gives a satisfactory range of eccentricities
		##velocity = -vector(0.984,0,0)   # gives period of 12.0 "months"
		#speed = mag(velocity)
		steps = 5
		dt = 0.5 / float(steps)
		step = 0
		#time = 0
		ccolor = color.white
		if data1 != None:
			if data1 == 2:
				planet = sphere(pos = poss, color = color.cyan, radius = 0.04)
				velocity = vector(-0.9 ,0,0)
			else if data1 == 3:
				planet = sphere(pos = poss, color = color.red, radius = 0.06)
				velocity = vector(-0.9 ,0,0)
			else if data1 == 4:
				planet = sphere(pos = poss, color = color.blue, radius = 0.08)
				velocity = vector(-1.0 ,0,0)
			else if data1 == 5:
				planet = sphere(pos = poss, color = color.orange, radius = 0.02)
				velocity = vector(-1.1 ,0,0)
			else if data1 == 6:
				planet = sphere(pos = poss, color = color.magenta, radius = 0.05)
				velocity = vector(-1.15 ,0,0)
			else if data1 == 7:
				planet = sphere(pos = poss, color = color.blue, radius = 0.047)
				velocity = vector(-1.2 ,0,0)
			else if data1 == 8:
				planet = sphere(pos = poss, color = color.green, radius = 0.09)
				velocity = vector(-1.25 ,0,0)
			else if data1 == 9:
				planet = sphere(pos = poss, color = color.white, radius = 0.095)
				velocity = vector(-1.28 ,0,0)
			else :
				planet = sphere(pos = poss, color = color.black, radius = 0.07)
				velocity = vector(-1.28 ,0,0)
		oldpos = vector(planet.pos)
		#ccolor = MonthStep(time)
		#curve(pos=[sun.pos, planet.pos], color = ccolor)  
		def k():
			
			rate(10,k)
			oldpos = vector(planet.pos)
			if!(oldpos.x >0 and planet.pos.x<0):
				
			
			#rate (steps*2)                  #keep rate down so that development of orbit can be followed
			#time = time + dt
			
     # construction vector(planet.pos) makes oldpos a varible in its own right
												# oldpos = planet.pos makes "oldposs" point to "planet.pos"
												# oldposs = planet.pos[:] does not work, because vector does not permit slicing
				denom = mag(planet.pos) ** 3
				velocity.x = velocity.x - planet.pos.x * dt /denom				#inverse square law; force points toward sun
				velocity.y = velocity.y - planet.pos.y * dt /denom
				velocity.z = velocity.z - planet.pos.z * dt /denom
				planet.pos.x = planet.pos.x + velocity.x* dt
				planet.pos.y = planet.pos.y + velocity.y* dt
				planet.pos.z = planet.pos.z + velocity.z* dt

				# plot orbit
				
					
				
				curve(pos =[oldpos, planet.pos], color = color.red)
				#step = step + 1
				step+=1
				if step == steps:
					step = 0
					
					#ccolor = MonthStep(time)
					curve(pos=[sun.pos, planet.pos], color = color.red)
				#else:
					#plot radius vector
					#if(data1==5):
						#curve(pos=[sun.pos, planet.pos], color = color.green)
					#else:
						#curve(pos=[sun.pos, planet.pos], color = color.green)
			
  
    #MonthStep(time, 50, 0)
    #label(pos=(2.5,-2.5,0), text='Click for another orbit')
    #scene.mouse.getclick()
    #for obj in scene.objects:
    #    if obj is sun or obj is planet: continue
    #    obj.visible = 0  # clear the screen to do it again
		k()
	movemove()
def handler(data):
	rate(1,progress)
	if data != None:
		move(data)
def progress():
    csmPull(df,handler)

df = 'Command'
profile = {
    'dm_name': 'KeplersLaws2',
    'df_list': [df]
}
csmRegister(profile)

rate(1, progress)
		
