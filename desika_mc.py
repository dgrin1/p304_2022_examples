import numpy as np
def f(x):
	return np.sin(x)
#note, we’re going from x=[1,2] since from x=[0,2], then we’ll have #part of the function that gets negative.
#===================== #MODFIABLE HEADER #=====================
a=1 
b=2
NDARTS = 100000 #=====================
#set up the function
x = np.linspace(a,b,1000) 
y=f(x)
#set up the box that goes around the function ymax = np.max(y)
ymin = 0.
ymax=np.max(y)
#so now the box goes from [a,b] on the x axis , and [ymin,ymax] on the y axis .
#throw darts that go in the box somewhere
xrand = np.random.uniform(a,b, size=NDARTS)
yrand = np.random.uniform(ymin,ymax, size=NDARTS)
integral_counter = np.sum(yrand < f(xrand))
#In Class Example Consider our standard integral, 
#f (x) = x4 − 2x + 1 over the range [a,b] = [1, 2]. 
#You want to write a box that encapsulates this integral, 
#without giving too much space above it 
#(or the code will take forever to reach meaningful results) 
#and then start throwing darts at it! 
#NOTE: we’re going from the interval [1,2] 
#(which has an analytic solution of 4.2) as opposed to 
#[0,2] which has an analytic solution of 4.4 because the function 
#becomes negative for a bit in the area [0,2].

area_of_box = ymax*(b-a)
area = float(integral_counter)/NDARTS*area_of_box
print("area = ", area)