# ADA P1 Meter Integration for Home Assistant

This is a custom integration for [Home Assistant](https://www.home-assistant.io/) that provides sensor data from an ADA P1 Meter, including total energy consumption, phase voltage, current, power factors, and more.

## Features

- **Total Imported and Exported Energy** (active and reactive)
- **Voltage and Current for Each Phase (L1, L2, L3)**
- **Instantaneous Power** (imported and exported)
- **Power Factor and Frequency**

## Installation

### HACS Installation (Recommended)
1. Add this repository to HACS as a custom repository.
2. Search for "ADA P1 Meter" in the HACS store and install it.
3. Restart Home Assistant.

### Manual Installation
1. Download the files from this repository.
2. Place them in your Home Assistant `custom_components/ada12` directory.
3. Restart Home Assistant.

## Configuration

To configure the integration:
1. Go to **Settings** > **Devices & Services** > **Add Integration**.
2. Search for "ADA P1 Meter" and enter the connection details (e.g., hostname and port).
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

## License

This project is licensed under the MIT License.

![ADA P1 Meter Icon](images/icon.png)

