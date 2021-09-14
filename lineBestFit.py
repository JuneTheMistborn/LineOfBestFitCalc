from matplotlib import pyplot as plt

points = [(1,3),(2,5),(3,4),(5,10),(7,9),(8,13),(9,15),(11,13),(14,20)]

xSum, ySum = 0, 0
xMax, yMax, xMin, yMin = 0, 0, 0, 0
for point in points:
    xSum += point[0]
    ySum += point[1]
    if point[0] < xMin:
        xMin = point[0]
    elif point[0] > xMax:
        xMax = point[1]
    if point[1] < yMin:
        yMin = point[0]
    elif point[1] > yMax:
        yMax = point[1]
    plt.scatter(point[0], point[1])
xAvg = xSum/len(points)
yAvg = ySum/len(points)
sumSqr = 0
sumProd = 0
for point in points:
    x = point[0]
    y = point[1]
    sumSqr += (x-xAvg)**2
    sumProd += (x-xAvg)*(y-yAvg)
b = sumProd/sumSqr
a = yAvg-(b*xAvg)
lnYMin = (b*xMin)+a
lnYMax = (b*xMax)+a
plt.plot((xMin, xMax), (lnYMin, lnYMax))
plt.show()
