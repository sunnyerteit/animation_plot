'''
Runs animated plot of sensor data in .csv-file.
'''

import numpy as np
import csv
import matplotlib.pyplot as plt
import matplotlib.animation as animation

FILE = 'sensor_data.csv'

TIME_LIST = []

SENSOR_LIST = [
    [],
    []
]

SENSOR_NAMES = []

with open(FILE) as file:

    csv_reader = csv.reader(file, delimiter=',')

    for row_index, row in enumerate(csv_reader):

        if row_index == 0:

            SENSOR_NAMES.append(row[1])
            SENSOR_NAMES.append(row[2])

        else:

            TIME_LIST.append(float(row[0]))
            SENSOR_LIST[0].append(float(row[1]))
            SENSOR_LIST[1].append(float(row[2]))

FIG, ax = plt.subplots()
SENSOR_1, = ax.plot(TIME_LIST, SENSOR_LIST[0], label=SENSOR_NAMES[0])
SENSOR_2, = ax.plot(TIME_LIST, SENSOR_LIST[1], label=SENSOR_NAMES[1])

plt.grid()
plt.legend()
plt.xlabel('Time [s]')
plt.ylabel('Acceleration [m/s2]')


def Update(
        index,
        SENSOR_1,
        SENSOR_2):
    """
    """

    SENSOR_1.set_data(TIME_LIST[:index], SENSOR_LIST[0][:index])
    SENSOR_2.set_data(TIME_LIST[:index], SENSOR_LIST[1][:index])

    return SENSOR_1, SENSOR_2


ANIMATION = animation.FuncAnimation(FIG, Update, len(TIME_LIST), fargs=[SENSOR_1, SENSOR_2],
                                    interval=25, blit=True)
plt.show()
