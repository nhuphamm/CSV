
#using the datetime module
#adding dates to the x axis
#1) changing the file to include all the data for the year of 2018
#2) change the title to - Daily and low high temperature - 2018 
#3) extract low temps from the file and add to chart
#4) shade in the area between high and low 

import csv
from datetime import datetime 

infile = open('sitka_weather_2018_simple.csv','r')

csvfile = csv.reader(infile)

header_row = next(csvfile)

for index, column_header in enumerate(header_row):
    print(index,column_header)

highs = []
dates = []
lows = []

mydate = datetime.strptime('2018-07-01','%Y-%m-%d')
print(mydate)

for row in csvfile:
    highs.append(int(row[5]))
    lows.append(int(row[6]))
    thedate = datetime.strptime(row[2],'%Y-%m-%d')
    dates.append(thedate)

# print(highs)

import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot(dates, highs, c='red',alpha=0.5)
plt.plot(dates, lows, c='blue',alpha=0.5)

plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

plt.fill_between(dates,highs,lows,color="pink")

plt.title("Daily high and low temperatures - 2018", fontsize=16)
plt.xlabel("")
plt.ylabel("Temperature(F)",fontsize=12)
plt.tick_params(axis="both",which="major",labelsize=12)

fig.autofmt_xdate()

plt.show()

plt.subplot(2,1,1)
plt.plot(dates,highs,c='red')
plt.title("Highs")

plt.subplot(2,1,2)
plt.plot(dates,lows,c='blue')
plt.title("Lows")

plt.suptitle("Highs and Lows of Sitka, Alaska")

plt.show()



