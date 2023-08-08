![harware](/Hardware/autosuite.jpg)
![software1](/Software/screenshot/sniffer.png)

# AutoSuite
Autosuite:an open source multi-protocol low-cost vehicle bus testing framework 
AutoSUite consisting of the hardware and software. AutoSuite can be used to access the FlexRay bus and simulate malicious ECUs to send forged data to realize cross-domain ECU attacks and discover potential security vulnerabilities.  
# Architecture
![arch](/Software/screenshot/AutoSuiteARCH.jpg)
## 3D
The STL/DXF/DWG file of metal shell of AutoSuite, you can 3D print or CNC your own AutoSuite shell.
## Hardware
We will upload later.
## Firmware 
We will upload later.
## Software
### Requirements
```
pip install PySider6
pip install hidapi
pip install cantools
pip install pyserial
```
### Usage
```
cd AutoSuite/Software
python mainWindow.py
```
#### Connect Device
![connect](/Software/screenshot/setdevices.png)
* Click **Device-->Set Device Parameters**, choose **Connection Mode**, and config bus parameters.
* Click **Connect** to connect device. 

#### Sniffing 
![sniff](/Software/screenshot/sniffer.png) 
#### Signal Fuzz 
![fuzz](/Software/screenshot/signalfuzz.png) 
#### Import and Parse DBC 
![dbc](/Software/screenshot/importdbc.png)  
#### Send Data
![senddata](/Software/screenshot/senddata.png)

### Create EXE
Run AutoSuite/Software/pack.bat
## Reference
* [MPC5748G Microcontroller Data Sheet](https://www.nxp.com.cn/docs/en/data-sheet/MPC5748G.pdf) 
* [MPC5748G Hardware Design Guidelines](https://www.nxp.com/webapp/Download?colCode=AN5220) 
* [MPC574xG SDK Hands On Training](https://www.nxp.com/webapp/Download?colCode=MPC574xG-SDK-HOT) 
* [openpilot/flexray_adapter/](https://github.com/nanamiwang/openpilot/tree/flexray_bounty/flexray_adapter) 
* [opendbc](https://github.com/commaai/opendbc) 
* [FlexRay Protocol Specification Version 2.1 Revision A](https://www.softwareresearch.net/fileadmin/src/docs/teaching/SS08/PS_VS/FlexRayCommunicationSystem.pdf)    
## Licensing
MIT License

