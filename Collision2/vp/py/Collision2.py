from visual import *
size = 0.1 #球半徑 0.1 m
speed=5
num=5

scene = display(width=600, height=600,texture="https://s3.amazonaws.com/glowscript/textures/stucco_texture.jpg") #畫面設定
scene.userspin=False
scene.userzoom=False
#scene.scale =(0.1,0.1,0.1)
scene.range=2
temp=vector(10,30,0.6) #num,mass,size
live=vector(11,0,0)


b1 = sphere(radius = size,texture="https://s3.amazonaws.com/glowscript/textures/stucco_texture.jpg" ) #畫球 1

b2 = sphere(radius = temp.z,texture="https://s3.amazonaws.com/glowscript/textures/earth_texture.jpg") #畫球 2

#b3 = sphere(radius = size,texture="https://s3.amazonaws.com/glowscript/textures/metal_texture.jpg")

b1.pos = vector( 0, -1.8, 0) #球 1 初位置

b2.pos = vector( random()-0.5 , random() , 0) #球 2 初位置

#b3.pos = vector(random()*(random()*3)-0.5 , random()*(random()*3)-0.5, 0)

b1.v = vector(0, 0, 0) #球 1 初速

b2.v = vector(0 , 0, 0) #球 2 初速

#b3.v = vector(0 , 0, 0)
wall_1=box(length=0.1, height=4, width=0, color=color.green, pos= vector(-1.95,0,0))
wall_2=box(length=0.1, height=4, width=0, color=color.green, pos= vector(1.95,0,0))
wall_3=box(length=4, height=0.1, width=0, color=color.green, pos= vector(0,1.95,0))
wall_4=box(length=4, height=0.1, width=0, color=color.green, pos= vector(0,-1.95,0))

Barrel= cylinder(pos=vector(0,-1.95,0),   axis=vector(0,0.7,0), radius=0.2)


dt = 0.001

#while True:
def ball_collision(data):
  rate(1000,ball_collision)
  
#  print(data))
  b1.pos = b1.pos+b1.v * dt
  b2.pos = b2.pos+b2.v * dt
  

    
  l=((b1.pos.x-b2.pos.x)**2+(b1.pos.y-b2.pos.y)**2+(b1.pos.z-b2.pos.z)**2)**0.5
  if temp.z<0.25:
     ball_size=0.25
  if temp.z>=0.25:
     ball_size=temp.z

  if l<=ball_size and dot(b1.v, b2.v) <= 0 :
    

     v1prime = b1.v - (b1.pos-b2.pos) * dot (b1.v-b2.v, b1.pos-b2.pos) / l**2

     v2prime = b2.v - (b2.pos-b1.pos) * dot (b2.v-b1.v, b2.pos-b1.pos) / l**2

     b1.v, b2.v = v1prime, v2prime
     s_size.text='earth live:'+str(live.x)
     temp.z=temp.z-0.05 
     live.x=live.x-1	 
     b2.radius=temp.z 
     temp.y=temp.y-1

  if temp.z<=0.05:
     s0.text='Win , 0 is restart'


     reset()
     label_off()
     b2.pos=vector(0,0,0)
     s0.visible=True
     b2.radius=2.1

  if temp.z!=0 and temp.x==0:
     s0.text='Lose, 0 is restart'
     reset()	 
  
  if b2.pos.x<-1.8:
     b2.v.x=-b2.v.x

  if b2.pos.x>1.8:
     b2.v.x=-b2.v.x

  if b2.pos.y>1.8:
     b2.v.y=-b2.v.y
     Barrel.visible= False
     label_off()

  if b2.pos.y<-1.8:
     b2.v.y=-b2.v.y

  if b1.pos.x<-1.85:
     b1.v.x=-b1.v.x
     temp.y=temp.y-1
  if b1.pos.x>1.85:
     b1.v.x=-b1.v.x
     temp.y=temp.y-1
  if b1.pos.y>1.85:
     b1.v.y=-b1.v.y
     Barrel.visible= False
     label_off()
     temp.y=temp.y-1
  if b1.pos.y<-1.85:
     b1.v.y=-b1.v.y
     temp.y=temp.y-1
  if temp.y==0:
     reset()
     temp.y=30
  s_mass.text='bullet_live:'+str(temp.y)
