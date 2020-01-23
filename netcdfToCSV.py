# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import netCDF4
import pandas as pd 

data = netCDF4.Dataset("G:\My Drive\SKRIPSIAN\program\python\edit.nc")
print(data.variables.keys())

lat = data.variables['latitude'][:]
lon = data.variables['longitude'][:]
thetao = data.variables['thetao'][:]
bottomT = data.variables['bottomT'][:]
so = data.variables['so'][:]
zos = data.variables['zos'][:]
depth = data.variables['depth'][:]
time = data.variables['time']
dtime = netCDF4.num2date(time[:],time.units)
nlon = len(lon)
nlat = len(lat)

bottomTlist = []
zoslist = []
latlist = []
lonlist = []
timelist= []


print('convert bottomT and zos')
for i in range(len(dtime)):
    utime = dtime[i]
    for j in range(nlat):
        ulat = lat[j]
        for k in range(nlon):
            ulon = lon[k]
            ubottomT = bottomT[i,j,k]
            uzos = zos[i,j,k]
            timelist.append(utime)
            latlist.append(ulat)
            lonlist.append(ulon)
            bottomTlist.append(ubottomT)
            zoslist.append(uzos)
udata = {'time':timelist, 'latitude':latlist, 'longitude':lonlist,
         'bottomT': bottomTlist, 'zos': zoslist}
df = pd.DataFrame(udata)
df.to_csv('bottomT.csv', index = True, header = True)

latlist = []
lonlist = []
timelist = []
depthlist = []
solist = []
thetaolist = []
print('convert so and thetao')
for i in range(len(dtime)):
    utime = dtime[i]
    for j in range(len(depth)):
        udepth = depth[j]
        for k in range(nlat):
            ulat = lat[k]
            for l in range(nlon):
                ulon = lon[l]
                uso = so[i,j,k,l]
                uthetao = thetao[i,j,k,l]
                timelist.append(utime)
                depthlist.append(udepth)
                latlist.append(ulat)
                lonlist.append(ulon)
                solist.append(uso)
                thetaolist.append(uthetao)
udata2 = {'time':timelist, 'latitude':latlist, 'longitude':lonlist,
          'depth': depthlist, 'so':solist, 'thetao': thetaolist}
df2 = pd.DataFrame(udata2)
df2.to_csv('so_thetao.csv', index= True, header = True)