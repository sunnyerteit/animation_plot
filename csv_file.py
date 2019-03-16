'''
Generates randomized data in a structured .csv-file.
'''

import csv
import numpy as np
import random
import math

POINTS = 1000

TIME = 10

TIME_LIST = np.linspace(0, TIME, POINTS)


with open('sensor_data.csv', mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerow([
        'Time [s]',
        'Sensor 1 [m/s2]',
        'Sensor 2 [m/s2]'
    ])

    for time in TIME_LIST:
        csv_writer.writerow([
            time,
            (1 + 0.15 * (0.5 - random.random())) * math.sin(time),
            (0.65 + 0.34 * (0.5 - random.random())) * math.sin(time + 23.1)
        ])