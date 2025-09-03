from homeassistant import config_entries
import voluptuous as vol
from homeassistant.core import callback
import logging
from .product_config import get_product_list, get_product_name

DOMAIN = "ada12"
_LOGGER = logging.getLogger(__name__)


class Ada12ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}
        product_options = dict(get_product_list())

        if user_input is not None:
            try:
                product_type = user_input.get("product_type", "ada12")
                device_id = user_input.get("device_id", "")
                title = get_product_name(product_type)
                if device_id:
                    title = f"{title} {device_id}"
                return self.async_create_entry(title=title, data=user_input)
            except Exception:
                errors["base"] = "cannot_connect"

        # Form schema: lehet host+port vagy teljes URL
        data_schema = vol.Schema({
            vol.Required("product_type", default="ada12"): vol.In(product_options),
            vol.Optional("device_id", default=""): str,
            vol.Optional("host", default=""): str,
            vol.Optional("port", default=8989): int,
            vol.Optional("url", default=""): str,
        })

        return self.async_show_form(step_id="user", data_schema=data_schema, errors=errors)

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return Ada12OptionsFlowHandler(config_entry)


class Ada12OptionsFlowHandler(config_entries.OptionsFlow):
    def __init__(self, config_entry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        product_options = dict(get_product_list())
        options_schema = vol.Schema({
            vol.Optional(
                "product_type", default=self.config_entry.data.get("product_type", "ada12")
            ): vol.In(product_options),
            vol.Optional("device_id", default=self.config_entry.data.get("device_id", "")): str,
            vol.Optional("host", default=self.config_entry.data.get("host", "")): str,
            vol.Optional("port", default=self.config_entry.data.get("port", 8989)): int,
            vol.Optional("url", default=self.config_entry.data.get("url", "")): str,
        })

        return self.async_show_form(step_id="init", data_schema=options_schema)
