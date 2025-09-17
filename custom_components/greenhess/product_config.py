"""Product configuration for ADA family devices."""

# Product definitions with their supported sensors
# ignored entries pziot-e02: username, password, wifi_ssid, local_ip, os_version, mac_address, cosem_logical_device_name,
# ignored entries ada one: username, password, os_version, local_ip, cosem_logical_device_name, client_id, current_tariff, timestamp
PRODUCT_CONFIGS = {
    "ada12": {
        "name": "ADA P1 Meter",
        "description": "Full-featured smart meter with all sensors",
        "host": "okosvillanyora.local",
        "default_port": 8989,
        "sensors": {
        # Összesített energia
        "active_import_energy_total": {
            "unit": "kWh",
            "friendly_name": "Total Imported Energy",
            "icon": "mdi:transmission-tower-import"
        },
        "active_export_energy_total": {
            "unit": "kWh",
            "friendly_name": "Total Exported Energy",
            "icon": "mdi:transmission-tower-export"
        },
        "total_active_energy": {
            "unit": "kWh",
            "friendly_name": "Total Active Energy",
            "icon": "mdi:lightning-bolt"
        },

        # Tarifa szerinti bontás
        "active_import_energy_tariff_1": {
            "unit": "kWh",
            "friendly_name": "Imported Energy Tariff 1",
            "icon": "mdi:counter"
        },
        "active_import_energy_tariff_2": {
            "unit": "kWh",
            "friendly_name": "Imported Energy Tariff 2",
            "icon": "mdi:counter"
        },
        "active_import_energy_tariff_3": {
            "unit": "kWh",
            "friendly_name": "Imported Energy Tariff 3",
            "icon": "mdi:counter"
        },
        "active_import_energy_tariff_4": {
            "unit": "kWh",
            "friendly_name": "Imported Energy Tariff 4",
            "icon": "mdi:counter"
        },
        "active_export_energy_tariff_1": {
            "unit": "kWh",
            "friendly_name": "Exported Energy Tariff 1",
            "icon": "mdi:counter"
        },
        "active_export_energy_tariff_2": {
            "unit": "kWh",
            "friendly_name": "Exported Energy Tariff 2",
            "icon": "mdi:counter"
        },
        "active_export_energy_tariff_3": {
            "unit": "kWh",
            "friendly_name": "Exported Energy Tariff 3",
            "icon": "mdi:counter"
        },
        "active_export_energy_tariff_4": {
            "unit": "kWh",
            "friendly_name": "Exported Energy Tariff 4",
            "icon": "mdi:counter"
        },

        # Reaktív energia (kVArh)
        "reactive_import_energy": {
            "unit": "kVArh",
            "friendly_name": "Reactive Imported Energy",
            "icon": "mdi:sine-wave"
        },
        "reactive_export_energy": {
            "unit": "kVArh",
            "friendly_name": "Reactive Exported Energy",
            "icon": "mdi:sine-wave"
        },
        "reactive_energy_qi": {
            "unit": "kVArh",
            "friendly_name": "Reactive Energy QI",
            "icon": "mdi:sine-wave"
        },
        "reactive_energy_qii": {
            "unit": "kVArh",
            "friendly_name": "Reactive Energy QII",
            "icon": "mdi:sine-wave"
        },
        "reactive_energy_qiii": {
            "unit": "kVArh",
            "friendly_name": "Reactive Energy QIII",
            "icon": "mdi:sine-wave"
        },
        "reactive_energy_qiv": {
            "unit": "kVArh",
            "friendly_name": "Reactive Energy QIV",
            "icon": "mdi:sine-wave"
        },

        # Pillanatnyi teljesítmény
        "instantaneous_power_import": {
            "unit": "kW",
            "friendly_name": "Instantaneous Imported Power",
            "icon": "mdi:flash"
        },
        "instantaneous_power_export": {
            "unit": "kW",
            "friendly_name": "Instantaneous Exported Power",
            "icon": "mdi:flash"
        },
        "instantaneous_power_import_l1": {
            "unit": "kW",
            "friendly_name": "Instantaneous Imported Power L1",
            "icon": "mdi:flash"
        },
        "instantaneous_power_import_l2": {
            "unit": "kW",
            "friendly_name": "Instantaneous Imported Power L2",
            "icon": "mdi:flash"
        },
        "instantaneous_power_import_l3": {
            "unit": "kW",
            "friendly_name": "Instantaneous Imported Power L3",
            "icon": "mdi:flash"
        },
        "instantaneous_power_export_l1": {
            "unit": "kW",
            "friendly_name": "Instantaneous Exported Power L1",
            "icon": "mdi:flash"
        },
        "instantaneous_power_export_l2": {
            "unit": "kW",
            "friendly_name": "Instantaneous Exported Power L2",
            "icon": "mdi:flash"
        },
        "instantaneous_power_export_l3": {
            "unit": "kW",
            "friendly_name": "Instantaneous Exported Power L3",
            "icon": "mdi:flash"
        },

        # Pillanatnyi reaktív teljesítmény
        "instantaneous_reactive_power_qi": {
            "unit": "kVAr",
            "friendly_name": "Instantaneous Reactive Power QI",
            "icon": "mdi:sine-wave"
        },
        "instantaneous_reactive_power_qii": {
            "unit": "kVAr",
            "friendly_name": "Instantaneous Reactive Power QII",
            "icon": "mdi:sine-wave"
        },
        "instantaneous_reactive_power_qiii": {
            "unit": "kVAr",
            "friendly_name": "Instantaneous Reactive Power QIII",
            "icon": "mdi:sine-wave"
        },
        "instantaneous_reactive_power_qiv": {
            "unit": "kVAr",
            "friendly_name": "Instantaneous Reactive Power QIV",
            "icon": "mdi:sine-wave"
        },

        # Feszültségek
        "voltage_phase_l1": {
            "unit": "V",
            "friendly_name": "Voltage Phase 1 (L1)",
            "icon": "mdi:flash"
        },
        "voltage_phase_l2": {
            "unit": "V",
            "friendly_name": "Voltage Phase 2 (L2)",
            "icon": "mdi:flash"
        },
        "voltage_phase_l3": {
            "unit": "V",
            "friendly_name": "Voltage Phase 3 (L3)",
            "icon": "mdi:flash"
        },

        # Áramerősségek
        "current_phase_l1": {
            "unit": "A",
            "friendly_name": "Current Phase 1 (L1)",
            "icon": "mdi:current-ac"
        },
        "current_phase_l2": {
            "unit": "A",
            "friendly_name": "Current Phase 2 (L2)",
            "icon": "mdi:current-ac"
        },
        "current_phase_l3": {
            "unit": "A",
            "friendly_name": "Current Phase 3 (L3)",
            "icon": "mdi:current-ac"
        },
        "current_phase_Bl1": {
            "unit": "A",
            "friendly_name": "Current Phase 1 (calculated) (L1)",
            "icon": "mdi:current-ac"
        },
        "current_phase_Bl2": {
            "unit": "A",
            "friendly_name": "Current Phase 2 (calculated) (L2)",
            "icon": "mdi:current-ac"
        },
        "current_phase_Bl3": {
            "unit": "A",
            "friendly_name": "Current Phase 3 (calculated) (L3)",
            "icon": "mdi:current-ac"
        },

        # Frekvencia
        "frequency": {
            "unit": "Hz",
            "friendly_name": "Frequency",
            "icon": "mdi:sine-wave"
        },

        # Teljesítménytényező
        "power_factor": {
            "unit": "",
            "friendly_name": "Power Factor",
            "icon": "mdi:cosine-wave"
        },
        "power_factor_l1": {
            "unit": "",
            "friendly_name": "Power Factor (L1)",
            "icon": "mdi:cosine-wave"
        },
        "power_factor_l2": {
            "unit": "",
            "friendly_name": "Power Factor (L2)",
            "icon": "mdi:cosine-wave"
        },
        "power_factor_l3": {
            "unit": "",
            "friendly_name": "Power Factor (L3)",
            "icon": "mdi:cosine-wave"
        },

        # Egyéb
        "meter_serial_number": {
            "unit": "",
            "friendly_name": "Meter Serial Number",
            "icon": "mdi:identifier"
        },
        "circuit_breaker_status": {
            "unit": "",
            "friendly_name": "Circuit Breaker Status",
            "icon": "mdi:toggle-switch"
        },
        "current_tariff": {
            "unit": "",
            "friendly_name": "Current Tariff",
            "icon": "mdi:calendar"
        },
        "timestamp": {
            "unit": "",
            "friendly_name": "Timestamp",
            "icon": "mdi:clock-outline"
        }
    }
    },
    "adaone": {
        "name": "ADA One",
        "description": "Basic meter with essential sensors only",
        "host": "adaone.local",
        "default_port": 80,
        "sensors": {
            "active_import_energy_total": {
                "unit": "kWh",
                "friendly_name": "Total Imported Energy",
                "icon": "mdi:transmission-tower-import"
            },
            "active_export_energy_total": {
                "unit": "kWh",
                "friendly_name": "Total Exported Energy",
                "icon": "mdi:transmission-tower-export"
            },
            "total_active_energy": {
                "unit": "kWh",
                "friendly_name": "Total Active Energy",
                "icon": "mdi:transmission-tower-import"
            },
            "power_factor": {
                "unit": "",
                "friendly_name": "Power Factor",
                "icon": "mdi:cosine-wave"
            },
            "power_factor_l1": {
                "unit": "",
                "friendly_name": "Power Factor (L1)",
                "icon": "mdi:cosine-wave"
            },
            "power_factor_l2": {
                "unit": "",
                "friendly_name": "Power Factor (L2)",
                "icon": "mdi:cosine-wave"
            },
            "power_factor_l3": {
                "unit": "",
                "friendly_name": "Power Factor (L3)",
                "icon": "mdi:cosine-wave"
            },
            "voltage_phase_l1": {
                "unit": "V",
                "friendly_name": "Voltage Phase 1 (L1)",
                "icon": "mdi:flash"
            },
            "voltage_phase_l2": {
                "unit": "V",
                "friendly_name": "Voltage Phase 2 (L2)",
                "icon": "mdi:flash"
            },
            "voltage_phase_l3": {
                "unit": "V",
                "friendly_name": "Voltage Phase 3 (L3)",
                "icon": "mdi:flash"
            },
            "current_phase_l1": {
                "unit": "A",
                "friendly_name": "Current Phase 1 (L1)",
                "icon": "mdi:current-ac"
            },
            "current_phase_Bl1": {
                "unit": "A",
                "friendly_name": "Current Phase 1 (calculated) (L1)",
                "icon": "mdi:current-ac"
            },
            "current_phase_l2": {
                "unit": "A",
                "friendly_name": "Current Phase 2 (L2)",
                "icon": "mdi:current-ac"
            },
            "current_phase_Bl2": {
                "unit": "A",
                "friendly_name": "Current Phase 2 (calculated) (L2)",
                "icon": "mdi:current-ac"
            },
            "current_phase_l3": {
                "unit": "A",
                "friendly_name": "Current Phase 3 (L3)",
                "icon": "mdi:current-ac"
            },
            "current_phase_Bl3": {
                "unit": "A",
                "friendly_name": "Current Phase 3 (calculated) (L3)",
                "icon": "mdi:current-ac"
            },
            "instantaneous_power_import": {
                "unit": "kW",
                "friendly_name": "Instantaneous Imported Power",
                "icon": "mdi:flash"
            },
            "instantaneous_power_export": {
                "unit": "kW",
                "friendly_name": "Instantaneous Exported Power",
                "icon": "mdi:flash"
            },
            "meter_serial_number": {
                "unit": "",
                "friendly_name": "Meter Serial Number",
                "icon": "mdi:identifier"
            }
        }
    },
    "adabridge": {
        "name": "ADA Bridge",
        "description": "Compact meter with minimal sensors",
        "host": "adabridge.local",
        "default_port": 80,
        "sensors": {
            "active_import_energy_total": {
                "unit": "kWh",
                "friendly_name": "Total Imported Energy",
                "icon": "mdi:transmission-tower-import"
            },
            "voltage_phase_l1": {
                "unit": "V",
                "friendly_name": "Voltage Phase 1 (L1)",
                "icon": "mdi:flash"
            },
            "current_phase_l1": {
                "unit": "A",
                "friendly_name": "Current Phase 1 (L1)",
                "icon": "mdi:current-ac"
            },
            "instantaneous_power_import": {
                "unit": "kW",
                "friendly_name": "Instantaneous Imported Power",
                "icon": "mdi:flash"
            }
        }
    },
    "adapziote02": {
        "name": "ADA PZIOT-E02",
        "description": "Compact meter with minimal sensors",
        "host": "pziot-e02.local",
        "default_port": 80,
        "sensors": {
            "active_energy_import_total": {
                "unit": "kWh",
                "friendly_name": "Total Imported Energy",
                "icon": "mdi:transmission-tower-import"
            },
            "voltage_l1": {
                "unit": "V",
                "friendly_name": "Voltage Phase 1 (L1)",
                "icon": "mdi:flash"
            },
            "current_phase_l1": {
                "unit": "A",
                "friendly_name": "Current Phase 1 (L1)",
                "icon": "mdi:current-ac"
            },
            "calculated_current_phase_l1": {
                "unit": "A",
                "friendly_name": "Current Phase 1 (calculated) (L1)",
                "icon": "mdi:current-ac"
            },
            "calculated_power_phase_l1": {
                "unit": "kW",
                "friendly_name": "Power Phase 1 (calculated) (L1)",
                "icon": "mdi:flash"
            },
            "power_factor_l1": {
                "unit": "",
                "friendly_name": "Power Factor (L1)",
                "icon": "mdi:cosine-wave"
            },
            "active_power_import": {
                "unit": "kW",
                "friendly_name": "Active Power Import",
                "icon": "mdi:flash"
            },
            "reactive_power_qi": {
                "unit": "kVAr",
                "friendly_name": "Reactive Power QI (inductive)",
                "icon": "mdi:sine-wave"
            },
            "frequency": {
                "unit": "Hz",
                "friendly_name": "Frequency",
                "icon": "mdi:waveform"
            },
            "meter_serial_number": {
                "unit": "",
                "friendly_name": "Meter Serial Number",
                "icon": "mdi:identifier"
            }
        }
}
}

def get_product_list():
    """Return list of available products for dropdown."""
    return [(key, config["name"]) for key, config in PRODUCT_CONFIGS.items()]

def get_product_sensors(product_type):
    """Return sensors configuration for a specific product."""
    return PRODUCT_CONFIGS.get(product_type, {}).get("sensors", {})

def get_product_name(product_type):
    """Return the display name for a product type."""
    return PRODUCT_CONFIGS.get(product_type, {}).get("name", product_type)
