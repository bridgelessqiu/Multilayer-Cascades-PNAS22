import seaborn as sns
import pandas as pd
import numpy as np
from pdb import set_trace
import matplotlib.pyplot as plt
from matplotlib import rc

# Power-law network: queries ratio vs average degree

plt.style.use('seaborn-whitegrid')
plt.rcParams.update({'figure.figsize':(4.5,5), 'figure.dpi':100})

rc('font', **{'family': 'Computer Modern', 'size': 10})
rc('text', usetex=True)

l = range(10, 210, 10)
x = np.array(l)

network_name = "pl_change_d_alpha"

y_nk_0 = np.array([0.494937, 0.398137, 0.362585, 0.330988, 0.313386, 0.294679, 0.281482, 0.273877, 0.266179, 0.250875, 0.247967, 0.23916, 0.238872, 0.231362, 0.225349, 0.228354, 0.222859, 0.220561, 0.218059, 0.224245])

y_nk_5 = np.array([0.552921, 0.508214, 0.485487, 0.490366, 0.481568, 0.476465, 0.477564, 0.474949, 0.472751, 0.479936, 0.474639, 0.477126, 0.472933, 0.47533, 0.463943, 0.467733, 0.466029, 0.471126, 0.469124, 0.473812])

y_nk_9 = np.array([0.571927, 0.573525, 0.572026, 0.56642, 0.575608, 0.578507, 0.580697, 0.588092, 0.582893, 0.581502, 0.59269, 0.584495, 0.590592, 0.590892, 0.594585, 0.586088, 0.594484, 0.594082, 0.597877, 0.591281])

y_binary_0 = np.array([0.0941773, 0.171692, 0.245357, 0.312293, 0.375755, 0.431894, 0.482303, 0.537622, 0.588103, 0.617386, 0.658995, 0.689213, 0.736655, 0.748246, 0.786155, 0.82823, 0.855257, 0.862607, 0.89388, 0.936058])

y_binary_5 = np.array([0.0971314, 0.179786, 0.260264, 0.340233, 0.415742, 0.489947, 0.560953, 0.62946, 0.698949, 0.766065, 0.828464, 0.892311, 0.949905, 1.00638, 1.06301, 1.11942, 1.17439, 1.23094, 1.28377, 1.33688])

y_binary_9 = np.array([0.0992999, 0.186682, 0.270636, 0.353303, 0.434195, 0.512464, 0.590091, 0.664556, 0.736847, 0.810655, 0.880121, 0.946597, 1.01558, 1.08112, 1.14946, 1.20982, 1.27825, 1.33294, 1.39844, 1.45374])

line_width=2

plt.plot(x, y_nk_0, linestyle='dotted', color = "darkgrey", marker='o', linewidth = line_width, label = r"\textsc{AnchorLinearSearch:}$\theta=0$")
plt.plot(x, y_nk_5, linestyle='dotted', color = "tomato", marker='s', linewidth = line_width, label = r"\textsc{AnchorLinearSearch:}$\theta=0.5$") 
plt.plot(x, y_nk_9, linestyle='dotted', color = "darkseagreen", marker='^', linewidth = line_width, label = r"\textsc{AnchorLinearSearch:}$\theta=0.9$") 

plt.plot(x, y_binary_0, '-', color = "darkgrey", marker='o', linewidth = line_width, label = r"\textsc{AnchorBinarySearch:}$\theta=0$") 
plt.plot(x, y_binary_5, '-', color = "tomato", marker='s', linewidth = line_width, label = r"\textsc{AnchorBinarySearch:}$\theta=0.5$") 
plt.plot(x, y_binary_9, '-', color = "darkseagreen", marker='^', linewidth = line_width, label = r"\textsc{AnchorBinarySearch:}$\theta=0.9$") 

plt.yscale('log')

plt.xlabel(r'Average degree', fontsize=17)
plt.ylabel(r'Query ratio $\gamma$', fontsize = 17)
plt.legend(loc='lower left', fontsize=13)

plt.xlim(10, 200)
plt.ylim(0, 2)

file_name = network_name + ".pdf"

plt.savefig(file_name, bbox_inches='tight', pad_inches = 0.07)