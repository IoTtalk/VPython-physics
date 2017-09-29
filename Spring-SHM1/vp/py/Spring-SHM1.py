g = 9.8             #���O�[�t�� 9.8 m/s^2
size1 = 0.03         #�y�b�| 0.05 m
size2 = 0.05
size3 = 0.1
size4 = 0.03         #�y�b�| 0.05 m
size5 = 0.05
size6 = 0.1
size7 = 0.03         #�y�b�| 0.05 m
size8 = 0.05
size9 = 0.1

r1 = 1             #�u®��� 0.5m
r2 = 1
r3 = 1
r4 = 0.7             #�u®��� 0.5m
r5 = 0.7
r6 = 0.7
r7 = 0.5             #�u®��� 0.5m
r8 = 0.5
r9 = 0.5

m1 = 0.1             #�y��q 0.2 kg
m2 = 0.3
m3 = 0.5
m4 = 0.1             #�y��q 0.2 kg
m5 = 0.3
m6 = 0.5
m7 = 0.1             #�y��q 0.2 kg
m8 = 0.3
m9 = 0.5

k = 10              #�u®�O�`�� 10 N/m
k1 = 20

scene = display(width=800, height=800, center=vector(0, -r1*0.6, 0), background=vector(0.5,0.5,0))  #�]�w�e��
ceiling = box(length=0.8, height=0.005, width=0.8, color=color.white)                    #�e�Ѫ�O

ball1 = sphere(radius = size1,  color=color.red)                              #�e�y
spring1 = helix(radius=0.02, thickness =0.01, color = color.red)     
spring1.pos = vector(-0.3,0,-0.3)                           #�e�u®,���ʺݦb(0,0,0)
ball1.pos0 = vector(-0.3, -r1, -0.3)#�y�����m�A�Y�u®�B�ʺݪ����m
ball1.pos = vector(-0.3, -r1 , -0.3)#�y�b�ɶ��ע��ɪ���m
ball1.v = vector(0, 0, 0)    #�y��t
spring1.visible = False
ball1.visible = False

ball2 = sphere(radius = size2,color = color.red)
spring2 = helix(radius=0.02, thickness = 0.01, color = color.red)
spring2.pos = vector(0,0,-0.3)
ball2.pos0 = vector(0, -r2, -0.3)
ball2.pos = vector(0, -r2, -0.3)
ball2.v = vector(0, 0, 0)
spring2.visible = False
ball2.visible = False

ball3 = sphere(radius = size3,color = color.red)
spring3 = helix(radius=0.02, thickness = 0.01, color = color.red)
spring3.pos = vector(0.3,0,-0.3)
ball3.pos0 = vector(0.3, -r3, -0.3)
ball3.pos = vector(0.3, -r3, -0.3)
ball3.v = vector(0, 0, 0)
spring3.visible = False
ball3.visible = False

ball4 = sphere(radius = size4,  color=color.yellow)                              #�e�y
spring4 = helix(radius=0.02, thickness =0.01, color = color.yellow)     
spring4.pos = vector(-0.3,0, 0)                           #�e�u®,���ʺݦb(0,0,0)
ball4.pos0 = vector(-0.3, -r4, 0)#�y�����m�A�Y�u®�B�ʺݪ����m
ball4.pos = vector(-0.3, -r4 , 0)#�y�b�ɶ��ע��ɪ���m
ball4.v = vector(0, 0, 0)    #�y��t
spring4.visible = False
ball4.visible = False

ball5 = sphere(radius = size5,color = color.yellow)
spring5 = helix(radius=0.02, thickness = 0.01, color = color.yellow)
spring5.pos = vector(0,0,0)
ball5.pos0 = vector(0, -r5, 0)
ball5.pos = vector(0, -r5, 0)
ball5.v = vector(0, 0, 0)
spring5.visible = False
ball5.visible = False

