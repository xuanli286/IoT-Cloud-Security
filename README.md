# Getting Started
1. Launch Terminal and execute the following commands.
    ``` 
    ssh xuanli@xuanli.local
    ```
    ```
    cd IoT-Cloud-Security
    ```
    ```
    sudo apt install python3-paho-mqtt
    ```
    ```
    python producer.py
    ```
    
2. Under AWS IoT Core, navigate to <b>Test</b> > <b>MQTT test client</b>. Subscribe to `raspi/data` topic to see the messages.

# VNC Viewer
Launch VNC Viewer and connect to `192.168.111.20:5901`.