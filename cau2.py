from sympy import *
import numpy as np

def giai_he_pt():
    x,y,z=symbols('x,y,z')
    pt1=Eq(2*x - 5*y + z, -5)
    pt2=Eq(4*x + 2*y - 2*z, 2)
    pt3=Eq(x + y - z, 0)
    hpt = solve((pt1, pt2, pt3), (x,y,z))
    print(hpt)
    return hpt

def tinh_gioi_han():
    x=symbols('x')
    f = ((x**3 - 3*x**2)*(1/3))+((x**2 - 2*x)*(1/2))
    gh=limit(f, x, oo)
    print('ket qua gioi han: ', gh)
    return gh

def tinh_dao_ham():
    x=symbols('x')
    f=(2*x -1)/(x+2)
    dh=diff(f, x)
    print('dao ham cua fx la: ',dh)
    return dh

def tinh_nguyen_ham():
    x=symbols('x')
    f=x/(x**2 + 1)
    nh=integrate(f,x)
    print('nguyen ham cua f= ',nh)
    return nh

def tinh_tich_phan():
    x=symbols('x')
    f=(1 - x*tan(x))/(x**2 * cos(x) + x)
    tp = integrate(f, (x,2*pi/3,pi))
    print('tich phan fx la:',tp)
    return tp

