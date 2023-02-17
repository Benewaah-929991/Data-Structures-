#author BENEWAAH GLORIA -6932321
#QUESTION A
w='intensity of loading'
w=10 #kilo Newtons per meter
x='axis of deflection'
x=0
L='length of beam'
L=12 #meters
#The equations
M='Bending moment'
M=w*(-6*x**2+6*L*x-L**2)/12 #calculates bending moment
V='Shear force'
V=w*(L/2-x) #calculates the shear force
x=0
print() 
print('The bending moment when x is {0} is {1}'.format(x,M)) #prints the bending moment when x=0
print()
print('The shear force when x is {0} is {1}'.format(x,V)) #prints the shear force when x=0

w='intensity of loading'
w=10 #kilo Newtons per meter
x='axis of direction'
x=L=12
L='length of beam'
L=12 #meters
M='Bending moment'
M=w*(-6*x**2+6*L*x-L**2)/12 #calculates bending moment
V='Shear force'
V=w*(L/2-x) #calculates the shear force
x=12
print() 
print('The bending moment when x is {0} is {1}'.format(x,M)) #prints the bending moment when x=L
print()
print('The shear force when x is {0} is {1}'.format(x,V)) #prints the shear force when x=L


#QUESTION B
from numpy import sqrt
#distance at which bending moment is zero
#x=L/2 plus or minus square root of L**2/12
L='length of the beam'
L=12 #meters
x1=(L/2+sqrt(L**2/12))
x2=(L/2-sqrt(L**2/12))
answer=(x2,x1)
print()
print('The point at which the bending moment is zero({0:.4f},{1:.4f}'.format(x1,x2))


#QUESTION C
#Estimating when the shear force is zero 
'The shear force,V=w*(L/2-x)'
w=10 #kilo Newtons per meter
L=12 #meters
#when the shear force is zero
x=L/2
print()
print('The point at which the shear force is zero is{0:.2f}meters'.format(x)) 


#QUESTION D
import numpy as np
#10mm=0.01m
'Span steps=SS'
SS=np.arange(0,L+0.01,0.01)
#generates array of steps of 0.01 across the length of the span 
'Bending moment at each step=BMs'
BMs=w*(-6*SS**2+6*L*SS-L**2)/12 #calculates the bending moment for each across the span
print()
print('The bending moment at every 0.01 meters along the span is{0} in kN/m'.format(BMs))


#QUESTION E
'Shear force at each step=Vs'
Vs=w*(L/2-SS) #calculate the shear force for each step across the span 
print()
print('The shear force at every 0.01 meters across the span is {0} in kN'.format(Vs))


#QUESTION F
import numpy as np
'Absolute bending moment=abs_BM'
abs_BM=abs(BMs) #calculates the absolute bending moment for the bending moment at each step
'The point at which the absolute values of bending moment is minimum=L_BM_min'
L_BM_min=SS[abs_BM==abs_BM.min()]
print()
print('The points at which the absolute values of the bending moment is minimum is {0:.2f},{1:}'.format(x2,L_BM_min[0]))


#QUESTION G
#Relative error,RE=(|Expected-Actual|/Actual value)*100%
#Expected value=distances(x2,x1) at which the bending moment is minimum
#Actual value=values obtained in QUESTION F 
RE=(abs(L_BM_min[0])/L_BM_min[0])*100
print()
print('The relative error is {0:.2f} in %'.format(RE))


#QUESTION H
'The point at which the discretized values of the bending moment is maximum=a'
a=L/2
print()
print('Points along which the bending moment is maximum is{0} in meters'.format(a))

'The point at which the discretized values of the bending moment is minimum=b'
b=(0,L)
print()
print('Points along which the bending moment is minimum is{0} in meters'.format(b))


