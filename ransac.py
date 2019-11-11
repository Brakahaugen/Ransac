import random
from statistics import mean 
import math  
import matplotlib.pyplot as plt


f = open('dataset1.txt')
table_x = []
table_y = []

for l in f:
    row = l.split()
    table_x.append(float(row[0]))
    table_y.append(float(row[1]))

plt.scatter(table_x, table_y)
plt.show()


#model
r = 0
x = 0
y = 0

#n – minimum number of data points required to estimate model parameters
n = 10

#k – maximum number of iterations allowed in the algorithm
k = 100000

#t – threshold value to determine data points that are fit well by model 
t = 0.012

#d – number of close data points required to assert that a model fits well to data
d = len(table_x)/30
    
iteration = 0
best_x = 0
best_y = 0
best_r = 0
bestErr = 999
betterCount = 1
while iteration < k:
    #Instantiating variables
    iteration += 1
    maybeInliers = random.sample(range(0, len(table_x)), n)
    alsoInliers = []


    #creating model based on the randomly selected points
    x = mean([table_x[i] for i in maybeInliers])
    y = mean([table_y[i] for i in maybeInliers])
    r = 0
    for i in maybeInliers:
        r += math.sqrt((x-table_x[i])**2 + (y-table_y[i])**2)
    r = r/len(maybeInliers)
    
    #appending the other points that are inside the threshold t
    for i in range(0, len(table_x)):
        if i in maybeInliers:
            continue

        #t_0 distance from circle
        t_0 = abs(math.sqrt((x-table_x[i])**2 + (y-table_y[i])**2) - r)
        if t > t_0:
            alsoInliers.append(i)
        
    if len(alsoInliers) > d:
        inliers = maybeInliers + alsoInliers

        #Create new model based on the inliers
        x = mean([table_x[i] for i in inliers])
        y = mean([table_y[i] for i in inliers])
        r = 0
        for i in inliers:
            r += math.sqrt((x-table_x[i])**2 + (y-table_y[i])**2)
        r = r/len(inliers)

        #Error measure using lsm
        lsm = 0
        for i in inliers: 
            lsm += (math.sqrt((x-table_x[i])**2 + (y-table_y[i])**2) - r)**2

        if lsm < bestErr:
            best_x = x
            best_y = y
            best_r = r
            bestErr = lsm
            print(str(betterCount) + ": found better estimation: " + str(bestErr) )
            betterCount += 1

print("number of inliers: " + str(len(inliers)))
plt.scatter(table_x, table_y, c='r', marker='o', label='-1')        
plt.scatter([table_x[i] for i in inliers], [table_y[i] for i in inliers], c='b', marker='x', label='1')
plt.legend(loc='upper left')
plt.show()

circle1 = plt.Circle((x, y), r, color='r')
ax = plt.gca()
ax.cla() # clear things for fresh plot

# change default range so that new circles will work
ax.set_xlim((0, 10))
ax.set_ylim((0, 10))
# some data
ax.plot(range(11), 'o', color='black')
# key data point that we are encircling
ax.plot((5), (5), 'o', color='y')

ax.add_artist(circle1)
ax.add_artist(circle2)
ax.add_artist(circle3)
fig.savefig('plotcircles2.png')






