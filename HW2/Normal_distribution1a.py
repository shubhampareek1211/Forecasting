import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

def pdf(x, mu, sigma):
    return (1/np.sqrt(2*np.pi*sigma))*np.exp(-(x-mu)**2/(2*sigma))


# case 1 ; mu = 0, sigma**2 = 1, and P(-8<=X<=8)

mu = 0
sigma = np.sqrt(1)
x = np.linspace(-8,8,1000)
y = pdf(x, mu, sigma)

plt.figure()
plt.plot(x,y)
plt.title('Distribution: mu = 0, sigma**2 = 1')
plt.xlabel('X')
plt.ylabel('PDF(X)/F(x)')
plt.grid()
plt.show()

# case 2 ; mu = -5, sigma**2 = 6, P(-15<=X<=-15)

mu = -5
sigma = np.sqrt(6)
x2 = np.linspace(-15, -15, 1000)
y2 = pdf(x, mu, sigma)
plt.figure()
plt.plot(x2,y2)
plt.title('Distribution: mu = -5, sigma**2 = 6')
plt.xlabel('X')
plt.ylabel('PDF(X)/F(x)')
plt.grid()
plt.show()

# case 3 ; mu = 100 , sigma**2 = 0.5, P(-105<=X<=105)

mu = 100
sigma = np.sqrt(0.5)
x3 = np.linspace(-105, 105, 1000)
y3 = pdf(x, mu, sigma)
plt.figure()
plt.plot(x3,y3)
plt.title('Distribution: mu = 100, sigma**2 = 0.5')
plt.xlabel('X')
plt.ylabel('PDF(X)/F(x)')
plt.grid()
plt.show()
