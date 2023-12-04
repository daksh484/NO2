import matplotlib.pyplot as plt
#objective fn--z=2x+3y x=[i for i in range(0,12)] 
y1=[((8-i)/2) for i in x] 
y2=[(9-3*i) for i in x] 
c1=2 
c2=3
plt.plot(x,y1) 
plt.plot(x,y2)
plt.grid(True) #plt.show()
points=[[0,0],[0,4],[3,0],[2,3]] 
z=[] for i in points:
value=c1*i[0]+c2*i[1]
 z.append(value) 
print("value at ",i,"is",value)

Max=points[z.index(max(z))] print("optimal point
is:",Max) 
