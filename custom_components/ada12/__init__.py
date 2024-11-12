import logging
import aiohttp
import async_timeout
from datetime import timedelta
from homeassistant.helpers.event import async_track_time_interval

_LOGGER = logging.getLogger(__name__)
_LOGGER.info("ADA P1 Meter integráció indul")

DOMAIN = "ada12"

async def async_setup(hass, config):
    """Set up the ADA P1 Meter component."""

    async def fetch_data():
        """Fetch JSON data from the okosvillanyora.local server."""
        url = "http://okosvillanyora.local:8989/json"
        try:
            async with aiohttp.ClientSession() as session:
                async with async_timeout.timeout(10):
                    async with session.get(url) as response:
                        return await response.json()
        except Exception as e:
            _LOGGER.error(f"Error fetching data: {e}")
            return None

    async def update_data(now):
        """Periodically update the data."""
        data = await fetch_data()
        if data:
            # Define all sensors with their state and attributes
            sensors = {
                "sensor.ada12_active_import_energy_total": {
                    "state": data.get("active_import_energy_total", 0),
                    "attributes": {"unit_of_measurement": "kWh", "friendly_name": "Összes importált energia"}
                },
                "sensor.ada12_active_import_energy_tariff_1": {
                    "state": data.get("active_import_energy_tariff_1", 0),
                    "attributes": {"unit_of_measurement": "kWh", "friendly_name": "Importált energia tarifa 1"}
                },
                "sensor.ada12_active_import_energy_tariff_2": {
                    "state": data.get("active_import_energy_tariff_2", 0),
                    "attributes": {"unit_of_measurement": "kWh", "friendly_name": "Importált energia tarifa 2"}
                },
                "sensor.ada12_active_import_energy_tariff_3": {
                    "state": data.get("active_import_energy_tariff_3", 0),
                    "attributes": {"unit_of_measurement": "kWh", "friendly_name": "Importált energia tarifa 3"}
                },
                "sensor.ada12_active_import_energy_tariff_4": {
                    "state": data.get("active_import_energy_tariff_4", 0),
                    "attributes": {"unit_of_measurement": "kWh", "friendly_name": "Importált energia tarifa 4"}
                },
                "sensor.ada12_active_export_energy_total": {
                    "state": data.get("active_export_energy_total", 0),
                    "attributes": {"unit_of_measurement": "kWh", "friendly_name": "Összes exportált energia"}
                },
                "sensor.ada12_active_export_energy_tariff_1": {
                    "state": data.get("active_export_energy_tariff_1", 0),
                    "attributes": {"unit_of_measurement": "kWh", "friendly_name": "Exportált energia tarifa 1"}
                },
                "sensor.ada12_active_export_energy_tariff_2": {
                    "state": data.get("active_export_energy_tariff_2", 0),
                    "attributes": {"unit_of_measurement": "kWh", "friendly_name": "Exportált energia tarifa 2"}
                },
                "sensor.ada12_reactive_import_energy": {
                    "state": data.get("reactive_import_energy", 0),
                    "attributes": {"unit_of_measurement": "kVArh", "friendly_name": "Reaktív importált energia"}
                },
                "sensor.ada12_reactive_export_energy": {
                    "state": data.get("reactive_export_energy", 0),
                    "attributes": {"unit_of_measurement": "kVArh", "friendly_name": "Reaktív exportált energia"}
                },
                "sensor.ada12_voltage_phase_l1": {
                    "state": data.get("voltage_phase_l1", 0),
                    "attributes": {"unit_of_measurement": "V", "friendly_name": "Fázis 1 (L1) feszültség"}
                },
                "sensor.ada12_voltage_phase_l2": {
                    "state": data.get("voltage_phase_l2", 0),
                    "attributes": {"unit_of_measurement": "V", "friendly_name": "Fázis 2 (L2) feszültség"}
                },
                "sensor.ada12_voltage_phase_l3": {
                    "state": data.get("voltage_phase_l3", 0),
                    "attributes": {"unit_of_measurement": "V", "friendly_name": "Fázis 3 (L3) feszültség"}
                },
                "sensor.ada12_current_phase_l1": {
                    "state": data.get("current_phase_l1", 0),
                    "attributes": {"unit_of_measurement": "A", "friendly_name": "Fázis 1 (L1) áramerősség"}
                },
                "sensor.ada12_current_phase_l2": {
                    "state": data.get("current_phase_l2", 0),
                    "attributes": {"unit_of_measurement": "A", "friendly_name": "Fázis 2 (L2) áramerősség"}
                },
                "sensor.ada12_current_phase_l3": {
                    "state": data.get("current_phase_l3", 0),
                    "attributes": {"unit_of_measurement": "A", "friendly_name": "Fázis 3 (L3) áramerősség"}
                },
                "sensor.ada12_power_factor": {
                    "state": data.get("power_factor", 0),
                    "attributes": {"friendly_name": "Teljesítménytényező"}
                },
                "sensor.ada12_frequency": {
                    "state": data.get("frequency", 0),
                    "attributes": {"unit_of_measurement": "Hz", "friendly_name": "Frekvencia"}
                },
                "sensor.ada12_instantaneous_power_import": {
                    "state": data.get("instantaneous_power_import", 0),
                    "attributes": {"unit_of_measurement": "kW", "friendly_name": "Pillanatnyi importált teljesítmény"}
                },
                "sensor.ada12_instantaneous_power_export": {
                    "state": data.get("instantaneous_power_export", 0),
                    "attributes": {"unit_of_measurement": "kW", "friendly_name": "Pillanatnyi exportált teljesítmény"}
                },
                "sensor.ada12_meter_serial_number": {
                    "state": data.get("meter_serial_number", ""),
                    "attributes": {"friendly_name": "Mérő sorozatszáma"}
                }
            }

            # Frissítsd az összes szenzor állapotát és attribútumait
            for sensor_id, sensor_data in sensors.items():
                hass.states.async_set(sensor_id, sensor_data["state"], sensor_data["attributes"])

    # Az update_data hívása minden 60 másodpercben
    async_track_time_interval(hass, update_data, timedelta(seconds=60))

    # Első adatfrissítés
    await update_data(None)
    return True
