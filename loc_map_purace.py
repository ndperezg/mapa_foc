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
#print dep

fig = plt.figure(figsize=(20,20))
ax1 = fig.add_subplot(211)

map = Basemap(llcrnrlon=-76.42000,llcrnrlat=2.3000,urcrnrlon=-76.38000,urcrnrlat=2.33000, projection='cyl', resolution=None)
map.drawparallels(np.linspace(2.3, 2.33, 4), labels=[1, 1, 0, 0], fmt="%.2f", dashes=[2, 2])
map.drawmeridians(np.linspace(-76.42, -76.38, 4), labels=[0, 0, 1, 1], fmt="%.2f", dashes=[2, 2])
x, y = map(lon, lat)



for i in range(len(dep)):
	if dep[i] < 0.2:
		
		d1 = map.scatter(x[i], y[i], 50, color="ivory", marker="o", edgecolor="k", zorder=50)

	elif 0.2 <= dep[i] < 0.4:
		
		d2 = map.scatter(x[i], y[i], 50, color="y", marker="o", edgecolor="k", zorder=50)

	elif 0.4 <= dep[i] < 0.6:
		
		d3 =map.scatter(x[i], y[i], 50, color="orange", marker="o", edgecolor="k", zorder=50)
	
	elif 0.6 <= dep[i] < 0.8:
		
		d4 = map.scatter(x[i], y[i], 50, color="r", marker="o", edgecolor="k", zorder=50)

	elif 0.8 <= dep[i] < 1.0:
		
		d5 = map.scatter(x[i], y[i], 50, color="aqua", marker="o", edgecolor="k", zorder=50)

	elif 1.0 <= dep[i] < 1.2:
		
		d6 = map.scatter(x[i], y[i], 50, color="g", marker="o", edgecolor="k", zorder=50)

labels = ['z<0.2','z<0.4','z<0.6','z<0.8','z<1.0','z<1.2']

map.arcgisimage(service='World_Topo_Map', xpixels = 1500, verbose= True)
leg = ax1.legend([d1, d2, d3, d4, d5, d6], labels, frameon= True, title='Profundidad (km)', scatterpoints = 1)
ax1.tick_params(labelsize=20)

ax2 = fig.add_subplot(212)
ax2.plot(x,dep,'o')
ax2.set_xlim(-76.42,-76.38)
ax2.invert_yaxis()
ax2.tick_params(labelsize=20, bottom = False, labelbottom=False, labelright = False, right = False)
ax2.set_aspect(0.015)
plt.show()


