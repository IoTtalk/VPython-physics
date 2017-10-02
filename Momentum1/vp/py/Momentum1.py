from visual import *
#  1. 參數設定
density ={'wood':400.0, 'metal':900.0, 'earth':2600.0}       #物質密度 單位: kg/m**3
size = 0.05             #球半徑 0.05 m
L = 1.00                #地板長
dt = 0.001       	#兩連續畫面間之時間間隔
V = (4/3)*pi*(size)**3	#體積
P = 0.1             	#初始動量 kg*m/s
winflag=False
#  2. 畫面設定
#pos是中心點
scene = display(width=800, height=800, background=vector(1/2.55,1.5/2.55,1/2.55))
bottom = box(pos=vector(0,0,0), length=2*L, height=0.001, width=2,color=color.white*1.8,texture=textures.wood_old)
goal1 = box(pos=vector(random()-0.5,0,-0.40), length=0.25, height=0.0011, width=0.4,color=color.red*2)
goal2 = box(pos=vector(random()-0.5,0,0), length=0.25, height=0.0011, width=0.4,color=color.red*2)
goal3 = box(pos=vector(random()-0.5,0,0.40), length=0.25, height=0.0011, width=0.4,color=color.red*2)
wall = box(pos=vector(L,size/2,0), length=0.01, height=size, width=2,color=vector(1.08,0.51,10.1))#length, height, width==x, y, z
wintext=label(pos=vector(0,0,-1), text='balls -> red cell',height=40)
#  3. 球的設定
balls = {}
balls['wood'] = sphere(pos=vector(-L,size,-0.40), radius=size, color=color.white*2,texture=textures.wood)
balls['metal'] = sphere(pos=vector(-L,size,0), radius=size, color=color.white*1.5,texture=textures.metal)
balls['earth'] = sphere(pos=vector(-L,size,0.40), radius=size, color=color.white*2,texture=textures.earth)

for material in ['wood','metal','earth']:
    balls[material].m = V*density[material]
    balls[material].v = P/balls[material].m

#  4. 運動
def move():
    global winflag
    if(not winflag):
        rate(1000,move)
    for material in ['wood','metal','earth']:
        balls[material].pos.x += balls[material].v *dt
        balls[material].rotate(axis=vector(0,0,1), angle=-balls[material].v*dt/size)
        if balls[material].pos.x >= L-size :
            balls[material].pos.x -= 2*L
    if(balls['wood'].pos.x>goal1.pos.x-goal1.length/2 and balls['wood'].pos.x<goal1.pos.x+goal1.length/2) and\
      (balls['metal'].pos.x>goal2.pos.x-goal2.length/2 and balls['metal'].pos.x<goal2.pos.x+goal2.length/2) and\
      (balls['earth'].pos.x>goal3.pos.x-goal3.length/2 and balls['earth'].pos.x<goal3.pos.x+goal3.length/2):
        wintext.text='Win!!'
        winflag=True
        wintext.color=color.yellow
        return
def handler(data):
    rate(10,progress)
    if data != None:
        SetMass(data)
def progress():
    csmPull(df,handler)

df='BallNumber'
profile={
    'dm_name':'Momentum1',
    'df_list':[df]
}
csmRegister(profile)

rate(1,progress)
rate(1,move)

def SetMass(num):
    global P
    #print(num)
    if num in [1,2,3]:
        #print(1)
        material='wood'
    elif num in [4,5,6]:
        #print(2)
        material='metal'
    elif num in [7,8,9]:
        #print(3)
        material='earth'
    elif num in [0]:
        #print(0)
        refresh()
        return
    elif num in [10]:
        goal1.length-=0.05
        goal2.length-=0.05
        goal3.length-=0.05
        return
    elif num in [11]:
        goal1.length+=0.05
        goal2.length+=0.05
        goal3.length+=0.05
        return
    else:
        return
    balls[material].radius=(1/(((num-1)%3)/5+1))*0.05
    balls[material].pos.y=balls[material].radius
    V = (4/3)*pi*(balls[material].radius)**3
    balls[material].m = V*density[material]
    balls[material].v = P/balls[material].m

def refresh():
    global winflag,size,P,V
    balls['wood'].pos=vector(-L,size,-0.40)
    balls['wood'].radius=size
    balls['wood'].color=color.white*2
    balls['wood'].texture=textures.wood
    
    balls['metal'].pos=vector(-L,size,0)
    balls['metal'].radius=size
    balls['metal'].color=color.white*1.5
    balls['metal'].texture=textures.metal
    
    balls['earth'].pos=vector(-L,size,0.40)
    balls['earth'].radius=size
    balls['earth'].color=color.white*2
    balls['earth'].texture=textures.earth
    for material in ['wood','metal','earth']:
        balls[material].m = V*density[material]
        balls[material].v = P/balls[material].m
    
    wintext.text='balls -> red cell'
    wintext.color=color.white
    
    goal1.length=0.25
    goal2.length=0.25
    goal3.length=0.25
    
    if winflag==True:
        rate(1,move)
        goal1.pos.x=random()-0.5
        goal2.pos.x=random()-0.5
        goal3.pos.x=random()-0.5
        winflag=False
    