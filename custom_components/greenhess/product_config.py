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
            "icon": "mdi:transmission-tower-import"
        },
        "active_export_energy_total": {
            "unit": "kWh",
            "icon": "mdi:transmission-tower-export"
        },
        "total_active_energy": {
            "unit": "kWh",
            "icon": "mdi:lightning-bolt"
        },

        # Tarifa szerinti bontás
        "active_import_energy_tariff_1": {
            "unit": "kWh",
            "icon": "mdi:counter"
        },
        "active_import_energy_tariff_2": {
            "unit": "kWh",
            "icon": "mdi:counter"
        },
        "active_import_energy_tariff_3": {
            "unit": "kWh",
            "icon": "mdi:counter"
        },
        "active_import_energy_tariff_4": {
            "unit": "kWh",
            "icon": "mdi:counter"
        },
        "active_export_energy_tariff_1": {
            "unit": "kWh",
            "icon": "mdi:counter"
        },
        "active_export_energy_tariff_2": {
            "unit": "kWh",
            "icon": "mdi:counter"
        },
        "active_export_energy_tariff_3": {
            "unit": "kWh",
            "icon": "mdi:counter"
        },
        "active_export_energy_tariff_4": {
            "unit": "kWh",
            "icon": "mdi:counter"
        },

        # Reaktív energia (kVArh)
        "reactive_import_energy": {
            "unit": "kVArh",
            "icon": "mdi:sine-wave"
        },
        "reactive_export_energy": {
            "unit": "kVArh",
            "icon": "mdi:sine-wave"
        },
        "reactive_energy_qi": {
            "unit": "kVArh",
            "icon": "mdi:sine-wave"
        },
        "reactive_energy_qii": {
            "unit": "kVArh",
            "icon": "mdi:sine-wave"
        },
        "reactive_energy_qiii": {
            "unit": "kVArh",
            "icon": "mdi:sine-wave"
        },
        "reactive_energy_qiv": {
            "unit": "kVArh",
            "icon": "mdi:sine-wave"
        },

        # Pillanatnyi teljesítmény
        "instantaneous_power_import": {
            "unit": "kW",
            "icon": "mdi:flash"
        },
        "instantaneous_power_export": {
            "unit": "kW",
            "icon": "mdi:flash"
        },
        "instantaneous_power_import_l1": {
            "unit": "kW",
            "icon": "mdi:flash"
        },
        "instantaneous_power_import_l2": {
            "unit": "kW",
            "icon": "mdi:flash"
        },
        "instantaneous_power_import_l3": {
            "unit": "kW",
            "icon": "mdi:flash"
        },
        "instantaneous_power_export_l1": {
            "unit": "kW",
            "icon": "mdi:flash"
        },
        "instantaneous_power_export_l2": {
            "unit": "kW",
            "icon": "mdi:flash"
        },
        "instantaneous_power_export_l3": {
            "unit": "kW",
            "icon": "mdi:flash"
        },

        # Pillanatnyi reaktív teljesítmény
        "instantaneous_reactive_power_qi": {
            "unit": "kVAr",
            "icon": "mdi:sine-wave"
        },
        "instantaneous_reactive_power_qii": {
            "unit": "kVAr",
            "icon": "mdi:sine-wave"
        },
        "instantaneous_reactive_power_qiii": {
            "unit": "kVAr",
            "icon": "mdi:sine-wave"
        },
        "instantaneous_reactive_power_qiv": {
            "unit": "kVAr",
            "icon": "mdi:sine-wave"
        },

        # Feszültségek
        "voltage_phase_l1": {
            "unit": "V",
            "icon": "mdi:flash"
        },
        "voltage_phase_l2": {
            "unit": "V",
            "icon": "mdi:flash"
        },
        "voltage_phase_l3": {
            "unit": "V",
            "icon": "mdi:flash"
        },

        # Áramerősségek
        "current_phase_l1": {
            "unit": "A",
            "icon": "mdi:current-ac"
        },
        "current_phase_l2": {
            "unit": "A",
            "icon": "mdi:current-ac"
        },
        "current_phase_l3": {
            "unit": "A",
            "icon": "mdi:current-ac"
        },
        "current_phase_Bl1": {
            "unit": "A",
            "icon": "mdi:current-ac"
        },
        "current_phase_Bl2": {
            "unit": "A",
            "icon": "mdi:current-ac"
        },
        "current_phase_Bl3": {
            "unit": "A",
            "icon": "mdi:current-ac"
        },

        # Frekvencia
        "frequency": {
            "unit": "Hz",
            "icon": "mdi:sine-wave"
        },

        # Teljesítménytényező
        "power_factor": {
            "unit": "",
            "icon": "mdi:cosine-wave"
        },
        "power_factor_l1": {
            "unit": "",
            "icon": "mdi:cosine-wave"
        },
        "power_factor_l2": {
            "unit": "",
            "icon": "mdi:cosine-wave"
        },
        "power_factor_l3": {
            "unit": "",
            "icon": "mdi:cosine-wave"
        },

        # Egyéb
        "meter_serial_number": {
            "unit": "",
            "icon": "mdi:identifier"
        },
        "circuit_breaker_status": {
            "unit": "",
            "icon": "mdi:toggle-switch"
        },
        "current_tariff": {
            "unit": "",
            "icon": "mdi:calendar"
        },
        "timestamp": {
            "unit": "",
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
                "icon": "mdi:transmission-tower-import"
            },
            "active_export_energy_total": {
                "unit": "kWh",
                "icon": "mdi:transmission-tower-export"
            },
            "total_active_energy": {
                "unit": "kWh",
                "icon": "mdi:transmission-tower-import"
            },
            "power_factor": {
                "unit": "",
                "icon": "mdi:cosine-wave"
            },
            "power_factor_l1": {
                "unit": "",
                "icon": "mdi:cosine-wave"
            },
            "power_factor_l2": {
                "unit": "",
                "icon": "mdi:cosine-wave"
            },
            "power_factor_l3": {
                "unit": "",
                "icon": "mdi:cosine-wave"
            },
            "voltage_phase_l1": {
                "unit": "V",
                "icon": "mdi:flash"
            },
            "voltage_phase_l2": {
                "unit": "V",
                "icon": "mdi:flash"
            },
            "voltage_phase_l3": {
                "unit": "V",
                "icon": "mdi:flash"
            },
            "current_phase_l1": {
                "unit": "A",
                "icon": "mdi:current-ac"
            },
            "current_phase_Bl1": {
                "unit": "A",
                "icon": "mdi:current-ac"
            },
            "current_phase_l2": {
                "unit": "A",
                "icon": "mdi:current-ac"
            },
            "current_phase_Bl2": {
                "unit": "A",
                "icon": "mdi:current-ac"
            },
            "current_phase_l3": {
                "unit": "A",
                "icon": "mdi:current-ac"
            },
            "current_phase_Bl3": {
                "unit": "A",
                "icon": "mdi:current-ac"
            },
            "instantaneous_power_import": {
                "unit": "kW",
                "icon": "mdi:flash"
            },
            "instantaneous_power_export": {
                "unit": "kW",
                "icon": "mdi:flash"
            },
            "meter_serial_number": {
                "unit": "",
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
                "icon": "mdi:transmission-tower-import"
            },
            "voltage_phase_l1": {
                "unit": "V",
                "icon": "mdi:flash"
            },
            "current_phase_l1": {
                "unit": "A",
                "icon": "mdi:current-ac"
            },
            "instantaneous_power_import": {
                "unit": "kW",
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
                "icon": "mdi:transmission-tower-import"
            },
            "voltage_l1": {
                "unit": "V",
                "icon": "mdi:flash"
            },
            "current_phase_l1": {
                "unit": "A",
                "icon": "mdi:current-ac"
            },
            "calculated_current_phase_l1": {
                "unit": "A",
                "icon": "mdi:current-ac"
            },
            "calculated_power_phase_l1": {
                "unit": "kW",
                "icon": "mdi:flash"
            },
            "power_factor_l1": {
                "unit": "",
                "icon": "mdi:cosine-wave"
            },
            "active_power_import": {
                "unit": "kW",
                "icon": "mdi:flash"
            },
            "reactive_power_qi": {
                "unit": "kVAr",
                "icon": "mdi:sine-wave"
            },
            "frequency": {
                "unit": "Hz",
                "icon": "mdi:waveform"
            },
            "meter_serial_number": {
                "unit": "",
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
