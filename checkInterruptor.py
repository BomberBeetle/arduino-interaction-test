import serial.tools.list_ports
import serial
import keyboard
import time
import datetime
AVports =[comport.device for comport in serial.tools.list_ports.comports()]
print("Portas Disponíveis: " + str(AVports))
portIndex = input()
portIndex = int(portIndex)
print("Porta Escolhida: " + AVports[portIndex])
usePort = AVports[portIndex]
ser = serial.Serial(usePort, 19200)
time.sleep(2)
say = ' '
total = 1;
cycles = 1;
m=0;
startime = datetime.datetime.now()
while True:
    ser.write(b'c')
    if (b"O interruptor esta ligado.") in ser.readline() :
        total += 1
        cycles += 1
    else:
        cycles += 1
    m = total/cycles
    if keyboard.is_pressed('b'):
        print("O interruptor fica ligado, em média, " + str((m*100)) + "% do tempo.")
