"""
For more details about this component, please refer to the documentation at
https://home-assistant.io/cookbook/python_component_basic_state/

Aim to merge into
https://github.com/timcnicholls/home-assistant/blob/transport-api/homeassistant/components/sensor/uk_transport.py
"""

import voluptuous as vol
import logging
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.entity import Entity

from datetime import datetime, timedelta
import requests
import json

SCAN_INTERVAL = timedelta(minutes=1)

DOMAIN = 'tube_state'     # the top level variable - should match the name of the compoenent
CONF_LINE= 'line'         # get from config, look for 'line' and assign value to CONF_LINE

CONFIG_SCHEMA = vol.Schema({
    DOMAIN: vol.Schema({
      vol.Required(CONF_LINE): cv.string,    # check that mandatory variables are provided
    })
}, extra=vol.ALLOW_EXTRA)

_LOGGER = logging.getLogger(__name__)      # enable logging to console


def setup_platform(hass, config, add_devices, discovery_info=None):     # this config is a dict of the user supplied variables
    sensors = []          # config[DOMAIN].get(CONF_LINE, DEFAULT_LINE)      # create local varlaible, if CONF_LINE exists, use, else
    for tube in config.get(CONF_LINE):
        sensors.append(LondonTubeSensor(tube))

    add_devices(sensors)
    _LOGGER.info("The 'tube_state' component is ready!")


class LondonTubeSensor(Entity):    # Entity
    """
    Sensor that reads the status of a tube lines.
    """

    TRANSPORT_API_URL_BASE = "https://api.tfl.gov.uk/line/mode/tube/status"
    ICON = 'mdi:subway'

    def __init__(self, line):
        """Initialize the sensor."""
        self._data = {}
        self._url = self.TRANSPORT_API_URL_BASE
        self._line = line
        self._state = None

    @property
    def line(self):
        """Return the name of the sensor."""
        return self._line

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._line

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def icon(self):
        """Icon to use in the frontend, if any."""
        return self.ICON

    @property
    def unit_of_measurement(self):
        """Return the unit this state is expressed in."""
        return ""

    def update(self):
        """Perform an API request."""

        try:
            response = requests.get(self._url)
            response.raise_for_status()

            lines = [line['id'] for line in response.json()]
            statuses = [line['lineStatuses'][0]['statusSeverityDescription'] for line in response.json()]
            status_dict = {key:value for key, value in zip(lines, statuses)}

            self._data = status_dict
            self._state = status_dict[self.line.lower()]   # Get lower case as requireds

        except requests.RequestException as req_exc:
            print(
                'Invalid response from transportapi.com: %s', req_exc
            )
