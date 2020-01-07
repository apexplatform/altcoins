#!#/usr/bin/python3
import matplotlib.pyplot as plt
import numpy as np
#apply the pyplot python library for altcoins visualization
#an exaple to show the visualization on ADA and BTC
btcusd = np.array([1.23, 2, 3, 4])
adausd = np.array([0.2, 0.2, 0.3, 0.4])
plt.plot(btcusd, 'r--', adausd, 'r--')

plt.show()
