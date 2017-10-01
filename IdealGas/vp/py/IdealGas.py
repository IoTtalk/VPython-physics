MaxN = 9
L = ((24.4E-3/(6E23))*MaxN)**(1/3.0)/2
m, size = 4E-3/6E23, 310E-12
L_size = L-size
k, T = 1.38E-23, 450.0#298.0 or 500 or 4000.0
time, dt = 0, 0.5E-13
vrms = (3*k*T/m)**0.5
atoms = []
momentum = 0
#initialization of display
scene = display(width=800, height=800, background=vector(0.2, 0.2, 0))
container = box(length=2*L, height=2*L, width=2*L, opacity=0.2, color=color.yellow)
for i in range(MaxN):
    position = vector(-L_size+2*L_size*random(), -L_size+2*L_size*random(), -L_size+2*L_size*random())
    if i == 0:
        atom = sphere(pos=position, radius=size, color=color.yellow, make_trail=True, retain=10)
    else:
        atom = sphere(pos=position, radius=size, color=vector(random(), random(), random()))
    ra, rb = pi*random(), 2*pi*random()
    atom.m, atom.v = m, vector(vrms*sin(ra)*cos(rb), vrms*sin(ra)*sin(rb), vrms*cos(ra))
    atoms.append(atom)

def vcollision(a1, a2):
    v1prime = a1.v-2*a2.m/(a1.m+a2.m)*(a1.pos-a2.pos)*dot(a1.v-a2.v, a1.pos-a2.pos)/((a1.pos.x-a2.pos.x)**2+(a1.pos.y-a2.pos.y)**2+(a1.pos.z-a2.pos.z)**2)
    v2prime = a2.v-2*a1.m/(a1.m+a2.m)*(a2.pos-a1.pos)*dot(a2.v-a1.v, a2.pos-a1.pos)/((a1.pos.x-a2.pos.x)**2+(a1.pos.y-a2.pos.y)**2+(a1.pos.z-a2.pos.z)**2)
    return v1prime, v2prime
def animate(N):
    for i in range(N):
        atoms[i].pos = atoms[i].pos + atoms[i].v*dt
    for target in range(N-1):
        for later in range(target, N):
            if (atoms[target].pos.x-atoms[later].pos.x)**2+(atoms[target].pos.y-atoms[later].pos.y)**2+(atoms[target].pos.z-atoms[later].pos.z)**2 <= (2*size)**2 and dot(atoms[target].pos-atoms[later].pos, atoms[target].v-atoms[later].v) < 0:
                atoms[target].v, atoms[later].v = vcollision(atoms[target], atoms[later])
                atoms[target].color, atoms[later].color = color.red, color.red
    for n in range(N):
        if abs(atoms[n].pos.x) >= L_size and atoms[n].pos.x*atoms[n].v.x > 0:
            atoms[n].v.x = - atoms[n].v.x
            momentum += 2*m*abs(atoms[n].v.x)
        if abs(atoms[n].pos.y) >= L_size and atoms[n].pos.y*atoms[n].v.y > 0:
            atoms[n].v.y = - atoms[n].v.y
            momentum += 2*m*abs(atoms[n].v.y)         
        if abs(atoms[n].pos.z) >= L_size and atoms[n].pos.z*atoms[n].v.z > 0:
            atoms[n].v.z = - atoms[n].v.z
            momentum += 2*m*abs(atoms[n].v.z)
def handler(nBase):
    if nBase != None:
        if nBase == 0:
            for index in range(MaxN):
                atoms[index].visible = False
        else:
            for index in range(nBase, MaxN):
                atoms[index].visible = False
            for index in range(nBase):
                atoms[index].visible = True
            animate(nBase)
    else:
        animate(MaxN)
    time += dt
    csmPush(df0, (momentum/(6*(2*L)**2*time)))
    rate(1/dt, progress)
def progress():
#handler(int(random()*10)%(MaxN+1))
    csmPull(df1, handler)

df1 = 'AtomNumber'
df0 = 'BarPressure'
profile = {
    'dm_name': 'IdealGas',
    'df_list': [df0, df1]
}

csmRegister(profile)
progress()
#rate(1, progress)