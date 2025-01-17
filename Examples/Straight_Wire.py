from BlibV3 import B
import numpy as np
#positions
xpos = np.linspace(-10,10,1000)
ypos,zpos=np.zeros(1000),np.zeros(1000)
#make grid
u =np.linspace(-10,10,50)
x,y,z = np.meshgrid(u,u,u)
#B field
Bx,By,Bz,B = B(x,y,z,xpos,ypos,zpos)[:3]
#plot 3d vector field
import plotly.graph_objects as go
vector = [go.Cone(x=x.ravel(),y=y.ravel(),z=z.ravel(),u=Bx.ravel(),v=By.ravel(),w=Bz.ravel())]
wire = [go.Scatter3d(x=xpos,y=ypos,z=zpos,mode='markers')]
go.Figure(data=vector+wire).show()