"""Product configuration for ADA family devices."""

# Product definitions with their supported sensors
PRODUCT_CONFIGS = {
    "ada12": {
        "name": "ADA P1 Meter",
        "description": "Full-featured smart meter with all sensors",
        "sensors": {
            "active_import_energy_total": {
                "unit": "kWh",
                "friendly_name": "Összes importált energia",
                "icon": "mdi:transmission-tower-import"
            },
            "active_import_energy_tariff_1": {
                "unit": "kWh",
                "friendly_name": "Importált energia tarifa 1",
                "icon": "mdi:transmission-tower-import"
            },
            "active_import_energy_tariff_2": {
                "unit": "kWh",
                "friendly_name": "Importált energia tarifa 2",
                "icon": "mdi:transmission-tower-import"
            },
            "active_import_energy_tariff_3": {
                "unit": "kWh",
                "friendly_name": "Importált energia tarifa 3",
                "icon": "mdi:transmission-tower-import"
            },
            "active_import_energy_tariff_4": {
                "unit": "kWh",
                "friendly_name": "Importált energia tarifa 4",
                "icon": "mdi:transmission-tower-import"
            },
            "active_export_energy_total": {
                "unit": "kWh",
                "friendly_name": "Összes exportált energia",
                "icon": "mdi:transmission-tower-export"
            },
            "active_export_energy_tariff_1": {
                "unit": "kWh",
                "friendly_name": "Exportált energia tarifa 1",
                "icon": "mdi:transmission-tower-export"
            },
            "active_export_energy_tariff_2": {
                "unit": "kWh",
                "friendly_name": "Exportált energia tarifa 2",
                "icon": "mdi:transmission-tower-export"
            },
            "reactive_import_energy": {
                "unit": "kVArh",
                "friendly_name": "Reaktív importált energia",
                "icon": "mdi:sine-wave"
            },
            "reactive_export_energy": {
                "unit": "kVArh",
                "friendly_name": "Reaktív exportált energia",
                "icon": "mdi:sine-wave"
            },
            "voltage_phase_l1": {
                "unit": "V",
                "friendly_name": "Fázis 1 (L1) feszültség",
                "icon": "mdi:flash"
            },
            "voltage_phase_l2": {
                "unit": "V",
                "friendly_name": "Fázis 2 (L2) feszültség",
                "icon": "mdi:flash"
            },
            "voltage_phase_l3": {
                "unit": "V",
                "friendly_name": "Fázis 3 (L3) feszültség",
                "icon": "mdi:flash"
            },
            "current_phase_l1": {
                "unit": "A",
                "friendly_name": "Fázis 1 (L1) áramerősség",
                "icon": "mdi:current-ac"
            },
            "current_phase_l2": {
                "unit": "A",
                "friendly_name": "Fázis 2 (L2) áramerősség",
                "icon": "mdi:current-ac"
            },
            "current_phase_l3": {
                "unit": "A",
                "friendly_name": "Fázis 3 (L3) áramerősség",
                "icon": "mdi:current-ac"
            },
            "power_factor": {
                "unit": "",
                "friendly_name": "Teljesítménytényező",
                "icon": "mdi:cosine-wave"
            },
            "frequency": {
                "unit": "Hz",
                "friendly_name": "Frekvencia",
                "icon": "mdi:waveform"
            },
            "instantaneous_power_import": {
                "unit": "kW",
                "friendly_name": "Pillanatnyi importált teljesítmény",
                "icon": "mdi:flash"
            },
            "instantaneous_power_export": {
                "unit": "kW",
                "friendly_name": "Pillanatnyi exportált teljesítmény",
                "icon": "mdi:flash"
            },
            "meter_serial_number": {
                "unit": "",
                "friendly_name": "Mérő sorozatszáma",
                "icon": "mdi:identifier"
            }
        }
    },
    "adaone": {
        "name": "ADA One",
        "description": "Basic meter with essential sensors only",
        "sensors": {
            "active_import_energy_total": {
                "unit": "kWh",
                "friendly_name": "Összes importált energia",
                "icon": "mdi:transmission-tower-import"
            },
            "active_export_energy_total": {
                "unit": "kWh",
                "friendly_name": "Összes exportált energia",
                "icon": "mdi:transmission-tower-export"
            },
            "voltage_phase_l1": {
                "unit": "V",
                "friendly_name": "Fázis 1 (L1) feszültség",
                "icon": "mdi:flash"
            },
            "current_phase_l1": {
                "unit": "A",
                "friendly_name": "Fázis 1 (L1) áramerősség",
                "icon": "mdi:current-ac"
            },
            "instantaneous_power_import": {
                "unit": "kW",
                "friendly_name": "Pillanatnyi importált teljesítmény",
                "icon": "mdi:flash"
            },
            "meter_serial_number": {
                "unit": "",
                "friendly_name": "Mérő sorozatszáma",
                "icon": "mdi:identifier"
            }
        }
    },
    "adanode": {
        "name": "ADA Node",
        "description": "Single phase meter with basic monitoring",
        "sensors": {
            "active_import_energy_total": {
                "unit": "kWh",
                "friendly_name": "Összes importált energia",
                "icon": "mdi:transmission-tower-import"
            },
            "active_import_energy_tariff_1": {
                "unit": "kWh",
                "friendly_name": "Importált energia tarifa 1",
                "icon": "mdi:transmission-tower-import"
            },
            "active_import_energy_tariff_2": {
                "unit": "kWh",
                "friendly_name": "Importált energia tarifa 2",
                "icon": "mdi:transmission-tower-import"
            },
            "voltage_phase_l1": {
                "unit": "V",
                "friendly_name": "Fázis 1 (L1) feszültség",
                "icon": "mdi:flash"
            },
            "current_phase_l1": {
                "unit": "A",
                "friendly_name": "Fázis 1 (L1) áramerősség",
                "icon": "mdi:current-ac"
            },
            "power_factor": {
                "unit": "",
                "friendly_name": "Teljesítménytényező",
                "icon": "mdi:cosine-wave"
            },
            "frequency": {
                "unit": "Hz",
                "friendly_name": "Frekvencia",
                "icon": "mdi:waveform"
            },
            "instantaneous_power_import": {
                "unit": "kW",
                "friendly_name": "Pillanatnyi importált teljesítmény",
                "icon": "mdi:flash"
            }
        }
    },
    "adabridge": {
        "name": "ADA Bridge",
        "description": "Compact meter with minimal sensors",
        "sensors": {
            "active_import_energy_total": {
                "unit": "kWh",
                "friendly_name": "Összes importált energia",
                "icon": "mdi:transmission-tower-import"
            },
            "voltage_phase_l1": {
                "unit": "V",
                "friendly_name": "Fázis 1 (L1) feszültség",
                "icon": "mdi:flash"
            },
            "current_phase_l1": {
                "unit": "A",
                "friendly_name": "Fázis 1 (L1) áramerősség",
                "icon": "mdi:current-ac"
            },
            "instantaneous_power_import": {
                "unit": "kW",
                "friendly_name": "Pillanatnyi importált teljesítmény",
                "icon": "mdi:flash"
            }
        }
    },
    "adapziote02": {
        "name": "ADA PZIOT-E02",
        "description": "Compact meter with minimal sensors",
        "sensors": {
            "active_import_energy_total": {
                "unit": "kWh",
                "friendly_name": "Összes importált energia",
                "icon": "mdi:transmission-tower-import"
            },
            "voltage_phase_l1": {
                "unit": "V",
                "friendly_name": "Fázis 1 (L1) feszültség",
                "icon": "mdi:flash"
            },
            "current_phase_l1": {
                "unit": "A",
                "friendly_name": "Fázis 1 (L1) áramerősség",
                "icon": "mdi:current-ac"
            },
            "instantaneous_power_import": {
                "unit": "kW",
                "friendly_name": "Pillanatnyi importált teljesítmény",
                "icon": "mdi:flash"
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
