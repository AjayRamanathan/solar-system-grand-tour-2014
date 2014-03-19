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
#az seems to be too high
#Iteration wont work after 1st iteration

import xlwt, xlrd
import numpy as np
import math

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

Input = xlrd.open_workbook('Input.xlsx')

sun = Input.sheet_by_name('Sun')
mercury = Input.sheet_by_name('Mercury')
venus = Input.sheet_by_name('Venus')
earth = Input.sheet_by_name('Earth')
moon = Input.sheet_by_name('Moon')
mars = Input.sheet_by_name('Mars')
jupiter = Input.sheet_by_name('Jupiter')
saturn = Input.sheet_by_name('Saturn')
uranus = Input.sheet_by_name('Uranus')
neptune = Input.sheet_by_name('Neptune')
pluto = Input.sheet_by_name('Pluto')

def main():

	m1 = 1000000
	x = 10000 + int(earth.cell_value(0, 1))
	y = 10000 + int(earth.cell_value(0, 2))
	z = 10000 + int(earth.cell_value(0, 3))
	vx,vy,vz = 0,0,0
	ax,ay,az = 0,0,0
	
	book = xlwt.Workbook(encoding="utf-8")
	sheet = book.add_sheet("Output")

	sheet.write(0,0,0)
	sheet.write(0,1,x)
	sheet.write(0,2,y)
	sheet.write(0,3,z)
	sheet.write(0,4,vx)
	sheet.write(0,5,vy)
	sheet.write(0,6,vz)
	sheet.write(0,7,ax)
	sheet.write(0,8,ay)
	sheet.write(0,9,az)

	for N in xrange(17519):

		foo = getTotalAcceleration(x,y,z,N)
		ax = foo[0]
		ay = foo[1]
		az = foo[2]
		x = x+(60*30*vx)+(60*60*60*60*ax)
		y = y+(60*30*vy)+(60*60*60*60*ay)
		z = z+(60*30*vz)+(60*60*60*60*az)
		vx = 60*60*ax
		vy = 60*60*ay 
		vz = 60*60*az

		sheet.write(N+1,0,N+1)
		sheet.write(N+1,1,x)
		sheet.write(N+1,2,y)
		sheet.write(N+1,3,z)
		sheet.write(N+1,4,vx)
		sheet.write(N+1,5,vy)
		sheet.write(N+1,6,vz)
		sheet.write(N+1,7,ax)
		sheet.write(N+1,8,ay)
		sheet.write(N+1,9,az)

	book.save("trial.xls")

def getTotalAcceleration(x,y,z,N):
	Accel = np.asarray([0,0,0])
	p1 = [x,y,z]
	p1 = np.asarray(p1)

	a = sun.cell_value(N, 1)
	b = sun.cell_value(N, 2)
	c = sun.cell_value(N, 3)
	p2 = [a,b,c]
	p2 = np.asarray(p2)
	Accel += getAcceleration(p1,p2,Mass_Sun )

	a = mercury.cell_value(N, 1)
	b = mercury.cell_value(N, 2)
	c = mercury.cell_value(N, 3)
	p2 = [a,b,c]
	p2 = np.asarray(p2)
	Accel += getAcceleration(p1,p2,Mass_Mercury)

	a = venus.cell_value(N, 1)
	b = venus.cell_value(N, 2)
	c = venus.cell_value(N, 3)
	p2 = [a,b,c]
	p2 = np.asarray(p2)
	Accel += getAcceleration(p1,p2,Mass_Venus)

	a = earth.cell_value(N, 1)
	b = earth.cell_value(N, 2)
	c = earth.cell_value(N, 3)
	p2 = [a,b,c]
	p2 = np.asarray(p2)
	Accel += getAcceleration(p1,p2,Mass_Earth)

	a = moon.cell_value(N, 1)
	b = moon.cell_value(N, 2)
	c = moon.cell_value(N, 3)
	p2 = [a,b,c]
	p2 = np.asarray(p2)
	Accel += getAcceleration(p1,p2,Mass_Moon)

	a = mars.cell_value(N, 1)
	b = mars.cell_value(N, 2)
	c = mars.cell_value(N, 3)
	p2 = [a,b,c]
	p2 = np.asarray(p2)
	Accel += getAcceleration(p1,p2,Mass_Mars)

	a = jupiter.cell_value(N, 1)
	b = jupiter.cell_value(N, 2)
	c = jupiter.cell_value(N, 3)
	p2 = [a,b,c]
	p2 = np.asarray(p2)
	Accel += getAcceleration(p1,p2,Mass_Jupiter)

	a = saturn.cell_value(N, 1)
	b = saturn.cell_value(N, 2)
	c = saturn.cell_value(N, 3)
	p2 = [a,b,c]
	p2 = np.asarray(p2)
	Accel += getAcceleration(p1,p2,Mass_Saturn)

	a = uranus.cell_value(N, 1)
	b = uranus.cell_value(N, 2)
	c = uranus.cell_value(N, 3)
	p2 = [a,b,c]
	p2 = np.asarray(p2)
	Accel += getAcceleration(p1,p2,Mass_Uranus)

	a = neptune.cell_value(N, 1)
	b = neptune.cell_value(N, 2)
	c = neptune.cell_value(N, 3)
	p2 = [a,b,c]
	p2 = np.asarray(p2)
	Accel += getAcceleration(p1,p2,Mass_Neptune)

	a = pluto.cell_value(N, 1)
	b = pluto.cell_value(N, 2)
	c = pluto.cell_value(N, 3)
	p2 = [a,b,c]
	p2 = np.asarray(p2)
	Accel += getAcceleration(p1,p2,Mass_Pluto)

	return Accel

def getAcceleration(p1,p2,m2): #Calculates acceleration between two objects
	vector = p2-p1
	radius = math.sqrt(vector.dot(vector))
	acceleration = 0
	acceleration = np.asarray(( vector * G*m2 / radius**3 )) 
	#print acceleration
	return acceleration   

def getDistance(p1,p2): #calculates Distance between two objects
	vector = p2-p1
	distance = math.sqrt(vector.dot(vector))	
	return distance 

if __name__ == '__main__': main()