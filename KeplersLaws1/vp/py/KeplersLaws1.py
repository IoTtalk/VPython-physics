#Kepler's Laws.py

# plots the orbit of a planet in an eccentric orbit to illustrate
# the sweeping out of equal areas in equal times, with sun at focus
# The eccentricity of the orbit is random and determined by the initial velocity
# program uses normalised units (G =1)

# program by Peter Borcherds, University of Birmingham, England


scene = display(title = "Kepler's law of equal area", width=1000, height=1000, range=3.2)
duration = 'Period: '
sun = sphere(color = color.yellow, radius = 0.1)    # motion of sun is ignored (or centre of mass coordinates)
scale = 1
poss = vector(0,scale,0)  
#planet = sphere(pos = poss, color = color.cyan, radius = 0.02)
#pla
def move(data):

	planet = sphere(pos = data*poss, color = color.cyan, radius = data/100)
	#for i in [1,10]:
	#	pla[i] = sphere(pos = poss, color = color.cyan, radius = data/100)
	def movemove():
		
		velocity = vector(-0.7,0,0)          # gives a satisfactory range of eccentricities
		##velocity = -vector(0.984,0,0)   # gives period of 12.0 "months"
		speed = mag(velocity)
		steps = 5
		dt = 0.5 / float(steps)
		step = 0
		#time = 0
		ccolor = color.white
		oldpos = vector(planet.pos)
		#ccolor = MonthStep(time)
		curve(pos=[sun.pos, planet.pos], color = color.blue)  
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
				#if step%5 == 0:
					curve(pos=[sun.pos, planet.pos], color = color.blue)
				#else:
					#plot radius vector
				#	curve(pos=[sun.pos, planet.pos], color = color.blue)
	
  
    #MonthStep(time, 50, 0)
    #label(pos=(2.5,-2.5,0), text='Click for another orbit')
    #scene.mouse.getclick()
    #for obj in scene.objects:
    #    if obj is sun or obj is planet: continue
    #    obj.visible = 0  # clear the screen to do it again
		k()
	movemove()
def handler(data):
	rate(1, progress)
	if data != None and data !=1:
		move(data)
	#else :
	#	move(2)
    
def progress():
    csmPull(df,handler)

df = 'Command'
profile = {
    'dm_name': 'KeplersLaws1',
    'df_list': [df]
}
csmRegister(profile)

rate(1, progress)
		
