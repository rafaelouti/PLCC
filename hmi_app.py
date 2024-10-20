import tkinter as tk
from PLCControlle import PLCController

class HMIApp:
    def __init__(self, root, plc_controller):
        self.root = root
        self.plc_controller = plc_controller
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Valor do Sensor:")
        self.label.pack()
        self.value_label = tk.Label(self.root, text="0")
        self.value_label.pack()
        self.update_button = tk.Button(self.root, text="Atualizar", command=self.update_value)
        self.update_button.pack()

    def update_value(self):
        sensor_value = self.plc_controller.modbus_driver.read_register(100)
        self.value_label.config(text=str(sensor_value))

if __name__ == "__main__":
    root = tk.Tk()
    modbus_driver = ModbusDriver('/dev/ttyUSB0', 1)
    plc_controller = PLCController(modbus_driver)
    app = HMIApp(root, plc_controller)
    root.mainloop()
