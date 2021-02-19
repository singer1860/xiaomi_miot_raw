"""Provide info to system health."""
from yarl import URL

from homeassistant.components import system_health
from homeassistant.core import HomeAssistant, callback

from .deps.const import DOMAIN


@callback
def async_register(
    hass: HomeAssistant, register: system_health.SystemHealthRegistration
) -> None:
    """Register system health callbacks."""
    register.async_register_info(system_health_info, "/config/integrations")


async def system_health_info(hass):
    """Get info for the info page."""
    is_logged_in = hass.data[DOMAIN].get('cloud_instance') is not None

    data = {
        "logged_in": is_logged_in,
    }

    if is_logged_in:
        data["can_reach_micloud_server"] = system_health.async_check_can_reach_url(
        hass, "https://api.io.mi.com"
    )

    return data
