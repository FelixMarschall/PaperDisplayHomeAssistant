# PaperDisplayIntegration

## Setup

### permissons to access the RP spi interface are necessary

1. create rule file

```sudo nano /etc/udev/rules.d/50-spi.rules```

2. add line

```SUBSYSTEM=="spidev", GROUP="spiuser", MODE="0660"```

3. add current user to group

```
sudo groupadd spiuser
sudo adduser "$USER" spiuser
sudo reboot
```

https://forum.up-community.org/discussion/2141/solved-tutorial-gpio-i2c-spi-access-without-root-permissions

## Start

1. enter venv with 
```source myenv/bin/activate```

2. start uvicorn
  ```uvicorn main:app --host 0.0.0.0```

## Bind it as a RESTful sensor in HomeAssistant

https://www.home-assistant.io/integrations/sensor.rest

configuration.yaml

```
rest_command:
  eink_01_init:
    url: "http://aifb-bis-iot-rpi-eink-01.aifb.kit.edu:8000/display/init"
    method: GET
  eink_01_test:
    url: "http://aifb-bis-iot-rpi-eink-01.aifb.kit.edu:8000/display/test"
    method: GET
  eink_01_clear:
    url: "http://aifb-bis-iot-rpi-eink-01.aifb.kit.edu:8000/display/clear"
    method: GET
```
