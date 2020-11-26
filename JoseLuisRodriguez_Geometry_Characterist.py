# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 06:37:35 2020

@author: luisc
"""

#First input that we ask number of sides
print('Welcome to the program Polygon information')
nsides = abs(int(input("Enter the numbers of sides from the polygon")))
respond = " You choose a polygon with {} sides"
print()
print (respond.format(nsides))

x= []
y= []
a=sx=sy=ix=iy=ixy=0

#Ask about the coordinates
print("Enter x and y coordinates for polygon points ...")
print ( "Example of writing : X,Y")

for side in range(nsides):
    line = input(f"Point {side + 1}: ")
    coordinates = line.split(",")   
    x.append(float(coordinates[0]))
    y.append(float(coordinates[1]))

x.append(x[0])
y.append(y[1])

print()
print('The points for your polygon are:')
print()
print(f"{'Point':10} {'x':10} {'y':10}")
print("-" * 30)

for i in range(nsides):
    print(f"{i+1:<10d} {x[i]:<10.2f} {y[i]:<10.2f}")
print()

for i in range(nsides):
#Area
    a += (x[i+1] - x[i]) * (y[i+1]**2 + y[i] * y[i+1] + y[i]**2)
    sx +=  (x[i+1] - x[i]) * (y[i+1]**2 + y[i] * y[i+1] + y[i]**2)    
    sy += (y[i+1] - y[i]) * (x[i+1]**2 + x[i] * x[i+1] + x[i]**2)      
    ix += (x[i+1] - x[i]) * (y[i+1]**3 +  y[i+1]**2 * y[i] + y[i+1] * y[i]**2 + y[i]**3)  
    iy += (y[i+1] - y[i]) * (x[i+1]**3 +  x[i+1]**2 * x[i] + x[i+1] * x[i]**2 + x[i]**3)
    ixy += (y[i+1] - y[i]) * (y[i+1] * (3* x[i+1]**2 + 2 * x[i] * x[i+1] + x[i]**2) + y[i] * (3 * x[i]**2 + 2 * x[i] * x[i+1] + x[i+1]**2))

      
print(f"The area is {a*0.5:5.3f}")  
print(f"The Sx is {abs((1.0/6.0)*sx):5.3f}")
print(f"The Sy is {abs((1.0/6.0)*sy):5.3f}")    
print(f"The Ix is {abs((1.0/12.0)*ix):5.3f}")
print(f"The Iy is {abs((1.0/12.0)*iy):5.3f}")
print(f"The Ixy is {abs((1.0/24.0)*ixy):5.3f}")

      
#xt
xt=abs(sy/a)
print(f"The xt is {xt:5.3f}")
      
#yt
yt=abs(sx/a)
print(f"The yt is {yt:5.3f}")
      
#Ixt
print(f"The Ixt is {abs(ix - yt**2 *a):5.3f}")

#Iyt
print(f"The Iyt is {abs(iy- xt**2 *a):5.3f}")    

#Ixyt
print(f"The Ixyt is {abs(ixy+ xt* yt* a):5.3f}")