import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import poisson

# case 1 ; lambda = 0.03

lam1 = 0.03
x1 = np.arange(0, 10)
y1 = poisson.pmf(x1, lam1)

plt.figure()
plt.stem(x1, y1)
plt.title("Poisson Distribution: lambda = 0.03")
plt.xlabel("X")
plt.ylabel("PMF(X)")
plt.grid()
plt.show()


# case 2; lambda = 50

lam2 = 50
x2 = np.arange(0, 100)
y2 = poisson.pmf(x2, lam2)

plt.figure()
plt.stem(x2, y2)
plt.title("Poisson Distribution: lambda = 50")
plt.xlabel("X")
plt.ylabel("PMF(X)")
plt.grid()
plt.show()

# case 3; lambda = 1000
lam3 = 1000
x3 = np.arange(800, 1000)
y3 = poisson.pmf(x3, lam3)

plt.figure()
plt.stem(x3, y3)
plt.title("Poisson Distribution: lambda = 1000")
plt.xlabel("X")
plt.ylabel("PMF(X)")
plt.grid()
plt.show()