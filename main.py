from communication.modbus_driver import ModbusDriver
from control.plc_controller import PLCController
from hmi.hmi_app import HMIApp
from monitoring.data_logger import DataLogger
from scada.scada_dashboard import SCADADashboard
import tkinter as tk
import threading

def main():
    modbus_driver = ModbusDriver('/dev/ttyUSB0', 1)
    plc_controller = PLCController(modbus_driver)
    data_logger = DataLogger(plc_controller, 'data_log.csv')
    scada_dashboard = SCADADashboard('data_log.csv')

    # Start data logging in a separate thread
    threading.Thread(target=data_logger.log_data).start()

    # Start HMI
    root = tk.Tk()
    app = HMIApp(root, plc_controller)
    root.mainloop()

    # Plot data after closing HMI
    scada_dashboard.plot_data()

if __name__ == "__main__":
    main()
