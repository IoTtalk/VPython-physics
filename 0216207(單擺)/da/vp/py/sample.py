from visual import *
g=9.8               #���O�[�t�� 9.8 m/s^2
size = 0.05         #�y�b�| 0.05 m
L = 1.0             #�ӽu�� 1.0m
theta = 15 * pi / 180  #���\�_�l���� = 15 degrees
omega = 0           #�쨤�t�� = 0

scene = display(width=1200, height=1000,center = (0, -L/2, 0), background=(0.5,0.5,0))     #�]�w�e��
ceiling = box(length=2, height=0.001, width=2, color=color.blue)    #�e�Ѫ�O
ball = sphere(radius = size,  color=color.red)                      #�e�y
string = cylinder(pos=(0,0,0), radius=0.003)                           #�e�ӽu�A�@�ݦb(0,0,0)          

dt = 0.001   
while True:
    rate(1000)

    alpha = 
    omega += 
    theta += 
#(�ΧA�����z���ѡA��o�T�楼�����{���ɧ���)
    
    ball.pos = vector(L * sin(theta), -L*cos(theta), 0)
    string.axis = ball.pos - string.pos
