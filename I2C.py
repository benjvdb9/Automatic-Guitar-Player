import time
import smbus

bus = smbus.SMBus(1)
address = 0x12

print("Send 1:")
bus.write_byte(address, 1)
print("Data sent !")

time.sleep(1)

data = bus.read_byte(address)
print(data)
