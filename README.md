# ADA Family Meters Integration for Home Assistant

![HACS Default](https://img.shields.io/badge/HACS-Default-orange.svg?style=flat-square)
![Home Assistant](https://img.shields.io/badge/Supports-Home%20Assistant-blue?style=flat-square)
![HACS Supported](https://img.shields.io/badge/HACS-Supported-41BDF5?style=flat-square)
![Version](https://img.shields.io/badge/dynamic/json?url=https://raw.githubusercontent.com/lewfpv/adap1meter/main/custom_components/greenhess/manifest.json&query=$.version&label=version&color=blue)
![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green?style=flat-square)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)
![Platform: Sensor](https://img.shields.io/badge/Platform-Sensor-lightgrey?style=flat-square)

This is a custom integration for [Home Assistant](https://www.home-assistant.io/) that provides sensor data from an ADA Meter, including total energy consumption, phase voltage, current, power factors, and more.

## Compatible devices

|						|(images/0.jpg)			|(images/1.jpg)			|(images/3.jpg)			|(images/4.jpg)			|
|						|**ADA P1 Meter**		|**ADA One**			|**ADA Bridge**			|**ADA PZIOT-E02**		|
|----------------------:|:---------------------:|:---------------------:|:---------------------:|:---------------------:|
|ESP Model				|ESP32 WROOM			|ESP D1 Mini			|ESP32 WROOM U32		|ESP8266EX				|
|Hardware/Firmware		|GreenHESS				|GreenHESS				|GreenHESS				|Peacefair/GreenHESS	|
|Functions				|36 datapoints, MQTT	|24 datapoints, MQTT	|Telegram API			|6 datapoints, MQTT 	|
|Connection				|RJ12 (P1 Port)			|RJ12 (P1 Port)			|USB					|DIN					|
|Configure with			|WiFi hotspot			|WiFi hotspot			|USB					|WiFi hotspot			|
|Data collection		|Serial, DSMR, Telegram	|Serial, DSMR, Telegram	|API, DSMR, Telegram	|Modbus					|
|Home Assistant ready	|✅						|✅						|✅						|✅						|
|MQTT Connection		|Optional				|okosvillanyora.hu		|Optional				|okosvillanyora.hu		|

[More information...](https://greenhess.com/ismerd-meg-az-uj-ada-termekeinket "More information...")

## Features

- **Total Imported and Exported Energy** (active and reactive)
- **Voltage and Current for Each Phase (L1, L2, L3)**
- **Instantaneous Power** (imported and exported)
- **Power Factor and Frequency**

## Installation

### HACS [Home Assistant Community Store] Installation (Recommended)
1. Add this repository to HACS as a custom repository. Go to HACS -> Custom repositories (top right corner).
(Required to install HACS first follow -> [THIS](https://www.hacs.xyz/docs/use/download/download/#to-download-hacs "HACS install tutorial"))

![add custom repo png](images/addcustomrepo.png)

2. Search for "ADA Family Meters" in the HACS store and install it.
3. Restart Home Assistant. :sparkles:

### Manual Installation
1. Download the files from this repository.
2. Place the `greenhess` folder in your Home Assistant `custom_components/` directory.
3. Restart Home Assistant.

## Configuration

To configure the integration:
1. Go to **Settings** > **Devices & Services** > **Add Integration**.
2. Search for "ADA Family Meters", select model, enter the connection details (e.g., hostname and port) or can use custom url (url must contain valid json data). If you add multiple devices from the same model you can use prefix for better identification.

![connect to png](images/connecttoada.png)

3. The integration will create sensors for each available measurement from the meter.

## Supported Sensors

- **Total Imported Energy** (kWh)
- **Total Exported Energy** (kWh)
- **Voltage for Phase L1, L2, L3** (V)
- **Current for Phase L1, L2, L3** (A)
- **Power Factor**
- **Frequency** (Hz)
- And more...

## Troubleshooting

If you encounter any issues, please check the Home Assistant logs under **Settings** > **Logs**. For more help, create an issue in this repository.

---

## Notes on mDNS and `.local` Domains

Issues with mDNS and `.local` domain resolution may occur on certain systems. This can lead to problems when the integration attempts to connect to devices using a `.local` domain. If you encounter this issue, there are a few options to resolve it:

1. Use the device's IP address instead of the `.local` domain.
2. Set up a local DNS server to resolve `.local` domains within your network.

To address this issue manually in the code, locate the following section in the `__init__.py` file of the integration:

```python
"""Fetch JSON data from the okosvillanyora.local server."""
url = "http://okosvillanyora.local:8989/json"
```

Replace the .local domain with the device's IP address, as shown below:

```python
"""Fetch JSON data from the okosvillanyora.local server."""
url = "http://<ADA_DEVICE_IP>:8989/json"
```

After making this change, restart Home Assistant to apply the updates.

---

## License

This project is licensed under the MIT License.

![ADA P1 Meter Icon](images/icon.png)
