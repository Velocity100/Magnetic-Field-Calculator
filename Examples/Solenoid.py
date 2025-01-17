import numpy as np
from BlibV3 import B
#positions
rz=17.5
r=5
z=1.5*rz

n = 10000
turns = 100*np.pi
t = np.linspace(0,turns,n)
xpos, ypos, zpos = np.cos(t)*r, np.sin(t)*r, np.linspace(0,rz,n)
#make grid
u = np.linspace(-8,8,25)
v = np.linspace(0,rz,25)
x,y,z = np.meshgrid(u,u,v)
#B field
Bx,By,Bz = B(x,y,z,xpos,ypos,zpos)[:3]
#plot 3d vector field 
import plotly.graph_objects as go
vector = [go.Cone(x=x.ravel(),y=y.ravel(),z=z.ravel(),u=Bx.ravel(),v=By.ravel(),w=Bz.ravel())]
wire = [go.Scatter3d(x=xpos,y=ypos,z=zpos,mode='markers')]
go.Figure(data=vector+wire).show()