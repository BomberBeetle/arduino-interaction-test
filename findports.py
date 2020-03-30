import serial.tools.list_ports
import serial
import keyboard
import time
AVports =[comport.device for comport in serial.tools.list_ports.comports()]
print("Portas Disponiveis: " + str(AVports))
portIndex = input()
portIndex = int(portIndex)
print("Porta Escolhida: " + AVports[portIndex])
usePort = AVports[portIndex]
ser = serial.Serial(usePort, 19200)
time.sleep(2)
say = ' '
total = 0;
cycles = 1;
m=0;
while True:
    ser.write(b'c')
    if (b"O interruptor esta ligado.") in ser.readline():
        total += 1
        cycles += 1
    else:
        cycles += 1
    m = total/cycles
    if keyboard.is_pressed('a'):
        ser.write(b'x')
        print(ser.readline())
    if keyboard.is_pressed('b'):
        ser.write(b'c')
        print(ser.readline())
    if keyboard.is_pressed('x'):
        print("O interruptor fica ligado, em media, " + str((m*100)) + " por cento do tempo.")
			


