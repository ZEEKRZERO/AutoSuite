![harware](/Hardware/autosuite.jpg)
![software1](/Software/screenshot/Snipaste_2023-08-04_16-35-06.png)

# AutoSuite
Autosuite:an open source multi-protocol low-cost vehicle bus testing framework 
AutoSUite consisting of the hardware and software. AutoSuite can be used to access the FlexRay bus and simulate malicious ECUs to send forged data to realize cross-domain ECU attacks and discover potential security vulnerabilities.  
## 3D
The STL/DXF/DWG file of metal shell of AutoSuite, you can 3D print or CNC your own AutoSuite shell.
## Hardware
We will upload after [BlackHat USA 2023](https://www.blackhat.com/us-23/arsenal/schedule/index.html#autosuite-an-open-source-multi-protocol-low-cost-vehicle-bus-testing-framework-33563)
## Firmware 
We will upload after [BlackHat USA 2023](https://www.blackhat.com/us-23/arsenal/schedule/index.html#autosuite-an-open-source-multi-protocol-low-cost-vehicle-bus-testing-framework-33563)
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

### Create EXE
Run AutoSuite/Software/pack.bat
## Reference
[openpilot/flexray_adapter/](https://github.com/nanamiwang/openpilot/tree/flexray_bounty/flexray_adapter)
## Licensing
MIT License

