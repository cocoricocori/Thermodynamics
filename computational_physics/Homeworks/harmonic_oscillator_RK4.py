#2014103332 김민기
from numpy import arange, array
from pylab import plot, xlabel, ylabel, show, legend

#damped H.O. let m=0.1m k=1 then,
# c=1 for overdamping, c=0.6325 for critical damping, c=0.1 for underdamping.
#y= (d/dt) x
#m (d/dt) y + c y + k x = 0

k=1
m=0.1
c1=1.5
c2=0.6325
c3=0.1
def f1(r1,t):
    x=r1[0]
    y=r1[1]
    f_x=y
    f_y=-(c1*y+k*x)/m
    return array([f_x,f_y],float)
def f2(r2,t):
    x=r2[0]
    y=r2[1]
    f_x=y
    f_y=-(c2*y+k*x)/m
    return array([f_x,f_y],float)
def f3(r3,t):
    x=r3[0]
    y=r3[1]
    f_x=y
    f_y=-(c3*y+k*x)/m
    return array([f_x,f_y],float)

# init. condit.
t_i=0.0
x_i=0.1
y_i=0

t_f=8.0
h=0.0001
pt=[]
px1=[]#for underdamping
py1=[]
px2=[]#for critical damping
py2=[]
px3=[]#for overdamping
py3=[]
r1=[x_i,y_i]
r2=[x_i,y_i]
r3=[x_i,y_i]
x=x_i
y=y_i
t=t_i

pt.append(t)
px1.append(x)
py1.append(y)
px2.append(x)
py2.append(y)
px3.append(x)
py3.append(y)
#underdamping
while t<=t_f:
    k11=h*f1(r1,t)
    k21=h*f1(r1+0.5*k11, t+0.5*h)
    k31=h*f1(r1+0.5*k21, t+0.5*h)
    k41=h*f1(r1+k31, t+h)
    r1+=(k11+2*k21+2*k31+k41)/6

    k12=h*f2(r2,t)
    k22=h*f2(r2+0.5*k12, t+0.5*h)
    k32=h*f2(r2+0.5*k22, t+0.5*h)
    k42=h*f2(r2+k32, t+h)
    r2+=(k12+2*k22+2*k32+k42)/6

    k13=h*f3(r3,t)
    k23=h*f3(r3+0.5*k13, t+0.5*h)
    k33=h*f3(r3+0.5*k23, t+0.5*h)
    k43=h*f3(r3+k33, t+h)
    r3+=(k13+2*k23+2*k33+k43)/6

    t+=h
    px1.append(r1[0])
    py1.append(r1[1])
    px2.append(r2[0])
    py2.append(r2[1])
    px3.append(r3[0])
    py3.append(r3[1])
    pt.append(t)

plot(pt,px1,'r', label="overdamping")


plot(pt,px2,'b', label="critical damping")


plot(pt,px3,'g', label="underdamping")
xlabel(r'$t$')
ylabel(r'$x$')
legend(loc='upper left')
show()
    
