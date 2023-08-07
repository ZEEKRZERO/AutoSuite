@echo off
setlocal
set "pyside6_lupdate=%PYTHON%\Scripts\pyside6-lupdate.exe"
echo %pyside6_lupdate%
REM 指定文件夹路径
set "folder=%cd%"
set "trans=%cd%\translations\trans.ts"
echo %trans%
echo %folder%
REM 变量用于保存拼接后的文件路径
set "files="

REM 获取指定文件夹下的所有.py文件并拼接
for /r "%folder%" %%i in (*.py) do (
   %pyside6_lupdate% %%i -ts %trans%
)

endlocal

pause