ball6 = sphere(radius = size6,color = color.yellow)
spring6 = helix(radius=0.02, thickness = 0.01, color = color.yellow)
spring6.pos = vector(0.3,0,0)
ball6.pos0 = vector(0.3, -r6, 0)
ball6.pos = vector(0.3, -r6, 0)
ball6.v = vector(0, 0, 0)
spring6.visible = False
ball6.visible = False

ball7 = sphere(radius = size7,  color=color.white)                              #�e�y
spring7 = helix(radius=0.02, thickness =0.01, color = color.white)     
spring7.pos = vector(-0.3,0,0.3)                           #�e�u®,���ʺݦb(0,0,0)
ball7.pos0 = vector(-0.3, -r7, 0.3)#�y�����m�A�Y�u®�B�ʺݪ����m
ball7.pos = vector(-0.3, -r7 , 0.3)#�y�b�ɶ��ע��ɪ���m
ball7.v = vector(0, 0, 0)    #�y��t
spring7.visible = False
ball7.visible = False

ball8 = sphere(radius = size8,color = color.white)
spring8 = helix(radius=0.02, thickness = 0.01, color = color.white)
spring8.pos = vector(0,0,0.3)
ball8.pos0 = vector(0, -r8, 0.3)
ball8.pos = vector(0, -r8, 0.3)
ball8.v = vector(0, 0, 0)
spring8.visible = False
ball8.visible = False

ball9 = sphere(radius = size9,color = color.white)
spring9 = helix(radius=0.02, thickness = 0.01, color = color.white)
spring9.pos = vector(0.3,0,0.3)
ball9.pos0 = vector(0.3, -r9, 0.3)
ball9.pos = vector(0.3, -r9, 0.3)
ball9.v = vector(0, 0, 0)
spring9.visible = False
ball9.visible = False

dt = 0.001
def move(data):
	console.log(data)
	console.log("in move")
	if (data == 1):
		spring1.visible = True
		ball1.visible = True
		console.log("1 pressed")
	if data == 2:
		spring2.visible = True
		ball2.visible = True
		console.log("2 pressed")
	if data == 3:
		spring3.visible = True
		ball3.visible = True
		console.log("3 pressed")
	if data == 4:
		spring4.visible = True
		ball4.visible = True
		console.log("4 pressed")
	if data == 5:
		spring5.visible = True
		ball5.visible = True
		console.log("5 pressed")
	if data == 6:
		spring6.visible = True
		ball6.visible = True
		console.log("6 pressed")
	if data == 7:
		spring7.visible = True
		ball7.visible = True
		console.log("7 pressed")
	if data == 8:
		spring8.visible = True
		ball8.visible = True
		console.log("8 pressed")
	if data == 9:
		spring9.visible = True
		ball9.visible = True
		console.log("9 pressed")
	if data == 0:
		console.log("0 pressed")
		spring1.visible = False
		ball1.visible = False
		spring2.visible = False
		ball2.visible = False
		spring3.visible = False
		ball3.visible = False
		
		spring4.visible = False
		ball4.visible = False
		spring5.visible = False
		ball5.visible = False
		spring6.visible = False
		ball6.visible = False
		
		spring7.visible = False
		ball7.visible = False
		spring8.visible = False
		ball8.visible = False
		spring9.visible = False
		ball9.visible = False
	
	
def come1():
	rate(1000,come1)
	spring1.axis = ball1.pos - spring1.pos#�u®�������׼u®���ʺݪ���m�V�q��y�{�b����m�V�q
	ball1.a = vector(0, - g - k * (ball1.pos.y - ball1.pos0.y )/m1 , 0)#�y���[�t�ת�y���q = - g - k*(�u®�����q)/m
	ball1.v = ball1.v + ball1.a*dt
	ball1.pos = ball1.pos + ball1.v*dt
def come2():
	rate(1000,come2)
	spring2.axis = ball2.pos - spring2.pos#�u®�������׼u®���ʺݪ���m�V�q��y�{�b����m�V�q
	ball2.a = vector(0, - g - k * (ball2.pos.y - ball2.pos0.y )/m2 , 0)#�y���[�t�ת�y���q = - g - k*(�u®�����q)/m
	ball2.v = ball2.v + ball2.a*dt
	ball2.pos = ball2.pos + ball2.v*dt
