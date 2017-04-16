"""

The data has 245057 points,
Blue means nonskin and red means skin

We start with 1000 random points: skinnonskin1000
then we take 2500 points to visualize the data: skinnonskin2500
Lets make the points 10,000:skinnonskin10k

It seems there is a cluster towards the top-right of the centre where the colour is nonskin.
Lets see more examples:

25,000 data points: skinnonskin25k

"""


import matplotlib.pyplot as plt
import numpy as np
import random

def randrange(n, vmin, vmax):
    '''
    Helper function to make an array of random numbers having shape (n, )
    with each number distributed Uniform(vmin, vmax).
    '''
    return (vmax - vmin)*np.random.rand(n) + vmin

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

n = 100
dataset = np.loadtxt("D:\Machine Learning - Stanford\machineLearning\Skin_NonSkin.txt", delimiter="\t")
x = dataset[:,0]
y = dataset[:,1]
z = dataset[:,2]
r=dataset[:,3]
print(len(dataset))

l=[]
for i in range(25000):
    l+=[random.randrange(245057)]



for elem in l:
    print(elem)
    xs=x[elem]
    ys=y[elem]
    zs=z[elem]
    if r[elem]==2:
        ax.scatter(xs, ys, zs, c='r')
    else:
         ax.scatter(xs, ys, zs, c='b')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()

