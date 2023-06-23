# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 18:32:33 2023

full function coulombCalc NO USER INTERFACE
"""

import math
import numpy as np
import matplotlib.pyplot as plt

magArray = [0]
xArray = [0]
yArray = [0]
zArray = [0]

coulConst = 8.988 * pow(10,9)

#a user defined function which calculates the electric field from one point charge
def pointCharge(xPoint, yPoint, zPoint):
    xParticle = float(input("enter the coordinate of the charged particle"))
    yParticle = float(input("the y coordinate?"))
    zParticle = float(input("the z coordinate?"))
    q = float(input("enter the charge of the particle"))

    x = xParticle - (xPoint)
    y = yParticle - (yPoint)
    z = zParticle - (zPoint)

    rMagnitude = math.sqrt((x * x) + (y * y) + (z * z))

    xUnit = x / rMagnitude
    yUnit = y / rMagnitude
    zUnit = z / rMagnitude

    eMag = coulConst * (q / (rMagnitude * rMagnitude))
    eX = eMag * xUnit
    eY = eMag * yUnit
    eZ = eMag * zUnit

    print("magnitude of the electric field: <",eX, ",",eY,",",eZ,">")
       
    magArray.append(eMag)
    xArray.append(eX)
    yArray.append(eY)
    zArray.append(eZ)
    return(0)

#a used defined function which the user can choose which charge to add and it 
#chooses the right function to run
def oneCharge (xPoint, yPoint, zPoint):
    typeCharge = str(input("what charge would you like to add?"))
    if typeCharge == 'p':
        pointCharge(xPoint, yPoint, zPoint)
    else:
        print("error! not a valid type of charge")
        oneCharge()
    addCharge()
    return (0)
        
def addCharge():
    yesNo = input("would you like to add another charge? (1/2)")
    
    if yesNo == 1:
        oneCharge()
    if yesNo == 2:
        print("ok! here's your final magnitude values:")
    return(0)
        
#main function
def main():
    xPoint = float(input("enter the x coordinate of the point of interest"))
    yPoint = float(input("the y coordinate"))
    zPoint = float(input("the z coordinate"))
    
    oneCharge(xPoint, yPoint, zPoint)
    
main()

xComp = np.sum(xArray)
yComp = np.sum(yArray)
zComp = np.sum(zArray)

#plotting
xComp = 5
yComp = 6

V = np.array([[xComp,yComp], [xComp,0], [0,yComp]])
origin = np.array([[0, 0, 0],[0, 0, 0]]) # origin point

plt.quiver(*origin, V[:,0], V[:,1], color=['r','b','g'], scale=21)
plt.show()









