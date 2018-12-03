import pandas
import matplotlib.pyplot as plt
from os import path
import os
import re
data = {}
finish_time_pat = re.compile(r'(\d+) us')
for f in os.listdir('.'):
    if f.endswith('.log'):
        idx = int(re.findall(r'(\d+)\.log', f)[0])
        data_points = [int(i) for i in finish_time_pat.findall(open(f).read())]
        print(idx, data_points)
keys = list(sorted(data.keys()))
vals = [data[k] for k in keys ]
plt.boxplot(vals)
plt.show()


