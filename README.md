# EV3-RFCOMM
Our wireless channel on the EV3 device is through the legace Bluetooth connection. In leJOS EV3, RFCOMM (Radio Frequency Communication) can be used to establish classic Bluetooh serial port communication. This allows you to send and receive raw data packets between your EV3 brick and a PC (including Raspberry Pi), smartphone, and another brick, just like a physical serial cable. 

Python's built-in socket module has native support for Bluetooth RFCOMM sockets on Linux (via AF_BLUETOOTH for low-level Bluetooth communication). We just need standard library on Linux.

## 0. Prerequisite
You need to pair the Pi with EV3, and connect them via Personal Area Network (PAN), so that you can load the server program to the Pi and maintain the Bluetooth connection. 

## 1. On the EV3 side
We can use the BTConnector and wait for a connection with NXTConnection.RAW mode. This creates input and output streams you can use for communication.

You can find the [BTServer.java](/src/EV3/BTServer.java) program to start the server side and wait for the client to connect. Please put both `BTServer.java` and `BTConnection.java` (from [here](/src/EV3/BTConnection.java)) under a package named `bluetooth`, or please change the package declaration. 

## 2. On the Pi side
The underlying protocol for this Bluetooth communication is independent from the programming language used, so we can have Python program on the Pi as the client. You can find the [example code here](/src/Pi/bluetooth_client.py). Once the server is ready and listening, then you can start this client program. 

**Please pay attention**: when sending data, you need to append "\r\n" at the end of message. 



