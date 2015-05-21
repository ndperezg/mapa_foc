from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
from obspy.imaging.beachball import Beach

lat, lon, dep = [], [], []

data = open('excel.txt')
ordenado = open('ordenado.txt')
"""
for line in data:
#	print line[22:23] , line[24:29]
	lat.append(float(line[22:23])+np.float64(line[24:29])/60.0)
	lon.append(float(line[30:33])+np.float64(line[33:38])/60.0)
print lat, lon
"""

for line in ordenado:
	lat.append(float(line.split(' ')[0]))
	lon.append(float(line.split(' ')[1]))
	if line.split(' ')[2] == '':
		dep.append(0)
	else:
		dep.append(float(line.split(' ')[2]))
print dep

map = Basemap(llcrnrlon=-76.42000,llcrnrlat=2.3000,urcrnrlon=-76.38000,urcrnrlat=2.33000, projection='cyl', resolution=None)
map.drawparallels(np.linspace(2.3, 2.33, 4), labels=[1, 1, 0, 0], fmt="%.2f", dashes=[2, 2])
map.drawmeridians(np.linspace(-76.42, -76.38, 4), labels=[0, 0, 1, 1], fmt="%.2f", dashes=[2, 2])
x, y = map(lon, lat)

for i in range(len(dep)):
	if dep[i] < 0.2:
		map.scatter(x[i], y[i], 50, color="w", marker="o", edgecolor="k", zorder=50)
	elif 0.2 <= dep[i] < 0.4:
		map.scatter(x[i], y[i], 50, color="y", marker="o", edgecolor="k", zorder=50)
	elif 0.4 <= dep[i] < 0.6:
		map.scatter(x[i], y[i], 50, color="m", marker="o", edgecolor="k", zorder=50)	
	elif 0.6 <= dep[i] < 0.8:
		map.scatter(x[i], y[i], 50, color="g", marker="o", edgecolor="k", zorder=50)
	elif 0.8 <= dep[i] < 1.0:
		map.scatter(x[i], y[i], 50, color="c", marker="o", edgecolor="k", zorder=50)
	elif 1.0 <= dep[i] < 1.2:
		map.scatter(x[i], y[i], 50, color="r", marker="o", edgecolor="k", zorder=50)

map.arcgisimage(service='World_Topo_Map', xpixels = 1500, verbose= True)
plt.show()


