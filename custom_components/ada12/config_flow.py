from homeassistant import config_entries
import voluptuous as vol
from homeassistant.core import callback
import logging

DOMAIN = "ada12"
_LOGGER = logging.getLogger(__name__)

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

    async def async_step_ssdp(self, discovery_info):
        """Handle SSDP discovery."""
        _LOGGER.info(f"SSDP discovered device: {discovery_info}")

        # Az SSDP által visszaadott információk alapján ellenőrizzük az eszközt
        host = discovery_info.get("host")  # Az eszköz IP-címe
        if not host:
            return self.async_abort(reason="no_host_found")

        # Egyedi azonosító beállítása (pl. host alapján)
        await self.async_set_unique_id(host)
        self._abort_if_unique_id_configured()

        # Alapértelmezett adatokat állítunk be az észlelés alapján
        self.context.update({"title_placeholders": {"name": f"Ada12 - {host}"}})
        return self.async_create_entry(title=f"Ada12 - {host}", data={"host": host, "port": 8989})

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
            # Mentjük az új beállításokat
            return self.async_create_entry(title="", data=user_input)

        # Jelenlegi értékek betöltése a konfigurációból
        options_schema = vol.Schema({
            vol.Optional("host", default=self.config_entry.data.get("host", "okosvillanyora.local")): str,
            vol.Optional("port", default=self.config_entry.data.get("port", 8989)): int,
        })

        return self.async_show_form(step_id="init", data_schema=options_schema)
