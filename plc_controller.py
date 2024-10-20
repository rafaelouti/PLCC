class PLCController:
    def __init__(self, modbus_driver):
        self.modbus_driver = modbus_driver

    def control_logic(self):
        # Exemplo de lógica de controle
        sensor_value = self.modbus_driver.read_register(100)
        if sensor_value > 50:
            self.modbus_driver.write_register(200, 1)  # Liga um atuador
        else:
            self.modbus_driver.write_register(200, 0)  # Desliga o atuador
