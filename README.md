# PortinariDucks
ESP8266 controller for duckling cage

Connect the DHT11 on the ESP8266 as described on the picture.

![Squematics](https://github.com/pedromalta/PortinariDucks/raw/master/DH11-with-amica_.jpg)

Load the Lua Scripts onto the ESP8266, you only need to configure the `credentials.lua` file with your `SSID` and `Password`.

There's a Python/Mongo app to record the data, you only need to configure the IP of your ESP8266 module and run the `docker-compose up`
