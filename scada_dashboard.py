import matplotlib.pyplot as plt
import csv

class SCADADashboard:
    def __init__(self, log_file):
        self.log_file = log_file

    def plot_data(self):
        times = []
        values = []
        with open(self.log_file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                times.append(float(row[0]))
                values.append(float(row[1]))
        plt.plot(times, values)
        plt.xlabel('Time')
        plt.ylabel('Sensor Value')
        plt.show()
