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
            "friendly_name_en": "Total Imported Energy",
            "friendly_name": "Összes importált energia ",
            "icon": "mdi:transmission-tower-import"
        },
        "active_export_energy_total": {
            "unit": "kWh",
            "friendly_name_en": "Total Exported Energy",
            "friendly_name": "Összes exportált energia",
            "icon": "mdi:transmission-tower-export"
        },
        "total_active_energy": {
            "unit": "kWh",
            "friendly_name_en": "Total Active Energy",
            "friendly_name": "Összes aktív energia",
            "icon": "mdi:lightning-bolt"
        },

        # Tarifa szerinti bontás
        "active_import_energy_tariff_1": {
            "unit": "kWh",
            "friendly_name_en": "Imported Energy Tariff 1",
            "friendly_name": "Importált energia tarifa 1",
            "icon": "mdi:counter"
        },
        "active_import_energy_tariff_2": {
            "unit": "kWh",
            "friendly_name_en": "Imported Energy Tariff 2",
            "friendly_name": "Importált energia tarifa 2",
            "icon": "mdi:counter"
        },
        "active_import_energy_tariff_3": {
            "unit": "kWh",
            "friendly_name_en": "Imported Energy Tariff 3",
            "friendly_name": "Importált energia tarifa 3",
            "icon": "mdi:counter"
        },
        "active_import_energy_tariff_4": {
            "unit": "kWh",
            "friendly_name_en": "Imported Energy Tariff 4",
            "friendly_name": "Importált energia tarifa 4",
            "icon": "mdi:counter"
        },
        "active_export_energy_tariff_1": {
            "unit": "kWh",
            "friendly_name_en": "Exported Energy Tariff 1",
            "friendly_name": "Exportált energia tarifa 1",
            "icon": "mdi:counter"
        },
        "active_export_energy_tariff_2": {
            "unit": "kWh",
            "friendly_name_en": "Exported Energy Tariff 2",
            "friendly_name": "Exportált energia tarifa 1",
            "icon": "mdi:counter"
        },
        "active_export_energy_tariff_3": {
            "unit": "kWh",
            "friendly_name_en": "Exported Energy Tariff 3",
            "friendly_name": "Exportált energia tarifa 1",
            "icon": "mdi:counter"
        },
        "active_export_energy_tariff_4": {
            "unit": "kWh",
            "friendly_name_en": "Exported Energy Tariff 4",
            "friendly_name": "Exportált energia tarifa 1",
            "icon": "mdi:counter"
        },

        # Reaktív energia (kVArh)
        "reactive_import_energy": {
            "unit": "kVArh",
            "friendly_name_en": "Reactive Imported Energy",
            "friendly_name": "Reaktív importált energia",
            "icon": "mdi:sine-wave"
        },
        "reactive_export_energy": {
            "unit": "kVArh",
            "friendly_name_en": "Reactive Exported Energy",
            "friendly_name": "Reaktív exportált energia",
            "icon": "mdi:sine-wave"
        },
        "reactive_energy_qi": {
            "unit": "kVArh",
            "friendly_name_en": "Reactive Energy QI",
            "friendly_name": "Reaktív energia QI",
            "icon": "mdi:sine-wave"
        },
        "reactive_energy_qii": {
            "unit": "kVArh",
            "friendly_name_en": "Reactive Energy QII",
            "friendly_name": "Reaktív energia QII",
            "icon": "mdi:sine-wave"
        },
        "reactive_energy_qiii": {
            "unit": "kVArh",
            "friendly_name_en": "Reactive Energy QIII",
            "friendly_name": "Reaktív energia QIII",
            "icon": "mdi:sine-wave"
        },
        "reactive_energy_qiv": {
            "unit": "kVArh",
            "friendly_name_en": "Reactive Energy QIV",
            "friendly_name": "Reaktív energia QIV",
            "icon": "mdi:sine-wave"
        },

        # Pillanatnyi teljesítmény
        "instantaneous_power_import": {
            "unit": "kW",
            "friendly_name_en": "Instantaneous Imported Power",
            "friendly_name": "Pillanatnyi importált teljesítmény",
            "icon": "mdi:flash"
        },
        "instantaneous_power_export": {
            "unit": "kW",
            "friendly_name_en": "Instantaneous Exported Power",
            "friendly_name": "Pillanatnyi exportált teljesítmény",
            "icon": "mdi:flash"
        },
        "instantaneous_power_import_l1": {
            "unit": "kW",
            "friendly_name_en": "Instantaneous Imported Power L1",
            "friendly_name": "Pillanatnyi importált teljesítmény L1",
            "icon": "mdi:flash"
        },
        "instantaneous_power_import_l2": {
            "unit": "kW",
            "friendly_name_en": "Instantaneous Imported Power L2",
            "friendly_name": "Pillanatnyi importált teljesítmény L2",
            "icon": "mdi:flash"
        },
        "instantaneous_power_import_l3": {
            "unit": "kW",
            "friendly_name_en": "Instantaneous Imported Power L3",
            "friendly_name": "Pillanatnyi importált teljesítmény L3",
            "icon": "mdi:flash"
        },
        "instantaneous_power_export_l1": {
            "unit": "kW",
            "friendly_name_en": "Instantaneous Exported Power L1",
            "friendly_name": "Pillanatnyi exportált teljesítmény L1",
            "icon": "mdi:flash"
        },
        "instantaneous_power_export_l2": {
            "unit": "kW",
            "friendly_name_en": "Instantaneous Exported Power L2",
            "friendly_name": "Pillanatnyi exportált teljesítmény L2",
            "icon": "mdi:flash"
        },
        "instantaneous_power_export_l3": {
            "unit": "kW",
            "friendly_name_en": "Instantaneous Exported Power L3",
            "friendly_name": "Pillanatnyi exportált teljesítmény L3",
            "icon": "mdi:flash"
        },

        # Pillanatnyi reaktív teljesítmény
        "instantaneous_reactive_power_qi": {
            "unit": "kVAr",
            "friendly_name_en": "Instantaneous Reactive Power QI",
            "friendly_name": "Pillanatnyi reaktív teljesítmény QI",
            "icon": "mdi:sine-wave"
        },
        "instantaneous_reactive_power_qii": {
            "unit": "kVAr",
            "friendly_name_en": "Instantaneous Reactive Power QII",
            "friendly_name": "Pillanatnyi reaktív teljesítmény QII",
            "icon": "mdi:sine-wave"
        },
        "instantaneous_reactive_power_qiii": {
            "unit": "kVAr",
            "friendly_name_en": "Instantaneous Reactive Power QIII",
            "friendly_name": "Pillanatnyi reaktív teljesítmény QIII",
            "icon": "mdi:sine-wave"
        },
        "instantaneous_reactive_power_qiv": {
            "unit": "kVAr",
            "friendly_name_en": "Instantaneous Reactive Power QIV",
            "friendly_name": "Pillanatnyi reaktív teljesítmény QIV",
            "icon": "mdi:sine-wave"
        },

        # Feszültségek
        "voltage_phase_l1": {
            "unit": "V",
            "friendly_name_en": "Voltage Phase 1 (L1)",
            "friendly_name": "Fázis 1 (L1) feszültség",
            "icon": "mdi:flash"
        },
        "voltage_phase_l2": {
            "unit": "V",
            "friendly_name_en": "Voltage Phase 2 (L2)",
            "friendly_name": "Fázis 2 (L2) feszültség",
            "icon": "mdi:flash"
        },
        "voltage_phase_l3": {
            "unit": "V",
            "friendly_name_en": "Voltage Phase 3 (L3)",
            "friendly_name": "Fázis 3 (L3) feszültség",
            "icon": "mdi:flash"
        },

        # Áramerősségek
        "current_phase_l1": {
            "unit": "A",
            "friendly_name_en": "Current Phase 1 (L1)",
            "friendly_name": "Fázis 1 (L1) áramerősség",
            "icon": "mdi:current-ac"
        },
        "current_phase_l2": {
            "unit": "A",
            "friendly_name_en": "Current Phase 2 (L2)",
            "friendly_name": "Fázis 2 (L2) áramerősség",
            "icon": "mdi:current-ac"
        },
        "current_phase_l3": {
            "unit": "A",
            "friendly_name_en": "Current Phase 3 (L3)",
            "friendly_name": "Fázis 3 (L3) áramerősség",
            "icon": "mdi:current-ac"
        },
        "current_phase_Bl1": {
            "unit": "A",
            "friendly_name_en": "Current Phase 1 (calculated) (L1)",
            "friendly_name": "Fázis 1 (L1) számított áramerősség",
            "icon": "mdi:current-ac"
        },
        "current_phase_Bl2": {
            "unit": "A",
            "friendly_name_en": "Current Phase 2 (calculated) (L2)",
            "friendly_name": "Fázis 2 (L2) számított áramerősség",
            "icon": "mdi:current-ac"
        },
        "current_phase_Bl3": {
            "unit": "A",
            "friendly_name_en": "Current Phase 3 (calculated) (L3)",
            "friendly_name": "Fázis 3 (L3) számított áramerősség",
            "icon": "mdi:current-ac"
        },

        # Frekvencia
        "frequency": {
            "unit": "Hz",
            "friendly_name_en": "Frequency",
            "friendly_name": "Hálózati frekvencia",
            "icon": "mdi:sine-wave"
        },

        # Teljesítménytényező
        "power_factor": {
            "unit": "",
            "friendly_name_en": "Power Factor",
            "friendly_name": "Teljesítménytényező",
            "icon": "mdi:cosine-wave"
        },
        "power_factor_l1": {
            "unit": "",
            "friendly_name_en": "Power Factor (L1)",
            "friendly_name": "Teljesítménytényező (L1)",
            "icon": "mdi:cosine-wave"
        },
        "power_factor_l2": {
            "unit": "",
            "friendly_name_en": "Power Factor (L2)",
            "friendly_name": "Teljesítménytényező (L2)",
            "icon": "mdi:cosine-wave"
        },
        "power_factor_l3": {
            "unit": "",
            "friendly_name_en": "Power Factor (L3)",
            "friendly_name": "Teljesítménytényező (L3)",
            "icon": "mdi:cosine-wave"
        },

        # Egyéb
        "meter_serial_number": {
            "unit": "",
            "friendly_name_en": "Meter Serial Number",
            "friendly_name": "Mérő sorozatszáma",
            "icon": "mdi:identifier"
        },
        "circuit_breaker_status": {
            "unit": "",
            "friendly_name_en": "Circuit Breaker Status",
            "friendly_name": "Kismegszakító állapot",
            "icon": "mdi:toggle-switch"
        },
        "current_tariff": {
            "unit": "",
            "friendly_name_en": "Current Tariff",
            "friendly_name": "Aktív tarifa",
            "icon": "mdi:calendar"
        },
        "timestamp": {
            "unit": "",
            "friendly_name_en": "Timestamp",
            "friendly_name": "Időbélyeg",
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
                "friendly_name_en": "Total Imported Energy",
                "friendly_name": "Összes importált energia ",
                "icon": "mdi:transmission-tower-import"
            },
            "active_export_energy_total": {
                "unit": "kWh",
                "friendly_name_en": "Total Exported Energy",
                "friendly_name": "Összes exportált energia",
                "icon": "mdi:transmission-tower-export"
            },
            "total_active_energy": {
                "unit": "kWh",
                "friendly_name_en": "Total Active Energy",
                "friendly_name": "Összes aktív energia",
                "icon": "mdi:transmission-tower-import"
            },
            "power_factor": {
                "unit": "",
                "friendly_name_en": "Power Factor",
                "friendly_name": "Teljesítménytényező",
                "icon": "mdi:cosine-wave"
            },
            "power_factor_l1": {
                "unit": "",
                "friendly_name_en": "Power Factor (L1)",
                "friendly_name": "Teljesítménytényező (L1)",
                "icon": "mdi:cosine-wave"
            },
            "power_factor_l2": {
                "unit": "",
                "friendly_name_en": "Power Factor (L2)",
                "friendly_name": "Teljesítménytényező (L2)",
                "icon": "mdi:cosine-wave"
            },
            "power_factor_l3": {
                "unit": "",
                "friendly_name_en": "Power Factor (L3)",
                "friendly_name": "Teljesítménytényező (L3)",
                "icon": "mdi:cosine-wave"
            },
            "voltage_phase_l1": {
                "unit": "V",
                "friendly_name_en": "Voltage Phase 1 (L1)",
                "friendly_name": "Fázis 1 (L1) feszültség",
                "icon": "mdi:flash"
            },
            "voltage_phase_l2": {
                "unit": "V",
                "friendly_name_en": "Voltage Phase 2 (L2)",
                "friendly_name": "Fázis 1 (L2) feszültség",
                "icon": "mdi:flash"
            },
            "voltage_phase_l3": {
                "unit": "V",
                "friendly_name_en": "Voltage Phase 3 (L3)",
                "friendly_name": "Fázis 1 (L3) feszültség",
                "icon": "mdi:flash"
            },
            "current_phase_l1": {
                "unit": "A",
                "friendly_name_en": "Current Phase 1 (L1)",
                "friendly_name": "Fázis 1 (L1) áramerősség",
                "icon": "mdi:current-ac"
            },
            "current_phase_Bl1": {
                "unit": "A",
                "friendly_name_en": "Current Phase 1 (calculated) (L1)",
                "friendly_name": "Fázis 1 (L1) számított áramerősség",
                "icon": "mdi:current-ac"
            },
            "current_phase_l2": {
                "unit": "A",
                "friendly_name_en": "Current Phase 2 (L2)",
                "friendly_name": "Fázis 2 (L2) áramerősség",
                "icon": "mdi:current-ac"
            },
            "current_phase_Bl2": {
                "unit": "A",
                "friendly_name_en": "Current Phase 2 (calculated) (L2)",
                "friendly_name": "Fázis 2 (L2) számított áramerősség",
                "icon": "mdi:current-ac"
            },
            "current_phase_l3": {
                "unit": "A",
                "friendly_name_en": "Current Phase 3 (L3)",
                "friendly_name": "Fázis 3 (L3) áramerősség",
                "icon": "mdi:current-ac"
            },
            "current_phase_Bl3": {
                "unit": "A",
                "friendly_name_en": "Current Phase 3 (calculated) (L3)",
                "friendly_name": "Fázis 3 (L3) számított áramerősség",
                "icon": "mdi:current-ac"
            },
            "instantaneous_power_import": {
                "unit": "kW",
                "friendly_name_en": "Instantaneous Imported Power",
                "friendly_name": "Pillanatnyi importált teljesítmény",
                "icon": "mdi:flash"
            },
            "instantaneous_power_export": {
                "unit": "kW",
                "friendly_name_en": "Instantaneous Exported Power",
                "friendly_name": "Pillanatnyi exportált teljesítmény",
                "icon": "mdi:flash"
            },
            "meter_serial_number": {
                "unit": "",
                "friendly_name_en": "Meter Serial Number",
                "friendly_name": "Mérő sorozatszáma",
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
                "friendly_name_en": "Total Imported Energy",
                "friendly_name": "Összes importált energia ",
                "icon": "mdi:transmission-tower-import"
            },
            "voltage_phase_l1": {
                "unit": "V",
                "friendly_name_en": "Voltage Phase 1 (L1)",
                "friendly_name": "Fázis 1 (L1) feszültség",
                "icon": "mdi:flash"
            },
            "current_phase_l1": {
                "unit": "A",
                "friendly_name_en": "Current Phase 1 (L1)",
                "friendly_name": "Fázis 1 (L1) áramerősség",
                "icon": "mdi:current-ac"
            },
            "instantaneous_power_import": {
                "unit": "kW",
                "friendly_name_en": "Instantaneous Imported Power",
                "friendly_name": "Pillanatnyi importált teljesítmény",
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
                "friendly_name_en": "Total Imported Energy",
                "friendly_name": "Összes importált energia ",
                "icon": "mdi:transmission-tower-import"
            },
            "voltage_l1": {
                "unit": "V",
                "friendly_name_en": "Voltage Phase 1 (L1)",
                "friendly_name": "Fázis 1 (L1) feszültség",
                "icon": "mdi:flash"
            },
            "current_phase_l1": {
                "unit": "A",
                "friendly_name_en": "Current Phase 1 (L1)",
                "friendly_name": "Fázis 1 (L1) áramerősség",
                "icon": "mdi:current-ac"
            },
            "calculated_current_phase_l1": {
                "unit": "A",
                "friendly_name_en": "Current Phase 1 (calculated) (L1)",
                "friendly_name": "Fázis 1 (L1) számított áramerősség",
                "icon": "mdi:current-ac"
            },
            "calculated_power_phase_l1": {
                "unit": "kW",
                "friendly_name_en": "Power Phase 1 (calculated) (L1)",
                "friendly_name": "Fázis 1 (L1) számított energia",
                "icon": "mdi:flash"
            },
            "power_factor_l1": {
                "unit": "",
                "friendly_name_en": "Power Factor (L1)",
                "friendly_name": "Teljesítménytényező (L1)",
                "icon": "mdi:cosine-wave"
            },
            "active_power_import": {
                "unit": "kW",
                "friendly_name_en": "Active Power Import",
                "friendly_name": "Aktív importált teljesítmény",
                "icon": "mdi:flash"
            },
            "reactive_power_qi": {
                "unit": "kVAr",
                "friendly_name_en": "Reactive Power QI (inductive)",
                "friendly_name": "Reaktív teljesítmény QI (induktív)",
                "icon": "mdi:sine-wave"
            },
            "frequency": {
                "unit": "Hz",
                "friendly_name_en": "Frequency",
                "friendly_name": "Hálózati frekvencia",
                "icon": "mdi:waveform"
            },
            "meter_serial_number": {
                "unit": "",
                "friendly_name_en": "Meter Serial Number",
                "friendly_name": "Mérő sorozatszáma",
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
