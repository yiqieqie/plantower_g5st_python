import time
import serial

class plantower_ctrl:
  def __init__(self):
    self.ser = serial.Serial( #下面这些参数根据情况修改
      port='/dev/ttyUSB0',
      baudrate=9600,
      parity=serial.PARITY_NONE,
      bytesize=serial.EIGHTBITS,
      stopbits=serial.STOPBITS_ONE,
      xonxoff=False,
      timeout=3.0
    )

  def monitor(self, bytelen):
    if bytelen == 40: 
      try:
        print("start: " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        data = self.ser.read(bytelen)
        #print(data)
        data_hex = [hex(x) for x in data]
        #print(data_hex)
        data_hex_a = [ "%02X" % x for x in data ]
        print('PM1.0: ')
        print(int(''.join(data_hex_a[4:6]), 16))
        print('PM2.5-标准: ')
        print(int(''.join(data_hex_a[8:10]), 16))
        print('PM2.5-大气: ')
        print(int(''.join(data_hex_a[12:14]), 16))
        print('甲醛: ')
        print(int(''.join(data_hex_a[28:30]), 16)/1000)
        print('温度: ')
        print(int(''.join(data_hex_a[30:32]), 16)/10)
        print('湿度: ')
        print(int(''.join(data_hex_a[32:34]), 16)/10)
      except IOError:
        print("IOErrot")
    else:
      self.ser.read(bytelen)
      

if __name__ == '__main__':
  sensor = plantower_ctrl()
  while True:
    bytelen = sensor.ser.inWaiting()
    sensor.monitor(bytelen)
    time.sleep(1) 
