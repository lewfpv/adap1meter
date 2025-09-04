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

from .product_config import get_product_sensors, get_product_name

_LOGGER = logging.getLogger(__name__)
SCAN_INTERVAL = timedelta(seconds=10)


async def async_setup_entry(hass, config_entry, async_add_entities):
    config_data = {**config_entry.data, **config_entry.options}
    product_type = config_data.get("product_type", "ada12")
    prefix = config_data.get("prefix", "").strip()

    # ------------------------
    # URL logika (kötelező mező)
    # ------------------------
    url = config_data.get("url")
    if not url:
        raise ValueError("URL must be specified in configuration")

    product_sensors = get_product_sensors(product_type)
    product_name = get_product_name(product_type)

    # prefix hozzáadása a product_name elé
    if prefix:
        display_name = f"{prefix} {product_name}"
    else:
        display_name = product_name

    async def async_update_data():
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
        name=f"{display_name} coordinator",
        update_method=async_update_data,
        update_interval=SCAN_INTERVAL,
    )

    await coordinator.async_config_entry_first_refresh()

    sensors = []
    for sensor_key, sensor_config in product_sensors.items():
        # unique_id tartalmazza a prefixet is
        unique_id_parts = [url, product_type, sensor_key]
        if prefix:
            unique_id_parts.insert(0, prefix)
        unique_id = "_".join(unique_id_parts)

        # név prefix-szel
        name_parts = [display_name, sensor_config["friendly_name"]]
        sensor_name = " ".join(name_parts)

        sensors.append(
            Ada12Sensor(
                coordinator=coordinator,
                product_type=product_type,
                sensor_key=sensor_key,
                sensor_config=sensor_config,
                unique_id=unique_id,
                name=sensor_name,
            )
        )

    async_add_entities(sensors)


class Ada12Sensor(CoordinatorEntity, Entity):
    def __init__(self, coordinator, product_type, sensor_key, sensor_config, unique_id, name):
        super().__init__(coordinator)
        self._product_type = product_type
        self._sensor_key = sensor_key
        self._sensor_config = sensor_config
        self._unique_id = unique_id
        self._name = name
        self._attributes = {"icon": sensor_config["icon"]}
        if sensor_config["unit"]:
            self._attributes["unit_of_measurement"] = sensor_config["unit"]

    @property
    def name(self):
        return self._name

    @property
    def unique_id(self):
        return self._unique_id

    @property
    def state(self):
        data = self.coordinator.data or {}
        return data.get(self._sensor_key, 0 if self._sensor_config["unit"] else "")

    @property
    def extra_state_attributes(self):
        return self._attributes
