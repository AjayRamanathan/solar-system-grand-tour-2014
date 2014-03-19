#!/usr/bin/env python

#The MIT License (MIT)

#Copyright (c) 2014 Ajay Ramanathan

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

#Unit Kg, s and Km

G = 6.67259*(10**-14)

#Sun
Radius_Sun = 696342
Mass_Sun = 1.9891*(10**30)
Radius_Sun_Eff_G = 3.64313721523e+11
Radius_Sun_Colli = 914696.055283
Radius_Sun_Fly_By = 4603351.11118

#Mercury
Radius_Mercury = 2440.7
Mass_Mercury = 3.3022*(10**23)
Radius_Mercury_Eff_G = 148439303.077
Radius_Mercury_Colli = 3206.03763974
Radius_Mercury_Fly_By = 16134.8863878

#Venus
Radius_Venus = 6052.8
Mass_Venus = 4.8676*(10**24)
Radius_Venus_Eff_G = 569907879.258
Radius_Venus_Colli = 7950.79470062
Radius_Venus_Fly_By = 40013.6191781

#Earth
Radius_Earth = 6378.1
Mass_Earth = 5.97219*(10**24)
Radius_Earth_Eff_G = 631268368.225
Radius_Earth_Colli = 8378.1
Radius_Earth_Fly_By = 42164.1

#Moon
Radius_Moon = 1738.14
Mass_Moon = 7.3477*(10**22)
Radius_Moon_Eff_G = 70020132.4927
Radius_Moon_Colli = 2283.17378749
Radius_Moon_Fly_By = 11490.4295596

#Mars
Radius_Mars = 3396.3
Mass_Mars = 6.4185*(10**23)
Radius_Mars_Eff_G = 206949314.845
Radius_Mars_Colli = 4461.28800583
Radius_Mars_Fly_By = 22452.1303884

#Jupiter
Radius_Jupiter = 71496
Mass_Jupiter = 1.8986*(10**27)
Radius_Jupiter_Eff_G = 11255478387.9
Radius_Jupiter_Colli = 93915.2157539
Radius_Jupiter_Fly_By = 472643.027485

#Saturn
Radius_Saturn = 60272
Mass_Saturn = 5.6846*(10**26)
Radius_Saturn_Eff_G = 6158815236.23
Radius_Saturn_Colli = 79171.6723162
Radius_Saturn_Fly_By = 398443.836754

#Uranus
Radius_Uranus = 25563
Mass_Uranus = 8.6823*(10**25)
Radius_Uranus_Eff_G = 2406936396.27
Radius_Uranus_Colli = 33578.8667942
Radius_Uranus_Fly_By = 168990.904548

#Neptune
Radius_Neptune = 24779
Mass_Neptune = 1.0243*(10**26)
Radius_Neptune_Eff_G = 2614332407.52
Radius_Neptune_Colli = 32549.0255562
Radius_Neptune_Fly_By = 163808.067277

#Pluto
Radius_Pluto = 1163
Mass_Pluto = 1.312*(10**22)
Radius_Pluto_Eff_G = 29587899.6889
Radius_Pluto_Colli = 1527.68540788
Radius_Pluto_Fly_By = 7688.3160032

#Solar_System
Radius_Solar_System = 7311000000
Radius_Probe_Max = 7311000000*1.2

def main():

	x,y,z = 0,0,0
	vx,vy,vz = 0,0,0
	ax,ay,az = 0,0,0
	
	
def getAcceleration(p1,m1,p2,m2): #Calculates acceleration between two objects
	vector = p2-p1
	radius = sqrt(vector.dot(vector))
	acceleration = 0
	if m1 != 0 and m2 != 0:
	  acceleration = array(( vector * G*m1*m2 / radius**3 ))/m1  
	return acceleration   

def getDistance(p1,p2): #calculates Distance between two objects
	vector = p2-p1
	distance = sqrt(vector.dot(vector))	
	return distance 

if __name__ == '__main__': main()