#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('speedtest.log')    #Read speedtest.log as csv

df['Timestamp']
df['Download'] *= 0.000008       #Bits to Megabytes
df['Upload'] *= 0.000008
df['Download'] /= 8
df['Upload'] /= 8

download = df['Download']
upload = df['Upload']
date = df['Timestamp'].str.slice(start=0, stop=10) #Slice the Sztring to Format the date from Unix Time, to Human-readable time

y1 = (download)
y2 = (upload)
x1 = (date)

fig, ax1 = plt.subplots()

ax1.set_xlabel('Timestamp')
ax1.set_ylabel('Download', color='green')
plot1 = ax1.plot(x1, y1, color = 'green', label = 'Download')
ax1.tick_params(axis = 'y', labelcolor = 'green')

#Both graphs will be plotted in one Graphic

ax2 = ax1.twinx()
ax2.set_ylabel('Upload', color='blue') 
plot2 = ax2.stem(x1, y2, label = 'Upload')
ax2.tick_params(axis = 'y', labelcolor = 'blue')

plt.show()
#plt.savefig("Speedtest.png")
