## Mapas de sismicidad para intervalos de 2 meses en Pto Gaitan


from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import glob


## Defining the map
map = Basemap(llcrnrlon=-71.7,llcrnrlat=3.64,urcrnrlon=-71.1,urcrnrlat=4.1, projection='cyl', resolution=None)
#map.arcgisimage(service='ESRI_StreetMap_World_2D', xpixels = 3000, verbose= True) # Could Be
#map.arcgisimage(service='World_Topo_Map', xpixels = 3000, verbose= True) # Could be
map.arcgisimage(service='NatGeo_World_Map', xpixels = 1500, verbose= True) # THIS IS THE ONE!!!!!
#map.arcgisimage(service='ESRI_Imagery_World_2D', xpixels = 3000, verbose= True) # Too cloudy


## Ploting Wells
fil = open('CoordenadasPozos.csv', 'r')
cont1, cont2, cont3, cont4, cont5, cont6, cont7, cont9, contq1, contq3, contq4 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
for line in fil:
	lat_pozos = float(line.split(';')[1])
	lon_pozos = float(line.split(';')[0])
	#print lon_pozos, lat_pozos
	pad = line.split(';')[-1]
	#print pad, type(pad)
	x, y = map(lon_pozos, lat_pozos)
	if pad == '1\n':
		cont1 = cont1 + 1
		col = 'b'
		pad1 = map.scatter(x, y, color=col, marker='^', s=150, edgecolor='black', zorder=50)
	elif pad == '2\n':
		cont2 = cont2 + 1
		col = 'g'
		pad2 = map.scatter(x, y, color=col, marker='^', s=150, edgecolor='black', zorder=50)
	elif pad == '3\n':
		cont3 = cont3 + 1
		col = '#ffff00'
		pad3 = map.scatter(x, y, color=col, marker='^', s=150, edgecolor='black', zorder=50)
	elif pad == '4\n':
		cont4 = cont4 + 1
		col = '#8b4513'
		pad4 = map.scatter(x, y, color=col, marker='^', s=150, edgecolor='black', zorder=50)
	elif pad == '5\n':
		cont5 = cont5 + 1
		col = '#ff69b4'
		pad5 = map.scatter(x, y, color=col, marker='^', s=150, edgecolor='black', zorder=50)
	elif pad == '6\n':
		cont6 = cont6 + 1
		col = '#f0f8ff'
		pad6 = map.scatter(x, y, color=col, marker='^', s=150, edgecolor='black', zorder=50)
	elif pad == '7\n':
		cont7 = cont7 + 1
		col = 'r'
		pad7 = map.scatter(x, y, color=col, marker='^', s=150, edgecolor='black', zorder=50)
	elif pad == '9\n':
		cont9 = cont9 + 1
		col = 'c'
		pad9 = map.scatter(x, y, color=col, marker='^', s=150, edgecolor='black', zorder=50)
	elif pad == 'QDW-1\n':
		contq1 = contq1 + 1
		col = '#080808'
		padq1 = map.scatter(x, y, color=col, marker='D', s=140, edgecolor='black', zorder=50)
	elif pad == 'QDW-3\n':
		contq3 = contq3 + 1
		col = '#4d4d4d'
		padq3 = map.scatter(x, y, color=col, marker='D', s=140, edgecolor='black', zorder=50)
	else:
		contq4 = contq4 + 1
		col = '#cccccc'
		padq4 = map.scatter(x, y, color=col, marker='D', s=140, edgecolor='black', zorder=50)
		
		
## Plotting new found wells


## Ploting events
ev_lats1 = []
ev_lons1 = []
ev_lats2 = []
ev_lons2 = []
ev_lats3 = []
ev_lons3 = []
ev_lats4 = []
ev_lons4 = []
ev_lats5 = []
ev_lons5 = []
ev_lats6 = []
ev_lons6 = []
l_imp_ev = []
fil2 = open('catalogo_spectraseis.txt', 'r')
for line in fil2:
	mon = float(line.split()[3])
	mag = float(line.split()[5])
	if mag > 2.8:
		l_imp_ev.append(line)
	if mon == 1 or mon == 2:
		ev_lons1.append(float(line.split()[0]))
		ev_lats1.append(float(line.split()[1]))
	elif mon == 3 or mon == 4:
		ev_lons2.append(float(line.split()[0]))
		ev_lats2.append(float(line.split()[1]))
	elif mon == 5 or mon == 6:
		ev_lons3.append(float(line.split()[0]))
		ev_lats3.append(float(line.split()[1]))
	elif mon == 7 or mon == 8:
		ev_lons4.append(float(line.split()[0]))
		ev_lats4.append(float(line.split()[1]))
	elif mon == 9 or mon == 10:
		ev_lons5.append(float(line.split()[0]))
		ev_lats5.append(float(line.split()[1]))
	elif mon == 11 or mon == 12:
		ev_lons6.append(float(line.split()[0]))
		ev_lats6.append(float(line.split()[1]))
x1, y1 = map(ev_lons1, ev_lats1)
x2, y2 = map(ev_lons2, ev_lats2)
x3, y3 = map(ev_lons3, ev_lats3)
x4, y4 = map(ev_lons4, ev_lats4)
x5, y5 = map(ev_lons5, ev_lats5)
x6, y6 = map(ev_lons6, ev_lats6)
mes = input('Feb:1 \nAbr:2 \nJun:3 \nAgo:4 \nOct:5 \nDic:6 \n')
if mes == 1:
	enefeb = map.scatter(x1, y1, color='#977316', edgecolor='#7f7400', s=25, zorder=10)
	leyend_month = plt.legend([enefeb], ['Ene-Feb'], loc=3)
	plt.gca().add_artist(leyend_month)
