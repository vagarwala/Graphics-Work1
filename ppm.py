import math
##Generates a PPM image

f = open("output.ppm", "w")
f.write("P3\n500 500\n255\n")

p = []

for x in range(500):
    l = []
    for y in range(500):
        l.append("0 0 0 ")
    p.append(l)

#define a circle in the format of [centerY, centerX, radius]
circle = [250, 250, 250]

#Modify image
for x in range(500):
    for y in range(500):
        if math.sqrt((x-circle[0])**2 + (y-circle[1])**2) < circle[2]:
            p[x][y] = "%s %s %s " % (100, 100, 100)
        f.write(p[x][y])
