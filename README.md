# Getting Started
1. Launch VNC Viewer and connect to `192.168.111.20:5901`.
2. Launch Terminal and execute the following commands.
    ``` 
    ssh xuanli@xuanli.local
    ```
    ```
    cd iot-test
    ```
    ```
    sudo apt install python3-paho-mqtt
    ```
    ```
    python iot.py
    ```
    
3. Under AWS IoT Core, navigate to <b>Test</b> > <b>MQTT test client</b>. Subscribe to `raspi/data` topic to see the messages.