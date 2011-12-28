import matplotlib.pyplot as plt

x = 0.1
y = 0.1

xs = []
ys = []

for bob in range(10000):
    new_x = (y + 1) - (1.4 * x ** 2)
    new_y = 0.3 * x
    print "(%s, %s)" % (new_x, new_y)
    xs.append(new_x)
    ys.append(new_y)
    x = new_x
    y = new_y
    #plt.plot(new_x, new_y, 'ro')
    #plt.plot(xs, ys, 'ro')
    #if bob % 100 == 0:
        #plt.show()

plt.plot(xs, ys, 'ro')
#plt.ylabel('SCIENCE!')
plt.xlabel('SCIENCE!')
plt.show()
