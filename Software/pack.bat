pyinstaller mainWindow.spec
set "source_folder1=%cd%\cfg"
set "source_folder2=%cd%\data"
set "destination_folder1=%cd%\dist\mainWindow\cfg"
set "destination_folder2=%cd%\dist\mainWindow\data"
xcopy "%source_folder1%" "%destination_folder1%" /E /I /Y
xcopy "%source_folder2%" "%destination_folder2%" /E /I /Y
pause
