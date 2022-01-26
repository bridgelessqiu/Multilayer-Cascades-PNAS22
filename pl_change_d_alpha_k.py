import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

# Power-law network: number of anchor node vs average degree

plt.style.use('seaborn-whitegrid')
plt.rcParams.update({'figure.figsize':(4.5,5), 'figure.dpi':100})

rc('font', **{'family': 'Computer Modern', 'size': 10})
rc('text', usetex=True)

l = range(10, 210, 10)

x = np.array(l)

network_name = "pl_change_d_alpha_k"

y_nk_0 = np.array([494.5, 397.7, 362.2, 330.6, 313.0, 294.3, 281.1, 273.5, 265.8, 250.5, 247.6, 238.8, 238.5, 231.0, 225.0, 228.0, 222.5, 220.2, 217.7, 223.9])

y_nk_5 = np.array([552.5, 507.8, 485.1, 490.0, 481.2, 476.1, 477.2, 474.6, 472.4, 479.6, 474.3, 476.8, 472.6, 475.0, 463.6, 467.4, 465.7, 470.8, 468.8, 473.5])

y_nk_9 = np.array([571.5, 573.1, 571.6, 566.0, 575.2, 578.1, 580.3, 587.7, 582.5, 581.1, 592.3, 584.1, 590.2, 590.5, 594.2, 585.7, 594.1, 593.7, 597.5, 590.9])

line_width=2

plt.plot(x, y_nk_0, '-', color = "darkgrey", marker='o', linewidth = line_width, label = r"$\theta=0$")
plt.plot(x, y_nk_5, '-', color = "tomato", marker='s', linewidth = line_width, label = r"$\theta=0.5$") 
plt.plot(x, y_nk_9, '-', color = "darkseagreen", marker='^', linewidth = line_width, label = r"$\theta=0.9$") 


plt.xlabel(r'Average degree', fontsize=17)
plt.ylabel(r'Average number of anchor nodes', fontsize = 17)
plt.legend(loc=(0.5,0.3), fontsize = 16)

plt.xlim(10, 200)
plt.ylim(0, 600)

file_name = network_name + ".pdf"

plt.savefig(file_name, bbox_inches='tight', pad_inches = 0.07)