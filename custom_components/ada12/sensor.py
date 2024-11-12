import logging
from homeassistant.helpers.entity import Entity
from . import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up the ADA12 sensor platform from a config entry."""
    # Feltételezve, hogy a `fetch_data` függvény elérhető az integrációból
    async_add_entities([ADASensor(hass.data[DOMAIN])])

class ADASensor(Entity):
    """Representation of a sensor that reads Okos Villanyóra data."""

    def __init__(self, fetch_data_func):
        """Initialize the sensor."""
        self._state = None
        self._attributes = {}
        self._fetch_data = fetch_data_func

    @property
    def name(self):
        """Return the name of the sensor."""
        return "ADA12"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def extra_state_attributes(self):
        """Return the state attributes."""
        return self._attributes
        
    @property
    def icon(self):
        """Set the icon of the sensor."""
        return "mdi:gauge"

    async def async_update(self):
        """Fetch new state data for the sensor."""
        try:
            data = await self._fetch_data()
            if data:
                self._state = data.get('active_import_energy_total', 0)  # Fő állapot

                # Az összes adat hozzáadása attribútumként
                self._attributes = {
                    "active_import_energy_total": data.get('active_import_energy_total', 0),
                    "active_import_energy_tariff_1": data.get('active_import_energy_tariff_1', 0),
                    "active_import_energy_tariff_2": data.get('active_import_energy_tariff_2', 0),
                    "active_import_energy_tariff_3": data.get('active_import_energy_tariff_3', 0),
                    "active_import_energy_tariff_4": data.get('active_import_energy_tariff_4', 0),
                    "active_export_energy_total": data.get('active_export_energy_total', 0),
                    "active_export_energy_tariff_1": data.get('active_export_energy_tariff_1', 0),
                    "active_export_energy_tariff_2": data.get('active_export_energy_tariff_2', 0),
                    "reactive_import_energy": data.get('reactive_import_energy', 0),
                    "reactive_export_energy": data.get('reactive_export_energy', 0),
                    "reactive_energy_qi": data.get('reactive_energy_qi', 0),
                    "reactive_energy_qiv": data.get('reactive_energy_qiv', 0),
                    "voltage_phase_l1": data.get('voltage_phase_l1', 0),
                    "voltage_phase_l2": data.get('voltage_phase_l2', 0),
                    "voltage_phase_l3": data.get('voltage_phase_l3', 0),
                    "current_phase_l1": data.get('current_phase_l1', 0),
                    "current_phase_l2": data.get('current_phase_l2', 0),
                    "current_phase_l3": data.get('current_phase_l3', 0),
                    "power_factor": data.get('power_factor', 0),
                    "power_factor_l1": data.get('power_factor_l1', 0),
                    "frequency": data.get('frequency', 0),
                    "instantaneous_power_import": data.get('instantaneous_power_import', 0),
                    "instantaneous_power_export": data.get('instantaneous_power_export', 0),
                    "instantaneous_reactive_power_qi": data.get('instantaneous_reactive_power_qi', 0),
                    "instantaneous_reactive_power_qii": data.get('instantaneous_reactive_power_qii', 0),
                    "instantaneous_reactive_power_qiii": data.get('instantaneous_reactive_power_qiii', 0),
                    "instantaneous_reactive_power_qiv": data.get('instantaneous_reactive_power_qiv', 0),
                    "current_limit_l1": data.get('current_limit_l1', 0),
                    "current_limit_l2": data.get('current_limit_l2', 0),
                    "current_limit_l3": data.get('current_limit_l3', 0),
                    "circuit_breaker_status": data.get('circuit_breaker_status', 'unknown'),
                    "limiter_threshold": data.get('limiter_threshold', 0),
                    "timestamp": data.get('timestamp', ''),
                    "meter_serial_number": data.get('meter_serial_number', '')
                }
        except Exception as e:
            _LOGGER.error(f"Failed to update ADA P1 Meter sensor: {e}")
