import numpy as np
from BlibV3 import B
#positions
n = 1000
r=0.15
theta = np.arange(0,2*np.pi+2*np.pi/n,2*np.pi/n)
zpos1 = np.cos(theta)*r
ypos1 = np.sin(theta)*r
xpos1 = np.ones_like(zpos1)*r/2

zpos2 = np.cos(theta)*r
ypos2 = np.sin(theta)*r
xpos2 = np.ones_like(xpos1)*-r/2

xpos = np.vstack((xpos1,xpos2))
ypos = np.vstack((ypos1,ypos2))
zpos = np.vstack((zpos1,zpos2))
#make grid
u = np.linspace(-0.2,0.2,25)
x,y,z = u,u,u
#B field
Bx,By,Bz = B(x,y,z,xpos,ypos,zpos)[:3]
#plot 3d vector field
import plotly.graph_objects as go
vector = [go.Cone(x=x.ravel(),y=y.ravel(),z=z.ravel(),u=Bx.ravel(),v=By.ravel(),w=Bz.ravel())]
wire = [go.Scatter3d(x=xpos[i],y=ypos[i],z=zpos[i],mode='markers') for i in range(len(xpos))]
go.Figure(data=vector+wire).show()