def come3():
	rate(1000,come3)
	spring3.axis = ball3.pos - spring3.pos#�u®�������׼u®���ʺݪ���m�V�q��y�{�b����m�V�q
	ball3.a = vector(0, - g - k * (ball3.pos.y - ball3.pos0.y )/m3 , 0)#�y���[�t�ת�y���q = - g - k*(�u®�����q)/m
	ball3.v = ball3.v + ball3.a*dt
	ball3.pos = ball3.pos + ball3.v*dt
def come4():
	rate(1000,come4)
	spring4.axis = ball4.pos - spring4.pos#�u®�������׼u®���ʺݪ���m�V�q��y�{�b����m�V�q
	ball4.a = vector(0, - g - k * (ball4.pos.y - ball4.pos0.y )/m4 , 0)#�y���[�t�ת�y���q = - g - k*(�u®�����q)/m
	ball4.v = ball4.v + ball4.a*dt
	ball4.pos = ball4.pos + ball4.v*dt
def come5():
	rate(1000,come5)
	spring5.axis = ball5.pos - spring5.pos#�u®�������׼u®���ʺݪ���m�V�q��y�{�b����m�V�q
	ball5.a = vector(0, - g - k * (ball5.pos.y - ball5.pos0.y )/m5 , 0)#�y���[�t�ת�y���q = - g - k*(�u®�����q)/m
	ball5.v = ball5.v + ball5.a*dt
	ball5.pos = ball5.pos + ball5.v*dt
def come6():
	rate(1000,come6)
	spring6.axis = ball6.pos - spring6.pos#�u®�������׼u®���ʺݪ���m�V�q��y�{�b����m�V�q
	ball6.a = vector(0, - g - k * (ball6.pos.y - ball6.pos0.y )/m6 , 0)#�y���[�t�ת�y���q = - g - k*(�u®�����q)/m
	ball6.v = ball6.v + ball6.a*dt
	ball6.pos = ball6.pos + ball6.v*dt
def come7():
	rate(1000,come7)
	spring7.axis = ball7.pos - spring7.pos#�u®�������׼u®���ʺݪ���m�V�q��y�{�b����m�V�q
	ball7.a = vector(0, - g - k1 * (ball7.pos.y - ball7.pos0.y )/m7 , 0)#�y���[�t�ת�y���q = - g - k*(�u®�����q)/m
	ball7.v = ball7.v + ball7.a*dt
	ball7.pos = ball7.pos + ball7.v*dt
def come8():
	rate(1000,come8)
	spring8.axis = ball8.pos - spring8.pos#�u®�������׼u®���ʺݪ���m�V�q��y�{�b����m�V�q
	ball8.a = vector(0, - g - k1 * (ball8.pos.y - ball8.pos0.y )/m8 , 0)#�y���[�t�ת�y���q = - g - k*(�u®�����q)/m
	ball8.v = ball8.v + ball8.a*dt
	ball8.pos = ball8.pos + ball8.v*dt
def come9():
	rate(1000,come9)
	spring9.axis = ball9.pos - spring9.pos#�u®�������׼u®���ʺݪ���m�V�q��y�{�b����m�V�q
	ball9.a = vector(0, - g - k1 * (ball9.pos.y - ball9.pos0.y )/m9 , 0)#�y���[�t�ת�y���q = - g - k*(�u®�����q)/m
	ball9.v = ball9.v + ball9.a*dt
	ball9.pos = ball9.pos + ball9.v*dt

come1()
come2()
come3()
come4()
come5()
come6()
come7()
come8()
come9()

	
def handler(data):
    rate(1, progress)
    if data != None:
        move(data)
    #balljump(data)
	
def progress():
    csmPull(df, handler)
	
df = 'Command'
profile = {
    'dm_name': 'Spring-SHM1',
    'df_list': [df],
	'd_name': 'f = -kx'
}

csmRegister(profile)
rate(1, progress) #�C�����@��progress






