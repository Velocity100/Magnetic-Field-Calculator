from BlibV3 import B
import numpy as np
#positions
k=5 #rose eq given by r = cos(kt)
n=1000
t = np.linspace(0,6*np.pi,n)
r = t
xpos,ypos = r*np.cos(t),r*np.sin(t)
zpos = np.zeros_like(xpos)
#make grid
u = np.linspace(-1.5,1.5,20)
x,y,z = np.meshgrid(u,u,u)
#B field
Bx,By,Bz = B(x,y,z,xpos,ypos,zpos)[:3]
#make 3d vector field
import plotly.graph_objects as go
vector = [go.Cone(x=x.ravel(),y=y.ravel(),z=z.ravel(),u=Bx.ravel(),v=By.ravel(),w=Bz.ravel())]
wire = [go.Scatter3d(x=xpos,y=ypos,z=zpos,mode='markers')]
go.Figure(data=vector+wire).show()