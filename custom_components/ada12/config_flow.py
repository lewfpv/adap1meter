from homeassistant import config_entries
import voluptuous as vol
from homeassistant.core import callback

DOMAIN = "ada12"  # Az integráció domain neve

class Ada12ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Ada12 integration."""

    VERSION = 1  # Verziószám a migrációhoz

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}

        if user_input is not None:
            # Ellenőrzés (opcionális)
            try:
                # Ha minden rendben, mentjük a konfigurációt
                return self.async_create_entry(title="Ada12", data=user_input)
            except Exception:
                errors["base"] = "cannot_connect"

        # Példa beviteli mezőkre
        data_schema = vol.Schema({
            vol.Required("host", default="okosvillanyora.local"): str,
            vol.Required("port", default=8989): int,
        })

        return self.async_show_form(
            step_id="user",
            data_schema=data_schema,
            errors=errors
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        """Handle the options flow."""
        return Ada12OptionsFlowHandler(config_entry)


class Ada12OptionsFlowHandler(config_entries.OptionsFlow):
    """Handle options flow for Ada12."""

    def __init__(self, config_entry):
        """Initialize options flow."""
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Manage the options."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        # Példa opciókhoz
        options_schema = vol.Schema({
            vol.Optional("debug", default=self.config_entry.options.get("debug", False)): bool,
        })

        return self.async_show_form(step_id="init", data_schema=options_schema)
