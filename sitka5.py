import csv
from datetime import datetime 
import matplotlib.pyplot as plt

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for index, column_header in enumerate(header_row):
        if column_header == 'TMAX':
            max_index = index
        elif column_header == 'TMIN':
            min_index = index
        elif column_header == 'NAME':
            station_name = next(reader)[index]


highs = []
dates = []
lows = []

with open(filename) as f:
    reader = csv.reader(f)
    next(reader) 
    for row in reader:
        try:
            high = int(row[max_index])
            low = int(row[min_index])
            thedate = datetime.strptime(row[2],'%Y-%m-%d')
        except ValueError:
            print(f"Missing data for {row}")
        else: 
            highs.append(high)
            lows.append(low)
            dates.append(thedate)


fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(12, 8))


ax1.plot(dates, highs, c='red', alpha=0.5)
ax1.plot(dates, lows, c='blue', alpha=0.5)
ax1.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
ax1.set_title(f"{station_name}", fontsize=16)
ax1.set_xlabel("", fontsize=12)
ax1.tick_params(axis="both", which="major", labelsize=12)


filename = 'death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for index, column_header in enumerate(header_row):
        if column_header == 'TMAX':
            max_index = index
        elif column_header == 'TMIN':
            min_index = index
        elif column_header == 'NAME':
            station_name2 = next(reader)[index]

highs = []
dates = []
lows = []

with open(filename) as f:
    reader = csv.reader(f)
    next(reader) 
    for row in reader:
        try:
            high = int(row[max_index])
            low = int(row[min_index])
            thedate = datetime.strptime(row[2],'%Y-%m-%d')
        except ValueError:
            print(f"Missing data for {row}")
        else: 
            highs.append(high)
            lows.append(low)
            dates.append(thedate)

ax2.plot(dates, highs, c='red', alpha=0.5)
ax2.plot(dates, lows, c='blue', alpha=0.5)
ax2.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
ax2.set_title(f"{station_name2}", fontsize=16)
ax2.set_xlabel("", fontsize=12)
ax2.tick_params(axis="both", which="major", labelsize=12)

fig.suptitle(f"Temperature comparison between {station_name} and {station_name2}")

fig.autofmt_xdate()

plt.show()
