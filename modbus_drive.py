import minimalmodbus
import serial

class ModbusDriver:
    def __init__(self, port, slave_address):
        self.instrument = minimalmodbus.Instrument(port, slave_address)
        self.instrument.serial.baudrate = 9600
        self.instrument.serial.bytesize = 8
        self.instrument.serial.parity = serial.PARITY_NONE
        self.instrument.serial.stopbits = 1
        self.instrument.serial.timeout = 1

    def read_register(self, register_address):
        return self.instrument.read_register(register_address)

    def write_register(self, register_address, value):
        self.instrument.write_register(register_address, value)
