import csv

from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

filename = 'death_valley_2014.csv'

# Get dates and high temperatures from file.

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)


# plot data
fig, ax = plt.subplots(dpi = 128, figsize = (10,6))
ax.plot(dates, highs, c = 'red', label= 'Highs', alpha = 0.5)
ax.plot(dates, lows, c = 'blue', label= 'Lows', alpha = 0.5)
plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)


#Format plot
ax.set_title("Daily high and low temperatures - 2014\n Death Valley, CA", fontsize = 18)
ax.set_xlabel(" ", fontsize = 12)
fig.autofmt_xdate()
ax.set_ylabel("Temeprature (F)", fontsize = 16)

ax.xaxis.set_major_locator(mdates.MonthLocator()) # Major ticks for each month
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))  # Format for month names
#ax.xaxis.set_minor_locator(mdates.DayLocator()) # Minor ticks for each day
#ax.set_xlim(datetime(2014, 1, 1), datetime(2014, 12, 31))

plt.tick_params(axis = "both", which = "major", labelsize =16)

fig.text(0.5, 0.01, 'Source: Death Valley Weather Data, 2014', ha='center', fontsize=12)
plt.subplots_adjust(bottom=0.25)

ax.legend(loc='upper right', fontsize=12, frameon = False)

plt.show()


