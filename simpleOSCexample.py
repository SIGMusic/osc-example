from simpleOSC import initOSCClient, sendOSCMsg
import time

ip = "127.0.0.1"
port = 9002

initOSCClient(ip, port)

sendOSCMsg("/vol", [0.05])
sendOSCMsg("/bypass", [1])

c_arp = [261.63, 329.63, 392.00, 523.25]

i=0
while(1):
  sendOSCMsg("/freq", [c_arp[i]])
  sendOSCMsg("/bang", [1])
  i = (i+1)%4
  time.sleep(0.5)
