from homeassistant import config_entries
import voluptuous as vol
from homeassistant.core import callback
import logging
from .product_config import get_product_list, get_product_name

DOMAIN = "ada12"
_LOGGER = logging.getLogger(__name__)


class Ada12ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Ada12 integration."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}

        if user_input is not None:
            try:
                product_type = user_input.get("product_type", "ada12")
                title = get_product_name(product_type)
                return self.async_create_entry(title=title, data=user_input)
            except Exception:
                errors["base"] = "cannot_connect"

        product_options = dict(get_product_list())
        data_schema = vol.Schema({
            vol.Required("product_type", default="ada12"): vol.In(product_options),
            vol.Optional("host"): str,
            vol.Optional("port", default=8989): int,
            vol.Optional("url"): str,
        })

        return self.async_show_form(
            step_id="user",
            data_schema=data_schema,
            errors=errors
        )

    async def async_step_ssdp(self, discovery_info):
        _LOGGER.info(f"SSDP discovered device: {discovery_info}")
        host = discovery_info.get("host")
        if not host:
            return self.async_abort(reason="no_host_found")

        await self.async_set_unique_id(host)
        self._abort_if_unique_id_configured()

        self.context.update({"title_placeholders": {"name": f"Ada12 - {host}"}})
        return self.async_create_entry(
            title=f"Ada12 - {host}",
            data={"product_type": "ada12", "url": f"http://{host}:8989/json"},
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return Ada12OptionsFlowHandler(config_entry)


class Ada12OptionsFlowHandler(config_entries.OptionsFlow):
    """Handle options flow for Ada12."""

    def __init__(self, config_entry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        product_options = dict(get_product_list())
        options_schema = vol.Schema({
            vol.Optional("product_type", default=self.config_entry.data.get("product_type", "ada12")): vol.In(product_options),
            vol.Optional("host", default=self.config_entry.data.get("host")): str,
            vol.Optional("port", default=self.config_entry.data.get("port", 8989)): int,
            vol.Optional("url", default=self.config_entry.data.get("url")): str,
        })

        return self.async_show_form(step_id="init", data_schema=options_schema)
