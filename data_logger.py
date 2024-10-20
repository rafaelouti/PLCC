import csv
import time

class DataLogger:
    def __init__(self, plc_controller, log_file):
        self.plc_controller = plc_controller
        self.log_file = log_file

    def log_data(self):
        with open(self.log_file, 'a', newline='') as file:
            writer = csv.writer(file)
            while True:
                sensor_value = self.plc_controller.modbus_driver.read_register(100)
                writer.writerow([time.time(), sensor_value])
                time.sleep(1)