def handler_2(data):
  
  if data !=None:

  #   Barrel.visible= False
     if data ==1:
        b1.v=vector(-((speed+0.1)/(5**0.5)),speed/(5**0.5)*2,0)
        Barrel.axis.x=-(Barrel.axis.y/(5**0.5))
        Barrel.axis.y=Barrel.axis.y/(5**0.5)*2
        temp.x=temp.x-1
     if data ==2:
        b1.v=vector(-((speed+0.1)/2),speed/2*(3**0.5),0)
        Barrel.axis.x=-(Barrel.axis.y/2)
        Barrel.axis.y=Barrel.axis.y/2*(3**0.5)
        temp.x=temp.x-1   
     if data ==3:
        b1.v=vector(-((speed+0.1)/(2**0.5)),(speed/(2**0.5)),0)
        Barrel.axis.x=-(Barrel.axis.y/(2**0.5))
        Barrel.axis.y=Barrel.axis.y/(2**0.5)
        temp.x=temp.x-1    
     if data ==4:
        b1.v=vector(-((speed+0.1)/2*(3**0.5)),speed/2,0)
        Barrel.axis.x=-(Barrel.axis.y/2*(3**0.5))
        Barrel.axis.y=Barrel.axis.y/2
        temp.x=temp.x-1     
     if data ==5:
        b1.v=vector(0.1,speed+0.1,0)
        Barrel.axis=vector(0,0.7,0)
        temp.x=temp.x-1
     if data ==6:
        b1.v=vector(((speed+0.1)/(5**0.5)),speed/(5**0.5)*2,0)
        Barrel.axis.x=(Barrel.axis.y/(5**0.5))
        Barrel.axis.y=Barrel.axis.y/(5**0.5)*2
        temp.x=temp.x-1
     if data ==7:
        b1.v=vector(((speed+0.1)/2),speed/2*(3**0.5),0)
        Barrel.axis.x=(Barrel.axis.y/2)
        Barrel.axis.y=Barrel.axis.y/2*(3**0.5)
        temp.x=temp.x-1  
     if data ==8:
        b1.v=vector((((speed+0.1)+0.1)/(2**0.5)),(speed/(2**0.5)),0)
        Barrel.axis.x=(Barrel.axis.y/(2**0.5))
        Barrel.axis.y=Barrel.axis.y/(2**0.5)
        temp.x=temp.x-1  
     if data ==9:
        b1.v=vector(((speed+0.1)/2*(3**0.5)),speed/2,0)
        Barrel.axis.x=(Barrel.axis.y/2*(3**0.5))
        Barrel.axis.y=Barrel.axis.y/2
        temp.x=temp.x-1    
     if data ==0:
        reset()
        temp.x=10
        temp.y=30
        temp.z=0.6
        b2.pos = vector(0 ,0,0)
        b2.radius=temp.z
        s0.text='0 is restart'
     s_bullet.text='bullet num:'+str(temp.x)
def label_off():
  s1.visible=False
  s2.visible=False
  s3.visible=False
  s4.visible=False
  s5.visible=False
  s6.visible=False
  s7.visible=False
  s8.visible=False
  s9.visible=False
  s0.visible=False
def label_on():
  s1.visible=True
  s2.visible=True
  s3.visible=True
  s4.visible=True
  s5.visible=True
  s6.visible=True
  s7.visible=True
  s8.visible=True
  s9.visible=True
  s0.visible=True
def reset():
  Barrel.axis=vector(0,0.7,0)
  b1.v=vector(0,0,0)
  b2.v=vector(0,0,0)
  b1.pos = vector( 0, -1.8, 0)

  Barrel.visible= True
  label_on()
  '''
def handler_2(data):

  if data != None:

     data=int(data)
     if data ==1:
        b1.pos.x=b1.pos.x-0.2
        b1.pos.y=b1.pos.y+0.2
     if data ==2:
        b1.pos.y=b1.pos.y+0.2
     if data ==3:
        b1.pos.x=b1.pos.x+0.2
        b1.pos.y=b1.pos.y+0.2
     if data ==4:
        b1.pos.x=b1.pos.x-0.2
     if data ==5:
        b1.pos=vector(0.6,0,0)
     if data ==6:
        b1.pos.x=b1.pos.x+0.2
     if data ==7:
        b1.pos.x=b1.pos.x-0.2
        b1.pos.y=b1.pos.y-0.2
     if data ==8:
        b1.pos.y=b1.pos.y-0.2
     if data ==10:
        b1.pos.x=b1.pos.x+0.2
        b1.pos.y=b1.pos.y-0.2

'''
s1=label(pos=vector(-0.35,-1.1,0), text='1')
s2=label(pos=vector(-0.5,-1.25,0), text='2')
s3=label(pos=vector(-0.65,-1.4,0), text='3')
s4=label(pos=vector(-0.8,-1.55,0), text='4')
s5=label(pos=vector(0,-1,0), text='5')
s6=label(pos=vector(0.35,-1.1,0), text='6')
s7=label(pos=vector(0.5,-1.25,0), text='7')
s8=label(pos=vector(0.65,-1.4,0), text='8')
s9=label(pos=vector(0.8,-1.55,0), text='9')
s0=label(pos=vector(0,0.25,0), text='0 is restart')
s_bullet=label(pos=vector(1.5,-1.85,0),text='bullet num:10')
s_mass=label(pos=vector(1.5,-1.65,0),text='bullet live:')
s_size=label(pos=vector(1.5,-1.45,0),text='earth live:12')
def progress():
#   csmPull(df_1,handler_1)
   csmPull(df_2,handler_2)
#  csmPull(df_3,handler_3)
   rate(1,progress)


#df_1='Direction'
df_2='Command'
#df_3='speed'

profile={
    'dm_name':'Collision2',
    'df_list':[df_2]
}

csmRegister(profile)
rate(1,ball_collision)

rate(1,progress)
