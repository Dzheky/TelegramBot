
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.dates import datetime as dt
from matplotlib.dates import DateFormatter
# from test import previous_values_w

# x_list = [1, 2, 3, 4, 5, 6, 7]
# y_list = [50.0, 49.8, 49.5, 49.6, 49.0, 49.7, 49.5]

# plt.title("Weight change chart for the last 7 days", fontsize=14, fontweight="bold", color="blue")
# plt.xlabel('time', fontsize=12, color="black")
# plt.ylabel('kg', fontsize=12, color="black")
# plt.plot(x_list, y_list, label="kg")
# plt.legend()
# plt.grid
# plt.show()

# Data for plotting
# t = ['2021-10-13', '2021-10-13', '2021-10-13', '2021-10-13', '2021-10-13', '2021-10-13', '2021-10-13']
# s = [49.9, 49.4, 49.7, 49.2, 49.0, 49.1, 49.3]



# dates= ['2021-10-13', '2021-10-13', '2021-10-13', '2021-10-13', '2021-10-13', '2021-10-13', '2021-10-13']
# t = [dt.datetime.strptime(d, '%Y-%m-%d') for d in dates]
# print(t)
# s = [49.9, 49.4, 49.7, 49.2, 49.0, 49.1, 49.3]

# fig, ax = plt.subplots()
# ax.plot(t, s)

# ax.set(xlabel='time (d)', ylabel='weight (kg)',
#        title='Weight change chart for 7 days')
# ax.grid()

# fig.savefig("test.png")
# plt.show()


formatter = DateFormatter('%d.%m')

f = plt.figure()
ax = f.add_subplot(111)

raw_dates = ['2021-10-13', '2021-10-14', '2021-10-14', '2021-10-16', '2021-10-17', '2021-10-18', '2021-10-19']
x = [dt.datetime.strptime(d, '%Y-%m-%d') for d in raw_dates]
y = [49.9, 49.4, 49.7, 49.2, 49.0, 49.1, 49.3]
ax.plot(x, y)

ax.xaxis.set_major_formatter(formatter)
plt.show()
