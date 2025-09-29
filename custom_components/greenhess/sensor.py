"""A simple sensor template for Home Assistant."""
from __future__ import annotations

import logging
import aiohttp
import async_timeout
from datetime import timedelta

from homeassistant.helpers.entity import Entity
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
    UpdateFailed,
)
from homeassistant.const import STATE_UNKNOWN

from .product_config import get_product_sensors, get_product_name

_LOGGER = logging.getLogger(__name__)
SCAN_INTERVAL = timedelta(seconds=10)


async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up the sensor from a config entry."""

    config_data = {**config_entry.data, **config_entry.options}
    prefix = config_data.get("prefix", "")
    product_type = config_data.get("product_type", "ada12")

    # ------------------------
    # URL logic
    # ------------------------
    url = config_data.get("url")
    if not url:
        host = config_data.get("host", "okosvillanyora.local")
        port = config_data.get("port", 8989)
        url = f"http://{host}:{port}/json"

    product_sensors = get_product_sensors(product_type)
    product_name = get_product_name(product_type)

    async def async_update_data():
        """Fetch data from the device."""
        try:
            async with aiohttp.ClientSession() as session:
                async with async_timeout.timeout(10):
                    async with session.get(url) as response:
                        return await response.json()
        except Exception as err:
            raise UpdateFailed(f"Error fetching data from {url}: {err}") from err

    coordinator = DataUpdateCoordinator(
        hass,
        _LOGGER,
        name=f"{prefix} {product_name} coordinator",
        update_method=async_update_data,
        update_interval=SCAN_INTERVAL,
    )

    await coordinator.async_config_entry_first_refresh()

    sensors = []
    for sensor_key, sensor_config in product_sensors.items():
        # This unique_id is good for identifying the entity internally.
        unique_id = f"{url}_{product_type}_{sensor_key}"

        # The 'translation_key' must be a simple, short string that matches a key in your JSON file.
        translation_key = sensor_key 

        _LOGGER.debug("Creating sensor: key=%s, translation_key=%s", sensor_key, translation_key)

        sensors.append(
            Ada12Sensor(
                coordinator=coordinator,
                product_type=product_type,
                sensor_key=sensor_key,
                sensor_config=sensor_config,
                unique_id=unique_id,
                prefix=prefix,
                product_name=product_name,
                translation_key=translation_key
            )
        )

    async_add_entities(sensors)


class Ada12Sensor(CoordinatorEntity, Entity):
    """Ada12 custom sensor."""
    ENERGY_SENSORS = ["active_import_energy_total", "active_export_energy_total"]

    def __init__(self, coordinator, product_type, sensor_key, sensor_config, unique_id, prefix, product_name, translation_key):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._product_type = product_type
        self._sensor_key = sensor_key
        self._sensor_config = sensor_config
        self._unique_id = unique_id
        self._prefix = prefix
        self._product_name = product_name
        
        # This is the key that Home Assistant will use to find thetranslation.
        self._attr_translation_key = translation_key
        
        self._attributes = {"icon": sensor_config["icon"]}
        self._attributes["uid"] = unique_id

        if sensor_key in self.ENERGY_SENSORS:
            self._attr_device_class = "energy"
            self._attr_state_class = "total_increasing"
            self._attr_unit_of_measurement = "kWh"
        elif sensor_config["unit"]:
            self._attr_unit_of_measurement = sensor_config["unit"]

        # ----------------------------------------------------------------------
        # ADDED DEBUG LINE
        # This will show you what Home Assistant's name attribute is
        # populated with after the class is initialized.
        # ----------------------------------------------------------------------
        _LOGGER.debug(
            "Sensor '%s' initialized. Unique ID: %s. Translation Key: %s. Final Name: %s",
            self.__class__.__name__,
            self.unique_id,
            self._attr_translation_key,
            self.name # Access the `name` property to force HA to get the value
        )

    @property
    def unique_id(self):
        """Return the unique ID for this sensor."""
        return self._unique_id

    @property
    def native_value(self):
        """Return the state of the sensor."""
        data = self.coordinator.data or {}
        value = data.get(self._sensor_key, None)
        return value

    @property
    def extra_state_attributes(self):
        """Return the state attributes."""
        return self._attributes
