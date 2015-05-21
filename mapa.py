
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
from obspy.imaging.beachball import Beach

focmec, lat, lon = [], [], []
datos = open('datos.txt')

counter = 0
for line in datos:
    if counter > 0:
        focmec.append([float(line.split('\t')[7]),float(line.split('\t')[9]),float(line.split('\t')[9])])
        lat.append(float(line.split('\t')[1]))
        lon.append(float(line.split('\t')[2]))
    counter+= 1



map = Basemap(llcrnrlon=-83.5,llcrnrlat=-4.5,urcrnrlon=-76,urcrnrlat=6, projection='cyl', resolution=None)
#map.drawcoastlines()



x, y = map(lon, lat)
#map.scatter(x, y, 200, color="r", marker="v", edgecolor="k", zorder=3)

ax = plt.gca()
for i in range(len(focmec)):
    b = Beach(focmec[i], xy=(x[i], y[i]), width=0.35, linewidth=1)
    b.set_zorder(1)
    ax.add_collection(b)

map.arcgisimage(service='NatGeo_World_Map', xpixels = 1500, verbose= True)
plt.show()