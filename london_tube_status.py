"""
Class for checking the status of London Underground tube lines, as well as the Overground, DLR and Tfl rail.
"""
import requests
from datetime import datetime

API_URL = 'https://api.tfl.gov.uk/line/mode/tube,overground,dlr,tflrail/status'


def parse_api_response(response):
    """Parse the TFL API json response."""
    lines = [line['name'] for line in response]
    data_dict = dict.fromkeys(lines)

    for line in response:
        statuses = [status['statusSeverityDescription']
                    for status in line['lineStatuses']]
        state = ' + '.join(sorted(set(statuses)))

        if state == 'Good Service':
            reason = 'Nothing to report'
        else:
            reason = ' *** '.join(
                [status['reason'] for status in line['lineStatuses']])

        attr = {'State': state, 'Description': reason}
        data_dict[line['name']] = attr

    return data_dict


class TubeData(object):
    """Get the latest tube data from TFL."""

    def __init__(self):
        """Initialize the TubeData object."""
        self.data = {}
        self.last_updated = None

    def update(self):
        """Get the latest data from TFL."""
        response = requests.get(API_URL)
        self.data = parse_api_response(response.json())
        self.last_updated = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

