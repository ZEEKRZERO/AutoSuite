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
* [Getting Started with the DEVKIT-MPC5748G](https://www.nxp.com/document/guide/getting-started-with-the-devkit-mpc5748g:NGS-DEVKIT-MPC5748G) 
* [openpilot/flexray_adapter/](https://github.com/nanamiwang/openpilot/tree/flexray_bounty/flexray_adapter) 
* [opendbc](https://github.com/commaai/opendbc) 
* FlexRay Protocol Specification Version 2.1 Revision A   
## Licensing
MIT License

