import numpy as np
import plotly.graph_objects as go
from BlibV3 import B
#positions
n = 1000
t = np.arange(0,2*np.pi+(2*np.pi)/n,(2*np.pi)/n)
r1 = 0.15
r2 = 0.15
r3 = 0.15
h_1 = -0.15
h_2 = 0
h_3 = 0.15

x1,y1 = np.cos(t)*r1, np.sin(t)*r1
z1 = np.ones_like(x1)*h_1

x2,y2 = np.cos(t)*r2, np.sin(t)*r2
z2 = np.ones_like(x2)*h_2

x3,y3 = np.cos(t)*r3, np.sin(t)*r3
z3 = np.ones_like(x3)*h_3

xpos,ypos,zpos = np.vstack((x1,x2,x3)),np.vstack((y1,y2,y3)),np.vstack((z1,z2,z3))
#make grid
u = np.linspace(-0.2,0.2,25)
x,y,z = np.meshgrid(u,u,u)
#B field
Bx,By,Bz = B(x,y,z,xpos,ypos,zpos)[:3]
#plot 3d vector field
import plotly.graph_objects as go
vector = [go.Cone(x=x.ravel(),y=y.ravel(),z=z.ravel(),u=Bx.ravel(),v=By.ravel(),w=Bz.ravel())]
wire = [go.Scatter3d(x=xpos[i],y=ypos[i],z=zpos[i],mode='markers') for i in range(len(xpos))]
go.Figure(data=vector+wire).show()