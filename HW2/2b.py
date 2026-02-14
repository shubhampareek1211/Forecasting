import numpy as np
from matplotlib import pyplot as plt

# shared time vector ( t in 0 ..... 100)

t = np.arange(0,101)

# Normal rando process X_t for t in {0,.....100}, mu = 0, sigma**2 = 1, 4 times repeat

mu = 0
sigma = np.sqrt(1)

n1 = np.random.normal(mu, sigma, 101)
n2 = np.random.normal(mu, sigma, 101)
n3 = np.random.normal(mu, sigma, 101)
n4 = np.random.normal(mu, sigma, 101)

fig2 = plt.figure(figsize=(20, 14))
fig2.suptitle("Quesiton 2b: Normal random process, mu = 0, sigma**2 = 1, 4 times repeat", fontsize=24)

# subplot 1

bx1 = plt.subplot(411)
plt.plot(t, n1)
plt.xlim(0, 100)
plt.ylim(-5,5)
plt.ylabel('$X_1$(t)',fontsize=20)
plt.tick_params('x', labelbottom=False)
plt.yticks(fontsize=12)
bx1.xaxis.grid(linewidth=2)
bx1.yaxis.grid(linewidth=1)


# subplot 2

bx2 = plt.subplot(412,sharex=bx1)
plt.plot(t, n2)
plt.xlim(0, 100)
plt.ylim(-5,5)
plt.ylabel('$X_2$(t)',fontsize=20)
plt.tick_params('x', labelbottom=False)
plt.yticks(fontsize=12)
bx2.xaxis.grid(linewidth=2)
bx2.yaxis.grid(linewidth=1)

# subplot 3

bx3 = plt.subplot(413,sharex=bx1)
plt.plot(t, n3)
plt.xlim(0, 100)
plt.ylim(-5,5)
plt.ylabel('$X_2$(t)',fontsize=20)
plt.tick_params('x', labelbottom=False)
plt.yticks(fontsize=12)
bx3.xaxis.grid(linewidth=2)
bx3.yaxis.grid(linewidth=1)

# subplot 4

bx4 = plt.subplot(414,sharex=bx1,sharey=bx1)
plt.plot(t, n4)
plt.xlim(0, 100)
plt.ylim(-5,5)
plt.ylabel('$X_2$(t)',fontsize=20)
plt.tick_params('x', labelbottom=False)
plt.yticks(fontsize=12)
bx4.xaxis.grid(linewidth=2)
bx4.yaxis.grid(linewidth=1)


plt.show()