# cognate-I SETUP

## need to install before proceed

1. please do install 2013 or up of Visual Studio
2. please do install Xampp server [ click me to install Xampp server ](https://www.apachefriends.org/download.html)
3. please install Python [ click me to install Python ](https://www.python.org/downloads/)
4. please install visual studio code [ click me to install Python ](https://code.visualstudio.com/download)
5. please install Arduino IDE

## using CMD pip install of the following
```shell
pip install cmake
```
```shell
pip install dlib
```
### NOTE: if this is succesfull proceed with this if not contact Art for installation failed

using visual studio code go to file/open folder and locate the cognate-I/Arduino folder 
once you located open the Terminal and run this command

```shell
pip install -r requirements.txt
```

### NOTE: if error occur contact me

## Arduino IDE setup

#### on your arduino IDE

go to preferences copy and paste this link
```shell
https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_dev_index.json 
```
on Additional Boards Manager URLs

#### go to Tools/Boards Managers and search this
```shell
esp32
```
after that 

#### go to Sketch/Include Library/Add .ZIP Library
locate the "esp32cam-main.zip" inside the cognate-I folder

## Setup Esp32 Cam
using arduino IDE locate open WifiCam.ino

#### on your arduino IDE change the board into AI Thinker ESP32-CAM
go to Tool/Board/ESP32 Arduino and locate the "AI Thinker ESP32-CAM"
#### on your 












