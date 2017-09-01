import numpy as np
import matplotlib
import matplotlib.pyplot as plt
%matplotlib notebook

n = 10
m = np.random.randint(10)
c = np.random.randint(10)

x = np.arange(10)
#print(x)
y = m*x+np.ones((1,n))+np.random.randint(-8,8,size=10)
x = np.array(x)[np.newaxis]
x1 = np.transpose(x)
o = np.ones((n,1))
#print(np.shape(x1))
#print(np.shape(o))
A = np.concatenate((x1,o),axis=1)
b = np.transpose(y)
#print(np.shape(A))
#print(A)
x = np.transpose(x)
y = np.transpose(y)
xstar = np.dot(np.linalg.pinv(A),b)
plt.plot(x,y,'ro')
ynew = xstar[0]*x+xstar[1]
plt.plot(x,ynew)
