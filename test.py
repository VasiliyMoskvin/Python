import matplotlib.pyplot as plt
import math

x = [i for i in range(10)]
R1 = x
dx = 2
h = 4
S1 = [math.pi * i ** 2 for i in R1]
S2 = [math.pi * h * (2 * (i + dx) + h) for i in R1]



#xv =
#y = [i ** 2 for i in x]

plt.plot(x, S1)
plt.plot(x, S2)
plt.grid(True)
plt.show()