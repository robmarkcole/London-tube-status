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
from homeassistant.const import ATTR_ATTRIBUTION

from datetime import datetime, timedelta
import requests
import json

SCAN_INTERVAL = timedelta(minutes=1)

DOMAIN = 'tube_state'     #  must match the name of the compoenent
CONF_LINE= 'line'         # get from config, look for 'line' and assign value to CONF_LINE
ATTRIBUTION = "Powered by TfL Open Data"
TUBE_LINES= ['Bakerloo',
             'Central',
             'Circle',
             'District',
             'Hammersmith-city',
             'Jubilee',
             'Metropolitan',
             'Northern',
             'Piccadilly',
             'Victoria',
             'Waterloo-city']

CONFIG_SCHEMA = vol.Schema({
    DOMAIN: vol.Schema({
      vol.Required(CONF_LINE): vol.In(TUBE_LINES)    # Check a valid line
    })
}, extra=vol.ALLOW_EXTRA)

_LOGGER = logging.getLogger(__name__)      # enable logging to console


def setup_platform(hass, config, add_devices, discovery_info=None):
    sensors = []
    for tube in config.get(CONF_LINE):
        sensors.append(LondonTubeSensor(tube))

    add_devices(sensors)
    _LOGGER.info("The tube_state component is ready!")


class LondonTubeSensor(Entity):    # Entity
    """
    Sensor that reads the status of a tube lines using the TFL API.
    """

    API_URL_BASE = "https://api.tfl.gov.uk/line/{}/status"
    ICON = 'mdi:subway'

    def __init__(self, line):
        """Initialize the sensor."""
        self._data = {}
        self._url = self.API_URL_BASE
        self._line = line
        self._state = 'Updating'

    @property
    def name(self):
        """Return the line name of the sensor."""
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
    def unit_of_measurement(self):    # Do I need?
        """Return the unit this state is expressed in."""
        return ""

    def update(self):
        """Perform an API request."""

        try:
            response = requests.get(self._url.format(self._line.lower()))
            response.raise_for_status()
            self._data = response.json()[0]['lineStatuses']   # convert to json and get statuses list
            self._statuses = [status['statusSeverityDescription'] for status in self._data]

            if 'Good Service' in self._statuses:   # if good status, this is the only status returned
                self._state = 'Good Service'
                self._description = 'Nothing to report'
            else:
                self._state = 'Disruptions'
                self._description = [status['reason'] for status in self._data] # get the reasons

        except requests.RequestException as req_exc:
            print(
                'Invalid response from API: %s', req_exc
            )
