#!/usr/bin/env python

#The MIT License (MIT)

#Copyright (c) 2014 Ajay Ramanathan

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
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


#Earth

Radius_Earth = 6378.1
Mass_Earth = 5.97219*(10^24)

Radius_Earth_Eff_G = Radius_Eff_G(Mass_Earth)
Radius_Earth_Colli = Radius_Colli(Radius_Earth)
Radius_Earth_Fly_By = Radius_Fly_By(Radius_Earth)

#Pluto

Radius_Pluto = 1163
Mass_Pluto = 1.312*(10^22)

Radius_Pluto_Eff_G = Radius_Eff_G(Mass_Pluto)
Radius_Pluto_Colli = Radius_Colli(Radius_Pluto)
Radius_Pluto_Fly_By = Radius_Fly_By(Radius_Pluto)

#Uranus

Radius_Uranus = 25563
Mass_Uranus = 8.6823*(10^25)

Radius_Uranus_Eff_G = Radius_Eff_G(Mass_Uranus)
Radius_Uranus_Colli = Radius_Colli(Radius_Uranus)
Radius_Uranus_Fly_By = Radius_Fly_By(Radius_Uranus)

#Neptune

Radius_Neptune = 24779
Mass_Neptune = 1.0243*(10^26)

Radius_Neptune_Eff_G = Radius_Eff_G(Mass_Neptune)
Radius_Neptune_Colli = Radius_Colli(Radius_Neptune)
Radius_Neptune_Fly_By = Radius_Fly_By(Radius_Neptune)

#Jupiter

Radius_Jupiter = 71496
Mass_Jupiter = 1.8986*(10^27)

Radius_Jupiter_Eff_G = Radius_Eff_G(Mass_Jupiter)
Radius_Jupiter_Colli = Radius_Colli(Radius_Jupiter)
Radius_Jupiter_Fly_By = Radius_Fly_By(Radius_Jupiter)

#Saturn

Radius_Saturn = 60272
Mass_Saturn = 5.6846*(10^26)

Radius_Saturn_Eff_G = Radius_Eff_G(Mass_Saturn)
Radius_Saturn_Colli = Radius_Colli(Radius_Saturn)
Radius_Saturn_Fly_By = Radius_Fly_By(Radius_Saturn)

#Mars

Radius_Mars = 3396.3
Mass_Mars = 6.4185*(10^23)

Radius_Mars_Eff_G = Radius_Eff_G(Mass_Mars)
Radius_Mars_Colli = Radius_Colli(Radius_Mars)
Radius_Mars_Fly_By = Radius_Fly_By(Radius_Mars)

#Moon

Radius_Moon = 1738.14
Mass_Moon = 7.3477*(10^22)

Radius_Moon_Eff_G = Radius_Eff_G(Mass_Moon)
Radius_Moon_Colli = Radius_Colli(Radius_Moon)
Radius_Moon_Fly_By = Radius_Fly_By(Radius_Moon)

#Venus

Radius_Venus = 6052.8
Mass_Venus = 4.8676*(10^24)

Radius_Venus_Eff_G = Radius_Eff_G(Mass_Venus)
Radius_Venus_Colli = Radius_Colli(Radius_Venus)
Radius_Venus_Fly_By = Radius_Fly_By(Radius_Venus)

#Mercury

Radius_Mercury = 2440.7
Mass_Mercury = 3.3022*(10^23)

Radius_Mercury_Eff_G = Radius_Eff_G(Mass_Mercury)
Radius_Mercury_Colli = Radius_Colli(Radius_Mercury)
Radius_Mercury_Fly_By = Radius_Fly_By(Radius_Mercury)

#Sun

Radius_Sun = 696342
Mass_Sun = 1.9891*(10^30)

Radius_Sun_Eff_G = Radius_Eff_G(Mass_Sun)
Radius_Sun_Colli = Radius_Colli(Radius_Sun)
Radius_Sun_Fly_By = Radius_Fly_By(Radius_Sun)

#Solar_System
#Calculating Maximimum distance travelled by Probe;
#Before the termination of Iteration.

Radius_Solar_System = 7311000000
Radius_Probe_Max = 7311000000*1.2

#All values are from Wikipedia,
#All Radius are Maximum Radius.

def Radius_Eff_G(Mass):    # Calculating Radius_Eff_G

#Lowest effective gravity,Millimeter per second; 0.000001

    G = 6.67259*(10^-11)
    Millimeter = 0.000001

    Radius_Eff_G = ((G*Mass)/Millimeter)^(1/2)
    return Radius_Eff_G

def Radius_Colli(Radius):    # Calculating Radius_Colli

    Collision_Co_Eff = (6378.1+2000)/6378.1

#Low Earth Orbit 2000km for Earth;
#If Probe goes below this; Hard to Control
#Calculating Collision_Co_Eff

    Radius_Colli = Collision_Co_Eff*Radius
    return Radius_Colli

def Radius_Fly_By(Radius):    # Calculating Radius_Fly_By

    Fly_By_Co_Eff = (6378.1+35786)/6378.1

#High Earth Orbit 35768km for Earth;
#Optimial Distance for best detail extraction;
#Calculating Fly_By_Co_Eff

    Radius_Fly_By = Fly_By_Co_Eff*Radius
    return Radius_Fly_By

