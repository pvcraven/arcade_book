"""
Create a candlestick chart for a stock
"""
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, WeekdayLocator,\
     DayLocator, MONDAY
from matplotlib.finance import quotes_historical_yahoo_ohlc, candlestick_ohlc

# Grab the stock data between these dates
date1 = (2014, 10, 13)
date2 = (2014, 11, 13)

# Go to the web and pull the stock info
quotes = quotes_historical_yahoo_ohlc('AAPL', date1, date2)
if len(quotes) == 0:
    raise SystemExit

# Set up the graph
fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)

# Major ticks on Mondays
mondays = WeekdayLocator(MONDAY)
ax.xaxis.set_major_locator(mondays)

# Minor ticks on all days
alldays = DayLocator()
ax.xaxis.set_minor_locator(alldays)

# Format the days
weekFormatter = DateFormatter('%b %d')  # e.g., Jan 12
ax.xaxis.set_major_formatter(weekFormatter)
ax.xaxis_date()

candlestick_ohlc(ax, quotes, width=0.6)

ax.autoscale_view()
plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')

plt.show()
