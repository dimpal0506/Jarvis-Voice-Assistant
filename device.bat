@echo off
echo Disconnecting old connections...
adb disconnect

echo Restarting ADB in TCP/IP mode on port 5555...
adb tcpip 5555

:: Directly use your phone IP
set IP=MOBILE_IPAddress

echo Connecting to device with IP %IP%:5555 ...
adb connect %IP%:5555

echo ✅ Device connected successfully!
adb devices
pause
