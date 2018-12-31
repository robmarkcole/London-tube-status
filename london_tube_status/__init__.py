"""
Class for checking the status of London Underground tube lines, as well as the Overground, DLR and Tfl rail.
"""
import requests
from datetime import datetime

API_URL = "https://api.tfl.gov.uk/line/mode/tube,overground,dlr,tflrail/status"


def parse_api_response(response):
    """Parse the TFL API json response."""
    lines = [line["name"] for line in response]
    data_dict = dict.fromkeys(lines)

    for line in response:
        try:
            statuses = [
                status["statusSeverityDescription"] for status in line["lineStatuses"]
            ]
            state = " + ".join(sorted(set(statuses)))

            if (
                state == "Good Service"
            ):  # if good status, this is the only status returned
                reason = "Nothing to report"
            else:
                reason = " *** ".join(
                    [status["reason"] for status in line["lineStatuses"]]
                )

            data_dict[line["name"]] = {"State": state, "Description": reason}

        except:
            data_dict[line["name"]] = {
                "State": None,
                "Description": "Error parsing API data",
            }

    return data_dict


class TubeData:
    """Get the latest tube data from TFL."""

    def __init__(self):
        """Initialize the TubeData object."""
        self._data = {}
        self._last_updated = None

    def update(self):
        """Get the latest data from TFL."""
        response = requests.get(API_URL)
        if response.status_code != 200:
            return
        self._data = parse_api_response(response.json())
        self._last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @property
    def data(self):
        """Return the data."""
        return self._data

    @property
    def last_updated(self):
        """Return the time data was last updated."""
        return self._last_updated