elif mes == 2:
	enefeb = map.scatter(x1, y1, color='#977316', edgecolor='#7f7400', s=25, zorder=10)
	marabr = map.scatter(x2, y2, color='#ae8319', edgecolor='#7f7400', s=25, zorder=10)
	leyend_month = plt.legend([enefeb, marabr], ['Ene-Feb', 'Mar-Abr'], loc=3)
	plt.gca().add_artist(leyend_month)
elif mes == 3:
	enefeb = map.scatter(x1, y1, color='#977316', edgecolor='#7f7400', s=25, zorder=10)
	marabr = map.scatter(x2, y2, color='#ae8319', edgecolor='#7f7400', s=25, zorder=10)
	mayjun = map.scatter(x3, y3, color='#c4941d', edgecolor='#7f7400', s=25, zorder=10)
	leyend_month = plt.legend([enefeb, marabr, mayjun], ['Ene-Feb', 'Mar-Abr', 'May-Jun'], loc=3)
	plt.gca().add_artist(leyend_month)
elif mes == 4:
	enefeb = map.scatter(x1, y1, color='#977316', edgecolor='#7f7400', s=25, zorder=10)
	marabr = map.scatter(x2, y2, color='#ae8319', edgecolor='#7f7400', s=25, zorder=10)
	mayjun = map.scatter(x3, y3, color='#c4941d', edgecolor='#7f7400', s=25, zorder=10)
	julago = map.scatter(x4, y4, color='#daa520', edgecolor='#7f7400', s=25, zorder=10)
	leyend_month = plt.legend([enefeb, marabr, mayjun, julago], ['Ene-Feb', 'Mar-Abr', 'May-Jun', 'Jul-Ago'], loc=3)
	plt.gca().add_artist(leyend_month)
elif mes == 5:
	enefeb = map.scatter(x1, y1, color='#977316', edgecolor='#7f7400', s=25, zorder=10)
	marabr = map.scatter(x2, y2, color='#ae8319', edgecolor='#7f7400', s=25, zorder=10)
	mayjun = map.scatter(x3, y3, color='#c4941d', edgecolor='#7f7400', s=25, zorder=10)
	julago = map.scatter(x4, y4, color='#daa520', edgecolor='#7f7400', s=25, zorder=10)
	sepoct = map.scatter(x5, y5, color='#e1af33', edgecolor='#7f7400', s=25, zorder=10)
	leyend_month = plt.legend([enefeb, marabr, mayjun, julago, sepoct], ['Ene-Feb', 'Mar-Abr', 'May-Jun', 'Jul-Ago', 'Sep-Oct'], loc=3)
	plt.gca().add_artist(leyend_month)
elif mes == 6:
	enefeb = map.scatter(x1, y1, color='#977316', edgecolor='#7f7400', s=25, zorder=10)
	marabr = map.scatter(x2, y2, color='#ae8319', edgecolor='#7f7400', s=25, zorder=10)
	mayjun = map.scatter(x3, y3, color='#c4941d', edgecolor='#7f7400', s=25, zorder=10)
	julago = map.scatter(x4, y4, color='#daa520', edgecolor='#7f7400', s=25, zorder=10)
	sepoct = map.scatter(x5, y5, color='#e1af33', edgecolor='#7f7400', s=25, zorder=10)
	novdic = map.scatter(x6, y6, color='#e4b849', edgecolor='#7f7400', s=25, zorder=10)
	leyend_month = plt.legend([enefeb, marabr, mayjun, julago, sepoct, novdic], ['Ene-Feb', 'Mar-Abr', 'May-Jun', 'Jul-Ago', 'Sep-Oct', 'Nov-Dic'], loc=3)
	plt.gca().add_artist(leyend_month)

elec = raw_input('Graficar importantes? (s/n)\n ')

if str(elec) == 's':
	l_lons_imp = []
	l_lats_imp = []
	for imp in l_imp_ev:
		print imp.split()
		imp_lon, imp_lat = imp.split()[0], imp.split()[1]
		l_lons_imp.append(imp_lon)
		l_lats_imp.append(imp_lat)
	ximp, yimp = map(l_lons_imp, l_lats_imp)
	imps = map.scatter(ximp, yimp, color='#FF00FF', edgecolor='#660066', marker='*', s=120, zorder=45)
	
		
else:
	print 'TENEEEE'

parallels = np.arange(0.0,7.7,0.2)
# labels = [left,right,top,bottom]
map.drawparallels(parallels,labels=[True,True,False,False])
meridians = np.arange(-75.,-70.,0.2)
map.drawmeridians(meridians,labels=[False,False,True,True])
plt.legend([imps, pad1, pad2, pad3, pad4, pad5, pad6, pad7, pad9, padq1, padq3, padq4], ['Evento Destacado', 'Pad 1, Pozos: %s' % cont1, 'Pad 2, Pozos: %s' % cont2, 'Pad 3, Pozos: %s' % cont3, 'Pad 4, Pozos: %s' % cont4, 'Pad 5, Pozos: %s' % cont5, 'Pad 6, Pozos: %s' % cont6, 'Pad 7, Pozos: %s' % cont7, 'Pad 9, Pozos: %s' % cont9, 'QDW1, Pozos: %s' % contq1, 'QDW3, Pozos: %s' % contq3, 'QDW4, Pozos: %s' % contq4], scatterpoints=1, loc=4)
plt.show()

