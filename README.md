# esp8266_micropython

Using micropython on the esp8266 huzzah breakout from adafruit, I am gathering temperature data from the DS18B20 onewire temperature sensor for which there is a library provided in micropython -

http://docs.micropython.org/en/v1.8/esp8266/esp8266/tutorial/onewire.html

After importing this library and importing the python socket module, I opened up a socket connection to the client (in this case my raspberry pi).  On the client I also used the python socket module to connect to the esp8266 and simply printed the data to the terminal after executing the script.  

All of this was done via wifi.  
