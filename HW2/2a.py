
# Poisson random variable process X_t fot t in range  (0,.....100) and let lambda = 50, repeat the stimulation four time

# Poisson random process X_t for t in {0, ..., 100} with lambda = 50.
# Repeat the simulation four times (4 sample paths).

import numpy as np
import matplotlib.pyplot as plt

# shared time vector ( t in 0 ..... 100)

t = np.arange(0,101)

# 2A possion process simulation lambda = 50, repeat 4 times

lambda_val = 50
p1 = np.random.poisson(lambda_val, 101)
p2 = np.random.poisson(lambda_val, 101)
p3 = np.random.poisson(lambda_val, 101)
p4 = np.random.poisson(lambda_val, 101)

fig1 = plt.figure(figsize=(20, 14))
fig1.suptitle(f"Poisson random process, lambda = {lambda_val}, fontsize=24")

# subplot 1

ax1 = plt.subplot(411)
plt.plot(t, p1)
plt.xlim(0, 100)
plt.ylim(20,80)
plt.ylabel('$X_1$(t)',fontsize=20)
plt.tick_params('x', labelbottom=False)
plt.yticks(fontsize=12)
ax1.xaxis.grid(linewidth=2)
ax1.yaxis.grid(linewidth=1)

# subplot 2

ax2 = plt.subplot(412,sharex=ax1)
plt.plot(t, p2)
plt.xlim(0, 100)
plt.ylim(20,80)
plt.ylabel('$X_2$(t)',fontsize=20)
plt.tick_params('x', labelbottom=False)
plt.yticks(fontsize=12)
ax2.xaxis.grid(linewidth=2)
ax2.yaxis.grid(linewidth=1)


ax3 = plt.subplot(413,sharex=ax1)
plt.plot(t, p3)
plt.xlim(0, 100)
plt.ylim(20,80)
plt.ylabel('$X_3$(t)',fontsize=20)
plt.tick_params('x', labelbottom=False)
plt.yticks(fontsize=12)
ax3.xaxis.grid(linewidth=2)
ax3.yaxis.grid(linewidth=1)

# subplot 4

ax4 = plt.subplot(414,sharex=ax1,sharey=ax1)
plt.plot(t, p4)
plt.xlim(0, 100)
plt.ylim(20,80)
plt.ylabel('$X_4$(t)',fontsize=20)
plt.tick_params('x', labelbottom=False)
plt.yticks(fontsize=12)
ax4.xaxis.grid(linewidth=2)
ax4.yaxis.grid(linewidth=1)

# to display all
plt.show()